#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re, time, random, thread
import settings
#from threading import Thread
import beon, ltalk, mindmix, textgen

string = StringIO.StringIO()
curl = pycurl.Curl()

regexp = r"\/anonymous\/(\d*)-(\d*)\-[\w|\-]*(virt|sex|seks|ebat|ebi|trah|[A-Za-z1-9]*)[\w|\-]*\-read\.shtml"
terminated = []
downed = []
protected = []
pastefile = "text.txt"

def message(gen='textgen',pastefile=settings.pastefile,min=3,max=10):
  if gen == 'textgen':
    src = textgen.train(pastefile)
    text = ""
    for i in range(random.randint(min, max)):
      text = text + "\n" + textgen.generate_sentence(src)
    text = text.encode('utf-8')
  elif gen == 'wordsgen':
    text = ""
    for i in range(random.randint(3, 10)):
      words = ""
      for i in range(random.randint(3, 10)):
	words = words + wordsgen.gen_word() + " "
      text = text + "%s.\n" % (words)
  return text

def posting(t, r, site, msg=None, user=None, stoponclose=settings.stoponclose, ocrtype=settings.ocr):
  target = ''.join(t[:2])
  for i in xrange(r):
    try:
      if msg == None:  
	rec = site.postmsg(target, message(), user)
      else:
	rec = site.postmsg(target, msg, user)
    except pycurl.error:
      print time.asctime(), "post error on %s post in %s, waiting" % (i, t)
      time.sleep(settings.errtimeout)
    else:
      if rec == site.redirrec:
	if ocrtype != None:
	  import ocr
	  code = ocr.main(ocrtype, t)
	  if code != None:
	    pass # Lock all posting threads and send code?
	else:
	  print time.asctime(), "rec redir on %s in %s: captcha or other shit, waiting" % (i, t)
	  time.sleep(settings.errtimeout)
      elif rec == site.antispamrec:
	print time.asctime(), "antispam detect on %s in %s, waiting" % (i, t)
	time.sleep(settings.errtimeout)
      elif rec == site.bumplimitrec or user != None and rec == site.userbumplimitrec:
	print time.asctime(), "bumplimit reached in %s, stop posting" % (t,)
	thread.exit()
      elif rec == site.cantaddrec or user != None and rec == site.cantaddcomrec:
	if stoponclose == True:
	  print time.asctime(), "%s closed, stop posting" % (t,)
	  thread.exit()
	else:
	  print time.asctime(), "post %s in %s can`t be posted, waiting" % (i, t)
	  time.sleep(settings.errtimeout)
      elif rec == site.succesrec or rec == site.othersuccesrec:
	print time.asctime(), "post %s in %s posted" % (i, t)
      else:
	print time.asctime(), "post %s in %s posted.. or not posted, lol" % (i, t)
	print rec.decode('cp1251')

def onbump(site,regexp=None,wait=30,threads=1,posts=1,f=1,b=2):
  print time.asctime(), "onbump force thread on %s started" % str(site)
  terminated = []
  while True:
    print time.asctime(), "request and scan topics"
    try:
      page = site.gettopics(f,b)
    except pycurl.error:
      print time.asctime(), "connection error, waiting"
    else:
      if regexp == None:
	found = list(set(re.findall(site.regexp, page)))
      else:
	found = list(set(re.findall(regexp, page)))
      if found == []:
	print time.asctime(), "no targets found"
      else:
	for t in found:
	  if t not in protected:
	    if t not in terminated:
	      print time.asctime(), "found %s, terminating" % (t,)
	      for i in range(threads):
		thread.start_new_thread(posting, (t, posts, site))
	      terminated.append(t)
      for t in terminated:
	if t not in found:
	  print time.asctime(), "removing downed %s from terminated" % (t,)
	  terminated.remove(t)
    time.sleep(wait)

def force(site,regexp=None,wait=30,threads=3,posts=1,f=1,b=6):
  print time.asctime(), "force thread on %s started" % str(site)
  while True:
    print time.asctime(), "request and scan topics"
    try:
      page = site.gettopics(f,b)
    except pycurl.error:
      print time.asctime(), "connection error, waiting"
    else:
      if regexp == None:
	found = list(set(re.findall(site.regexp, page)))
      else:
	found = list(set(re.findall(regexp, page)))
      if found == []:
	print time.asctime(), "no targets found"
      else:
	for i in range(threads):
	  t = random.choice(found)
	  if t in protected:
	    print time.asctime(), "%s protected, waiting" % (t,)
	  else:
	    print time.asctime(), "selected %s, posting" % (t,)
	    thread.start_new_thread(posting, (t, posts, site))
    time.sleep(wait)

def autobump(site,regexp=None,wait=30,f=5,b=11):
  print time.asctime(), "autobump thread on %s started" % str(site)
  while True:
    print time.asctime(), "request and scan topics"
    try:
      page = site.gettopics(f,b)
    except pycurl.error:
      print time.asctime(), "connection error, waiting"
    else:
      if regexp == None:
	found = list(set(re.findall(site.regexp, page)))
      else:
	found = list(set(re.findall(regexp, page)))
      if found == []:
	print time.asctime(), "no targets found, all right with teh threads"
      else:
	for t in found:
	  if t in protected:
	    print time.asctime(), "%s protected, bumping" % (t,)
	    thread.start_new_thread(posting, (t, 1, site, 'autobump же'))
	  else:
	    #print time.asctime(), "selected %s is not protected" % (t,)
	    pass
    time.sleep(wait)

def userwipe(site,user,regexp=None,threads=1,posts=100500,wait=30,f=1,b=2):
  print time.asctime(), "user wipe thread on %s started" % str(site)
  terminated = []
  while True:
    print time.asctime(), "request and scan topics"
    try:
      page = site.gettopics(f,b,user=user)
    except pycurl.error:
      print time.asctime(), "connection error, waiting"
    else:
      if regexp == None:
	found = list(set(re.findall(site.regexp, page)))
      else:
	found = list(set(re.findall(regexp, page)))
      if found == []:
	print time.asctime(), "no targets found"
      else:
	for t in found:
	    if t not in terminated:
	      print time.asctime(), "found %s, terminating" % (t,)
	      for i in range(threads):
		thread.start_new_thread(posting, (t,posts,site,None,user))
	      terminated.append(t)
    time.sleep(wait)

if __name__ == "__main__":
  print time.asctime(), "main thread started"
  '''def message():  
    src = open('anal.txt').read()
    msg = random.choice(src.split('<post-separator>'))
    return '[image-original-none-http://s.lurkmore.to/images/e/ef/%D0%90%D0%9A.jpg]\n'+msg
  thread.start_new_thread(force, (regexp,ltalk))
  thread.start_new_thread(force, (regexp,mindmix))
  force(regexp,beon)'''
  '''import sys, time
  site = beon #sys.argv[1]
  #if sys.argv[2] == 'none':
    #user = None
    #forum = sys.argv[3]
  #else:
  user = sys.argv[2]
  def message():
    import random, textgen
    src = textgen.train('necropaste.txt')
    text = ""
    for i in range(random.randint(3, 30)):
      text = text + "\n" + textgen.generate_sentence(src)
    text = text.encode('utf-8')
    return "[image-original-none-http://www.porjati.net/uploads/posts/2010-03/1269899770_1.jpg]\n[image-original-none-http://abutton.ru/uploads/posts/2011-03/13006454218743.jpeg]\n[image-original-none-http://beremenna-ya.narod.ru/images/samoproizvolnoe.prerivanie.beremennosti.jpg]\n[image-original-none-http://www.realisti.ru/upload/UserFiles/abortion-scream.jpg]\n[image-original-none-http://cs1249.vkontakte.ru/u2144059/12989474/x_3769c9a6.jpg]\n[image-original-none-http://demotivation.me/images/20081102/pr5xf2wcxhxz.jpg]\n[image-original-none-http://mystery-queen.com/data_images/Говно/Говно-01.jpg]\n[image-original-none-http://s.lurkmore.to/images/3/37/2ch35.jpg]\n[image-original-none-http://s.lurkmore.to/images/2/2c/124515683084.jpg]\n[image-original-none-http://s.lurkmore.to/images/a/a1/1261789192008.jpg]\n[image-original-none-http://s.lurkmore.to/images/4/48/1255809767106.jpg]\n[image-original-none-http://s.lurkmore.to/images/d/d5/2ch22.jpg]\n[image-original-none-http://s.lurkmore.to/images/9/92/2ch30.jpg]\n[image-original-none-http://img3.imagetitan.com/img1/1/35/shit2.jpg]\n[image-original-none-http://edge.ebaumsworld.com/picture/Socojo/ShitBricks.png]\n"+ text
  userwipe(site,user,r"\/"+user+".beon.ru\/(\d*)-(\d*)\-[\w|\-]*([A-Za-z1-9]*)[\w|\-]*\.zhtml")'''
  '''thread.start_new_thread(onbump, (beon,))
  autobump(beon,)'''