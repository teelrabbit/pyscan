#!/usr/bin/env python

import socket 
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
port_range = 65535;
ip = input("Enter IP:: ");
target = socket.gethostbyname(ip);

def scan(port):
    try:
        s.connect((target, port));
        return True;
    except:
        return False;

print("scanning ports ...");

for i in range(port_range):
    if scan(int(i)):
        print("port {} is open".format(i));

