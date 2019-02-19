import Crypto.Cipher.DES as DES
import codecs

flag = 'sysucsa{common_symmetric_cipher}'
key = 'sysucsa!'
c = DES.new(key)
print(c.encrypt(flag).hex())
print(c.decrypt(codecs.decode(c.encrypt(flag).hex(), 'hex')))
