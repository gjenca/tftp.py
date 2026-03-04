#!/usr/bin/env python

import socket
import struct
import sys

OPCODE_READ=1
OPCODE_WRITE=2
OPCODE_DATA=3
OPCODE_ACK=4
OPCODE_ERROR=5


class Rrq:

    def __init__(self,addr,data):

        self.addr=addr
        if len(data)<9:
            raise ValueError(f'Too short packet from {addr}')
        self.opcode=struct.unpack('!H',data[:2])[0]
        if self.opcode!=OPCODE_READ:
            raise ValueError(f'Not RRQ from {addr}, opcode={self.opcode}')
        nulls_num=self.data[2:].count(b'\x00')
        if nulls_num!=2:
            raise ValueError(f'Not two nulls {addr}')
        filename_b,mode_b,null_b=data[2:].split(b'\x00')
        if null_b:
            raise ValueError(f'Something follows the second null {addr}')
        if mode_b!=b'octet'
            raise ValueError(f'Unsupported mode {mode_b}')
        self.filename=filename_b
        self.mode=mode_b


s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('',9999))
data,addr=s.recvfrom(1024)
opcode=struct.unpack('>H',data[:2])[0]
filename_b,mode_b,null_b=data[2:].split(b'\x00')
print(opcode,filename_b,mode_b,null_b)
print(data,addr)
if opcode!=1:
    print(f'opcode=={opcode}')
    sys.exit(1)
s_r=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
send_back='Some short packet of data'.encode('utf-8')
opcode_r=struct.pack('>H',3)
block_num_r=struct.pack('>H',1)
reply=opcode_r+block_num_r+send_back
s_r.sendto(reply,addr)
data,addr=s_r.recvfrom(1024)
opcode,block_num_ack=struct.unpack('>HH',data[:4])
print(opcode,block_num_ack)
print(data,addr)
