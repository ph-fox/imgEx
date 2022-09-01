from bs4 import BeautifulSoup
import requests, re, sys, os,base64

def _help():
	print('Usage: python3 {} <keyword>'.format(os.path.basename(__file__)))

def grab(keyword):
	img_list = BeautifulSoup(requests.get(f"https://www.google.com/search?q={keyword}&source=lnms&tbm=isch").content, features="html.parser").find_all('img')
	num = int(input(f"Select number from 1-{len(img_list)}: "))-1
	c = 0
	for i in img_list:
		img_url = i['src']
		if(c>num):
			break
		if(re.match(r'http|s://',img_url)):
			name=base64.b64encode(img_url.encode()).decode().replace('/','')
			with open(f'image_{c}_{name}.jpg', 'wb') as h:
				h.write(requests.get(img_url).content)
			c+=1
	print('Done!')

if(__name__=="__main__"):
	try:
		keyword = '+'.join(sys.argv[1:])
		grab(keyword)
	except Exception as err:
		#print(err)
		_help()
		exit()

