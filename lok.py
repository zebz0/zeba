import requests
import random
from user_agent import generate_user_agent
from colorama import Back, init
import os
import sys
import subprocess
import webbrowser
import time
import requests
import threading
import datetime
init(autoreset=True)
gg = 0
bb = 0
B = '\x1b[38;5;208m'  # برتقالي
E = '\033[1;31m'  # أحمر
F = '\033[2;32m'  # أخضر
def printt(word, delay=1):
        	for letter in word:
        		sys.stdout.write(letter)
        		sys.stdout.flush()
        		time.sleep(delay)

zebz = """

⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠟⠛⠛⠛⢻⠋⠉⠉⠉⠉⠙⢉⠉⢹⡟⠉⢈⠉⢻⣿⠈⠙⢿⣿⡿⠀⢸⣿⣿⣿⣿⣿⠿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠃⠀⣴⣤⣀⣾⣇⣤⣼⠀⠀⣷⣿⣇⣿⠁⢠⣆⡄⠀⣿⣧⣀⠈⠿⠇⠀⣿⣿⣿⠟⠉⠀⢀⠀⠀⠀⠀⠐⠉⠻⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣅⠀⠈⠙⠻⣿⣿⣿⣿⠔⠀⣿⣿⣿⠇⠀⢘⠙⠃⢀⢿⣿⣷⣧⠀⠀⣸⣿⣿⡏⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿
⣿⣿⣿⣿⣿⡿⠻⣷⣷⡦⠀⢈⣿⣿⣿⠀⠀⣿⣿⣿⠎⡀⣦⣴⡀⠀⢸⣿⡿⠇⠀⣰⣿⣿⣿⠁⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⣿⣿
⣿⣿⣿⣿⣿⣧⡀⠀⠙⠄⣀⣼⣿⣿⣿⡀⠀⣿⣿⣿⢀⣀⣿⣿⣇⣀⣸⡏⠀⢄⣼⣿⣿⣿⣿⣇⢻⣿⣶⣄⠀⠀⠀⣠⣶⣿⡿⢰⣿⣿
⣿⣿⣿⣿⣿⣿⣧⣴⣾⣿⣿⣿⠿⠟⠛⠛⠛⢿⠋⡫⣿⡏⡉⠉⠉⠋⠉⢫⡉⠉⠉⠛⠻⣿⣿⣿⣆⠙⠿⣿⣧⠀⣰⣿⡿⠋⣠⣽⣿⣿
⣿⣿⣿⠟⠛⣿⣿⣿⣿⢋⠉⡇⠀⢠⣤⣄⣰⣾⠀⠁⣼⡇⠀⢼⣿⣿⠀⣸⡇⠀⢸⣦⡀⠈⢻⣿⣿⣷⣄⠀⠈⠀⠁⠀⢀⣸⣿⣿⣿⣿
⣿⣿⣿⡄⠀⡟⠀⠘⡟⠠⢸⡇⠀⠀⠁⢀⣈⣿⠀⠩⢺⡇⠀⠀⠂⣄⣦⣿⡇⠀⢸⣿⡇⠀⢨⣿⣿⣿⣿⣷⡀⠀⡀⣰⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡇⠀⢀⢀⠠⠉⣂⣾⡇⠀⠹⠷⠟⠿⣿⠀⠁⣾⠧⠀⢠⠀⠈⣿⣿⡇⠀⢸⡿⠃⠀⢸⣿⣿⣿⣿⣿⣿⡮⣺⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣇⠀⡀⣸⣆⠰⡥⣿⣧⣄⢀⡄⣤⣶⣿⠀⠬⣿⠀⠀⣸⣆⠀⠹⣿⡇⠠⣀⣂⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣄⣰⣿⣿⣄⣴⣿⣿⣿⣾⣿⣿⣿⣿⠒⢸⣿⣤⣴⣿⣿⣷⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿

"""
printt(zebz, delay=0.001)
ID = input(Back.RED + 'ENTER YOUR ID: ')
token = input(Back.YELLOW + 'ENTER YOUR TOKEN: ')
os.system('clear')
def mahos(user):
    global gg, bb
    cookies = {
        'mid': 'ZbYvEAABAAGbliASkVBpDVWAY_pH',
        'ig_did': '855D0C80-6CE9-4CD8-9422-80716840E82B',
        'datr': 'Dy-2ZZJdYLgoAXx26YCKgQPq',
        'ps_n': '0',
        'ps_l': '0',
        'fbm_124024574287414': 'base_domain=.instagram.com',
        'ig_nrcb': '1',
        'shbid': '"12527\\05452590120684\\0541740214349:01f76395e1e0f3c3bbe6bbb58d67a648bc61dd8dc9ca27e39c09a0fedf69baadccfe5b26"',
        'shbts': '"1708678349\\05452590120684\\0541740214349:01f71aba558f78800585763c100b904c416fca805fdc34aeccf83eee1a7703bce05e5fcf"',
        'csrftoken': 'WzQWLAi94BDiPqzwrwFuGaU8vzrPHhlD',
        'ds_user_id': '53186034340',
        'fbsr_124024574287414': 'xgY8i0_LuQl5c2L-VADm_0_9rFidsyApgBzLaltH7ck.eyJ1c2VyX2lkIjoiMTAwMDc5NzAzODA3MDUzIiwiY29kZSI6IkFRRDN2SzdEUXJfc1pHSzVNRFVTQ2ZUMXhzSVdjT1R6LW5iRFM1RFYzdmZTM0RDZWN6QUNHeTBFWVhLYVZkdEZkTEkxUkFvaFE2aWFvQmxISU5pVW1ydnlnQlVFZjhGOElLY2VhVFZuUW5IdlpybGJNREoxb0dxX1lOMm1PZmpKdHhMak9QZW02ZmRYcXp5NUhGeDdnSVlab3lEUjJ6bmFmbTE2WjRlYnF5SkRNbWdqZWwtZVBtbHk5WnU3MFRzS2VQVFdDRGNjOEFNRUttbTVkRmd4YTVEeVdhVkJySEtzM2RNYzNCN2l1elJoZ3NaTHBSbC1DS0QtMERnekgyeE9MMUVlcGdRZWlJcGpZdlYtTERKUU5VQXByd1lJRi1CY2xEQWRGX3Z2NGFxRXBTTjZ3WVVqSnlsX3ExYjVQNTJjUTY3VzBhOVZmZ09hbEdWS1RRa1hwb1pyIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCTzFPMDRBcXhJWkF5VVRtOHhFVTRnTFJrZUJXalVUNFpDdlpBZGdzd0tlODZCd0JuellIbDljdTdoNzhoSGVjTENVZ1lBejVvRnZvS2E4T0JHSDFyam1JWkJ3aHhGYVhTZnRMbzhaQ0J5WkM5bXFnbzRWWFRRclJXajh1Q0p0bnlGOENocXhIeFpBQkoyd3hsSFpCU1BXMm00aDB4cHpSSlpBdTJGcmtHMnRwM2dKNUFmc1VtVER4dHZlVXdaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNzA4NzU3MTQyfQ',
        'rur': '"CLN\\05453186034340\\0541740293151:01f7505815bf59bf34f381061daea65afbe0b8556c3933ca0199de747c8e403d66b76778"',
        'dpr': '2.1988937854766846',
    }

    headers = {
        'authority': 'www.instagram.com',
        'accept': '*/*',
        'accept-language': 'ar-YE,ar;q=0.9,en-YE;q=0.8,en-US;q=0.7,en;q=0.6',
        'content-type': 'application/x-www-form-urlencoded',
        'dpr': '2.19889',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/accounts/emailsignup/',
        'sec-ch-prefers-color-scheme': 'dark',
        'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
        'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Linux"',
        'sec-ch-ua-platform-version': '""',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': generate_user_agent(),
        'viewport-width': '891',
        'x-asbd-id': '129477',
        'x-csrftoken': 'WzQWLAi94BDiPqzwrwFuGaU8vzrPHhlD',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': 'hmac.AR39C0bslX48JTL3qnOmZoE2uaWZTpE8eYQODkG0TN-NL3aJ',
        'x-instagram-ajax': '1011632956',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'enc_password': '#PWD_INSTAGRAM_BROWSER:10:1708757243:AdBQAKpnJMEagksjmKCubfnpEXeVya4k0v8QwpO8sfrA6HUPGOMXIlhsGyD7VxfDZhtih3+0RkcUC8q2CxAg46Vnwj73Gy2ua81ckcDZmaFlj4Q8Yerp3ZwVvyZreu20DfSwOShEcNX4rCzZDyDAXeC+qA==',
        'email': 'mahosllll@mahos.com',
        'first_name': 'Ahmed',
        'username': f'{user}',
        'client_id': 'ZbYvEAABAAGbliASkVBpDVWAY_pH',
        'seamless_login_enabled': '1',
        'opt_into_one_tap': 'false',
    }

    res = requests.post(
        'https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/',
        cookies=cookies,
        headers=headers,
        data=data,
    ).text
    if '"errors"' in res and '"username_is_taken"' in res and '"dryrun_passed": false,' in res or 'username_has_special_char' in res:
        bb += 1
        print(Back.RED + f'[{bb}] Bad Username : {user}')
    elif '"dryrun_passed":true,' in res:
        gg += 1
        print(Back.GREEN + f'[{gg}] Available Username {user}')
        tlg = f'''
        Hi hunt Username INSTAGRM
        . ------------------------------------->
        [(҂⌣̀_⌣́)] --->{user} 
        .  ------------------------------------->
        [(ToT)] BY : @U_J_3'''
        requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={tlg}')
        print(tlg)
    else:
        print(res)
def randomusers():
    while True:        
        KK ="qwertyuiopasdfghjklzxcvbnm1234567890"
        ZEBZ=''.join(random.choices(KK, k=1))
        ZEBZ2=''.join(random.choices('_', k=1))
        ZEBZ3=''.join(random.choices(KK, k=1))
        ZEBZ4=''.join(random.choices('_', k=1))
        ZEBZ5=''.join(random.choices(KK, k=1))
        ALL=ZEBZ+ZEBZ2+ZEBZ3+ZEBZ4+ZEBZ5
        user = ALL
        mahos(user)
randomusers()
