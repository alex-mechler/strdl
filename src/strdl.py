"""
strdl is a HTML documentation generator for python file

author: Alexander Mechler

Copyright (C) 2016 Alexander Mechler

Licenced under the MIT license
"""
import argparse
import strdl_parser
import strdl_gen


def main():
    """
    Parse the args, and generate a strdl documentation for each
    :return: None
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=argparse.FileType('r'), nargs='+', help='The list of files to generate strdl documentation for')
    args = parser.parse_args()
    for file in args.filename:
        strdl_gen.generate_file(strdl_parser.parse(file))

#Only run if we are the main file being run
if __name__ == '__main__':
    main()
