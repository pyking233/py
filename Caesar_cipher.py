def code(plaintext, key=3):
    """加密函数"""
    c = ""
    for i in plaintext:
        if "a" <= i <= "z":
            c += chr(ord("a") + (ord(i)-ord("a") + key) % 26)
        elif "A" <= i <= "Z":
            c += chr(ord("A") + (ord(i)-ord("A") + key) % 26)
        else:
            c += i
    return c


def decode(cipher_text, key=3):
    """解密函数"""
    c = ""
    for i in cipher_text:
        if "a" <= i <= "z":
            c += chr(ord("a") + (ord(i)-ord("a") + (26 - key)) % 26)
        elif "A" <= i <= "Z":
            c += chr(ord("A") + (ord(i)-ord("A") + (26 - key)) % 26)
        else:
            c += i
    return c
