#!/usr/bin/python3
if __name__ == '__main__':
    """
        use function from calculator_1
    """
    from sys import argv

    length = len(argv) - 1
    out = 0
    if length == 0:
        print("{}".format(out))
    else:
        for i in range(1, length+1):
            out += int(argv[i])
        print("{}".format(out))
