import fileinput

from lib.controller.interface import Interface


def main():    
    Interface().apply_operations_from_file_input(fileinput.input())


if __name__ == '__main__':
    main()
