import requests, random, os, threading

#====الوان====
Z = '\033[1;31m'  # أحمر
X = '\033[1;33m'  # أصفر
F = '\033[2;32m'  # أخضر
C = "\033[1;97m"  # أبيض
B = '\033[2;32m'  # أخضر
Y = '\033[1;34m'  # أزرق داكن
W = '\033[0;37m'  # رمادي
e = "\u001b[38;5;242m" #رمادي داكن
m = "\u001b[38;5;15m" #ابيض
E = "\u001b[38;5;8m" #رمادي فاتح
p = '\x1b[1m'#عريض
#====الوان====
ses=requests.Session()
url = "http://api.scraperapi.com?api_key=eee4ac692be71e520ca4fdc5dacbd6f2&url=http://httpbin.org/ip"
try:
    prox = requests.get(url).text
    open('.zebz.txt', 'w').write(prox) 
except Exception as e:
    print('\x1b[1;91mError: \x1b[96m{}'.format(e))
prox = open('.zebz.txt', 'r').read().splitlines()
logo ="""\033[2;32m⠀\x1b[1m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣼⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠈⠻⣿⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣼⡿⠉⠀⣀⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢰⠋⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡝⠛⠉⠉⠉⠉⠉⠻⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠜⢻⡿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢋⣽⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣠⡿⠋⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣰⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡿⢀⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡝⠀⠀⠀⠈⠉⠛⠿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣷⣶⣤⡔⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣝⢿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⡿⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠈⠛⣛⣛⣂⣀⣀⣀⠀⣀⣀⣀⣀⣀⣀⡀⣈⣉⣀⣀⣀⠀⠀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⠋⢉⡻⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⠛⢻⣿⡿⠀⠛⣿⡟⠛⢻⣿⡇⠙⣿⡟⠛⢻⣿⡄⣿⣿⠛⣻⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⡄⠈⢿⣷⡹⣿⣿⣿⣿⣿⡃⠀⢀⣴⣿⠏⠀⠀⠀⣿⣷⣶⠀⠀⠀⠀⣿⣷⣶⣾⣿⠁⠀⢀⣴⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣧⠀⠘⣿⣿⣌⢻⣿⣿⡟⠁⣠⣾⣟⣁⣰⣶⠀⠀⣿⡇⠀⢰⣶⡆⠀⣿⣇⠀⣸⣿⠇⣠⣿⣟⣁⣰⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣧⠀⠘⣿⣿⣷⣍⢿⠀⠀⠛⠛⠛⠛⠛⠛⠀⠛⠛⠛⠛⠛⠛⠃⠛⠛⠛⠛⠛⠋⠀⠛⠛⠛⠛⠛⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠲⠀⠀⠻⣿⣿⣷⣜⡻⠿⣿⣿⣿⣿⣶⡦⠤⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣶⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠷⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

"""
print(logo)
token = input(f'{E}E{B}n{E}t{B}e{E}r {B}y{E}u{B}r{E}e {B}T{E}o{B}k{E}e{B}n : ')
os.system('clear')
print(logo)
id = input(f'{E}I{B}D :')
os.system('clear')
logo1 = """\033[2;32m⠀\x1b[1m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣰⡖⠀⣶⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣶⠀⣴⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣶⠀⣰⡶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢰⣶⣿⣷⣾⣿⣶⠆⠀⠀⠀⠀⠀⠀⢠⣶⣿⣷⣶⣿⣷⡆⠀⠀⠀⠀⠀⠀⢀⣶⣾⣿⣶⣿⣷⡖⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣤⣼⣿⣤⣿⣧⡄⠀⠀⠀⠀⠀⠀⠀⣤⣼⣿⣤⣾⣯⣤⠀⠀⠀⠀⠀⠀⠀⣠⣴⣿⣥⣼⣿⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠹⣿⠋⢹⡿⠉⠁⠀⠀⠀⠀⠀⠀⠀⠙⣿⡏⢩⣿⠉⠁⠀⠀⠀⠀⠀⠀⠀⠘⢿⡏⢉⣿⠏⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠘⠀⠛⠃⠀⠀⢀⣀⣀⣀⣀⣀⡀⠀⠘⠀⠚⠋⠀⠀⢀⣀⣀⣀⣀⣀⣀⠀⠈⠁⠘⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

"""
logo2 = """\033[2;32m⠀\x1b[1m
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣰⡖⠀⣶⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣶⠀⣴⡆⠀⠀⠀⢰⣶⠀⣴⡶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢰⣶⣿⣷⣾⣿⣶⠆⠀⠀⠀⠀⠀⠀⢠⣶⣿⣷⣶⣿⣷⡆⢠⣶⣾⣿⣶⣿⣷⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣤⣼⣿⣤⣿⣧⡄⠀⠀⠀⠀⠀⠀⠀⣤⣼⣿⣤⣾⣯⣤⠀⣠⣴⣿⣥⣼⣿⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠹⣿⠋⢹⡿⠉⠁⠀⠀⠀⠀⠀⠀⠀⠙⣿⡏⢩⣿⠉⠁⠀⠘⢿⡏⢩⣿⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠘⠀⠛⠃⠀⠀⢀⣀⣀⣀⣀⣀⡀⠀⠘⠀⠚⠋⠀⠀⠀⠀⠈⠀⠘⠛⠀⠀⢀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

"""
logo3 = """\033[2;32m⠀\x1b[1m

⠀⠀⠀⠀⣰⡖⠀⣶⡆⠀⠀⠀⢰⣶⠀⣴⡆⠀⠀⠀⢰⣶⠀⣴⡖⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢰⣶⣿⣷⣾⣿⣶⠆⢠⣶⣿⣷⣶⣿⣷⡆⢠⣶⣾⣷⣶⣿⣷⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣤⣼⣿⣤⣿⣧⡄⠀⣤⣼⣿⣤⣾⣯⣤⠀⣠⣴⣿⣥⣼⣿⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠹⣿⠋⢹⡿⠉⠁⠀⠙⣿⠏⢹⣿⠉⠁⠀⠘⢿⡏⢩⣿⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠘⠀⠛⠃⠀⠀⠀⠀⠘⠀⠚⠋⠀⠀⠀⠀⠈⠀⠘⠛⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
logo4 = """\033[2;32m⠀\x1b[1m

⠀⠀⠀⠀⠀⠀⠀⢀⣶⠆⢰⣶⠀⠀⠀⠀⠀⠀⢰⣶⠀⣴⡆⠀⠀⠀⠀⠀⠀⣶⡆⢀⣶⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣶⣾⣿⣶⣿⣷⣶⠀⠀⠀⢠⣶⣿⣷⣶⣿⣷⡆⠀⠀⠀⣰⣶⣿⣷⣾⣿⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⣤⣿⣧⣴⣿⣥⠄⠀⠀⠀⣤⣼⣿⣤⣾⣯⣤⠀⠀⠀⢀⣤⣾⣯⣤⣿⣧⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⢿⡿⠉⣿⡏⠉⠀⣠⣦⡄⠙⣿⡏⢩⣿⠉⠁⢀⣴⣦⠀⠻⣿⠉⣹⡟⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠃⠘⠛⠀⠀⠀⠈⠋⠀⠀⠘⠀⠚⠋⠀⠀⠀⠙⠋⠀⠀⠉⠀⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

"""
print(f"""              {W} • {F}Choose what suits you {W}• """)
print(f'               {F}—{W}———————————————————————{F}—{W}')
print(f"""
{e}-—-—-—-—-—-—-—-—-—-\n
{F}[{W} • {F}] {E}1 {F}→ {E}#_#_# {F}

[ {W}• {F}] {E}2 {F}→ {E}#_##_ {F}

[ {W}• {F}] {E}3 {F}→ {E}###__ {F}

[ {W}• {F}] {E}4 {F}→ {E}#.#.# {F}

{e}-—-—-—-—-—-—-—-—-—-""")
U = str(input(f'     {F}choose a number : {E}'))
os.system('clear')
if U=="1":    
    print(f"{logo1}")
elif U == "2":
    print(f"{logo2}")
elif U == "3":
    print(f"{logo3}")
elif U == "4":
    print(f"{logo4}")     
use = "qwertyuiopasdfghjklzxcvbnm1234567890"
usr = "_"
ust = "."
def cc():
	while True:
				if U == '1':
					a1 =  random.choice(use)
					a2 =  random.choice(usr)
					a3 =  random.choice(use)
					a4 =  random.choice(usr)
					a5 =  random.choice(use)
					user = a1 + a2 + a3 + a4 + a5
			
					url = 'https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/'
					headers = {
								    'authority': 'www.instagram.com',
								    'accept': '*/*',
								    'accept-language': 'ar-US,ar;q=0.9,es-US;q=0.8,es;q=0.7,en-US;q=0.6,en;q=0.5',
								    'content-type': 'application/x-www-form-urlencoded',
								    'origin': 'https://www.instagram.com',
								    'referer': 'https://www.instagram.com/accounts/emailsignup/',
								    'sec-ch-prefers-color-scheme': 'dark',
								    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
								    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
								    'sec-ch-ua-mobile': '?0',
								    'sec-ch-ua-model': '""',
								    'sec-ch-ua-platform': '"Linux"',
								    'sec-ch-ua-platform-version': '""',
								    'sec-fetch-dest': 'empty',
								    'sec-fetch-mode': 'cors',
								    'sec-fetch-site': 'same-origin',
								    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
								    'x-asbd-id': '129477',
								    'x-csrftoken': 'FNrzojHswMWxzSUlm97oP0o1dwwGwbEi',
								    'x-ig-app-id': '936619743392459',
								    'x-ig-www-claim': '0',
								    'x-instagram-ajax': '1014079837',
								    'x-requested-with': 'XMLHttpRequest',
							}
					data = {
							    'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1717867573:dirhkehdjd',
							    'email': 'zebz120zebz@gmail.com',
							    'first_name': 'zebz',
							    'username': f'{user}',
							    'client_id': 'ZgpqywABAAFLAegN2WhaNct-Aza5',
							    'seamless_login_enabled': '1',
							    'opt_into_one_tap': 'false',
							}
					re = requests.post(url , headers=headers, data=data).text
					if '"dryrun_passed":true' in re:
							print(f'{F}GOOD : {user}')
							GOG1 = f"""
	• GOOD USER	•					
	——————————
	
	× user → × {user} ×
	
	——————————			
	• By →  @e_z_d ★
							"""
							requests.get('https://api.telegram.org/bot' +str(token) + '/sendMessage?chat_id=' + str(id) + '&text=' + str(GOG1))
					else:
						print(f'{Z} Bad : {user}', end='\r')
				elif U == '2':
					
					a1 =  random.choice(use)
					a2 =  random.choice(usr)
					a3 =  random.choice(use)
					a4 =  random.choice(use)
					a5 =  random.choice(usr)
					user2 = a1 + a2 + a3 + a4 + a5
					url = 'https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/'
					headers = {
						    'authority': 'www.instagram.com',
						    'accept': '*/*',
						    'accept-language': 'ar-US,ar;q=0.9,es-US;q=0.8,es;q=0.7,en-US;q=0.6,en;q=0.5',
						    'content-type': 'application/x-www-form-urlencoded',
						    'origin': 'https://www.instagram.com',
						    'referer': 'https://www.instagram.com/accounts/emailsignup/',
						    'sec-ch-prefers-color-scheme': 'dark',
						    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
						    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
						    'sec-ch-ua-mobile': '?0',
						    'sec-ch-ua-model': '""',
						    'sec-ch-ua-platform': '"Linux"',
						    'sec-ch-ua-platform-version': '""',
						    'sec-fetch-dest': 'empty',
						    'sec-fetch-mode': 'cors',
						    'sec-fetch-site': 'same-origin',
						    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
						    'x-asbd-id': '129477',
						    'x-csrftoken': 'FNrzojHswMWxzSUlm97oP0o1dwwGwbEi',
						    'x-ig-app-id': '936619743392459',
						    'x-ig-www-claim': '0',
						    'x-instagram-ajax': '1014079837',
						    'x-requested-with': 'XMLHttpRequest',
					}
					data = {
					    'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1717867573:dirhkehdjd',
					    'email': 'zebz120zebz@gmail.com',
					    'first_name': 'zebz',
					    'username': f'{user2}',
					    'client_id': 'ZgpqywABAAFLAegN2WhaNct-Aza5',
					    'seamless_login_enabled': '1',
					    'opt_into_one_tap': 'false',
					}
					re = requests.post(url , headers=headers, data=data).text
					if '"dryrun_passed":true' in re:
							print(f'{F} GOOD : {user2}')
							GOG2 = f"""
	• GOOD USER	•					
	——————————
	
	× user → × {user2} ×
	
	——————————			
	• By →  @e_z_d ★
							"""
							requests.get('https://api.telegram.org/bot' +str(token) + '/sendMessage?chat_id=' + str(id) + '&text=' + str(GOG2))
					else:
							print(f'{Z} Bad : {user2}', end='\r')
				elif U == '3':
						a1 =  random.choice(use)
						a2 =  random.choice(use)
						a3 =  random.choice(use)
						a4 =  random.choice(usr)
						a5 =  random.choice(usr)
						user3 = a1 + a2 + a3 + a4 + a5			
						url = 'https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/'
						headers = {
							    'authority': 'www.instagram.com',
							    'accept': '*/*',
							    'accept-language': 'ar-US,ar;q=0.9,es-US;q=0.8,es;q=0.7,en-US;q=0.6,en;q=0.5',
							    'content-type': 'application/x-www-form-urlencoded',
							    'origin': 'https://www.instagram.com',
							    'referer': 'https://www.instagram.com/accounts/emailsignup/',
							    'sec-ch-prefers-color-scheme': 'dark',
							    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
							    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
							    'sec-ch-ua-mobile': '?0',
							    'sec-ch-ua-model': '""',
							    'sec-ch-ua-platform': '"Linux"',
							    'sec-ch-ua-platform-version': '""',
							    'sec-fetch-dest': 'empty',
							    'sec-fetch-mode': 'cors',
							    'sec-fetch-site': 'same-origin',
							    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
							    'x-asbd-id': '129477',
							    'x-csrftoken': 'FNrzojHswMWxzSUlm97oP0o1dwwGwbEi',
							    'x-ig-app-id': '936619743392459',
							    'x-ig-www-claim': '0',
							    'x-instagram-ajax': '1014079837',
							    'x-requested-with': 'XMLHttpRequest',
						}
						data = {
						    'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1717867573:dirhkehdjd',
						    'email': 'zebz120zebz@gmail.com',
						    'first_name': 'zebz',
						    'username': f'{user3}',
						    'client_id': 'ZgpqywABAAFLAegN2WhaNct-Aza5',
						    'seamless_login_enabled': '1',
						    'opt_into_one_tap': 'false',
						}
						re = requests.post(url , headers=headers, data=data).text
						if '"dryrun_passed":true' in re:
								print(f'{F} GOOD : {user3}')
								GOG3 = f"""
	• GOOD USER	•					
	——————————
	
	× user → × {user3} ×
	
	——————————			
	• By →  @e_z_d ★
							"""
								requests.get('https://api.telegram.org/bot' +str(token) + '/sendMessage?chat_id=' + str(id) + '&text=' + str(GOG3))
						else:
							print(f'{Z} Bad : {user3}', end='\r')
				elif U == '4':
					a1 =  random.choice(use)
					a2 =  random.choice(ust)
					a3 =  random.choice(use)
					a4 =  random.choice(ust)
					a5 =  random.choice(use)
					user4 = a1 + a2 + a3 + a4 + a5			
					url = 'https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/'
					headers = {
						    'authority': 'www.instagram.com',
						    'accept': '*/*',
						    'accept-language': 'ar-US,ar;q=0.9,es-US;q=0.8,es;q=0.7,en-US;q=0.6,en;q=0.5',
						    'content-type': 'application/x-www-form-urlencoded',
						    'origin': 'https://www.instagram.com',
						    'referer': 'https://www.instagram.com/accounts/emailsignup/',
						    'sec-ch-prefers-color-scheme': 'dark',
						    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
						    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
						    'sec-ch-ua-mobile': '?0',
						    'sec-ch-ua-model': '""',
						    'sec-ch-ua-platform': '"Linux"',
						    'sec-ch-ua-platform-version': '""',
						    'sec-fetch-dest': 'empty',
						    'sec-fetch-mode': 'cors',
						    'sec-fetch-site': 'same-origin',
						    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
						    'x-asbd-id': '129477',
						    'x-csrftoken': 'FNrzojHswMWxzSUlm97oP0o1dwwGwbEi',
						    'x-ig-app-id': '936619743392459',
						    'x-ig-www-claim': '0',
						    'x-instagram-ajax': '1014079837',
						    'x-requested-with': 'XMLHttpRequest',
					}
					data = {
					    'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1717867573:dirhkehdjd',
					    'email': 'zebz120zebz@gmail.com',
					    'first_name': 'zebz',
					    'username': f'{user4}',
					    'client_id': 'ZgpqywABAAFLAegN2WhaNct-Aza5',
					    'seamless_login_enabled': '1',
					    'opt_into_one_tap': 'false',
					}
					re = requests.post(url , headers=headers, data=data).text
					if '"dryrun_passed":true' in re:
							print(f'{F} GOOD : {user4}')
							GOG3 = f"""
	• GOOD USER	•					
	——————————
	
	× user → × {user3} ×
	
	——————————			
	• By →  @e_z_d ★
							"""
							requests.get('https://api.telegram.org/bot' +str(token) + '/sendMessage?chat_id=' + str(id) + '&text=' + str(GOG3))
					else:
						print(f'{Z} Bad : {user4}', end='\r')
				else:
					print("يرجى ختيار 1/2/3/4")
					exit()						
Threads = []
for t in range(5):
    x = threading.Thread(target=cc)
    x.start()
    Threads.append(x)
for Th in Threads:
    Th.join()
