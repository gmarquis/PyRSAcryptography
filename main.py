import rsa

    ## Generate private and public keys ##
public_key, private_key = rsa.newkeys(2096)
with open("public.pem", "wb") as f:
    f.write(public_key.save_pkcs1("PEM"))
with open("private.pem", "wb") as f:
    f.write(private_key.save_pkcs1("PEM"))

    ## Use Public key to encode ##
with open("public.pem", "rb") as f:
 public_key = rsa.PublicKey.load_pkcs1(f.read())
 message = "Hello, this message becomes encrypted."
 encrypted_message = rsa.encrypt(message.encode(), public_key)
    ## Write encode message to file ##
 with open("encrypted_message.txt", "wb") as f:
    f.write(encrypted_message)

    ## Use Private key to decode ##
with open("private.pem", "rb") as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())
encrypted_message = open("encrypted_message.txt", "rb").read()
decoded_message = rsa.decrypt(encrypted_message, private_key)
print(decoded_message.decode())