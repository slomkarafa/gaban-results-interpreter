# todo change
# -*- coding: utf-8 -*-
from src import serial
from src import config


def main():
    _serial = serial.Serial()
    filename = '1'
    while 1:
        # filename = input("Enter output filename\n")

        _serial.read_to_file("{}{}.csv".format(config.OUT_PATH, filename))


if __name__ == "__main__":
    main()
