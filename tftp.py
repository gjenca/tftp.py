#!/usr/bin/env python

import socket
import struct

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('',9999))
data,addr=s.recvfrom(1024)
opcode=struct.unpack('>H',data[:2])[0]
filename_b,mode_b,null_b=data[2:].split(b'\x00')
print(opcode,filename_b,mode_b,null_b)
print(data,addr)

