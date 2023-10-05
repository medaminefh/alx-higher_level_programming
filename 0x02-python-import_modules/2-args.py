#!/usr/bin/python3
if __name__ == '__main__':
    """
        use function from calculator_1
    """
    from sys import argv

    length = len(argv) - 1
    if length == 1:
        print("{} argument:".format(length))
        print("{}: {}".format(length, argv[length]))
    else:
        if length == 0:
            print("{} arguments.".format(length))
        else:
            print("{} arguments:".format(length))
            for i in range(1, length + 1):
                print("{}: {}".format(i, argv[i]))
