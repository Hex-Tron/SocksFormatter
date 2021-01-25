#!/usr/bin/python3

import sys,re
file1=sys.argv[1]
pattern=r'[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}:[0-9]{1,5}'
l=[]
def fuc(line):
    x=re.search(pattern,line)
    if x!=None:
            df=x.group()
            test=df.split(':')
            your_format='socks5\t{}\t{}\n'.format(test[0],test[1])
            l.append(your_format)

with open(file1) as rd:
    for i in rd:
        fuc(i)
        
with open('new.txt','w') as wr:
    wr.writelines(l)

#Made by Hex