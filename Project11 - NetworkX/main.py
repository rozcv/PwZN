import networkx as nx
import matplotlib.pyplot as plt

g = nx.read_edgelist('Email-Enron.txt', create_using=nx.Graph(), nodetype=int)
k = nx.read_edgelist("s.txt", create_using=nx.Graph(), nodetype=int)
node_list = list(g.nodes)
listdegrees = []

for node in node_list:
    d = g.degree[node]
    listdegrees.append(d)
# print(listdegrees)
plt.plot(node_list, listdegrees, 'o', markersize=1, color='darkorange')
plt.title("Rozkład stopni wierzchołków")
plt.show()

listneighbours = []

for nod in node_list:
    a = list(g.adj[nod])
    n = len(a)
    listneighbours.append(n)

# print(listneighbours)
# plt.plot(node_list,listneighbours,'o',markersize=1, color='darkblue')
# plt.title("Rozkład - ile węzłów w każdej składowej ")
# plt.show()


# plt.show()

nx.draw_random(k, with_labels=False, node_color='darkorange', node_size=3, width=1, edge_color='lightblue')
plt.show()
nx.draw_random(g, with_labels=False, node_color='darkorange', node_size=3, width=1, edge_color='lightblue')
plt.show()


short1 = nx.average_shortest_path_length(k)
print(f'Shortest path k graphh: {short1}')
short = nx.average_shortest_path_length(g,weight=None)
print(f'Shortest path g graphh: {short}')

