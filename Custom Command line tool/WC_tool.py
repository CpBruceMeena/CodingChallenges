import sys
import os

def get_count_from_file_data(option, data):
    resp = []
    if option:
        if option == '-c':
            resp.append(len(data.encode('utf-8')))
        elif option == '-l':
            lines = data.splitlines()  # splitlines() returns a list of lines
            line_count = len(lines)
            resp.append(line_count)
        elif option == '-w':
            resp.append(len(data.split()))
        elif option == '-m':
            resp.append(len(data))
    return resp

def get_count(option, file_path):
    resp = []
    if option:
        if option == '-c':
            resp.append(os.path.getsize(file_path))
            resp.append(file_path)

        elif option == '-l':
            line_count = 0
            with open(file_path, "r") as file:
                line_count = sum(1 for line in file)
            resp.append(line_count)
            resp.append(file_path)

        elif option == '-w':
            word_count = 0
            with open(file_path, "r") as file:
                for line in file:
                    words = line.split()  # Split line into words
                    word_count += len(words)
            resp.append(word_count)
            resp.append(file_path)

        elif option == '-m':
            character_count = 0
            with open(file_path, "r") as file:
                content = file.read()
                character_count = len(content.replace(" ", "").replace("\n", "").replace("\t", ""))
            resp.append(character_count)
            resp.append(file_path)
    return resp
    
    
def main():
    option = ''
    file_name = ''
    if sys.stdin.isatty():
        if len(sys.argv) > 1:
            if len(sys.argv) == 2:
                file_name = sys.argv[1]
            else:            
                option = sys.argv[1]
                file_name = sys.argv[2]
            if option:
                resp = get_count(option, file_name)
                print(' '.join(map(str, resp)))
            else:
                file_name = sys.argv[1]
                resp2 = get_count('-l', file_name)
                resp3 = get_count('-w', file_name)
                resp1 = get_count('-c', file_name)
                resp = [resp2[0], resp3[0], resp1[0], resp1[1]]
                print(' '.join(map(str, resp)))
        else:
            print("No argument provided")
        return

    content = sys.stdin.read()
    if content:
        option = sys.argv[1]
        resp = get_count_from_file_data(option, content)
        print(' '.join(map(str, resp)))
        
if __name__ == '__main__':
    main()

