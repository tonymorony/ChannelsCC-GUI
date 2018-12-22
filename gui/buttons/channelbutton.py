from kivy.app import App
from kivy.uix.listview import ListItemButton
from lib import rpclib


class ChannelListItemButton(ListItemButton):

    def select(self):
        # setting active channel id after button release
        self.background_color = [1., 0., 0., 1]
        application = App.get_running_app()
        application.active_channel_id = str(self.text)
        application.root.ids.userpage.ids.channelinformation.text = str(rpclib.channels_info(application.rpc_connection,
                                                                        application.active_channel_id))

    def deselect(self):
        application = App.get_running_app()
        application.active_channel_id = ""
        application.root.ids.userpage.ids.channelinformation.text = ""
        self.background_color = [0., 1., 0., 1]
