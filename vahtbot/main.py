#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re, time, random, thread, pycurl, StringIO
import settings, wordsgen, beon, ltalk, mindmix, gyxu

def message():
  text = ""
  for i in range(random.randint(3, 10)):
    words = ""
    for i in range(random.randint(3, 10)):
	words = words + wordsgen.gen_word() + " "
    text = text + "%s.\n" % (words)
  return "[H][B]U hv bn VahtBot`ed!\nBMSMA, Captcha is powerless, this thread will die! GTFO![/H][/B]\n[image-original-none-http://i019.radikal.ru/0803/b7/08846e75bfbc.gif][image-original-none-http://img167.imageshack.us/img167/2088/443yk2.gif]\n"+ text

def posting(t, r, site, msg=None, user=None):
  target = ''.join(t[:2])
  for i in xrange(r):
    try:
      if msg == None:  
	rec = site.postmsg(target, message(), user)
      else:
	rec = site.postmsg(target, msg, user)
    except pycurl.error:
      print time.asctime(), "post error on %s post in %s, waiting" % (i, t)
      time.sleep(5)
    else:
      if rec == site.redirrec:
	print time.asctime(), "rec redir on %s in %s: captcha or other shit" % (i, t)
      elif rec == site.antispamrec:
	print time.asctime(), "antispam detect on %s in %s, waiting" % (i, t)
	time.sleep(5)
      elif rec == site.bumplimitrec or user != None and rec == site.userbumplimitrec:
	print time.asctime(), "bumplimit reached in %s, stop posting" % (t,)
	thread.exit()
      elif rec == site.cantaddrec:
	print time.asctime(), "post %s in %s can`t be posted, waiting" % (i, t)
	time.sleep(5)
      elif rec == site.succesrec:
	print time.asctime(), "post %s in %s posted" % (i, t)
      else:
	print time.asctime(), "post %s in %s posted.. or not posted, lol" % (i, t)
	print rec.decode('cp1251')

def threadwipe(site,regexp=None,wait=30,threads=1,posts=200,f=1,b=2):
  print time.asctime(), "threadwipe thread on %s started" % str(site)
  terminated = []
  downed = []
  while True:
    print time.asctime(), "request and scan topics"
    try:
      page = site.gettopics(f,b)
    except pycurl.error:
      print time.asctime(), "connection error, waiting"
    else:
      if regexp == None:
	found = list(set(re.findall(site.targetregexp, page)))
      else:
	found = list(set(re.findall(regexp, page)))
      if found == []:
	print time.asctime(), "no targets found"
      else:
	for t in found:
	  if t in downed:
	    print time.asctime(), "%s bumped by someone, terminating again" % (t,)
	    downed.remove(t)
	  if t in terminated:
	    print time.asctime(), "lol, %s already terminated" % (t,)
	  else:
	    print time.asctime(), "found %s, terminating" % (t,)
	    for i in range(threads):
	      thread.start_new_thread(posting, (t, posts, site))
	    terminated.append(t)
      for t in terminated:
	if t not in found:
	  print time.asctime(), "removing downed %s from terminated" % (t,)
	  downed.append(t)
	  terminated.remove(t)
    time.sleep(wait)

if __name__ == "__main__":
  thread.start_new_thread(threadwipe, (mindmix,))
  thread.start_new_thread(threadwipe, (ltalk,))
  thread.start_new_thread(threadwipe, (gyxu,))
  threadwipe(beon,)
