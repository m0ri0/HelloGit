class UnionFind:
    def __init__(self, n=1):
        self.par = [i for i in range(n)]
        self.rank = [0] * (n+1)
        self.cnt = 0

    
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]
    
    def groupsize(self):
        self.cnt = 0
        for i, x in enumerate(self.par):
            if x == i:
                self.cnt += 1
        return self.cnt
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
    
    def same_check(self, x, y):
        return self.find(x) == self.find(y)