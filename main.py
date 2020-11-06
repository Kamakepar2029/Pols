import requests
import lxml.html
import os

print('Structure type:\nDiscovered open port 80/tcp on 176.52.247.66\nDiscovered open port 80/tcp on 107.154.218.233')



print('https://raw.githubusercontent.com/Kamakepar2029/allnerwork/main/allnetworksdiscovered.txt')

url = str(input('Url with structure: '))

netfile = requests.get(url)
massof = (netfile.text).split('\n')

tohtmlfile = '<head><title>Scanned Ports ans Servers</title></head><body>'

start = 0
end = len(massof)
while start < end-1:
  lol = massof[start].split(' ')
  urls = 'http://'+lol[5]
  print(lol)
  try:
    mybody = requests.get(urls)
    mybtxt = (mybody.text).lower()
    mymass = mybtxt.split('<title>')
    pol = mymass[1].split('</title>')
    pols = pol[0]
    print(pols)
    tohtmlfile = tohtmlfile+'<a href="'+urls+'">'+pols+'</a><br>'
  except:
    print('Site is not ready')
  start+=1

print('It is getted here:')
print(tohtmlfile)

print('We can upload it to your github.')

upload = str(input('Upload? y/n'))

if upload == 'y':
  mk = 'mkdir server'
  cds = 'cd server'
  inits = 'git init'
  addperson = 'git config --global user.email "no-reply@kamakepar.ru"'
  addemail = 'git config --global user.name "Server Transformer & Uploader"'
  adds = 'git add *'
  comm = 'git commit -m "FIles Uploaded Successfully"'
  br = 'git branch -M main'
  print('add repo as:\nhttps://github.com/example/example.git')
  addrepo = str(input('Add repo: '))
  orig = 'git remote add origin '+addrepo
  pushing = 'git push -u origin main'
  os.system(mk)
  f = open("server/main.html", "a")
  f.write(tohtmlfile)
  f.close()
  os.system(cds)
  os.system(inits)
  os.system(addperson)
  os.system(addemail)
  os.system(adds)
  os.system(comm)
  os.system(br)
  os.system(orig)
  os.system(pushing)
  print('It is getted to your github!')
else:
  print('Then copy the contents:')
  print(tohtmlfile)