from SizeAppend import SizeAppend
from Crypto.Cipher import AES
filename = 'ov7670_top.v'
SizeAppend(filename)
fi = open('keys.txt', 'r')
AES_Key = fi.readline()
fi.close()
IVblock = 'This is an IV456'
fi = open(filename, 'r')
plaintxt = fi.read() #reads the entire file
obj = AES.new(AES_Key, AES.MODE_CBC, IVblock)
ciphertext = obj.encrypt(plaintxt)
fo = open('cipher.txt', 'w')
fo.write(ciphertext)
fi.close()
fo.close()
print ("File encryption is done!")

#obj2 = AES.new(AES_Key, AES.MODE_CBC, IVBlock)
#obj2.decrypt(ciphertext)