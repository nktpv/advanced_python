import sys

def nl(file_path=None):
    if file_path:
        with open(file_path, 'r',  encoding='utf-8') as file:
            lines = file.readlines()
            for line_number, line in enumerate(lines, start=1):
                print(f'\t{line_number}\t{line}', end='')
    else:
        for line_number, line in enumerate(sys.stdin, start=1):
            print(f'\t{line_number}\t{line}', end='')

if __name__ == "__main__":
    if len(sys.argv) == 2:
        file_path = sys.argv[1]
        nl(file_path)
    else:
        nl()
