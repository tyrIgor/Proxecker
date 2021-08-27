#This Proxy Checker is just an orgnized of the proxy-checker by ApsOps
#https://github.com/ApsOps/proxy-checker/blob/master/proxy_checkpy3.py

from proxyChecker import checkProxy
from termcolor import colored 

doneInfoGrabing = False




proxyListInput = input(colored("Please Enter your Proxy list: ", "yellow"))


proxList = proxyListInput.split(" ")
timeout = input("Timeout (30s - Deafult): ")

def checkTimeout(period):
     user = checkProxy("User")
     user.checkproxy(proxList, int(period))


if timeout.isdigit():
   if int(timeout) == 0:
     checkTimeout(30)
   else:
      checkTimeout(timeout) 

elif timeout.strip () == "" or timeout == "":

    checkTimeout(30) 

else:
  while doneInfoGrabing == False:
    timeout = input("Please Enter a digit value: ")
    if timeout.isdigit():
      doneInfoGrabing = True
      if int(timeout) == 0:
        checkTimeout(30)
      elif timeout.strip () == "" or timeout == "":
        checkTimeout(30) 
      else:
        checkTimeout(timeout) 
    else:
      timeout = input("Please Enter a digit value or hit: ")


