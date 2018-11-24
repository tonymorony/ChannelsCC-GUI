from kivy.app import App
from kivy.uix.listview import ListItemButton


class ChannelListItemButton(ListItemButton):

    def on_release(self):
        # setting active channel id after button release
        App.get_running_app().active_channel_id = str(self.text)
