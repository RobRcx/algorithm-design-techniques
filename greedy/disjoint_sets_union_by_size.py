class DisjointSet:

    def __init__(self, n):
        self.makeset(n)

    def makeset(self, n):
        self.S = [-1 for x in range(n)]

    def find(self, x):
        if self.S[x] < 0:
            return x
        else:
            return self.find(self.S[x])

    def union(self, el1, el2):
        root1 = self.find(el1)
        root2 = self.find(el2)
        if root1 == root2:
            return

        if self.S[root2] < self.S[root1]:
            self.S[root2] += self.S[root1]
            self.S[root1] = root2
        else:
            self.S[root1] += self.S[root2]
            self.S[root2] = root1

ds = DisjointSet(7)
ds.union(5, 6)
ds.union(1, 2)
ds.union(0, 2)

print(ds.find(5), ds.find(1), ds.find(2))