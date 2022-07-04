"""
获取本机本地IP和公网IP地址
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

import socket
import requests


class Get_IP(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box(style=Pack(direction=COLUMN))

        button = toga.Button(
            '获取本机本地IP和公网IP',
            on_press=self.get_local_open_ip,
            style=Pack(padding=5)
        )

        main_box.add(button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def get_local_open_ip(self, widget):
        # 获取本机本地ip地址
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        my_socket.connect(('8.8.8.8', 80))
        local_ip = my_socket.getsockname()[0]
        my_socket.close()

        # 获取公网IP地址
        open_ip = requests.get('http://ifconfig.me/ip').text
        local_open_ip = '本地IP：' + local_ip + '\n' + '公网IP：' + open_ip
        self.main_window.info_dialog('本地IP和公网IP', local_open_ip)


def main():
    return Get_IP()
