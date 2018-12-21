from kivy.app import App
from kivy.config import Config
from kivy.lang import Builder

Config.set('kivy', 'window_icon', 'gui/img/favicon.ico')
Config.set('graphics', 'width', '1024')
Config.set('graphics', 'height', '768')


class ChannelsCCApp(App):

    title = "ChannelsCC GUI"

    is_connected = False

    rpc_connection = None

    active_channel_id = ""

    def build(self):
        gui = Builder.load_file("gui/kv/channelscc.kv")
        return gui


if __name__ == "__main__":
    ChannelsCCApp().run()
