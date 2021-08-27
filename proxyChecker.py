import urllib.request , socket
from termcolor import colored 
import time

class checkProxy():

  def __init__(self, name):
    print(colored("{} - ProxyChecker Begins...".format(name), "green"))

  def checkproxy(self, prList , timeOut=30):

    self.proxyList = prList
    self.timeOut = timeOut
    
    socket.setdefaulttimeout(int(self.timeOut))

  
    proxyList = [] # there are two sample proxy ip

    for proxy in  self.proxyList:
        if proxy == "":
          pass
        else: 
         proxyList.append(proxy)

    print(colored("This may take some time, Please wait...", "yellow"))
    

    def is_bad_proxy(pip):    
        try:        
            proxy_handler = urllib.request.ProxyHandler({'http': pip})        
            opener = urllib.request.build_opener(proxy_handler)
            opener.addheaders = [('User-agent', 'Mozilla/5.0')]
            urllib.request.install_opener(opener)        
            sock=urllib.request.urlopen('http://www.google.com')  # change the url address here
            #sock=urllib.urlopen(req)
        except urllib.error.HTTPError as e:        
            print('Error code: ', e.code)
            return e.code
        except Exception as detail:
          
            print( "ERROR:", detail)
            return 1
        return 0
        

    for item in proxyList:

        if is_bad_proxy(item):
            print (colored("{} - [NOT WORKING]".format(item), "red"))
           
        else:
            print (colored("{} - [WORKING]".format(item), "green"))

