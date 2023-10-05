#!/usr/bin/python3
if __name__ == '__main__':
    """
        use function from calculator_1
    """
    from  sys import argv

    l = len(argv) - 1
    if l == 1:
        print("{} argument:".format(l))
        print("{}: {}".format(l, argv[l]))
    else:
        if l == 0:
            print("{} arguments.".format(l))
        else:
            print("{} arguments:".format(l))
            for i in range(1, l + 1):
                print("{}: {}".format(i, argv[i]))
