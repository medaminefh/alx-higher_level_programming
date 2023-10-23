#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    out = []
    for i in range(list_length):
        try:
            out.append(my_list_1[i]/my_list_2[i])
        except ZeroDivisionError:
            out.append(0)
            print("division by 0")
        except TypeError:
            out.append(0)
            print("wrong type")
        except IndexError:
            out.append(0)
            print("out of range")
        finally:
            pass
    return out
