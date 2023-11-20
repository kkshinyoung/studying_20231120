import requests
import re

if __name__ == '__main__':
    req = requests.get("http://ipconfig.kr")
    out_addr = re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]
    print(out_addr)