import httplib
import urllib
import urllib2
import json
import requests


def req(r, data):
    print r
    #print data
    q = urllib2.urlopen(r, urllib.urlencode(data))
    s = q.read()
    print s
    return s

con = open('index.html')
con = con.read()

data = {
    'from': 'caesars game <lhr@caesarsgame.com>',
    'html':con,
    'recipient-variables':'{"liyonghelpme@foxmail.com":{"name":"liyonghelpme"}, "liyonghelpme@gmail.com":{"name":"gmailme"}}',
    'to':['liyonghelpme@foxmail.com', 'liyonghelpme@gmail.com'],
    'subject':'Hello, %recipient.name%',
    'text':'mail from caesars game studio'
}
r = 'https://api.mailgun.net/v2/caesarsgame.com/messages'

aukey = ('api', 'key-4gvn2lebl2z9lquwo4kb72w2y31gv7-5')

print len(data['html'])
r = requests.post(r, auth=aukey, data=data)
print r
print r.text
print r.encoding


