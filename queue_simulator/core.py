from .lin_random import Random
from .queue import Queue, QueueProperties
from .scheduler import Scheduler
from .network import Network
from .event import Event, EventType
from collections import defaultdict

QUEUE_1_PROPERTIES = QueueProperties(
    name='Q1',
    servers=2,
    capacity=3,
    min_arrival=2,
    max_arrival=3,
    min_service=2,
    max_service=5
)

QUEUE_2_PROPERTIES = QueueProperties(
    name='Q2',
    servers=1,
    capacity=3,
    min_service=3,
    max_service=5
)

NETWORK = [
    {
        'source': 'Q1',
        'target': 'Q2',
        'probability': 100
    }
]

FIRST_ENTRY_TIME = 2.5
ITERATIONS = 100000
AVERAGE_FROM = 5
SEED = None


class QueueSimulator:
    def __init__(self, queues_description, network_description):
        self.random = Random(SEED)
        self.scheduler = Scheduler()
        self.network = Network(self.random)
        self.queues = {q.name: Queue(q, self.scheduler, self.random) for q in queues_description}

        for net in network_description:
            self.network.add_entry(net['source'], net['target'], net['probability'])

        first_event = Event(EventType.ENTRY, FIRST_ENTRY_TIME, 'Q1')
        self.scheduler.add_event(first_event)

    def run(self):
        for i in range(ITERATIONS):
            event = self.scheduler.remove_first()
            if event.event_type == EventType.ENTRY:
                self.queues[event.queue].enter_event(event)
            elif event.event_type == EventType.EXIT:
                redirect_to = self.network.get_destiny(event.queue)
                self.queues[event.queue].compute_time(event.event_time)
                self.queues[event.queue].process_exit()
                if redirect_to is not None:
                    self.queues[redirect_to].compute_time(event.event_time)
                    self.queues[redirect_to].process_enter()


def print_statistics(states):
    total_time = sum(states)
    row_format = "{:>15}" * 3
    print(row_format.format('State', 'Time', 'Probability'))
    for i, state in enumerate(states):
        probability = round((state * 100) / total_time, 4)
        round_state = round(state, 4)
        print(row_format.format(i, round_state, f'{probability}%'))


def main():
    queues_states = defaultdict(list)
    queues = [QUEUE_1_PROPERTIES, QUEUE_2_PROPERTIES]
    for i in range(AVERAGE_FROM):
        qs = QueueSimulator(queues, NETWORK)
        qs.run()
        for q in qs.queues.values():
            queues_states[q.queue_properties.name].append(q)

    for qp in queues:
        arrival_str  = f" | arrival: {qp.min_arrival}..{qp.max_arrival}" if qp.min_arrival is not None and qp.max_arrival is not None else ""
        print(f"G/G/{qp.servers}/{qp.capacity}{arrival_str} | service: {qp.min_service}..{qp.max_service}")
        states_list = [q.states for q in queues_states[qp.name]]
        losses_list = [q.losses for q in queues_states[qp.name]]

        states = [sum(v[i] for v in states_list) / len(states_list) for i in range(len(states_list[0]))]
        print_statistics(states)
        print(f"Losses: {round(sum(losses_list)/len(losses_list))}")
        print("")
