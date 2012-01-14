#!/usr/bin/env python
# -*- coding: utf-8 -*-

USER_AGENT = "Googlebot/2.1 (+http://www.googlebot.com/bot.html)" #User-Agent for all operations.
PROXY_ADDR = "127.0.0.1:9050" #SOCKS proxy (tor) address. Type None for no proxy mode.


threadlimit = None #Posting threads limit. Default None.
wait = 30 #Wait time. Default may be 30.
errtimeout = 5 #Error timeout. Default may be 5.
randselect = True #Random element selection from list. Default True.
textfile = 'text.txt' #File for textgen.
imagelist = 'imagelist.txt'
separator = '<separator>'
stoponclose = True #Stop posting if topic closed. Default True, you may want to disable it.
ocr = None #Can be none, hands, chip or ocr. Default None and other not work 4n.
chipcom = ['sudo', "/etc/init.d/tor", 'restart'] # ip change (tor restart) command.
redirlim = 10 #REDIR rec limit for tor (ip change) ocr. Default 10.