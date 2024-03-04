import sys

def wc(files=None):
    def count_lines_words_bytes(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            lines = content.count('\n')
            words = len(content.split())
            bytes_count = len(content.encode('utf-8'))
            return lines, words, bytes_count

    def print_statistics(file_path, lines, words, bytes_count):
        print(f"\t{lines}\t{words}\t{bytes_count}\t{file_path}")

    def print_total(total_lines, total_words, total_bytes):
        print(f"\t{total_lines}\t{total_words}\t{total_bytes}\ttotal")

    total_lines, total_words, total_bytes = 0, 0, 0

    if files is None:
        content = sys.stdin.read()
        lines = content.count('\n')
        words = len(content.split())
        bytes_count = len(content.encode('utf-8'))
        print_statistics('', lines, words, bytes_count)
        total_lines += lines
        total_words += words
        total_bytes += bytes_count
    else:
        for file_path in files:
            lines, words, bytes_count = count_lines_words_bytes(file_path)
            print_statistics(file_path, lines, words, bytes_count)
            total_lines += lines
            total_words += words
            total_bytes += bytes_count

        if len(files) > 1:
            print_total(total_lines, total_words, total_bytes)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_paths = sys.argv[1:]
        wc(file_paths)
    else:
        wc()
