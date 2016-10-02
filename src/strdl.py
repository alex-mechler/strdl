import argparse
import strdl_parser
import strdl_gen


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=argparse.FileType('r'), nargs='+', help='The list of files to generate strdl documentation for')
    args = parser.parse_args()
    for file in args.filename:
        strdl_gen.generate_file(strdl_parser.parse(file))


if __name__ == '__main__':
    main()
