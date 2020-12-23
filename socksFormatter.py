#!/usr/bin/python3
import sys
file1=sys.argv[1]

def socks(file):
    with open(file,'r') as rd:
        line=rd.readlines()
    l=[]
    for i in line:
        x=i.split(':')
        l.append('socks5\t{}\t{}'.format(x[0],x[1]))
    with open('new.txt','w') as wr:
        wr.writelines(l)
socks(file1)

