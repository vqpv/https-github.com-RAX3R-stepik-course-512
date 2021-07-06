n = int(input())

scopes = {'global': {'parent': '', 'variables': []}}


def create(_namespace, parent):
    if _namespace not in scopes:
        scopes[_namespace] = {'parent': parent, 'variables': []}


def add(_namespace, var):
    if _namespace in scopes:
        scopes[_namespace]['variables'].append(var)


def get(_namespace, var):
    if _namespace == 'global':
        print('None' if var not in scopes[_namespace]['variables'] else _namespace)
    elif var in scopes[_namespace]['variables']:
        print(_namespace)
    else:
        get(scopes[_namespace]['parent'], var)


for _ in range(n):
    command, namespace, arg = input().split()

    if command == "create":
        create(namespace, arg)

    elif command == "add":
        add(namespace, arg)

    elif command == "get":
        get(namespace, arg)
