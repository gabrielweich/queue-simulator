from .helpers import fit
from .random import Random
from .queue import Queue, QueueProperties
from .scheduler import Scheduler
from .event import Event, EventType

QUEUE_PROPERTIES = QueueProperties(
    servers=2,
    capacity=5,
    min_arrival=2,
    max_arrival=4,
    min_service=3,
    max_service=5
)


FIRST_ENTRY_TIME = 3
ITERATIONS = 100000
AVERAGE_FROM = 5
SEED = None


class QueueSimulator:
    def __init__(self):
        self.random = Random(SEED)
        self.populate_random()
        self.scheduler = Scheduler()
        self.queue = Queue(QUEUE_PROPERTIES, self.scheduler, self.random)

        self.queue.scheduler = self.scheduler
        self.queue.random = self.random

        first_event = Event(EventType.ENTRY, FIRST_ENTRY_TIME)
        self.scheduler.add_event(first_event)

    def populate_random(self):
        for i in range(ITERATIONS):
            self.random.linear_congruential()

    def run(self):
        for i in range(len(self.random.numbers) - 1):
            event = self.scheduler.remove_first()
            if event.event_type == EventType.ENTRY:
                self.queue.enter_event(event)
            elif event.event_type == EventType.EXIT:
                self.queue.exit_event(event)


def print_statistics(states):
    total_time = sum(states)
    row_format = "{:>15}" * 3
    print(row_format.format('State', 'Time', 'Probability'))
    for i, state in enumerate(states):
        probability = round((state * 100)/total_time, 4)
        round_state = round(state, 4)
        print(row_format.format(i, round_state, f'{probability}%'))


def main():
    states_list = []
    for i in range(AVERAGE_FROM):
        q = QueueSimulator()
        q.run()
        states_list.append(q.queue.states)

    states = [sum(v[i] for v in states_list)/len(states_list) for i in range(len(states_list[0]))]
    print_statistics(states)

