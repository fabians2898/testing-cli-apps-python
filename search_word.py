# search_word.py
import click
import re

def sort_by_len(x):
   return sorted(x, key=len)

def get_words_from_string(x):
    regex = r'\b\w+\b'
    return re.findall(regex, x)

@click.command()
@click.option('--file', '-f')
def main(file):
    r_file = open(file, 'r')
    words = get_words_from_file(r_file.read())
    words = sort_by_len(words)
    longest_word = words[-1]
    print('{}, {}'.format(longest_word, longest_word[::-1]))


if __name__ == "__main__":
    main()