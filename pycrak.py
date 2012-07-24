#!/usr/bin/python
import hashlib

chars='abcdefghijklmnopqrstuvwxyz0123456789'
max=35
password=raw_input('Password: ')
hash=hashlib.sha1(password).hexdigest()
print('Testing password: %s; with hash: %s'%(password,hash))
guessing=[-1]
guessedhash=''

def add2list():
    length=len(guessing)
    guessing[-1]+=1

    if guessing[-1]>max:
        guessing[-1]=0
        if length>1:
            guessing[-2]+=1
        else:
            guessing.insert(0,0)
    if length>1 and guessing[-2]>max:
        guessing[-2]=0
        if length>2:
            guessing[-3]+=1
        else:
            guessing.insert(0,0)
    if length>2 and guessing[-3]>max:
        guessing[-3]=0
        if length>3:
            guessing[-4]+=1
        else:
            guessing.insert(0,0)
    if length>3 and guessing[-4]>max:
        guessing[-4]=0
        if length>4:
            guessing[-5]+=1
        else:
            guessing.insert(0,0)
    if length>4 and guessing[-5]>max:
        guessing[-5]=0
        if length>5:
            guessing[-6]+=1
        else:
            guessing.insert(0,0)
    if length>5 and guessing[-6]>max:
        if length>5:
            guessing[-7]+=1
        else:
            guessing.insert(0,0)

while guessedhash!=hash:
    add2list()
    guessedhash=''
    for each in guessing:
        guessedhash+=chars[each]
    guessedhash=hashlib.sha1(guessedhash).hexdigest()

print('Cracked!')
trueword=''
for each in guessing:
    trueword+=chars[each]
print 'Password is: %s'%trueword
print guessedhash

