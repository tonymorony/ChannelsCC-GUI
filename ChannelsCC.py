from kivy.app import App
from kivy.config import Config
from kivy.lang import Builder

Config.set('kivy', 'window_icon', 'gui/img/favicon.ico')


class ChannelsCCApp(App):

    title = "ChannelsCC GUI"

    is_connected = False

    rpc_connection = None

    def build(self):
        gui = Builder.load_file("gui/kv/channelscc.kv")
        return gui


if __name__ == "__main__":
    ChannelsCCApp().run()
