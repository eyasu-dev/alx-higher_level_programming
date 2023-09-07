#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    length = len(argv) - 1
    if length == 0:
        print("{}".format(length))
    else:
        sum = 0
        for i, arg in enumerate(argv):
            if i != 0:
                sum += int(arg)
        print(f"{sum}")
