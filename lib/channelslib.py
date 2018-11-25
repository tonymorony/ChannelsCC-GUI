from lib import rpclib
from kivy.app import App
import os.path
import json


def get_channels_list(rpc_connection):

    if App.get_running_app().is_connected:
        channels_list = rpclib.channels_info(rpc_connection)
        channels_txids = []
        channels_list.pop("result")
        channels_list.pop("name")

        for channel in channels_list.values():
            channels_txids.append(channel[-64:])
    else:
        channels_txids = ""

    return channels_txids


class ConfigReader:

    def __init__(self):
        if os.path.isfile("connection.json"):
            with open("connection.json", "r") as file:
                connection_json = json.load(file)
                self.rpc_server = connection_json["rpc_server"]
                self.rpc_user = connection_json["rpc_user"]
                self.rpc_password = connection_json["rpc_password"]
                self.rpc_port = connection_json["rpc_port"]
        else:
            self.rpc_server = ''
            self.rpc_user = ''
            self.rpc_password = ''
            self.rpc_port = ''
