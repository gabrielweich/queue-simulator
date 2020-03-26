from enum import Enum


class EventType(Enum):
    EXIT = 1
    ENTRY = 2


class Event:
    def __init__(self, event_type, event_time):
        self.event_type = event_type
        self.event_time = event_time

    def __lt__(self, other):
        return self.event_time < other.event_time
