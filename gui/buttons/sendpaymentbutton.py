from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.popup import Popup
from lib import rpclib
from decimal import *


class SendPaymentButton(Button):

    def send_payment(self):
        application = App.get_running_app()
        channel = application.active_channel_id
        payment_sum = application.root.ids.paymentpage.ids.paymentamount.text
        payment_hex = rpclib.channels_payment(application.rpc_connection, channel, str(int(Decimal(payment_sum))))
        try:
            payment_txid = rpclib.sendrawtransaction(application.rpc_connection, payment_hex["hex"])
        except Exception as e:
            application.root.ids.paymentpage.ids.paymentstatus.text = e
        else:
            print(payment_txid)
            application.root.ids.paymentpage.ids.paymentstatus.text = "Payment sent. TXID: " + str(payment_txid)
