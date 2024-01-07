import random


def fetchsocks5():
    with open('proxies.txt') as f:
     proxies = f.read().splitlines()
    return 'socks5://' + random.choice(proxies)

def fetchhttps():
    with open('proxies.txt') as f:
     proxies = f.read().splitlines()
    return 'https://' + random.choice(proxies)

def fetchhttp():
    with open('proxies.txt') as f:
     proxies = f.read().splitlines()
    return 'http://' + random.choice(proxies)

