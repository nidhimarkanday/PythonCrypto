#(Advanced Encryption Standard) is a symmetric block cipher
from Crypto.Cipher import AES
#Crypto.Cipher package contains algorithms for protecting the confidentiality of data.


key = b'Sixteen byte key'  #Prefix b is to specify bytes type
cipher = AES.new(key, AES.MODE_EAX)   # Creates new AES Cipher (key,MODE) nonce can also be provided at the time of init
#EAX means encrypt-then-authenticate-then-translate and is a mode of opertion for cryptographic block ciphers
nonce = cipher.nonce
ciphertext, tag = cipher.encrypt_and_digest(b'TESTING AES ALGORITHM')
#encrypt_and_digest method accepts our data and returns a tuple with the ciphertext
# and the MAC(Message Authentication Code (MAC) is cryptographic code, calculated by given key and given message), sometimes known as a tag, which confirms the authenticity and authority of the data.


print("***************The recipient can decrypt using ciphertext,tag,nonce ****************")


#nonce=bytes("HACK",'ascii')              #Uncomment to test failure 
cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)

plaintext = cipher.decrypt(ciphertext)
try:
    cipher.verify(tag)
    print("The message is authentic:", plaintext)
except ValueError:
    print("Key incorrect or message corrupted")