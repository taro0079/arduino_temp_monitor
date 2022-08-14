#!/bin/env python
# -*- coding: utf-8 -*-
import json
import time

import tornado.websocket
import tornado.web
import tornado.ioloop
import serial


from read_temperature import read_temperature


class SendWebSocket(tornado.websocket.WebSocketHandler):
    def __init__(self, application, request, **kwargs) -> None:
        super().__init__(application, request, **kwargs)
        self.ser = serial.Serial("COM5", 57600)

    def open(self):
        print('Session Opened. IP:' + self.request.remote_ip)
        self.ioloop = tornado.ioloop.IOLoop.instance()
        self.send_websocket()

    def on_close(self):
        self.ser.close()
        print("Session Closed")

    def check_origin(self, origin):
        return True

    def send_websocket(self):
        self.ioloop.add_timeout(time.time() + 60, self.send_websocket)
        if self.ws_connection:
            message = json.dumps({
                'data': read_temperature(self.ser),
            })
            self.write_message(message)


app = tornado.web.Application([(r"/ws/display", SendWebSocket)])

if __name__ == "__main__":
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()
