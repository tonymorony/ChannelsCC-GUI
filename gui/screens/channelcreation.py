from lib import rpclib
from kivy.uix.screenmanager import Screen
from kivy.app import App


class ChannelCreationPage(Screen):

    def create_channel(self):
        destpubkey = self.ids["destpubkey"].text
        numpayments = self.ids["numpayments"].text
        denomination = self.ids["denomination"].text
        new_channel = rpclib.channels_open(App.get_running_app().rpc_connection, destpubkey, numpayments, denomination)
        try:
            new_channel_txid = rpclib.sendrawtransaction(App.get_running_app().rpc_connection, new_channel["hex"])
        except Exception as e:
            self.ids["creationstatus"].text = str(new_channel)
        else:
            self.ids["creationstatus"].text = "Channel opening transaction [color=43c51a]" + new_channel_txid + "[/color] succesfully broadcasted"
