# -*- coding: utf-8 -*-
import smtplib
import sys
sys_argv = ['fromaddr', 'toaddr', 'subj', 'msg_txt', 'server']
for i in sys_argv:
    print str(input(i))
fromaddr = ''
toaddr = ''
subj = ''
msg_txt = ''
msg = "From: %s\nTo: %s\nSubject: %s\n\n%s"  % ( fromaddr, toaddr, subj, msg_txt)
username = 'irina_bogdanova_22'
password = 'chikibambone'
server = smtplib.SMTP_SSL('')
server.login(username, password)
server.sendmail(fromaddr, toaddr, msg)
server.quit()
