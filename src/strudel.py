import argparse
import strudel_parse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=argparse.FileType('r'), nargs='+', help='The list of files to generate strudel documentation for')
    args = parser.parse_args()
    for file in args.filename:
        strudel_parse.parse(file)


if __name__ == '__main__':
    main()
