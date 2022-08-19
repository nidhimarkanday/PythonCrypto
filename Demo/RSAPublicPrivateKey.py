from Crypto.PublicKey import RSA #Modules for generating, exporting or importing public keys (example: RSA or ECC).

key=RSA.generate(2048);

p_key=key.publickey().exportKey("PEM")
priv_Key=key.exportKey("PEM")
print(p_key);
print(priv_Key);