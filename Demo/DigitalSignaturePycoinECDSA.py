#Bitcoin is a good example of a system that relies on ECDSA for security. Every Bitcoin address is a cryptographic hash of an ECDSA public key. The ownership of the account is determined by who controls the ECDSA private key.
#https://cryptobook.nakov.com/digital-signatures/ecdsa-sign-verify-messages
#pip install pycoin before running this program if not already installed

from pycoin.ecdsa import secp256k1, sign, verify
import hashlib, secrets

def sha3_256Hash(msg):
    hashBytes = hashlib.sha3_256(msg.encode("utf8")).digest()
    return int.from_bytes(hashBytes, byteorder="big")

def signECDSAsecp256k1(msg, privKey):
    msgHash = sha3_256Hash(msg)
    signature = sign(secp256k1, privKey, msgHash)
    return signature

def verifyECDSAsecp256k1(msg, signature, pubKey):
    msgHash = sha3_256Hash(msg)
    valid = verify(secp256k1, pubKey, msgHash, signature)
    return valid