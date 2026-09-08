class BrowserHistory:

    class Page:
        def __init__(self, name: str, prev=None, nex = None):
            self.name = name
            self.prev = prev
            self.next = nex

    def __init__(self, homepage: str):
        self.start = self.Page(name=homepage)
        self.current = self.start

    def visit(self, url: str) -> None:
        page = self.Page(url)
        page.prev = self.current
        self.current.next = page
        self.current = page
        

    def back(self, steps: int) -> str:
        cur = self.current
        while(cur.prev):
            if steps == 0:
                break
            steps-=1
            #print(f"{cur.prev.name} <- {cur.name} ")
            cur = cur.prev
        self.current = cur
        #print(f"{cur.name} -> {cur.next.name} ")
        return cur.name
        

    def forward(self, steps: int) -> str:
        cur = self.current
        while(cur.next):
            if steps == 0:
                break
            steps-=1
            print(f"{cur.name}->{cur.next.name}")
            cur = cur.next
        self.current = cur
        return cur.name


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)