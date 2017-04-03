#!/usr/bin/env python3
import sys
from threading import Thread, Event

class TimeoutError(Exception):
    pass

class Resolve(Thread):
    def __init__(self, id, name):
        self.id = id
        self.finished = Event()
        self.t = Thread.__init__(self, None, self.resolve, name, (id, name))
        self.start()
        Thread(None, self.timeout).start()

    def resolve(self, id, name):
        f = open("hosts")
        while not self.finished.is_set():
            for l in f:
                if l == '\n' or l[0] == '#':
                    continue
                if name in l.split()[1:]:
                    self._stop(f'RESOLVED {self.id} 0 {l.split()[0]}')
            self._stop(f'RESOLVED {self.id} 3 "{self.name} not available"')
        f.close()
        #except Exception:
        #    self._stop(f'RESOLVED {self.id} 1 "fail to resolve"')

    def timeout(self, interval=1):
        self.finished.wait(interval)
        self._stop(f'RESOLVED {self.id} 4 "timeout exceeded"')

    def cancel(self):
        self._stop(f'CANCELED {self.id}')

    def _stop(self, message):
        if not self.finished.is_set():
            self.finished.set()
            return print(message)

print("INIT 1 0")
run = 1
pool = []

while run or pool:
    command, id, *name = sys.stdin.readline().split()
    if command == "RESOLVE":
        Resolve(id, *name)
        #print("print", pool)
        #pool[-1].start()
    elif command == "CANCEL":
        pass
