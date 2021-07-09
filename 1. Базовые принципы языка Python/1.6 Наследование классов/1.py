all_classes = {}

for _ in range(int(input())):
    text = input().split(' : ')
    parents = set() if len(text) == 1 else set(text[1].split())

    if text[0] in all_classes:
        all_classes[text[0]].update(parents)
    else:
        all_classes.update({text[0]: parents})

for key_1, values_1 in all_classes.items():
    for key_2, values_2 in all_classes.items():
        if key_1 in values_2:
            all_classes[key_2].update(values_1)

for _ in range(int(input())):
    c_classes = input().split()
    if c_classes[0] == c_classes[1]:
        print("Yes")
    else:
        if c_classes[0] in all_classes[c_classes[1]]:
            print("Yes")
        else:
            print("No")
