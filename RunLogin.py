import urllib3
from BeautifulSoup import BeautifulStoneSoup
import time
import threading
import sys
import datetime
import logging
def loginURU():
        logging.basicConfig(filename='myapp.log', level=logging.INFO)
        logging.info(datetime.datetime.now().time())
        logging.info('Started')
        f = urllib.urlopen("http://sar-najkaj.rhcloud.com/index.php/UserControl/LoginProcess")
        s = f.read()
        f.close()
        #print s

        soup = BeautifulStoneSoup(s)
        inputTag = soup.findAll(attrs={"name" : "magic"})

        try:
            output = inputTag[0]['value']
            print output
            post_params = {
                "4Tredir" : "http://google.com",
                "username" : "beebrain@live.uru.ac.th",
                "password" : "1234567890",
                "magic":output
                    }
            post_args = urllib.urlencode(post_params)
            url = 'http://172.31.255.1:1000/fgtauth?'+output
            fp = urllib.urlopen(url, post_args)
            soup = BeautifulStoneSoup(fp)
            logging.info('Login To www')
        except IndexError:
            logging.info('Logined')
        finally:
            f = urllib.urlopen("http://sar-najkaj.rhcloud.com/index.php/UserControl/LoginProcess")
            s = f.read()
            f.close()

            f = urllib.urlopen("http://pttsystems-najkaj.rhcloud.com/")
            s = f.read()
            f.close()
            logging.info("Request URL finall")
            return


#d = threading.Thread(name='daemon', target=loginURU)
#d.daemon = True
#d.start()
while True:
    loginURU()
    time.sleep(600)
sys.exit(0)
