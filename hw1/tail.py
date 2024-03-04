import sys

def tail(files=None):
    def print_tail(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines[-10:]:
                print(line, end='')

    if files is None:
        lines = sys.stdin.readlines()
        for line in lines[-17:]:
            print(line, end='')
    elif len(files) == 1:
        print_tail(files[0])
    else:
        for file_path in files:
            print("\n", f"==> {file_path} <==")
            print_tail(file_path)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_paths = sys.argv[1:]
        tail(file_paths)
    else:
        tail()
