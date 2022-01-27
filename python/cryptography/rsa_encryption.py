# !!! not built for production, only a pseudo random prime generator and low prime numbers
import sympy


A = 50

def generate_key_pair():
    p = sympy.randprime(A, 4*A)
    q = sympy.randprime(A, 4*A)

    n = p*q
    phi = (p-1) * (q-1)

    e = 65537

    d = pow(e, -1, phi)
    # (e*d)%phi = 1

    public_key = (n, e)
    private_key = (p, q, d)

    return public_key, private_key

def encrypt(key, raw_text):
    n = key[0]
    e = key[1]
    encrypted_text = ""

    for char in raw_text:
        intchar = ord(char)
        encrypted_text += chr(intchar**e % n)
    
    return encrypted_text

def decrypt(key, enc_text):
    n = key[0]*key[1]
    d = key[2]
    decrypted_text = ""

    for char in enc_text:
        intchar = ord(char)
        decrypted_text += chr(intchar**d % n)

    return decrypted_text



if __name__ == "__main__":
    # TEST CASES
    ka_public, ka_private = generate_key_pair()
    kb_public, kb_private = generate_key_pair()

    raw_text = "Hello World!"
    encrypt_msg = encrypt(ka_public, raw_text)
    decrypt_msg = decrypt(ka_private, encrypt_msg)
    assert raw_text == decrypt_msg
    print(raw_text, encrypt_msg, decrypt_msg)

    raw_text = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/*-+.^'"
    encrypt_msg = encrypt(kb_public, raw_text)
    decrypt_msg = decrypt(kb_private, encrypt_msg)
    assert raw_text == decrypt_msg
    print(raw_text, encrypt_msg, decrypt_msg)