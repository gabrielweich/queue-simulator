from .event import Event, EventType
from .scheduler import Scheduler
from .helpers import fit
from .lin_random import Random


class QueueProperties:
    def __init__(self, servers, min_service, max_service, capacity=None, min_arrival=None, max_arrival=None, name=None):
        self.servers = servers
        self.capacity = capacity
        self.min_arrival = min_arrival
        self.max_arrival = max_arrival
        self.min_service = min_service
        self.max_service = max_service
        self.name = name


class Queue:
    def __init__(self, queue_properties: QueueProperties, scheduler: Scheduler, random: Random):
        self.queue_properties = queue_properties
        self.scheduler = scheduler
        self.random = random

        self.states = [0 for i in range(self.queue_properties.capacity + 1)]
        self.current_size = 0
        self.losses = 0
        self.last_event_time = 0

    def enter_event(self, event: Event):
        self.compute_time(event.event_time)
        self.process_enter()
        enter_event = self._generate_entry_event()
        self.scheduler.add_event(enter_event)

    def process_enter(self):
        if self.current_size < self.queue_properties.capacity:
            self.current_size += 1
            if self.current_size <= self.queue_properties.servers:
                exit_event = self._generate_exit_event()
                self.scheduler.add_event(exit_event)
        else:
            self.losses += 1

    def process_exit(self):
        self.current_size -= 1
        if self.current_size >= self.queue_properties.servers:
            exit_event = self._generate_exit_event()
            self.scheduler.add_event(exit_event)

    def _generate_exit_event(self) -> Event:
        a = self.queue_properties.min_service
        b = self.queue_properties.max_service
        value = self.random.get_random()
        event_time = fit(a, b, value) + self.last_event_time
        origin = self.queue_properties.name

        return Event(EventType.EXIT, event_time, origin)

    def _generate_entry_event(self) -> Event:
        a = self.queue_properties.min_arrival
        b = self.queue_properties.max_arrival
        value = self.random.get_random()
        event_time = fit(a, b, value) + self.last_event_time
        origin = self.queue_properties.name

        return Event(EventType.ENTRY, event_time, origin)

    def exit_event(self, event: Event):
        self.compute_time(event.event_time)
        self.process_exit()

    def compute_time(self, event_time):
        delta_time = event_time - self.last_event_time
        self.states[self.current_size] += delta_time
        self.last_event_time = event_time
