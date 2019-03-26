import base64
from simplecrypt import encrypt, decrypt

_key = '90B86BE8F49F5995EE3297B6195FA8F07143CAE6363063360908BF7CCFE6D585'


def _encrypt(plain_text='', key=_key, base64mode=True):
    """TODO: Return this functionality"""
    # if base64mode:
    #     return base64.b64encode(encrypt(key, plain_text))
    # else:
    #     return encrypt(key, plain_text)
    return plain_text


def _decrypt(cipher_text='', key=_key, base64mode=True):
    """TODO: Return this functionality"""
    # if base64mode:
    #     return decrypt(key, base64.b64decode(cipher_text))
    # else:
    #     return decrypt(key, cipher_text)
    return cipher_text