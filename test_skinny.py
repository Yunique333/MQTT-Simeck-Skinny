from __future__ import print_function
from array import array
from operator import xor
from random import randint
from random import random
from time import sleep
import timeit
from datetime import datetime
import json
import binascii
import random
from SkinnyCipher import SkinnyCipher as Skinny


# valid cipher configurations stored:
# block_size:{key_size: number_rounds}
#    __valid_setups = {64: {64: 32, 128: 36, 192: 40},
#                      128: {128: 40, 256: 48, 384: 56}}

   
mess50bytes = '/home/FL1--T01:25.8C;T01:25.8C;H01:70.5%;H01:70.4%'
mess100bytes = '/home/FL01a -- T01:25.8C; T02:26.0C; Hum01: 70%; Hum02: 71%; L01: ON; L02: ON; Fan: OFF; Pow: 11.5W'
mess150bytes = '/home/FL01--T01:25.8C;T02:26.0C;Hum01:70.8%;Hum02:71.2%;L01:ON;L02:ON;L03:ON;L04:OFF;Fan01:OFF;Fan01:OFF;Fan02:OFF;Pow01:11.5W;Pow02:11.2W;Pow03:11.0W'
mess200bytes = '/home/FL01--T01:25.8C;T02:26.0C;Hum01:70.8%;Hum02:71.2%;L01:ON;L02:ON;L03:ON;L04:OFF;Fan01:OFF;Fan01:OFF;Fan02:OFF;Pow01:11.5W;Pow02:11.2W;Pow03:11.0W;Door01:CLOSE;Door02:OPEN;Win01:CLOSE;Win02:CLOSE '

mess = mess100bytes;
mess_si = len(mess)

#mess = binascii.hexlify(msg)

#mess=0x86743875fe
#messhex = msg.hex()
#mess = int.from_bytes(msg, byteorder='big', signed=False)
block_si = 64

key1 = 0x1FE2548B4A0D14DC
key1_si = 64

key2 = 0x1FEA0D14DC8B4A0D142548B4DC1FE254
key2_si = 128

cipher = Skinny(key1, key1_si, block_si, mode='ECB')

#print("message = ", msg)
print("mess = ", mess)
ciphertext = cipher.encrypt_dt(mess)
print("ciphertext = ", ciphertext)
plaintext = cipher.decrypt_dt(ciphertext)
print("plaintext = ", plaintext)

# shuffle string
mess = ''.join(random.sample(mess,mess_si))

print("mess = ", mess)
ciphertext = cipher.encrypt_dt(mess)
print("ciphertext = ", ciphertext)
plaintext = cipher.decrypt_dt(ciphertext)
print("plaintext = ", plaintext)