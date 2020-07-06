'''
Description
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl
nd it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work.
You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
'''

import random
class Codec():
    def __init__(self):
        self.urls = {}
        self.seeds = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def encode(self, longUrl):
        tiny_str = []
        for i in range(6):
            tiny_str.append(random.choice(self.seeds))
        str_setter ="http://tinyurl.com/"+"".join(tiny_str)
        self.urls[str_setter] = longUrl
        return str_setter

    def decode(self, shortUrl):
        return self.urls.get(shortUrl)