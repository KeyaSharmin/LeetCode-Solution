class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.heap = [(-p, -t) for (_,t,p) in tasks]
        heapify(self.heap)
        self.prio = {t: (p,u) for (u,t,p) in tasks}

    def add(self, u: int, t: int, p: int) -> None:
        heappush(self.heap, (-p,-t))
        self.prio[t] = (p,u)

    def edit(self, t: int, p: int) -> None:
        heappush(self.heap, (-p,-t))
        self.prio[t] = (p, self.prio[t][1])

    def rmv(self, t: int) -> None:
        del self.prio[t]

    def execTop(self) -> int:
        while self.heap:
            (p, t) = heappop(self.heap)
            if self.prio.get(-t, (None, None))[0] != -p:
                continue
            ret = self.prio[-t][1]
            del self.prio[-t]
            return ret
        return -1
