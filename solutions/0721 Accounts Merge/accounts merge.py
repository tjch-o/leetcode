class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)

        if px == py:
            return

        rpx, rpy = self.rank[px], self.rank[py]

        if rpx > rpy:
            self.parents[py] = px
            self.rank[px] += self.rank[py]
        else:
            self.parents[px] = py
            self.rank[py] += self.rank[px]


def accounts_merge(accounts):
    uf = UnionFind(len(accounts))
    email_to_id = {}
    email_to_name = {}

    for i, account in enumerate(accounts):
        name = account[0]
        emails = account[1:]

        for email in emails:
            if email not in email_to_id:
                email_to_id[email] = i
                email_to_name[email] = name
            else:
                # group accounts once a common email is found
                uf.union(i, email_to_id[email])

    grouped_accounts = {}

    for email in email_to_id:
        id = email_to_id[email]
        root = uf.find(id)

        if root not in grouped_accounts:
            grouped_accounts[root] = [email]
        else:
            grouped_accounts[root].append(email)

    result = []

    for id in grouped_accounts:
        name = accounts[id][0]
        grouped_accounts[id].sort()
        result.append([name] + grouped_accounts[id])
    return result
