import requests, random, threading, pazok
from user_agent import *


Z = '\033[1;31m'  # أحمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m'  # أخضر
e = "\u001b[38;5;242m" #رمادي داكن
m = "\u001b[38;5;15m" #ابيض
E = "\u001b[38;5;8m" #رمادي فاتح

Aa =0
Bb = 0
token="7082657991:AAFkfDXT5U9fcgdGXBHk8L9ewGvmjKJN0tI"
id=662667108

def cc():
    while True:
        global Aa, Bb
        uu = "qwertyuioplkjhgfdsamnbvcxz1234567890_"
        a="".join(random.choice(uu)for i in range(1))
        b="".join(random.choice(uu)for i in range(1))
        c="".join(random.choice(uu)for i in range(1))
        d="".join(random.choice(uu)for i in range(1))
        b="".join(random.choice(uu))
        c="".join(random.choice(uu))
        d="".join(random.choice(c))
        e="".join(random.choice(d))
        user1 ='_'+b+c+d+e
        user2 = b+'_'+c+d+e
        user3 = e+b+'_'+c+d
        user4 = e+b+c+'_'+d        
        s1 ='_'+a+a+b+b
        s2 = a+'_'+a+b+b
        s3 = a+a+'_'+b+b
        s4 = '_'+a+b+'_'+b
        s5 = a+a+a+a+b
        zebz = s1,s2,s3,s4,s5,user1,user2,user3,user4
        user =random.choice(zebz)
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
            'user-agent': str(generate_user_agent()),
            'x-asbd-id': '129477',
            'x-csrftoken': 'uBfsWtwDTXF4HPrDRO1Emh5rk0oggwpK',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': '0',
            'x-instagram-ajax': '1015175619',
            'x-requested-with': 'XMLHttpRequest',
        }
        
        data = {
            'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1722002107:sjbeejshe',
            'email': 'shaheen@gmail.com',
            'first_name': 'zebz',
            'username': user,
            'client_id': '16gv3b81s0f9rf1jol29ph9pso91i1s38x16a8il51ar301z14a445p',
            'seamless_login_enabled': '1',
            'opt_into_one_tap': 'false',
        }
        
        re = requests.post(url, headers=headers, data=data).text
        if '"dryrun_passed":true' in re:
            Aa +=1
            print(f' {E}[ {Bb} ] {F} GOOD USER : {E} {user}')
            RRT = f"""
{user}
  Done
  Attempt : {Bb}
"""            
            requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text="+str(RRT))
            
        elif '"spam":true' in re:
        	print(f'{X} VPN ')   
        else:
            Bb +=1
            print(f' {E}[ {Bb} ] {Z} BAD USER : {E} {user}', end='\r')
Threads = []
for t in range(5):
    x = threading.Thread(target=cc)
    x.start()
    Threads.append(x)
for Th in Threads:
    Th.join()                        
