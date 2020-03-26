import time


class Random:
    def __init__(self, seed=None):
        self.numbers = []
        self.seed = time.time() if seed is None else seed

    def linear_congruential(self, m=2**32, a=1103515245, c=12345):
        self.seed = (a*self.seed + c) % m
        self.numbers.append(self.seed/m)

    def get_random(self):
        return self.numbers.pop(0)
