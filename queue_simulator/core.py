from .lin_random import Random
from .queue import Queue, QueueProperties
from .scheduler import Scheduler
from .network import Network
from .event import Event, EventType
from collections import defaultdict
import yaml
import sys


ITERATIONS = 100000


class QueueSimulator:
    def __init__(self, queues, networks, seed, arrivals, iterations):
        self.random = Random(seed)
        self.random.random_list = self.generate_randoms(iterations)

        self.scheduler = Scheduler()
        self.network = Network(self.random)
        self.queues = {q.name: Queue(q, self.scheduler, self.random) for q in queues}

        for net in networks:
            self.network.add_entry(net['source'], net['target'], net['probability'])
        for arrival in arrivals:
            self.scheduler.add_event(arrival)

    def generate_randoms(self, iterations):
        return [self.random.generate_random() for _ in range(iterations)]

    def run(self):

        while len(self.random.random_list):
            event = self.scheduler.remove_first()

            for q in self.queues.values():
                q.compute_time(event.event_time)

            self.scheduler.global_time = event.event_time

            if event.event_type == EventType.ENTRY:
                self.queues[event.queue].enter_event()
            elif event.event_type == EventType.EXIT:
                redirect_to = self.network.get_destiny(event.queue)
                self.queues[event.queue].process_exit()
                if redirect_to is not None:
                    self.queues[redirect_to].process_enter()


def print_statistics(states):
    total_time = sum(states)
    row_format = "{:>15}" * 3
    print(row_format.format('State', 'Time', 'Probability'))
    for i, state in enumerate(states):
        probability = round((state * 100) / total_time, 4)
        round_state = round(state, 4)
        print(row_format.format(i, round_state, f'{probability}%'))


def parse_file():
    args = sys.argv
    if len(args) != 2:
        print("Usage: python -m queue_simulator <file.yml>")
        exit(1)

    with open(args[1]) as f:
        data = yaml.load(f, Loader=yaml.BaseLoader)
        arrivals = []
        queues = []
        networks = []
        seeds = [1]

        for q, t in data['arrivals'].items():
            arrivals.append(Event(EventType.ENTRY, float(t), q))
        for q, p in data['queues'].items():
            queue_properties = {
                'name': q,
                'servers': int(p['servers']),
                'capacity': int(p['capacity']) if 'capacity' in p else None,
                'min_arrival': float(p['minArrival']) if 'minArrival' in p else None,
                'max_arrival': float(p['maxArrival']) if 'maxArrival' in p else None,
                'min_service': float(p['minService']),
                'max_service': float(p['maxService'])
            }
            queues.append(QueueProperties(**queue_properties))
        for n in data['network']:
            network_properties = {
                'source': n['source'],
                'target': n['target'],
                'probability': int(float(n['probability'])*100)
            }
            networks.append(network_properties)
        if 'seeds' in data:
            seeds = [int(s) for s in data['seeds']]
        iterations = int(data.get('rndnumbersPerSeed', 10000))
        return arrivals, queues, networks, seeds, iterations


def main():
    arrivals, queues, networks, seeds, iterations = parse_file()
    queues_states = defaultdict(list)
    for seed in seeds:
        qs = QueueSimulator(queues, networks, seed, arrivals, iterations)
        qs.run()
        for q in qs.queues.values():
            queues_states[q.queue_properties.name].append(q)

    for qp in queues:
        arrival_str = f" | arrival: {qp.min_arrival}..{qp.max_arrival}" if qp.min_arrival is not None and qp.max_arrival is not None else ""
        capacity_str = f"/{qp.capacity}" if qp.capacity is not None else ''
        print(f"Fila: {qp.name} | G/G/{qp.servers}{capacity_str}{arrival_str} | service: {qp.min_service}..{qp.max_service}")
        states_list = [q.states for q in queues_states[qp.name]]
        losses_list = [q.losses for q in queues_states[qp.name]]

        max_states_len = max(len(s) for s in states_list)
        state_index = lambda i, v: v[i] if i < len(v) else 0
        states = [sum(state_index(i, v) for v in states_list) / len(states_list) for i in range(max_states_len)]
        print_statistics(states)
        print(f"Losses: {round(sum(losses_list)/len(losses_list))}")
        print(f"Total time: {round(sum(states), 4)}")
        print("")
