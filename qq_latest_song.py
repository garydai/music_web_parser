# coding=utf-8
import HTMLParser
from bs4 import BeautifulSoup
import urllib
import socket 
import sys
'''
# timeout in seconds 
timeout = 50 
socket.setdefaulttimeout(timeout) 
'''
'''
class parseLinks(HTMLParser.HTMLParser):

	def handle_starttag(self, tag, attrs):
		if tag == 'em':
			for name,value in attrs:
				if name == 'id':
					print value


lParser = parseLinks()

lParser.feed(urllib.urlopen("http://y.qq.com/y/static/index.html").read())
'''
'''	
	text = html.read(90000)
	html.close()
'''
f = open("new_song_list.txt","wb+")
f2 = open("random_song_list.txt","wb+")
try:

	html = urllib.urlopen('http://y.qq.com/y/static/index.html')
	tt = ''
	#chunk = 16*1024
#	while True:
	##	text = html.read(chunk)
	#	if not text:
#			break
	#	tt += text

	for i in range(0, 9):
		text = html.read(10000)
		tt += text

	soup = BeautifulSoup(tt)

	ol = soup.ol
	count = 0;
	musiclist = []
	for x in ol.find_all('li'):			
		em = x.find('span', {'class':'data'})
		musiclist.append(em.contents[0].encode('gbk'))
		print em.contents

	for i in musiclist:
		if count == 0:
			f.write(i)
		else:
			f.write('\r\n' + i)
		count = count + 1

	rocommend2	= soup.find('div', {'class':'mod_recommend_2'})

	ol = rocommend2.ol
	count = 0;
	hotmusiclist = []
	for x in ol.find_all('li'):			
		em = x.find('span', {'class':'data'})
		hotmusiclist.append(em.contents[0].encode('gbk'))
		print em.contents

	for i in hotmusiclist:
		if count == 0:
			f2.write(i)
		else:
			f2.write('\r\n' + i)
		count = count + 1


except socket.error, msg:
	print 'error'
    




print 12
