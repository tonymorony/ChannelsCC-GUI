from lib import rpclib
from kivy.app import App


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
