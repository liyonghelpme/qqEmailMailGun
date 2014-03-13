curl --user 'api:key-4gvn2lebl2z9lquwo4kb72w2y31gv7-5' \
    https://api.mailgun.net/v2/caesarsgame.com/messages \
    -F from='caesars game <lhr@caesarsgame.com>' \
    -F to='liyonghelpme@foxmail.com' \
    -F recipient-variables='{"liyonghelpme@foxmail.com":{"name":"liyonghelpme"}, "caesars321@gmail.com":{"name":"caesars321"}}' \
    -F subject='Hello, %%recipient.name%%' \
    --form-string html='<html><iframe src="index.html" style="top:0px; left:0px; right:0px; width:100%; height:100%;"></iframe></html>' \
    -F attachment=@index.html
