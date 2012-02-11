#!/usr/bin/env python
# -*- coding: utf-8 -*-
import settings

redirlist = []

def main(ocrtype, target=None, url=None):
  if ocrtype == 'chip':
    code = chip(target)
  elif ocrtype == 'hands':
    code = hands(url)
  elif ocrtype == 'ocr':
    pass
  return code

def chip(t, redirlim=settings.redirlim):
  import subprocess
  redirlist.append(t)
  if redirlist.count(t) > redirlim:
    retc = subprocess.call(settings.chipcom)
    if retc != 0:
      print time.asctime(), "recive %s returncode, check chipcom." % (retc,)
    for i in range(settings.redirlim):
      redirlist.remove(t)
  return None

def hands(url):
  import Image
  import StringIO
  # Or lock threads there? See main.posting.
  captcha = Image.open(StringIO.StringIO(getcaptcha(url)))
  captcha.show()
  code = raw_input('code:')
  captcha.save('samples/'+code+'.'+captcha.format)
  return code
  captcha.close()

def ocr():
  pass

def getcaptcha(url):
  """Get image and return buffer"""
  import pycurl, StringIO
  
  string = StringIO.StringIO()
  curl = pycurl.Curl()
  
  curl.setopt(pycurl.WRITEFUNCTION, string.write)
  if settings.USER_AGENT != None:
    curl.setopt(pycurl.USERAGENT, settings.USER_AGENT)
  if settings.PROXY_ADDR != None:
    curl.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_SOCKS5)
    curl.setopt(pycurl.HTTPPROXYTUNNEL,1)
    curl.setopt(pycurl.PROXY, settings.PROXY_ADDR)
  curl.setopt(pycurl.URL, url)
  
  curl.perform()
  curl.close()
  return string.getvalue()
  string.close()
  

'''<form method=POST action="http://a1.beon.ru/p/add_topic.cgi">
<input type=hidden name="stage" value="final"><input type=hidden name="catry" value="2">
<input type=hidden name="user_type" value="anonymous"><input type=hidden name="add" value="Дoбавить тему Ctrl+Enter">
<input type=hidden name="subject" value=""><input type=hidden name="forum_id" value="16">
<input type=hidden name="topic_id" value="">
<input type=hidden name="message" value="holy test">Введите символы на картинке:<br>
<input type=hidden name=chash value="06a660449c0af5af833b14e2e83aff1e">
<img src="http://a1.beon.ru/i/captcha/06a660449c0af5af833b14e2e83aff1e.png"><br>
<input type=text name=cacode size=5><input type=submit value="Далее..."></form></td>


POST /p/add_topic.cgi HTTP/1.1
Host: beon.ru
Connection: keep-alive
User-Agent: Googlebot/2.1 (+http://www.googlebot.com/bot.html)
Referer: http://beon.ru/p/add_topic.cgi
Pragma: no-cache
Cache-control: no-cache
Accept: text/html, text/*;q=0.9, image/jpeg;q=0.9, image/png;q=0.9, image/*;q=0.9, */*;q=0.8
Accept-Encoding: gzip, deflate, x-gzip, x-deflate
Accept-Charset: utf-8,*;q=0.5
Accept-Language: ru,en-US;q=0.9,en;q=0.8
Cookie: ref=mynameislegion; u=waipu:; g=1; l=7292082b71296024a7302384b71294479a7298474b71237329a7298730b71237344a7298603b71236532a7254581b71232447a7296764b71232708a7297473b71231878a7287400b71232262a7298169b71230680a; p=-240:1920:1080:14468043:0:Y; __utma=55390132.473815080.1323751479.1326417283.1326424764.197; __utmb=55390132.10.10.1326424764; __utmc=55390132; __utmz=55390132.1325568423.141.6.utmcsr=beon.ru|utmccn=(referral)|utmcmd=referral|utmcct=/users/oracles/
Content-Type: application/x-www-form-urlencoded
Content-Length: 175

topic_id=&user_type=anonymous&login=&password=&topic_options=all&premoderate=nobody&subject=&forum_id=16&message=holy+test&add=%C4o%E1%E0%E2%E8%F2%FC+%F2%E5%EC%F3+Ctrl%2BEnter

POST /p/add_topic.cgi HTTP/1.1
Host: a1.beon.ru
Connection: keep-alive
User-Agent: Googlebot/2.1 (+http://www.googlebot.com/bot.html)
Referer: http://beon.ru/p/add_topic.cgi
Pragma: no-cache
Cache-control: no-cache
Accept: text/html, text/*;q=0.9, image/jpeg;q=0.9, image/png;q=0.9, image/*;q=0.9, */*;q=0.8
Accept-Encoding: gzip, deflate, x-gzip, x-deflate
Accept-Charset: utf-8,*;q=0.5
Accept-Language: ru,en-US;q=0.9,en;q=0.8
Cookie: ref=mynameislegion; u=waipu:; g=1; l=7292082b71296024a7302384b71294479a7298474b71237329a7298730b71237344a7298603b71236532a7254581b71232447a7296764b71232708a7297473b71231878a7287400b71232262a7298169b71230680a; p=-240:1920:1080:14468043:0:Y; __utma=55390132.473815080.1323751479.1326417283.1326424764.197; __utmb=55390132.11.10.1326424764; __utmc=55390132; __utmz=55390132.1325568423.141.6.utmcsr=beon.ru|utmccn=(referral)|utmcmd=referral|utmcct=/users/oracles/
Content-Type: application/x-www-form-urlencoded
Content-Length: 247

stage=final&catry=2&user_type=anonymous&add=%C4o%E1%E0%E2%E8%F2%FC+%F2%E5%EC%F3+Ctrl%2BEnter&forum_id=16&subject=&topic_id=&message=holy+test&login=&password=&topic_options=all&premoderate=nobody&chash=8b49dbf6df75e82ce4726cac8121a09d&cacode=c366c'''