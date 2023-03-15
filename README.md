# Graviex_trading_bot
Python Trading bot

1. Market Making
2. Wash Trading
3. Info (Balances, Markets, Market Depth{bids & asks})

you will need two files
```
.env

Graviex_bot.py
```

Email: cryptominer8245@yahoo.com to get the files of this bot

Click here to contact me on Discord: <a href="https://discord.com/users/412476381725720576">Cryptominer8245</a>

For Install you will need Python3
check your version by opening a terminial and type
```python3 --version```

Update the package list and upgrade any existing packages:
```
sudo apt-get update
sudo apt-get upgrade
```
Install Python by running the following command:
```
sudo apt-get install python3
```
Verify the installation by checking the Python version:
```
python3 --version
```

The Bot needs a few libraries

to Install the libraries:
```
pip install requests
pip install termcolor
pip install prettytable
pip install python-dotenv
```

You will need to update your ``Private Keys`` and ``Coin Pairs`` in the .env file
Example:
```
# Graviex-Keys
# Api-Key
access_key=
# Api-Secret-Key
secret_key=
```

In The Bot ``Graviex_bot.py``

You can update the following lines of code to your stratigies
```
Sells:
minprice = 0.00000180
price = current_rate - 0.00000001
volume = desired_amount / current_rate * 1.01

Buys:
maxprice = 0.00000151
price = current_rate + 0.000000051
volume = desired_amount / current_rate + 0.05
```
add # to the ``buy_response = create_buy_order()`` line of code to stop the bot order from being placed

To start Bot in Terminal:
1. `screen -S Graviex Bot file`
2. start bot
```python3 Graviex_bot```
3. to exit screen and keep bot running hold the key `Control` and than press keys `A D` at the same time
4. to resume screen type `screen -r`
5. to stop bot press `Control c`

Trading Bot Example:

<img src="https://user-images.githubusercontent.com/40405385/225456228-2a5081d7-9d96-4733-9e27-8d9a8f87542a.png" width="25%" alt="Graviex_bot">

Disclaimer: 

```The trading bot provided herein is designed for informational and educational purposes only. It is not intended to be, and should not be construed as, financial, investment, or trading advice. Users of this trading bot assume full responsibility for any decisions made based on its outputs, and the creators and maintainers of the bot shall not be held liable for any losses, damages, or claims arising from the use of this tool. Trading in financial markets involves substantial risks, including the potential for loss of principal, and may not be suitable for all investors. Before using this trading bot, users should carefully consider their financial objectives, risk tolerance, and level of experience. We strongly recommend consulting with a qualified financial advisor before making any investment or trading decisions.```
