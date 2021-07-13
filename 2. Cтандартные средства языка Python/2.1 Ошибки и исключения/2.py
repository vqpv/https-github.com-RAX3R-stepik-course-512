exceptions = {}
t_exceptions = []


def found_path(exc, start, end, path=None):
    if path is None:
        path = []
    path = path + [start]
    if start == end:
        return path
    if start not in exc:
        return []
    for node in exc[start]:
        if node not in path:
            new_path = found_path(exc, node, end, path)
            if new_path:
                return new_path
    return []


n = int(input())

for _ in range(n):
    i = input().split()
    child = i[0]
    parents = i[2:]
    exceptions[child] = parents

m = int(input())

for _ in range(m):
    throwing = input()
    for t_e in t_exceptions:
        if len(found_path(exceptions, throwing, t_e)) > 1:
            print(throwing)
            break
    t_exceptions.append(throwing)
