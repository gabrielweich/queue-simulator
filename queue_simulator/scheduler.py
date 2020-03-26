import heapq
from .event import Event


class Scheduler:
    def __init__(self):
        self.events = []
        self.global_time = 0
        self.previous_time = 0

    def add_event(self, event: Event):
        heapq.heappush(self.events, event)

    def remove_first(self) -> Event:
        return heapq.heappop(self.events)
