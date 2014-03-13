import os
import urllib
import urllib2
f = open('index.html')
con = f.read()
print(len(con))

cmd = """
curl -s --user 'api:key-4gvn2lebl2z9lquwo4kb72w2y31gv7-5' \ 
    https://api.mailgun.net/v2/caesarsgame.com/messages \ 
    -F from='caesars game <lhr@caesarsgame.com>' \
    -F to='caesars321@gmail.com' \
    -F to='liyonghelpme@foxmail.com' \ 
    -F to='lhr@caesarsgame.com' \
    -F recipient-variables='{"liyonghelpme@foxmail.com":{"name":liyonghelpme}, "caesars321@gmail.com":{"name":"caesars321"}}' \
    -F subject='Hello, %%recipient.name%%' \
    -F "html=@index.html"
""" 
#print cmd

data = {
    'html':con
}
d = urllib.urlencode(data)
nf = open('data.txt', 'w')
nf.write(d)
nf.close()

#os.system(cmd)
cmd = """
curl -s --user 'api:key-4gvn2lebl2z9lquwo4kb72w2y31gv7-5' \
    https://api.mailgun.net/v2/caesarsgame.com/messages \
    -F from='caesars game <lhr@caesarsgame.com>' \
    -F to='caesars321@gmail.com' \
    -F to='liyonghelpme@foxmail.com' \
    -F to='lhr@caesarsgame.com' \
    -F recipient-variables='{"liyonghelpme@foxmail.com":{"name":liyonghelpme}, "caesars321@gmail.com":{"name":"caesars321"}}' \
    -F subject='Hello, %%recipient.name%%' \
    -d @data.txt
"""
print cmd


d2 = {
'html':'<html><h1>hello world</h1><html>'
}
nf = open('data2.txt', 'w')
nf.write(urllib.urlencode(d2))
nf.close()

cmd2 = """

"""


