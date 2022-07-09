import requests
from bs4 import BeautifulSoup

url = 'https://www.dju.ac.kr/biohealth/main.do'

html = requests.get(url).text

bs = BeautifulSoup(html, 'html.parser')

text = [ _ for _ in bs.text.replace('\r', '').replace('\t','').split('\n') if _ != '' and _ != ' ' ] 
for _ in text:
  print(_, end=" ")
print()

print(text)