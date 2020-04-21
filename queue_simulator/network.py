from collections import defaultdict
import itertools


class Network:
    def __init__(self, random):
        self.network = defaultdict(dict)
        self.random = random

    def add_entry(self, source, target, probability):
        self.network[source][target] = probability
        exit_probability = 100 - sum(v for k, v in self.network[source].items() if k is not None)
        self.network[source][None] = 0 if exit_probability < 0 else exit_probability

    def get_destiny(self, source):
        if source not in self.network:
            return None

        probabilities = list(itertools.chain.from_iterable(
            [[t]*p for t, p in self.network[source].items()]))

        rnd = self.random.get_random()
        rand_idx = int(rnd * 100)

        return probabilities[rand_idx]
