import re
import sys
from sys import argv


def __main__():
    file_name = argv[1]
    category_name = argv[2]
    with open(file_name, 'r') as f:
        for line in f:
            if line.startswith('Lesson'):
                sys.stdout.write("//Domino Chinese/{}/{}".format(
                    category_name, line
                ))
                continue
            match = re.match(
                r'(.*)\t\((.*)\) (.*)',
                line
            )
            characters, pinyin, english = match.group(1, 2, 3)
            sys.stdout.write("{}\t{}\t{}\n".format(
                characters, pinyin, english
            ))


if __name__ == '__main__':
    __main__()
