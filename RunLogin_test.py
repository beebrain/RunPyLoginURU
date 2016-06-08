import urllib3
from bs4 import BeautifulSoup
import time
import threading
import sys
import datetime
import logging
import requests
def loginURU():
        logging.basicConfig(filename='myapp.log', level=logging.INFO)
        logging.info(datetime.datetime.now().time())
        logging.info('Started')
        http = urllib3.PoolManager(10)
        f = http.request('GET',"http://sar-najkaj.rhcloud.com/index.php/UserControl/LoginProcess")
        s = f.data
        #print s

        soup = BeautifulSoup(s,'html.parser')
        #print soup.title
        inputTag = soup.findAll(attrs={"name" : "magic"})
        #print(inputTag)
        try:
                output = inputTag[0]['value']
                #print (output)
                
                post_params = {
                        "4Tredir" : "http://google.com",
                        "username" : "beebrain@live.uru.ac.th",
                        "password" : "1234567890",
                        "magic":output
                }
                
                #encoded_body = json.dumps(post_params)
                #print(encoded_body)
                url = 'http://172.31.255.1:1000/fgtauth?'+output
                r = requests.post(url, data=post_params)
                print (r.text)
                print("Login")
        except IndexError as e:
                print(str(e))
                logging.info('Logined')
        finally:
                f = http.request('GET',"http://sar-najkaj.rhcloud.com/index.php/UserControl/LoginProcess")
                s = f.data
                print (s)  
                f = http.request('GET',"http://pttsystems-najkaj.rhcloud.com/")
                s = f.data
                print (s)
                logging.info("Request URL finall")
                return
loginURU()
