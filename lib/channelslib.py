from lib import rpclib


def get_channels_list(rpc_connection):
    channels_list = rpclib.channels_info(rpc_connection)[2:]
    return channels_list
