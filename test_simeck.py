#!/usr/bin/env python
from __future__ import print_function
from operator import length_hint
from random import randint
import timeit
from time import sleep
from collections import deque
from datetime import datetime
import json
import binascii
from array import array
from operator import xor
import random
from SimeckCipher import SimeckCipher as Simeck


NUM_ROUNDS = {
    # (block_size, key_size): num_rounds
    (32, 64): 32,
    (48, 96): 36,
    (64, 128): 44,
}

mess50bytes = '/home/FL1--T01:25.8C;T01:25.8C;H01:70.5%'
mess100bytes = '/home/FL01a--T01:25.8C;T02:26.0C;Hum01:70.8%;Hum02:71.2%;L01:ON;L02:ON;Fan01:OFF;Fan02:OFF'
mess150bytes = '/home/FL01--T01:25.8C;T02:26.0C;Hum01:70.8%;Hum02:71.2%;L01:ON;L02:ON;L03:ON;L04:OFF;Fan01:OFF;Fan01:OFF;Fan02:OFF;Pow01:11.5W;Pow02:11.2W;;'
mess200bytes = '/home/FL01--T01:25.8C;T02:26.0C;Hum01:70.8%;Hum02:71.2%;L01:ON;L02:ON;L03:ON;L04:OFF;Fan01:OFF;Fan01:OFF;Fan02:OFF;Pow01:11.5W;Pow02:11.2W;Pow03:11.0W;Door01:CLOSE;Door02:OPEN;Win01:CLOSE;;'

mess = mess50bytes
mess_si = len(mess)

key1 = 0x1FE2548B4A0D14DC
key1_si = 64
block1_si = 32

key2 = 0x2541FE8B1FE24A0C548B4A0D14DCD14D
key2_si = 128
block2_si = 64

cipher = Simeck(master_key=key1, key_size=key1_si, block_size=block1_si)
#print("message = ", msg)
print("mess = ", mess)
ciphertext = cipher.encrypt_dt(mess,block1_si,key1_si,mess_si)
print("ciphertext = ", ciphertext)
plaintext = cipher.decrypt_dt(ciphertext,block1_si,key1_si)
print("plaintext = ", plaintext)

#msg2 = str(plaintext, 'ascii')
#print("message = ", msg2)