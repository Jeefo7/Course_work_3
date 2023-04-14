from func import *


JSON_operations = 'operations.json'


def main():
    operation = slice_operation(load_data(JSON_operations))
    for i in range(5):
        print(show_operation(operation[i]))


if __name__ == '__main__':
    main()
