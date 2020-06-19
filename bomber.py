#-------------------------------------------------------------------------------
# Name:        Way2sms
# Purpose:   send sms way2sms #
# Author:      Rishabh Roy
# Created:     09/08/2014
#-------------------------------------------------------------------------------
import urllib2
import cookielib
import sys
username=  ""    #write ur mobile number for way2sms inside " " 
passwd=   ""       #password for way2sms inside " "
message=raw_input("messge u want to send ")
number=raw_input("number of person u want to send sms ")
message="+".join(message.split(' '))
url= 'Send Free SMS to any mobile in india'
data = 'username='+username+'&password='+passwd
cj =cookielib.CookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders=[('User-Agent',"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36")]
try:
        usock = opener.open(url,data)
except IOError:
    print "cannot connect "
    sys.exit(1)
jession_id=str(cj).split('~')[1].split(' ')[0]
print jession_id
p= opener.open("http://site21.way2sms.com/ebrdg.action?id="+jession_id)
send_sms_url='http://site21.way2sms.com/smstoss.action'
send_sms_data= 'ssaction=ss&Token='+jession_id+'&mobile='+number+'&message='+message+'&msgLen='+str(140-len(message))
opener.addheaders=[('Referer','http://site21.way2sms.com/sendSms?Token='+jession_id)]
try:
    sms_sent_page = opener.open(send_sms_url,send_sms_data)
except IOError as e :
    print e
p=opener.open('http://site21.way2sms.com/smscofirm.action?SentMessage='+message+'&Token='+jession_id+'&status=0')




    
