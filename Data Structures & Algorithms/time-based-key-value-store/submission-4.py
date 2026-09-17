class TimeMap:

    def __init__(self):
        self.keys = {}
    
    class Person:

        def __init__(self, name:str):
            self.name = name
            self.values = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key not in self.keys:
            p = self.Person(name=key)
            self.keys[key] = p
        else:
            p = self.keys[key]

        p.values[timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keys:
            return ""
        p = self.keys[key]
        if timestamp in p.values:
            return p.values[timestamp]

        times = list(p.values.keys())
        times.sort()
        l = 0
        r = len(times)-1
        if timestamp>times[-1]:
            return p.values[times[-1]]
        if timestamp<times[0]:
            return ""

        while l<r-1:
            ind = (l+r)//2
            if times[ind]>timestamp:
                r = ind
            else:
                l = ind
        return p.values[times[l]]
