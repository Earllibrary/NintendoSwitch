# coding: utf-8

import subprocess
import time
import requests
from datetime import datetime

ninURL = "https://store.nintendo.co.jp/category/NINTENDOSWITCH/HAC_S_KAYAA.html"

#access the URL above every N minutes and check the word "SOLD OUT".

#notify via LINE if SWITCH is available
def message_LINE(message):
	
	yourToken = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
	
	line_notify_api = 'https://notify-api.line.me/api/notify'

	payload = {'message': message}
	headers = {'Authorization': 'Bearer ' + line_notify_token}  
	line_notify = requests.post(line_notify_api, data=payload, headers=headers)
                           
#check stock of nintendo store
def stock_NtdStr():
	s = subprocess.getoutput("curl "+ninURL)
	if("SOLD OUT" in s):
		print("sold out "+datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
		return False
	else:
		print("now on sale  "+datetime.now().strftime("%Y/%m/%d %H:%M:%S"))

if __name__ == "__main__":

	N = 30
	ninFlag = -1	#if flag=1, switch is on sale
	yodFlag = -1

	b = 1
	try:
		while b==1:
			if(stock_NtdStr()):
				message_LINE("SWITCH now on sale!\nat\n"+ninURL)
			time.sleep(N)
	except:
		message_LINE("エラーが発生して止まりました")
