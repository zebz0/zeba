import random
import requests
import os

############################
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
C = "\033[1;97m" #ابيض
y = '\033[1;35m'#وردي
f = '\033[2;35m'#بنفسجي
z = '\033[3;33m'#اصفر طوخ
G = '\033[2;36m'
E = '\033[1;31m'
V = '\033[1;35m'
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
M = '\x1b[1;37m'#ابیض
S = '\033[1;33m'
U = '\x1b[1;37m'#ابیض
BRed = '\x1b[1;31m'
BGreen = '\x1b[1;32m'
BYellow = '\x1b[1;33m'
R = '\x1b[1;34m'
Purple = '\x1b[1;35m'
BCyan = '\x1b[1;36m'
BWhite = '\x1b[1;37m'
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
O = '\x1b[38;5;208m' #برتقالي
BL = '\x1b[38;5;21m' #ازاق طوخ
YU = '\x1b[38;5;200m' #وردي طوخ
############################



log="""

        
        
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡤⠴⠶⠶⠷⠾⠶⠶⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠿⠦⣤⣤⣤⣤⣤⡤⠴⠒⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣉⣩⣶⣶⣤⣄⡀⠡⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡾⠛⠉⠀⠀⠀⠈⠉⠛⢷⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠒⡒⢄⠀⠀⠀⠀⣴⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠸⣀⡠⠃⠀⠀⢀⣿⠃⠀⣀⣄⡀⠀⠀⠀⠀⠀⠈⢄⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢦⡀⠀⠀⠀⠀⠘⣿⠀⢰⣿⣿⣿⠆⠀⠀⠀⢀⣴⣾⢿⡿⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢶⣤⣀⠀⠀⢿⡀⠀⢻⠛⠉⠀⠀⠀⠀⠘⠿⠟⣼⠇⠀⢀⣀⣤⡴⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    
        ⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣴⣶⣾⣿⣿⣦⡀⠘⢧⡀⠘⠀⠀⠀⠀⠀⠀⠀⠀⣠⠟⢀⣠⣾⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀    
        ⠐⠒⠲⢶⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣝⡲⣤⣄⣀⣀⣀⣠⣴⣾⣥⣶⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣄⣀⣀⣀⣠⠜    
        ⠀⠀⠀⠀⠠⠤⠤⠶⠾⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠉⠛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡍⠉⠛⠛⠛⠉⠁⠀⠀    
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠋⠉⠉⢩⣿⣿⣿⣿⣿⠇⡆⠀⠀⠀⢠⡹⣿⣿⣿⣿⠀⠈⠻⣿⡛⠷⡈⠛⢄⠀⠀⠀⠀⠀⠀⠀    
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⢠⡟⣉⣴⡿⠛⡟⢰⠇⠀⠀⠀⠸⡇⢻⣿⡗⠙⢷⡀⠀⠈⢣⡀⠈⠂⠀⠉⠀⠀⠀⠀⠀⠀    
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⠀⢡⠏⠀⢸⠃⣼⠀⠀⠀⠀⠀⣷⠸⣿⣿⡄⠀⠱⠀⠀⠀⠑⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠹⡆⣿⡄⠀⠀⠀⢀⣿⣸⠙⡇⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    
        ⠀⠀⠀⠀⠀⠀⠀⢰⣶⣶⣶⣶⣦⢰⣶⣶⣶⣶⣶⠀⠙⣿⡟⠀⣠⡄⢸⡿⠃⢰⣷⣶⣶⣤⡀⢰⣶⣶⣶⣶⣶⠀⠀⠀⠀⠀⠀⠀    
        ⠀⠀⠀⠀⠀⠀⠀⠘⠛⢀⣼⡿⠃⠀⢸⣿⣀⠘⠛⠀⠀⠸⡇⠀⢸⠀⣾⠁⠀⠀⣿⣇⣀⣽⡿⠘⠛⢀⣴⡿⠃⠀⠀⠀⠀⠀⠀⠀    
        ⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⠋⣀⣤⠀⢸⣿⠉⢠⣤⠀⠀⠀⢻⣄⣸⢸⡏⠀⠀⠀⣿⡏⠉⢻⣷⠀⣰⣿⠋⢀⣄⠀⠀⠀⠀⠀⠀⠀    
        ⠀⠀⠀⠀⠀⠀⠀⢸⣿⣷⣶⣿⣿⢰⣾⣿⣶⣾⣿⠀⠀⠀⠀⠙⠛⠛⠀⠀⠀⢰⣿⣷⣶⣿⠋⢸⣿⣷⣶⣾⣿⠀⠀⠀⠀⠀⠀⠀        
        
    
   

"""

print(log)


tok = input(R+ ': توكن بوتك  '+X)
id = input(C+ ': ايدي حسابك  '+X)

os.system('clear')

print(F+ ' _________________♡[المطوࢪه زيبز]♡_________________ ')
													


cho = int(input(V+ ' خلي رقم 2 : '+y))

os.system('clear')

while True:
	t = '1234567890'
	n = '0987654321'	
	m = 'QWERTYUIOPASDFGHJKLZXCVBNM'
	g = '1234567890QWERTYUIOPASDFGHJKLZXCVBNM_.'
				
	a = "".join(random.choice(t)for i in range(1))
	o = "".join(random.choice(t)for i in range(1))
	b = "".join(random.choice(n)for i in range(1))
	c = "".join(random.choice(m)for i in range(1))
	d= "".join(random.choice(g)for i in range(1))
			
	if cho==1:
		user = a+o+'.'+b+o
		print(user)
			
	if cho==2:
		user = a+o+'_'+b+d
		print(user)
		
			
	url= 'https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/'
	he = {
			'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.9', 'Content-Length': '65', 'Content-Type': 'application/x-www-form-urlencoded', 'Cookie': 'csrftoken=AImmzluk6xjPB1fmBY7xVE5wlHpvhl8I; mid=ZP_ZUQABAAHu1nPtyQOyuErC0lHG; ig_did=072E2501-E264-49A3-A431-A97AB70F7B9F; ig_nrcb=1; datr=Vdn_ZNg_QDqUksZZlJf6WHxv; dpr=2.7853219509124756', 'Dpr': '2.78532', 'Origin': 'https://www.instagram.com', 'Referer': 'https://www.instagram.com/accounts/emailsignup/', 'Sec-Ch-Prefers-Color-Scheme': 'light', 'Sec-Ch-Ua': '"Not)A;Brand";v="24", "Chromium";v="116"', 'Sec-Ch-Ua-Full-Version-List': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"', 'Sec-Ch-Ua-Mobile': '?0', 'Sec-Ch-Ua-Model': '""', 'Sec-Ch-Ua-Platform': '"Linux"', 'Sec-Ch-Ua-Platform-Version': '""', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36', 'Viewport-Width': '967', 'X-Asbd-Id': '129477', 'X-Csrftoken': 'AImmzluk6xjPB1fmBY7xVE5wlHpvhl8I', 'X-Ig-App-Id': '936619743392459', 'X-Ig-Www-Claim': '0', 'X-Instagram-Ajax': '1008575226', 'X-Requested-With': 'XMLHttpRequest'}
			
	da = {'email': '', 
			'first_name': '',
			 'username': user, 
			 'opt_into_one_tap': 'false'}
			
	re = requests.post(url,headers=he,data=da).text
			 
	if '''{"account_created": false, "errors": {"email": [{"message": "This field is required.", "code": "email_required"}], "__all__": [{"message": "Create a password at least 6 characters long.", "code": "too_short_password"}]}, "dryrun_passed": false, "username_suggestions": [], "status": "ok", "error_type": "form_validation_error"}''' in re:
		print(F+f' [user] ✔ ')
		
		tt = f"""
		~~~~~~~~~~~~~~~~~~
   				وصلك يوزࢪ ☑️
		~ [{user}] ~
		
		المطوࢪه / @U_J_3
	@z_v_1  /القناة 
	~~~~~~~~~~~~~~~~~~~
"""
		requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={id}&text="+str(tt))
			
	else:print(X+f' [user] ✘ ')
