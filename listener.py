#!/usr/bin/env python

# Simple and naive implementation for return the log stats
# Should probably be made into a websocket listener

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import serial
import threading
import time
import json
log = []

ARDUINO_SERIAL = '/dev/tty.usbmodemfd131'


class ArduinoLogger(threading.Thread):
    command = 'i'

    def run(self):
        s = serial.Serial(ARDUINO_SERIAL, 57600, timeout=1)

        # wait for arduino to be ready
        print 'Resetting arduino'
        time.sleep(5)
        print 'Done, listening'
        s.write(self.command)
        lastcommand = self.command
        while 1:
            line = s.readline()
            line = line.strip()
            log.append(line)
            if self.command != lastcommand:
                print 'received new command, sending: %s' % self.command
                s.write(self.command)
                lastcommand = self.command


class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        if self.path.find('command') != -1:
            command = self.path.split('command=')[1]
            if self.server.logger.command != command:
                self.server.logger.command = command
                print 'set new command'
            # logger.command = command
        line = log[len(log) - 1]
        line = line.split(',')
        self.wfile.write(json.dumps(line))
        return


def main():
    try:
        # start the logger
        logger = ArduinoLogger()
        logger.start()

        # start webserver
        server = HTTPServer(('', 5678), RequestHandler)
        server.logger = logger
        print 'started server for ...'
        server.serve_forever()
    except KeyboardInterrupt:
        print 'Shutting down server'
        server.socket.close()

if __name__ == '__main__':
    main()
