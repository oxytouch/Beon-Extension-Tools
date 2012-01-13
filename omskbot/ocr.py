#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
import settings

redirlist = []

def main(ocrtype, target):
  if ocrtype == 'chip':
    chip(target)
  elif ocrtype == 'hands':
    pass
  elif ocrtype == 'ocr':
    pass

def chip(t, redirlim=settings.redirlim):
  redirlist.append(t)
  if redirlist.count(t) > redirlim:
    retc = subprocess.call(settings.chipcom)
    if retc != 0:
      print time.asctime(), "recive %s returncode, check chipcom." % (retc,)
    for i in range(settings.redirlim):
      redirlist.remove(t)

def hands(t, url):
  import StringIO
  captcha = Image.open(StringIO(buffer))
  print captcha.show()
  pass

def ocr():
  pass

def getcaptcha(url):
  """Get image and return string"""
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
  return string
  string.close()
  

