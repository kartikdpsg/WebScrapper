import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL='https://www.amazon.in/Surf-Excel-Matic-Liquid-Detergent/dp/B072QRVVDS/ref=lp_21246962031_1_1?srs=21246962031&ie=UTF8&qid=1585207895&sr=8-1'

headers={"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'} #user agent lets servers identify application, os, what is version of browser.

def check_price():
	page = requests.get(URL,headers=headers) #gets all data from that website
	
	soup=BeautifulSoup(page.content,'html.parser') #parses all info
	price=soup.find(id="priceblock_ourprice").get_text() #gets what text is written for that id
	f=float(price[2:5])
	if(f<200):
		mail()
	print(f)

def mail():
	server=smtplib.SMTP('smtp.gmail.com',587) # smtp-simple mail transfer protocol, without it emails would go no where, of 2 types end-end and store and forward, works closely with mail transfer agent(MTA), 
	#tls-transfer layer security, ssl-secure socket layer these both are data encryption and cryptographic protocols used between servers, machines, applications etc.
	server.ehlo() # an smtp command sent by email client when connecting to email server
	server.starttls() # encrypts our connection
	server.ehlo()
	server.login('kartik.dpsg@gmail.com', 'eysynpxhfkbsmxxb') #logins to our gmail account
	subject='price fell down'
	body='check your product out'
	msg=f"Subject:{subject}\n\n{body}"
	server.sendmail('kartik.dpsg@gmail.com','kartikbooster@gmail.com',msg) #sends mail with defined subject and body
	print("mail sent")
	server.quit()

while(1):
	check_price()
	time.sleep(10) #sleeps for defined number of seconds
