import httplib
import urllib
import urllib2
import json
import logging
def req(r, data):
    q = urllib2.urlopen(r, urllib.urlencode(data))
    s = q.read()
    print s
    return s

def accreq(r, data, header, ty):
    print r
    if data != None:
        req = urllib2.Request(r, urllib.urlencode(data))
    else:
        req = urllib2.Request(r)

    req.add_header('Authorization', '%s %s' % (ty, header))
    print "request is", req

    res = urllib2.urlopen(req)
    s = res.read()
    print s
    return s


r = 'https://exmail.qq.com/cgi-bin/token'
data = {
'grant_type':'client_credentials',
'client_id':'liyonghelpme',
'client_secret':'32e123a1efe5164d4f62ab1f6168fe0a',
}
s = req(r, data)
#print s
user = json.loads(s)
act = user['access_token']
ty = user['token_type']

r = 'http://openapi.exmail.qq.com:12211/openapi/mail/authkey'
data = {
'alias':'lhr@caesarsgame.com'
}
s = accreq(r, data, act, ty)
s = json.loads(s)
ak = s['auth_key']

r = 'https://exmail.qq.com/cgi-bin/login?fun=bizopenssologin&method=bizauth&agent=liyonghelpme&user=lhr@caesarsgame.com&ticket=%s' % (ak)
s = accreq(r, None, act, ty)

r = 'http://openapi.exmail.qq.com:12211/openapi/mail/list'
data = {
'alias':'lhr@caesarsgame.com',
'limit':1000,
'filterfield':0,
'filtervalue':0,
}

s = accreq(r, data, act, ty)
allU = json.loads(s)
uList = {}

import re
email = re.compile('<(.*)>')
print "allUse is"
for k in allU['List']:
    send = k['Sender']
    e = email.findall(send)
    print e
    #print send
    if len(e) > 0:
        uList[e[0]] = True
    else:
        print "error user", send


print 'allUser'
for k in uList:
    print k





