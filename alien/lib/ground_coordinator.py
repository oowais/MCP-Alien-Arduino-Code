import bluetooth
import logging
import threading
import time

from lib.globals import LOGGER_TAG, GROUND_BLUETOOTH_MAC, GROUND_BLUETOOTH_PORT


class Prithvi(threading.Thread):
    def __init__(self, talk_queue):
        super(Prithvi, self).__init__(name=type(self).__name__)
        self.logger = logging.getLogger(LOGGER_TAG)
        self.q = talk_queue
        self.module_up = False
        self.ground_blue_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

    def module_setup(self):
        while not self.module_up:
            try:
                self.ground_blue_sock.connect((GROUND_BLUETOOTH_MAC, GROUND_BLUETOOTH_PORT))
            except (IOError, bluetooth.btcommon.BluetoothError):
                self.logger.error('Unable to connect to Ground Bluetooth, Module not up ...')
                self.module_up = False
                self.ground_blue_sock.close()
                time.sleep(1)
            else:
                self.logger.info('Connected to Ground Bluetooth Module..!')
                self.module_up = True

    def run(self):
        self.logger.info("Starting off Bluetooth instruction receiver thread ...")
        while True:
            if not self.module_up:
                self.module_setup()
            try:
                data = self.ground_blue_sock.recv(1).decode()
            except bluetooth.btcommon.BluetoothError:
                self.module_up = False
                self.ground_blue_sock.close()
                continue

            if data == "c":
                self.q.put("ground crocodile")
            elif data == "p":
                self.q.put("ground plant")
            elif data == "x":
                self.q.put("ground clear")
            else:
                self.logger.warning("Not able to recognize character.. Ignoring..")
