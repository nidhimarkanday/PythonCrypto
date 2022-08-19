
#pip install ecdsa
import ecdsa
from hashlib import sha256

def verifyECDSAsecp256k1(msg, signature, pubKey):
    key = open("d:/cryptopython/demo/ecdsakeys/pubkey.pem", "rb").read()
    fk = ecdsa.VerifyingKey.from_string(pubKey, curve=ecdsa.SECP256k1) # the default is sha1
    if(fk.verify(bytes.fromhex(signature), msg)):
        print('passed')
    return 

message=b"Hello World"

# SECP256k1 is the Bitcoin elliptic curve
sk = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1) #fn to generate key using mentioned curve,SHA1 defualt hashfunction
vk = sk.get_verifying_key()  #verifying key is public key
sig = sk.sign(message)
file_out = open("d:/cryptopython/demo/ecdsakeys/pubkey.pem", "wb")
file_out.write(vk.to_string().hex())
file_out.close()


sk = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1) #this is your sign (private key)
private_key = sk.to_string().hex() #convert your private key to hex
vk = sk.get_verifying_key() #this is your verification key (public key)
public_key = vk.to_string().hex()
#we are going to encode the public key to make it shorter
public_key = base64.b64encode(bytes.fromhex(public_key))


with open("d:/cryptopython/demo/ecdsakeys/bothkey.txt", "w") as f:
    f.write("Private key: {0}\nWallet address / Public key: {1}".format(private_key, public_key.decode()))
print("Your new address and private key are now in the file {0}".format(filename))

#verifyECDSAsecp256k1(message,sig,"d:/cryptopython/demo/ecdsakeys/pubkey.pem")



