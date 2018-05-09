#todo change
# -*- coding: utf-8 -*-
import serial
import time
import os
from . import config


def get_port():
    ports = ("COM1", "COM2", "COM3", "COM4", "COM5", "/dev/ttyUSB0", "/dev/ttyACM0")
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            # print("Available port is {}".format(port))
            return port
        except (OSError, serial.SerialException) as e:
            pass
            # print("Connection error \n" + str(e))


class Serial(serial.Serial):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.port = "/dev/ttyACM0"
        self.baudrate = config.baudrate
        self.parity = config.parity
        self.stopbits = config.stopbits
        self.bytesize = config.bytesize
        self.try_to_open()

    def try_to_open(self):
        while 1:
            try:
                self.port = get_port()
                self.open()
                break
            except Exception:
                print("Unsuccessful connection try")
                time.sleep(1)

    def read_to_file(self, filename="0"):
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        self.reset_input_buffer()
        self.reset_output_buffer()

        with open(filename, "w") as file:
            while 1:
                out = ''
                temp = self.readline()
                out = str(temp.decode()).replace("\00", "")
                if out != '':
                    if out != config.STOP:
                        # file.write(out)
                        print(out)
                    else:
                        print("File has been saved")
                        break
