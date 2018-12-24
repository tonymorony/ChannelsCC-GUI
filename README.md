# What Channels CC is?

Instant payment mechanism, designing as secured by POW. Imho much more better than Lighting Network. 

More information can be found here: https://github.com/KomodoPlatform/Mastering_CryptoConditions/blob/master/all_chapters.md#chapter-10---channels-example
And here: https://github.com/KomodoPlatform/komodo/blob/master/src/cc/channels.cpp

# What this tool do?

This tool is a graphical implementation of some ChannelsCC RPC calls.

At the moment it's a prototype / mock so I didn't care about UI beauty at all.

![alt text](https://i.imgur.com/Yb3R7xK.png) 

# Installation 

Developer installation. Tested on Ubuntu 18.04 (assuming python 3.6+ is installed by default)
And Komodo daemon was built from FSM branch of https://github.com/jl777/komodo/

Pre-built packages are under development.
```
sudo add-apt-repository ppa:kivy-team/kivy
sudo apt-get install python3-pip libssl-dev cython3 libgl-dev git python3-kivy
pip3 install requests wheel python-bitcoinlib slick-bitcoinrpc pygame
git clone https://github.com/tonymorony/trollbox_gui
cd trollbox_gui
python3 main.py
```

# RPC Connection

* In case of localhost daemon usage use 127.0.0.1 as RPC address. Username, password and port can be found in .conf file for desired asset chain

* If you want to use remote host for RPC connection you need to add your IP as rpcallowip= param to desired asset chain daemon config

![alt text](https://i.imgur.com/u6aAIht.png)

# Implemented calls

- [x] channelsopen (Use the "Open new channel" button on the main screen)

- [x] channelspayment (Use the "Make a payment" button on the main screen to go to payment screen)

- [ ]  channelsclose - Implementation in progress (with separation of list of channels to opened and closed)

- [ ]  channelsrefund - Implementation in progress

- [x] channelsinfo (Using in many places e.g. right part of main page)

- [x] channelslist (left part of main page)