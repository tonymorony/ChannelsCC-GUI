from kivy.app import App
from kivy.uix.listview import ListItemButton
from lib import rpclib


class ChannelListItemButton(ListItemButton):

    def on_release(self):
        # setting active channel id after button release
        application = App.get_running_app()
        application.active_channel_id = str(self.text)
        application.root.ids.userpage.ids.channelinformation.text = str(rpclib.channels_info(application.rpc_connection,
                                                                        application.active_channel_id))
