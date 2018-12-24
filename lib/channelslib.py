from lib import rpclib
from kivy.app import App
import os.path
import json


def get_channels_list(rpc_connection):

    if App.get_running_app().is_connected:
        channels_list = rpclib.channels_list(rpc_connection)
        try:
            del channels_list["result"]
            del channels_list["name"]
        except KeyError:
            pass
        channels_txids = []
        try:
            for channel in channels_list.keys():
                channels_txids.append(channel)
        except KeyError:
            channels_txids = ["No channels on this asset chain opened so far"]
    else:
        channels_txids = ""

    return channels_txids


def get_balance(rpc_connection):
    if App.get_running_app().is_connected:
        balance = str(rpclib.getbalance(rpc_connection))
        ticker = rpclib.getinfo(rpc_connection)["name"]
        balance_reflection = balance + " " + ticker
    # to not crash in some cases when not connected or losing connection
    else:
        balance_reflection = ""
    return balance_reflection


def get_channel_info(rpc_connection, channel_id):
    info = rpclib.channels_list(rpc_connection)[channel_id]
    info_with_id = "Channel " + str(channel_id) + " to wallet: " + info
    return info_with_id


def get_channel_additional_info(rpc_connection, channel_id):

    channel_info = rpclib.channels_info(rpc_connection, channel_id)
    denomination = channel_info["Denomination"]
    total_capacity = int(channel_info["Number of payments"]) * int(channel_info["Denomination"])

    already_spent_capacity = 0
    transactions_amount = 0

    for transaction in channel_info["Transactions"]:
        try:
            already_spent_capacity += int(transaction["Amount"])
            transactions_amount += 1
        except Exception:
            pass

    capacity_left = total_capacity - already_spent_capacity
    transactions_left = int(channel_info["Number of payments"]) - transactions_amount

    additional_info = {}
    additional_info["denomaination"] = denomination
    additional_info["payments_left"] = transactions_left
    additional_info["capacity_left"] = capacity_left

    return additional_info

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
