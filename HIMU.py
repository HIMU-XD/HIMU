#coding=utf-8
import os, sys, platform

os.system('SEX')

try:
    if sys.argv[1]=='update':
        os.system('rm -rf SEX')
except:pass
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('SEX'):
        os.system('curl -L https://github.com/HIMU-XD/HIMU/blob/main/SEX?raw=true -o SEX') 
        os.system('chmod 777 SEX;./SEX')
    else:
        os.system('chmod 777 SEX;./SEX')


