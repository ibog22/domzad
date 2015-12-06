# -*- coding: utf-8 -*-
import smtplib
import argparse
from email.message import Message
from email.header import Header
parser = argparse.ArgumentParser()
parser.add_argument('--fromaddr', type=str, default='dominica18l@mail.ru')
parser.add_argument('--toaddr', type=str, default='irina_bogdanova_22@mail.ru')
parser.add_argument('--subj', type=str, default='Очередное адовое домашнее задание')
parser.add_argument('--msg_text', type=str, default='Что-то даже получилось')
parser.add_argument('--host', type=str, default='smtp.mail.ru')
parser.add_argument('--port', type=int, default=465)
args_parsed = parser.parse_args()
args_parsed = vars(args_parsed)
args_parsed['msg_text'] = ' '.join(args_parsed['msg_text'])
msg = Message()
msg.set_charset("utf-8")
h = Header(args_parsed['subj'], 'utf-8')
msg['subj'] = h
msg.set_payload(args_parsed['msg_text'].encode('base64'))
username = 'dominica18l'
password = '10021990'
server = smtplib.SMTP(args_parsed['host'], args_parsed['port'])
server.set_debuglevel(1);
server.starttls()
server.login('dominica18l@mail.ru', '10021990bis')
server.sendmail(args_parsed['fromaddr'], args_parsed['toaddr'], msg.as_string())
server.quit()