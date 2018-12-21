from lib import rpclib, channelslib
from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
import json


class LoginPage(Screen):

    def verify_credentials(self):

        while True:
            try:
                server_input = self.ids["rpcserver"].text
                user_input = self.ids["rpcuser"].text
                password_input = self.ids["rpcpassword"].text
                port_input = int(self.ids["port"].text)
                connection = rpclib.rpc_connect(user_input, password_input, server_input, port_input)
                rpclib.getinfo(connection)
            except Exception as e:
                print(e)
                print("Not connected. Please check credentials")
                content = Button(text='Close me!')
                popup = Popup(content=content, auto_dismiss=False)
                # TODO: have to throw popup and in this case not clean text fields
                self.ids["rpcserver"].text = ''
                self.ids["rpcuser"].text = ''
                self.ids["rpcpassword"].text = ''
                self.ids["port"].text = ''
                break
            else:
                App.get_running_app().rpc_connection = connection
                App.get_running_app().is_connected = True
                if self.ids["savelogin"].active:
                    connection_details = {"rpc_server": self.ids["rpcserver"].text,
                                          "rpc_user": self.ids["rpcuser"].text,
                                          "rpc_password": self.ids["rpcpassword"].text,
                                          "rpc_port": self.ids["port"].text}
                    connection_json = json.dumps(connection_details)
                    with open("connection.json", "w+") as file:
                        file.write(connection_json)
                    print("Saved login details")
                self.manager.current = "user"
                # TODO: loading channels list on startup
                break
