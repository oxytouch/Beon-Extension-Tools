#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pycurl, StringIO
import settings

postuser = None #User for posting(author). Default None.
postpass = None #Pass for posting(author). Default none.

def postmsg (topicid, text, user=None, postuser=postuser,postpass=postpass):
  """Posting message to topic"""
  postdata= {"ajax": "1",
   "topic_id": topicid,
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
  if settings.USER_AGENT != None:
    curl.setopt(pycurl.USERAGENT, settings.USER_AGENT)
  if settings.PROXY_ADDR != None:
    curl.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_SOCKS5)
    curl.setopt(pycurl.HTTPPROXYTUNNEL,1)
    curl.setopt(pycurl.PROXY, settings.PROXY_ADDR)
  if user == None:
    curl.setopt(pycurl.URL, 'http://beon.ru/p/add_comment.cgi')
  else:
    curl.setopt(pycurl.URL, 'http://'+user+'.beon.ru/p/add_comment.cgi')
  curl.setopt(pycurl.POSTFIELDS, DATA_POST)
  curl.setopt(pycurl.POST,1)
  
  curl.perform()
  curl.close()
  return string.getvalue()
  string.close()

def gettopics(f,b, forum='anonymous', user=None):
  """Get topics from user/forum."""
  string = StringIO.StringIO() 
  curl = pycurl.Curl()
  curl.setopt(pycurl.WRITEFUNCTION, string.write)
  if settings.USER_AGENT != None:
    curl.setopt(pycurl.USERAGENT, settings.USER_AGENT)
  if settings.PROXY_ADDR != None:
    curl.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_SOCKS5)
    curl.setopt(pycurl.HTTPPROXYTUNNEL,1)
    curl.setopt(pycurl.PROXY, settings.PROXY_ADDR)
  if user == None:
    for i in range(f,b):
      curl.setopt(pycurl.URL, 'http://beon.ru/'+forum+'/'+str(i)+'.html')
      curl.perform()
  else:
    for i in range(f,b):
      curl.setopt(pycurl.URL, 'http://'+user+'.beon.ru/'+str(i)+'.html')
      curl.perform()
  curl.close()
  return string.getvalue()
  string.close()

def addimg(link,size='original',orient='none'):
  """Add tags to img link."""
  return '[image-'+size+'-'+orient+'-'+link+']'

def getposts(topic, forum='anonymous', user=None):
  """Get posts from topic."""
  curl = pycurl.Curl()
  curl.setopt(pycurl.WRITEFUNCTION, string.write)
  if settings.USER_AGENT != None:
    curl.setopt(pycurl.USERAGENT, settings.USER_AGENT)
  if settings.PROXY_ADDR != None:
    curl.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_SOCKS5)
    curl.setopt(pycurl.HTTPPROXYTUNNEL,1)
    curl.setopt(pycurl.PROXY, settings.PROXY_ADDR)
  if user == None:
    curl.setopt(pycurl.URL, 'http://beon.ru/'+forum+'/'+topic)
  else:
    for i in range(f,b):
      curl.setopt(pycurl.URL, 'http://'+user+'.beon.ru/'+topic)
      curl.perform()
  curl.setopt(pycurl.URL, link)
  curl.perform()
  curl.close()
  return string.getvalue()
  string.close()
'''
POST /p/add_topic.cgi HTTP/1.1
Host: a1.beon.ru
{'topic_id': '',
'user_type': 'anonymous',
'login': '',
'password': '',
'topic_options': 'all',
'premoderate': 'nobody',
'subject': '',
'forum_id': '16',
'message': 'holy+test',
'add': '%C4o%E1%E0%E2%E8%F2%FC+%F2%E5%EC%F3+Ctrl%2BEnter'}

POST /p/add_topic.cgi HTTP/1.1
Host: beon.ru
{'stage': 'final',
'catry': '1', # Captcha tryings count.
'user_type': 'anonymous',
'add': '%C4o%E1%E0%E2%E8%F2%FC+%F2%E5%EC%F3+Ctrl%2BEnter',
'forum_id': '16',
'subject': '',
'topic_id': '',
'message': 'holy+test',
'login': '',
'password': '',
'topic_options': 'all',
'premoderate': 'nobody',
'chash': '8b49dbf6df75e82ce4726cac8121a09d',
'cacode': 'c366c'}
'''
'''
from beon import *
import re
topics = list(set(re.findall(linkregexp, gettopics(f,b))))
string = StringIO.StringIO()
curl = pycurl.Curl()
curl.setopt(pycurl.WRITEFUNCTION, string.write)
if settings.USER_AGENT != None:
  curl.setopt(pycurl.USERAGENT, settings.USER_AGENT)
if settings.PROXY_ADDR != None:
  curl.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_SOCKS5)
  curl.setopt(pycurl.HTTPPROXYTUNNEL,1)
  curl.setopt(pycurl.PROXY, settings.PROXY_ADDR)
for t in topics:
  curl.setopt(pycurl.URL, t)
  curl.perform()
  print .
curl.close()
plist = []
for p in list(set(re.findall(r"(http\:\/\/i\d*.beon\.ru\/1\/0\/1\/\d*\/\d*\/\d*\/Picture\d*\.jpeg)", string.getvalue()))):
  plist.append('[image-original-none-'+p+']')
string.close()
print plist
photoregexp = r"(http\:\/\/i\d*.beon\.ru\/1\/0\/1\/\d*\/\d*\/\d*\/Picture\d*\.jpeg)"'''
#kto-mne-tak
targetregexp = r"\/anonymous\/(\d*)-(\d*)\-[\w|\-]*([vb]-?i*-?r-?t|se(?:x|ks|kas)|eb(?:at|i)|t-?r-?a-?h|(?:-ja|ischu)-(?:m\-|j\-|zh\-|devushk|par(?:en|nja)|hozja)|ots[o|\-]s|rolevit|-sis[\-|e][kc]|v(?:-pop|du(?:i\-|va))|rabyn|droch|[ob]?liz(?:at\-|va[it])|hentai|shlju(?:hu|shk)|kisk[au]-(?:vsja|mokr)|do-orgazm|shali|min-?et|nakaz(?:iva|hi|at)|(?:parni|devushki)-kto-hochet|hoch(?:u|esh)-tak-)[\w|\-]*\-read\.shtml"
topicregexp = r"\/anonymous\/(\d*-\d*\-[\w|\-]*[A-Za-z1-9]*[\w|\-]*\-read\.shtml)" # General regexp for getposts.
regexp = r"\/anonymous\/(\d*)-(\d*)\-[\w|\-]*([A-Za-z1-9]*)[\w|\-]*\-read\.shtml" # General regexp for topic number.
picregexp = r"(http\:\/\/i\d*.beon\.ru\/1\/0\/1\/\d*\/\d*\/\d*\/Picture\d*\.jpeg)" # Regexp for beon pictures in posts. Added j4f.
redirrec = 'REDIR'
antispamrec = 'ERROR\xd1\xf0\xe0\xe1\xee\xf2\xe0\xeb\xe0 \xe7\xe0\xf9\xe8\xf2\xe0 \xee\xf2 \xf1\xef\xe0\xec\xe0. \xcf\xee\xe6\xe0\xeb\xf3\xe9\xf1\xf2\xe0, \xef\xee\xe4\xee\xe6\xe4\xe8\xf2\xe5 \xed\xe5\xea\xee\xf2\xee\xf0\xee\xe5 \xe2\xf0\xe5\xec\xff \xe8 \xef\xee\xef\xf0\xee\xe1\xf3\xe9\xf2\xe5 \xe4\xee\xe1\xe0\xe2\xe8\xf2\xfc \xea\xee\xec\xec\xe5\xed\xf2\xe0\xf0\xe8\xe9 \xf1\xed\xee\xe2\xe0.'
bumplimitrec = 'HIDEERROR\xcf\xf0\xe5\xe2\xfb\xf8\xe5\xed\xee \xec\xe0\xea\xf1\xe8\xec\xe0\xeb\xfc\xed\xee\xe5 \xea\xee\xeb\xe8\xf7\xe5\xf1\xf2\xe2\xee \xea\xee\xec\xec\xe5\xed\xf2\xe0\xf0\xe8\xe5\xe2 \xe2 \xee\xe4\xed\xee\xec \xf2\xee\xef\xe8\xea\xe5. \xd1\xee\xe7\xe4\xe0\xe9\xf2\xe5, \xef\xee\xe6\xe0\xeb\xf3\xe9\xf1\xf2\xe0, \xe4\xf0\xf3\xe3\xee\xe9 \xf2\xee\xef\xe8\xea \xe8 \xef\xf0\xee\xe4\xee\xeb\xe6\xe8\xf2\xe5 \xee\xe1\xf1\xf3\xe6\xe4\xe5\xed\xe8\xe5 \xe2 \xed\xb8\xec.'
userbumplimitrec = 'HIDEERROR\xcf\xf0\xe5\xe2\xfb\xf8\xe5\xed\xee \xec\xe0\xea\xf1\xe8\xec\xe0\xeb\xfc\xed\xee\xe5 \xea\xee\xeb\xe8\xf7\xe5\xf1\xf2\xe2\xee \xea\xee\xec\xec\xe5\xed\xf2\xe0\xf0\xe8\xe5\xe2 \xe4\xeb\xff \xee\xe4\xed\xee\xe9 \xe7\xe0\xef\xe8\xf1\xe8. \xcf\xf0\xee\xe4\xee\xeb\xe6\xe8\xf2\xe5, \xef\xee\xe6\xe0\xeb\xf3\xe9\xf1\xf2\xe0, \xee\xe1\xf1\xf3\xe6\xe4\xe5\xed\xe8\xe5 \xe2 \xe4\xf0\xf3\xe3\xee\xe9 \xe7\xe0\xef\xe8\xf1\xe8.'
succesrec = '1'
othersuccesrec = 'HIDE1' #TODO: why not 1? can`t find 'HIDE' trigger.
wrongauthrec = ''
cantaddrec = '' # Yep, ''.
cantaddcomrec = 'ERROR\xca\xee\xec\xec\xe5\xed\xf2\xe8\xf0\xee\xe2\xe0\xf2\xfc \xe7\xe0\xef\xe8\xf1\xfc \xec\xee\xe3\xf3\xf2 \xf2\xee\xeb\xfc\xea\xee \xf3\xf7\xe0\xf1\xf2\xed\xe8\xea\xe8 \xf1\xee\xee\xe1\xf9\xe5\xf1\xf2\xe2\xe0.'