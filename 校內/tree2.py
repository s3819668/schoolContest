from collections import Counter

while True:
    n = int(input())
    if n == 0:
        break

    graph = {}
    for _ in range(n):
        m = input()
        if m == '0':
            break

        data = m.split(' ')

        for node in data:
            if node not in graph:
                graph[node] = []

        graph[data[0]].extend(data[1:])
        for node in data[1:]:
            graph[node].append(data[0])

    for node in graph:
        graph[node] = list(set(graph[node]))

    parent, children = [], []
    for k, v in graph.items():
        parent.extend([k] * len(v))
        children.extend(v)

parent = [int(i) for i in parent]
children = [int(i) for i in children]
leafs = [int(i) for i in children if Counter(parent)[i] == 1]

# while len(parent)>2:
#     leafs = [i for i in children if Counter(parent)[i] == 1]
for i in range(len(leafs)):
    for j in range(len(parent)):

        #刪除父與子
        if  parent[j]==leafs[i]:
            rec_parent=parent[j]
            rec_children=children[j]
            del parent[j]
            del children[j]
            break
    print(parent)
    print(children)
            #紀錄後刪除
    print(rec_parent)
    print(rec_children)
    #刪除對應子與父
    # for j in range(len(parent)):
    #     print(j)
    #     if  parent[j]==rec_children:
    #         if children[j]==rec_parent:
    #             del parent[j]
    #             del children[j]



