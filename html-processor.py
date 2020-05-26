import re

rexp1 = re.compile('<title>(.+?)</title>',re.DOTALL)

rexp2 = re.compile('<!--(.+?)-->',re.DOTALL)

#rexp3a = re.compile('<script.*?>(.+?)</script>',re.DOTALL)

#rexp3b = re.compile('<style>(.+?)</style>',re.DOTALL)

rexp3 = re.compile('<(style|script).*?>(.+?)</(style|script)>')

rexp4 = re.compile(r'<a(.*?href="(.+?)">.+?)</a>',re.DOTALL)

rexp5 = re.compile('<.*?>',re.DOTALL)

#html_entd= { '&amp;':'&','&gt;':'>','&lt;':'<','&nbsp;':' '}

def cb(m):
	if m.group(1) == 'amp':
		return  '&'
	elif m.group(1) == 'gt':
                return  '>'
	elif m.group(1) == 'lt':
                return  '<'
	elif m.group(1) == 'nbsp':
                return  ' '
rexp6 = re.compile('&(.+?);')

rexp7 = re.compile(r'\s+')

with open('testpage.txt','r') as fp:

	text = fp.read()

	for m in rexp1.finditer(text):
               print(m.group(1))
	
	for m2 in rexp4.finditer(text):
#		print('{} {}'.format(m2.group(2),m2.group(1)))
		print(m2.group(2))
		print(m2.group(1))

text = rexp2.sub(' ',text)

#text = rexp3a.sub(' ',text)
#text = rexp3b.sub(' ',text)
text = rexp3.sub(' ',text)

text = rexp5.sub(' ',text)

text = rexp6.sub(cb,text)

text = rexp7.sub(' ',text)

print(text)

