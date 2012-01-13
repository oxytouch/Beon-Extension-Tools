#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pycurl, StringIO

USER_AGENT = "Googlebot/2.1 (+http://www.googlebot.com/bot.html)"
PROXY_ADDR = "127.0.0.1:9050"

site = 'beon.ru'
redirrec = 'REDIR'
antispamrec = 'ERROR\xd1\xf0\xe0\xe1\xee\xf2\xe0\xeb\xe0 \xe7\xe0\xf9\xe8\xf2\xe0 \xee\xf2 \xf1\xef\xe0\xec\xe0. \xcf\xee\xe6\xe0\xeb\xf3\xe9\xf1\xf2\xe0, \xef\xee\xe4\xee\xe6\xe4\xe8\xf2\xe5 \xed\xe5\xea\xee\xf2\xee\xf0\xee\xe5 \xe2\xf0\xe5\xec\xff \xe8 \xef\xee\xef\xf0\xee\xe1\xf3\xe9\xf2\xe5 \xe4\xee\xe1\xe0\xe2\xe8\xf2\xfc \xea\xee\xec\xec\xe5\xed\xf2\xe0\xf0\xe8\xe9 \xf1\xed\xee\xe2\xe0.'
bumplimitrec = 'HIDEERROR\xcf\xf0\xe5\xe2\xfb\xf8\xe5\xed\xee \xec\xe0\xea\xf1\xe8\xec\xe0\xeb\xfc\xed\xee\xe5 \xea\xee\xeb\xe8\xf7\xe5\xf1\xf2\xe2\xee \xea\xee\xec\xec\xe5\xed\xf2\xe0\xf0\xe8\xe5\xe2 \xe2 \xee\xe4\xed\xee\xec \xf2\xee\xef\xe8\xea\xe5. \xd1\xee\xe7\xe4\xe0\xe9\xf2\xe5, \xef\xee\xe6\xe0\xeb\xf3\xe9\xf1\xf2\xe0, \xe4\xf0\xf3\xe3\xee\xe9 \xf2\xee\xef\xe8\xea \xe8 \xef\xf0\xee\xe4\xee\xeb\xe6\xe8\xf2\xe5 \xee\xe1\xf1\xf3\xe6\xe4\xe5\xed\xe8\xe5 \xe2 \xed\xb8\xec.'
userbumplimitrec = 'HIDEERROR\xcf\xf0\xe5\xe2\xfb\xf8\xe5\xed\xee \xec\xe0\xea\xf1\xe8\xec\xe0\xeb\xfc\xed\xee\xe5 \xea\xee\xeb\xe8\xf7\xe5\xf1\xf2\xe2\xee \xea\xee\xec\xec\xe5\xed\xf2\xe0\xf0\xe8\xe5\xe2 \xe4\xeb\xff \xee\xe4\xed\xee\xe9 \xe7\xe0\xef\xe8\xf1\xe8. \xcf\xf0\xee\xe4\xee\xeb\xe6\xe8\xf2\xe5, \xef\xee\xe6\xe0\xeb\xf3\xe9\xf1\xf2\xe0, \xee\xe1\xf1\xf3\xe6\xe4\xe5\xed\xe8\xe5 \xe2 \xe4\xf0\xf3\xe3\xee\xe9 \xe7\xe0\xef\xe8\xf1\xe8.'
succesrec = '1'
othersuccesrec = 'HIDE1' #TODO: why not 1? can`t find 'HIDE' trigger.
wrongauthrec = ''
cantaddrec = '' # Yep, ''.
cantaddcomrec = 'ERROR\xca\xee\xec\xec\xe5\xed\xf2\xe8\xf0\xee\xe2\xe0\xf2\xfc \xe7\xe0\xef\xe8\xf1\xfc \xec\xee\xe3\xf3\xf2 \xf2\xee\xeb\xfc\xea\xee \xf3\xf7\xe0\xf1\xf2\xed\xe8\xea\xe8 \xf1\xee\xee\xe1\xf9\xe5\xf1\xf2\xe2\xe0.'

def req (threadid, text, user=None,postuser=None,postpass=None):
  postdata= {"ajax": "1",
   "topic_id": threadid,
   "r": "",
   "message": text,
   "user_type": "anonymous",
   "alogin": "",
   "password": "",
   "authorize": "",
   "avatar": "",
   "button": "add",
   "photo": "0",
   "new_login": "",
   "name": "",
   "email": "",
   "www": "",
   "add": ""}
  if postuser != None:
    postdata["user_type"] = "notanon"
    postdata["alogin"] = postuser
    if postpass != None:
      postdata["password"] = postpass
  DATA_POST = "&".join(["%s=%s" % (k, v) for k, v in  postdata.items()])
  string = StringIO.StringIO()
  curl = pycurl.Curl()
  
  curl.setopt(pycurl.WRITEFUNCTION, string.write)
  curl.setopt(pycurl.USERAGENT, USER_AGENT)
  curl.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_SOCKS5)
  curl.setopt(pycurl.HTTPPROXYTUNNEL,1)
  curl.setopt(pycurl.PROXY, PROXY_ADDR)
  if user == None:
    curl.setopt(pycurl.URL, 'http://'+site+'/p/add_comment.cgi')
  else:
    curl.setopt(pycurl.URL, 'http://'+user+'.'+site+'/p/add_comment.cgi')
  curl.setopt(pycurl.POSTFIELDS, DATA_POST)
  curl.setopt(pycurl.POST,1)
  
  curl.perform()
  curl.close()
  return string.getvalue()
  string.close()

def message():
  import random, textgen
  src = textgen.train('necropaste.txt')
  text = ""
  for i in range(random.randint(3, 30)):
    text = text + "\n" + textgen.generate_sentence(src)
  text = text.encode('utf-8')
  return "[image-original-none-http://www.porjati.net/uploads/posts/2010-03/1269899770_1.jpg]\n[image-original-none-http://abutton.ru/uploads/posts/2011-03/13006454218743.jpeg]\n[image-original-none-http://beremenna-ya.narod.ru/images/samoproizvolnoe.prerivanie.beremennosti.jpg]\n[image-original-none-http://www.realisti.ru/upload/UserFiles/abortion-scream.jpg]\n[image-original-none-http://cs1249.vkontakte.ru/u2144059/12989474/x_3769c9a6.jpg]\n[image-original-none-http://demotivation.me/images/20081102/pr5xf2wcxhxz.jpg]\n[image-original-none-http://mystery-queen.com/data_images/Говно/Говно-01.jpg]\n[image-original-none-http://s.lurkmore.to/images/3/37/2ch35.jpg]\n[image-original-none-http://s.lurkmore.to/images/2/2c/124515683084.jpg]\n[image-original-none-http://s.lurkmore.to/images/a/a1/1261789192008.jpg]\n[image-original-none-http://s.lurkmore.to/images/4/48/1255809767106.jpg]\n[image-original-none-http://s.lurkmore.to/images/d/d5/2ch22.jpg]\n[image-original-none-http://s.lurkmore.to/images/9/92/2ch30.jpg]\n[image-original-none-http://img3.imagetitan.com/img1/1/35/shit2.jpg]\n[image-original-none-http://edge.ebaumsworld.com/picture/Socojo/ShitBricks.png]\n"+ text

if __name__ == '__main__':
  import sys, time
  threadid = sys.argv[1]
  if sys.argv[2] == 'none':
    user = None
  else:
    user = sys.argv[2]
  while True:
    try:
      rec = req(threadid, message(), user)
    except KeyboardInterrupt:
      print time.asctime(), "interrupted by user"
    except pycurl.error:
      print time.asctime(), "connection or proxy error"
    else: 
      if rec == redirrec:
	print time.asctime(), "rec redir: captcha or other shit"
      elif rec == antispamrec:
	print time.asctime(), 'antispam detect, waiting'
	time.sleep(5)
      elif rec == bumplimitrec or user != None and rec == userbumplimitrec:
	print time.asctime(), 'bumplimit reached'
	exit()
      elif rec == cantaddrec or user != None and rec == cantaddcomrec:
	print time.asctime(), 'can`t post, waiting.'
	time.sleep(5)
      elif rec == succesrec or rec == othersuccesrec:
	print time.asctime(), "msg posted"
      else:
	print time.asctime(), "msg posted.. or not posted, lol"
	print rec.decode('cp1251')
