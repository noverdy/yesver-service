from random import randint, getrandbits
from hashlib import md5


class Generator:
    def __init__(self, m: int, c: int, n: int, seed: int):
        self.m = m
        self.c = c
        self.n = n
        self.state = seed

    def next(self) -> int:
        self.state = (self.state * self.m + self.c) % self.n
        return self.state


class Tokenizer:
    def __init__(self, m: int, c: int, n: int):
        self.generator = Generator(m, c, n, randint(0, n))

    def generate_token(self) -> str:
        data = str(self.generator.next() ^ getrandbits(16))
        data = '0' * (8 - len(data) % 8) + data

        token = ''.join(md5(data[i:i + 8].encode()).hexdigest()
                        for i in range(0, len(data), 8))
        return token
