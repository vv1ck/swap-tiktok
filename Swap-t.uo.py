import requests , uuid , time
uid = uuid.uuid4()
r = requests.session()

print("""
	███████╗██╗    ██╗ █████╗ ██████╗     
	██╔════╝██║    ██║██╔══██╗██╔══██╗    
	███████╗██║ █╗ ██║███████║██████╔╝    
	╚════██║██║███╗██║██╔══██║██╔═══╝     
	███████║╚███╔███╔╝██║  ██║██║         
	╚══════╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝         
		╔╦╗╦╦╔═╔╦╗╔═╗╦╔═    
		 ║ ║╠╩╗ ║ ║ ║╠╩╗  By JOKER / t.uo
		 ╩ ╩╩ ╩ ╩ ╚═╝╩ ╩  """)
print('====================================')
ess = input("Enter Your sessionid :")
user = input("Enter Username : ")
time.sleep(1)
vv1ck = input('\nare you ready ? [ y / n ] : ')
print(' ')
if vv1ck == 'y':
	while True:
		url = "https://api16-normal-c-alisg.tiktokv.com:443/passport/login_name/update/"
		cookies = {"sessionid": f'{ess}'}
		headers = {
			"Connection": "close", 
			"Content-Length":"19",
			"x-Tt-Token": "",
			"X-SS-Cookie": "d_ticket=d0ea14600615c5b4ed590ea193e0242a16782", 
			"tt-request-time": "1612540707288", 
			"User-Agent": "TikTok 18.5.0 rv:172025 (iPhone; iOS 13.6.1; ar_SA@calendar=gregorian;numbers=latn) Cronet", 
			"x-tt-passport-csrf-token": f"{ess}", 
			"sdk-version": "2", 
			"passport-sdk-version": "5.12.1", 
			"X-SS-STUB": "658BF8A611C037E2DBA4F49839A1535B", 
			"x-tt-store-idc": "alisg", 
			"x-tt-store-region": "sa", 
			"X-SS-DP": "1233", 
			"x-tt-trace-id": "00-72ea8350105f59a9bc99830605e904d1-72ea8350105f59a9-01", 
			"Accept-Encoding": "gzip, deflate", 
			"X-Khronos": "1612540706", 
			"X-Gorgon": "8402a0846000919a57d648714b230a43412a3fb228e177b806bd", 
			"Content-Type": "application/x-www-form-urlencoded"}
		
		data = {
			"residence": "sa",
			"os_version": "13.6.1",
			"app_id": "1233",
			"iid": uid,
			"app_name": "musical_ly",
			"login_name": f'{user}'}
		
		req = r.post(url, headers=headers, cookies=cookies, data=data)
		
		if '"message":"success"' in req.text:
			print(f'D0NE SWAP >> {user}')
			input('bye ..')
		elif '"message":"error"' in req.text:
			print('Sorry, there is an error !')
		else:
			print('ERROR .. ')
else:
	print('         Okay bye .. ')
	print(' < insta: t.uo | tele: vv1ck > ')
