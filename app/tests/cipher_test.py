from app.services.ciphers.transposition import encode, decode


def test_encode():
    text = 'ola ma kota'
    secret = 'klucz'
    assert encode(secret, text) == ' k ot la a amo '


def test_decode():
    text = ' k ot la a amo '
    secret = 'klucz'
    assert decode(secret, text).rstrip() == 'ola ma kota'


def test_special_char():
    text = 'Ab.Cd,\tEf_12 34\n@'
    secret = 'okoń'
    assert decode(secret, encode(secret, text)).rstrip() == text
