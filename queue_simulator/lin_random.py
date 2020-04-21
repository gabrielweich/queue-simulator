import time


class Random:
    def __init__(self, seed=None):
        self.seed = time.time() if seed is None else seed

    def get_random(self, m=2**32, a=1103515245, c=12345):
        self.seed = (a * self.seed + c) % m
        number = self.seed / m
        return number
