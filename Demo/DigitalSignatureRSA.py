from Crypto.PublicKey import RSA  #Modules for generating, exporting or importing public keys (example: RSA or ECC).
from Crypto.Signature import PKCS1_v1_5 #Modules for assuring authenticity, that is, for creating and verifying digital signatures of messages (example: PKCS#1 v1.5).
from Crypto.Hash import SHA256 #Modules for creating cryptographic digests (example: SHA-256).
from base64 import b64decode 
from Crypto import Random #Modules for generating random data.

random_generator=Random.new().read
print('Generating public and Private keys for Alice to transfer information');
keyPair=RSA.generate(2048,random_generator) #fn to Create a new RSA key pair(Key length,Public RSA exponent integer)

priv_Key=keyPair.exportKey("PEM")#Export this RSA key, specifies format to wrap key PEM is alos default format
pub_key=keyPair.publickey().exportKey("PEM") # fn at the object level: The key will be the public key matching the given object.


f = open('AlicePubKey.pem', 'wb')
f.write(pub_key);
f.close()
print('Generated Public key for Alice::::::::::::');
f = open('AlicePrivKey.pem', 'wb')
f.write(priv_Key)
f.close()
print('Generated Private key for Alice::::::::::::');
#Now we have public and Private keys 
#Sign using private key

plaintxt='HelloWorld'           #declare data/file etc
hashA = SHA256.new(data=b'HelloWorld')      
#print(hashA)
rsakey = RSA.importKey(priv_Key)
digitalSignature = PKCS1_v1_5.new(rsakey).sign(hashA)  #PKCS1_v1_5  is an encryption standard



#Creating another set of Public key to test MATCH


keyPair2=RSA.generate(2048,random_generator)
pub_key2=keyPair2.publickey().exportKey("PEM") # fn at the object level: The key will be the public key matching the given object.
#print(priv_Key)

#print('********************Date Verification using Digital Signature***********************')
print('Keys generated successfully')

rsakey = RSA.importKey(pub_key2) 
hashB = SHA256.new(data=b'HelloWorld') 
# Assumes the data is base64 encoded to begin with

if(PKCS1_v1_5.new(rsakey).verify(hashB,digitalSignature)):
    print('')
else:
    print('')