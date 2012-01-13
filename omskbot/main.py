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

def message():
  src = textgen.train(pastefile)
  text = ""
  for i in range(random.randint(3, 10)):
    text = text + "\n" + textgen.generate_sentence(src)
  text = text.encode('utf-8')
  return random.choice(['[image-original-none-http://i29.beon.ru/1/0/1/25/83/78508325/Picture100.jpeg]', '[image-original-none-http://i58.beon.ru/1/0/1/18/80/78508018/Picture95.jpeg]', '[image-original-none-http://i67.beon.ru/1/0/1/41/87/78508741/Picture103.jpeg]', '[image-original-none-http://i14.beon.ru/1/0/1/7/35/78503507/Picture56.jpeg]', '[image-original-none-http://i68.beon.ru/1/0/1/25/56/78505625/Picture73.jpeg]', '[image-original-none-http://i64.beon.ru/1/0/1/50/57/78495750/Picture40.jpeg]', '[image-original-none-http://i74.beon.ru/1/0/1/61/83/78498361/Picture51.jpeg]', '[image-original-none-http://i52.beon.ru/1/0/1/76/52/78505276/Picture68.jpeg]', '[image-original-none-http://i8.beon.ru/1/0/1/8/75/78507508/Picture90.jpeg]', '[image-original-none-http://i12.beon.ru/1/0/1/10/55/78505510/Picture72.jpeg]', '[image-original-none-http://i6.beon.ru/1/0/1/6/52/78505206/Picture67.jpeg]', '[image-original-none-http://i31.beon.ru/1/0/1/2/41/78504102/Picture60.jpeg]', '[image-original-none-http://i36.beon.ru/1/0/1/92/68/78506892/Picture84.jpeg]', '[image-original-none-http://i24.beon.ru/1/0/1/59/72/78507259/Picture87.jpeg]', '[image-original-none-http://i25.beon.ru/1/0/1/11/72/78507211/Picture86.jpeg]', '[image-original-none-http://i91.beon.ru/1/0/1/91/79/78497991/Picture48.jpeg]', '[image-original-none-http://i6.beon.ru/1/0/1/75/49/78494975/Picture37.jpeg]', '[image-original-none-http://i14.beon.ru/1/0/1/57/65/78506557/Picture81.jpeg]', '[image-original-none-http://i29.beon.ru/1/0/1/59/82/78508259/Picture99.jpeg]', '[image-original-none-http://i50.beon.ru/1/0/1/5/50/78505005/Picture64.jpeg]', '[image-original-none-http://i10.beon.ru/1/0/1/26/81/78498126/Picture49.jpeg]', '[image-original-none-http://i67.beon.ru/1/0/1/48/86/78508648/Picture102.jpeg]', '[image-original-none-http://i85.beon.ru/1/0/1/85/85/78498585/Picture52.jpeg]', '[image-original-none-http://i91.beon.ru/1/0/1/82/88/78508882/Picture106.jpeg]', '[image-original-none-http://i75.beon.ru/1/0/1/17/38/78503817/Picture58.jpeg]', '[image-original-none-http://i20.beon.ru/1/0/1/23/34/78503423/Picture55.jpeg]', '[image-original-none-http://i24.beon.ru/1/0/1/30/82/78498230/Picture50.jpeg]', '[image-original-none-http://i36.beon.ru/1/0/1/15/88/78508815/Picture104.jpeg]', '[image-original-none-http://i2.beon.ru/1/0/1/22/53/78505322/Picture69.jpeg]', '[image-original-none-http://i95.beon.ru/1/0/1/27/43/78494327/Picture32.jpeg]', '[image-original-none-http://i32.beon.ru/1/0/1/58/79/78507958/Picture94.jpeg]', '[image-original-none-http://i70.beon.ru/1/0/1/19/76/78507619/Picture91.jpeg]', '[image-original-none-http://i27.beon.ru/1/0/1/39/60/78506039/Picture76.jpeg]', '[image-original-none-http://i75.beon.ru/1/0/1/62/58/78495862/Picture41.jpeg]', '[image-original-none-http://i34.beon.ru/1/0/1/72/81/78508172/Picture98.jpeg]', '[image-original-none-http://i34.beon.ru/1/0/1/28/63/78506328/Picture78.jpeg]', '[image-original-none-http://i23.beon.ru/1/0/1/61/39/78493961/Picture30.jpeg]', '[image-original-none-http://i46.beon.ru/1/0/1/57/67/78506757/Picture82.jpeg]', '[image-original-none-http://i43.beon.ru/1/0/1/71/87/78498771/Picture54.jpeg]', '[image-original-none-http://i76.beon.ru/1/0/1/41/88/78508841/Picture105.jpeg]', '[image-original-none-http://i24.beon.ru/1/0/1/84/38/78503884/Picture59.jpeg]', '[image-original-none-http://i94.beon.ru/1/0/1/7/55/78495507/Picture39.jpeg]', '[image-original-none-http://i76.beon.ru/1/0/1/41/88/78508841/Picture105.jpeg]', '[image-original-none-http://i81.beon.ru/1/0/1/60/74/78507460/Picture88.jpeg]', '[image-original-none-http://i3.beon.ru/1/0/1/0/58/78505800/Picture74.jpeg]', '[image-original-none-http://i2.beon.ru/1/0/1/56/78/78497856/Picture46.jpeg]', '[image-original-none-http://i85.beon.ru/1/0/1/85/85/78498585/Picture52.jpeg]', '[image-original-none-http://i91.beon.ru/1/0/1/82/88/78508882/Picture106.jpeg]', '[image-original-none-http://i50.beon.ru/1/0/1/76/60/78496076/Picture43.jpeg]', '[image-original-none-http://i54.beon.ru/1/0/1/73/51/78505173/Picture66.jpeg]', '[image-original-none-http://i36.beon.ru/1/0/1/51/71/78507151/Picture85.jpeg]', '[image-original-none-http://i46.beon.ru/1/0/1/92/64/78506492/Picture79.jpeg]', '[image-original-none-http://i4.beon.ru/1/0/1/40/54/78505440/Picture71.jpeg]', '[image-original-none-http://i42.beon.ru/1/0/1/47/47/78494747/Picture35.jpeg]', '[image-original-none-http://i97.beon.ru/1/0/1/86/83/78508386/Picture101.jpeg]', '[image-original-none-http://i62.beon.ru/1/0/1/44/78/78507844/Picture92.jpeg]', '[image-original-none-http://i70.beon.ru/1/0/1/58/50/78505058/Picture65.jpeg]', '[image-original-none-http://i5.beon.ru/1/0/1/8/81/78508108/Picture97.jpeg]', '[image-original-none-http://i25.beon.ru/1/0/1/41/61/78506141/Picture77.jpeg]', '[image-original-none-http://i98.beon.ru/1/0/1/96/35/78503596/Picture57.jpeg]', '[image-original-none-http://i22.beon.ru/1/0/1/90/59/78505990/Picture75.jpeg]', '[image-original-none-http://i15.beon.ru/1/0/1/39/42/78504239/Picture62.jpeg]', '[image-original-none-http://i47.beon.ru/1/0/1/65/48/78504865/Picture63.jpeg]', '[image-original-none-http://i81.beon.ru/1/0/1/60/74/78507460/Picture88.jpeg]', '[image-original-none-http://i7.beon.ru/1/0/1/40/79/78507940/Picture93.jpeg]', '[image-original-none-http://i66.beon.ru/1/0/1/66/41/78504166/Picture61.jpeg]', '[image-original-none-http://i23.beon.ru/1/0/1/40/41/78574140/Picture220.jpeg]', '[image-original-none-http://i67.beon.ru/1/0/1/83/18/78571883/Picture11.jpeg]', '[image-original-none-http://i29.beon.ru/1/0/1/94/41/78574194/Picture221.jpeg]', '[image-original-none-http://i4.beon.ru/1/0/1/88/73/78537388/Picture115.jpeg]', '[image-original-none-http://i76.beon.ru/1/0/1/89/27/78572789/Picture210.jpeg]', '[image-original-none-http://i92.beon.ru/1/0/1/49/72/78537249/Picture114.jpeg]', '[image-original-none-http://i47.beon.ru/1/0/1/29/44/78564429/Picture203.jpeg]', '[image-original-none-http://i11.beon.ru/1/0/1/85/71/78567185/Picture205.jpeg]', '[image-original-none-http://i16.beon.ru/1/0/1/68/28/78572868/Picture211.jpeg]', '[image-original-none-http://i43.beon.ru/1/0/1/0/86/78538600/Picture124.jpeg]', '[image-original-none-http://i45.beon.ru/1/0/1/86/83/78538386/Picture121.jpeg]', '[image-original-none-http://i42.beon.ru/1/0/1/13/34/78573413/Picture215.jpeg]', '[image-original-none-http://i71.beon.ru/1/0/1/26/27/78572726/Picture209.jpeg]', '[image-original-none-http://i44.beon.ru/1/0/1/97/29/78572997/Picture212.jpeg]', '[image-original-none-http://i93.beon.ru/1/0/1/6/45/78574506/Picture223.jpeg]', '[image-original-none-http://i66.beon.ru/1/0/1/0/41/78574100/Picture219.jpeg]', '[image-original-none-http://i55.beon.ru/1/0/1/94/45/78574594/Picture224.jpeg]', '[image-original-none-http://i53.beon.ru/1/0/1/21/71/78537121/Picture113.jpeg]', '[image-original-none-http://i18.beon.ru/1/0/1/3/32/78573203/Picture214.jpeg]', '[image-original-none-http://i42.beon.ru/1/0/1/98/24/78572498/Picture208.jpeg]', '[image-original-none-http://i46.beon.ru/1/0/1/67/80/78538067/Picture117.jpeg]', '[image-original-none-http://i75.beon.ru/1/0/1/21/51/78565121/Picture205.jpeg]', '[image-original-none-http://i52.beon.ru/1/0/1/74/34/78573474/Picture216.jpeg]', '[image-original-none-http://i33.beon.ru/1/0/1/79/97/78539779/Picture135.jpeg]', '[image-original-none-http://i91.beon.ru/1/0/1/27/64/78566427/Picture206.jpeg]', '[image-original-none-http://i77.beon.ru/1/0/1/85/82/78538285/Picture120.jpeg]', '[image-original-none-http://i69.beon.ru/1/0/1/92/42/78574292/Picture222.jpeg]', '[image-original-none-http://i69.beon.ru/1/0/1/12/17/78571712/Picture10.jpeg]', '[image-original-none-http://i29.beon.ru/1/0/1/25/68/78566825/Picture207.jpeg]', '[image-original-none-http://i25.beon.ru/1/0/1/68/14/78571468/Picture9.jpeg]', '[image-original-none-http://i52.beon.ru/1/0/1/52/99/78539952/Picture138.jpeg]', '[image-original-none-http://i37.beon.ru/1/0/1/98/35/78563598/Picture200.jpeg]', '[image-original-none-http://i71.beon.ru/1/0/1/76/87/78538776/Picture125.jpeg]', '[image-original-none-http://i78.beon.ru/1/0/1/2/31/78573102/Picture213.jpeg]', '[image-original-none-http://i48.beon.ru/1/0/1/42/85/78538542/Picture123.jpeg]', '[image-original-none-http://i72.beon.ru/1/0/1/28/34/78543428/Picture157.jpeg]', '[image-original-none-http://i47.beon.ru/1/0/1/25/30/78543025/Picture154.jpeg]', '[image-original-none-http://i86.beon.ru/1/0/1/14/2/78540214/Picture141.jpeg]', '[image-original-none-http://i42.beon.ru/1/0/1/20/69/78536920/Picture112.jpeg]', '[image-original-none-http://i89.beon.ru/1/0/1/60/53/78555360/Picture192.jpeg]', '[image-original-none-http://i71.beon.ru/1/0/1/6/62/78536206/Picture112.jpeg]', '[image-original-none-http://i10.beon.ru/1/0/1/3/33/78553303/Picture181.jpeg]', '[image-original-none-http://i65.beon.ru/1/0/1/26/81/78538126/Picture118.jpeg]', '[image-original-none-http://i26.beon.ru/1/0/1/16/3/78540316/Picture142.jpeg]', '[image-original-none-http://i96.beon.ru/1/0/1/25/31/78543125/Picture155.jpeg]', '[image-original-none-http://i95.beon.ru/1/0/1/16/95/78539516/Picture132.jpeg]', '[image-original-none-http://i77.beon.ru/1/0/1/77/12/78541277/Picture145.jpeg]', '[image-original-none-http://i83.beon.ru/1/0/1/74/29/78552974/Picture179.jpeg]', '[image-original-none-http://i90.beon.ru/1/0/1/69/38/78553869/Picture186.jpeg]', '[image-original-none-http://i11.beon.ru/1/0/1/23/38/78523823/Picture1586.jpeg]', '[image-original-none-http://i10.beon.ru/1/0/1/83/53/78535383/Picture109.jpeg]', '[image-original-none-http://i20.beon.ru/1/0/1/7/29/78542907/Picture153.jpeg]', '[image-original-none-http://i57.beon.ru/1/0/1/98/96/78539698/Picture134.jpeg]', '[image-original-none-http://i72.beon.ru/1/0/1/35/9/78550935/Picture170.jpeg]', '[image-original-none-http://i58.beon.ru/1/0/1/59/12/78551259/Picture172.jpeg]', '[image-original-none-http://i20.beon.ru/1/0/1/48/37/78543748/Picture159.jpeg]', '[image-original-none-http://i8.beon.ru/1/0/1/46/75/78537546/Picture116.jpeg]', '[image-original-none-http://i19.beon.ru/1/0/1/46/25/78542546/Picture150.jpeg]', '[image-original-none-http://i97.beon.ru/1/0/1/37/37/78553737/Picture185.jpeg]', '[image-original-none-http://i80.beon.ru/1/0/1/70/18/78551870/Picture175.jpeg]', '[image-original-none-http://i71.beon.ru/1/0/1/96/33/78553396/Picture182.jpeg]', '[image-original-none-http://i53.beon.ru/1/0/1/71/28/78562871/Picture195.jpeg]', '[image-original-none-http://i8.beon.ru/1/0/1/6/94/78539406/Picture131.jpeg]', '[image-original-none-http://i71.beon.ru/1/0/1/50/88/78538850/Picture126.jpeg]', '[image-original-none-http://i81.beon.ru/1/0/1/62/40/78554062/Picture188.jpeg]', '[image-original-none-http://i95.beon.ru/1/0/1/88/91/78539188/Picture129.jpeg]', '[image-original-none-http://i65.beon.ru/1/0/1/34/64/78536434/Picture111.jpeg]', '[image-original-none-http://i63.beon.ru/1/0/1/71/15/78541571/Picture146.jpeg]', '[image-original-none-http://i60.beon.ru/1/0/1/64/34/78553464/Picture183.jpeg]', '[image-original-none-http://i95.beon.ru/1/0/1/16/25/78552516/Picture178.jpeg]', '[image-original-none-http://i70.beon.ru/1/0/1/73/30/78553073/Picture180.jpeg]', '[image-original-none-http://i94.beon.ru/1/0/1/6/3/78550306/Picture169.jpeg]', '[image-original-none-http://i71.beon.ru/1/0/1/23/99/78539923/Picture137.jpeg]', '[image-original-none-http://i62.beon.ru/1/0/1/10/23/78552310/Picture177.jpeg]', '[image-original-none-http://i67.beon.ru/1/0/1/81/21/78552181/Picture176.jpeg]', '[image-original-none-http://i23.beon.ru/1/0/1/70/49/78544970/Picture167.jpeg]', '[image-original-none-http://i20.beon.ru/1/0/1/41/26/78542641/Picture151.jpeg]', '[image-original-none-http://i49.beon.ru/1/0/1/59/17/78541759/Picture147.jpeg]', '[image-original-none-http://i77.beon.ru/1/0/1/34/40/78544034/Picture161.jpeg]', '[image-original-none-http://i33.beon.ru/1/0/1/5/38/78543805/Picture160.jpeg]', '[image-original-none-http://i89.beon.ru/1/0/1/66/27/78542766/Picture152.jpeg]', '[image-original-none-http://i71.beon.ru/1/0/1/35/93/78539335/Picture130.jpeg]', '[image-original-none-http://i85.beon.ru/1/0/1/70/89/78538970/Picture127.jpeg]', '[image-original-none-http://i90.beon.ru/1/0/1/96/35/78543596/Picture158.jpeg]', '[image-original-none-http://i18.beon.ru/1/0/1/34/48/78534834/Picture167.jpeg]', '[image-original-none-http://i35.beon.ru/1/0/1/90/81/78538190/Picture119.jpeg]', '[image-original-none-http://i68.beon.ru/1/0/1/69/45/78544569/Picture164.jpeg]', '[image-original-none-http://i13.beon.ru/1/0/1/17/41/78544117/Picture162.jpeg]', '[image-original-none-http://i97.beon.ru/1/0/1/32/51/78555132/Picture191.jpeg]', '[image-original-none-http://i74.beon.ru/1/0/1/41/36/78553641/Picture184.jpeg]', '[image-original-none-http://i61.beon.ru/1/0/1/16/43/78544316/Picture163.jpeg]', '[image-original-none-http://i91.beon.ru/1/0/1/68/19/78541968/Picture148.jpeg]', '[image-original-none-http://i7.beon.ru/1/0/1/42/4/78540442/Picture143.jpeg]', '[image-original-none-http://i43.beon.ru/1/0/1/78/84/78538478/Picture122.jpeg]', '[image-original-none-http://i3.beon.ru/1/0/1/98/31/78543198/Picture156.jpeg]', '[image-original-none-http://i55.beon.ru/1/0/1/49/21/78542149/Picture149.jpeg]', '[image-original-none-http://i20.beon.ru/1/0/1/30/32/78563230/Picture197.jpeg]', '[image-original-none-http://i84.beon.ru/1/0/1/58/90/78539058/Picture128.jpeg]', '[image-original-none-http://i60.beon.ru/1/0/1/1/96/78539601/Picture133.jpeg]', '[image-original-none-http://i62.beon.ru/1/0/1/60/16/78551660/Picture174.jpeg]', '[image-original-none-http://i15.beon.ru/1/0/1/59/46/78544659/Picture165.jpeg]', '[image-original-none-http://i3.beon.ru/1/0/1/40/98/78539840/Picture136.jpeg]', '[image-original-none-http://i22.beon.ru/1/0/1/97/98/78549897/Picture168.jpeg]', '[image-original-none-http://i92.beon.ru/1/0/1/99/48/78554899/Picture190.jpeg]', '[image-original-none-http://i44.beon.ru/1/0/1/9/1/78540109/Picture140.jpeg]', '[image-original-none-http://i27.beon.ru/1/0/1/37/59/78555937/Picture193.jpeg]', '[image-original-none-http://i72.beon.ru/1/0/1/34/8/78550834/Picture168.jpeg]', '[image-original-none-http://i90.beon.ru/1/0/1/92/99/78539992/Picture139.jpeg]'])+'\n'+ text

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