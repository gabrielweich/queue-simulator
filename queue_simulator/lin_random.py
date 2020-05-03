import time


class Random:
    def __init__(self, seed=None, random_list=[]):
        self.seed = time.time() if seed is None else seed
        self.random_list = random_list

    def get_random(self):
        if len(self.random_list):
            return self.random_list.pop(0)
        return self.generate_random()

    def generate_random(self, m=2 ** 32, a=1103515245, c=12345):
        self.seed = (a * self.seed + c) % m
        number = self.seed / m
        return number
