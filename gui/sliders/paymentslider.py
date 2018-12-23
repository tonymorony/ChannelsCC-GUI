from kivy.app import App
from kivy.uix.slider import Slider
from lib import rpclib


class PaymentSlider(Slider):

    application = App.get_running_app()

    def set_slider_values(self):
        channel_info = rpclib.channels_info(self.application.rpc_connection, self.application.active_channel_id)
        # step is a denomination
        self.step = int(channel_info["Denomination"])
        # max is a capacity which left in a channel
        # which calculating as a: LEFT_CAPACITY = TOTAL_CAPACITY - AMOUNT_OF_ALL_ALREADY_DONE_PAYMENTS
        total_capacity = int(channel_info["Number of payments"]) * int(channel_info["Denomination"])

        already_spent_capacity = 0

        for transaction in channel_info["Transactions"]:
            try:
                already_spent_capacity += int(transaction["Amount"])
            except Exception:
                 pass

        self.max = total_capacity - already_spent_capacity


