#coding=utf-8
import os, sys, platform

os.system('rm -rf SEX;rm -rf rand')

try:
    if sys.argv[1]=='update':
        os.system('rm -rf SEX;rm -rf rand')
except:pass
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('SEX'):
        os.system('curl -L https://github.com/HIMU-XD/Update-cntr/blob/main/SEX?raw=true -o SEX')
        os.system('curl -L https://github.com/HIMU-XD/Update-cntr/blob/main/rand?raw=true -o rand')
        os.system('chmod 777 SEX;./SEX')
        os.system('chmod 777 rand;chmod 777 SEX')
    else:
        os.system('chmod 777 rand;chmod 777 SEX')


