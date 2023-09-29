import networkx as nx
import matplotlib.pyplot as plt
import turtle


# Find the shortest path and plot path
def shortest_route_and_plot(G):
    path = nx.shortest_path(G, source="StartingPoint", target="FinishingPoint", weight="weight")
    total_distance = nx.shortest_path_length(G, source="StartingPoint", target="FinishingPoint", weight="weight")
    print(path)
    print("Total Distance:", total_distance)

    # Plot path
    path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
    path_graph = G.subgraph(path)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500)
    nx.draw_networkx_nodes(path_graph, pos, node_color='red', node_size=500)
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=3)
    plt.show()


G = nx.Graph()
nodes = ["StartingPoint", "A", "B", "C", "D", "E", "F", "H", "J", "FinishingPoint"]

G.add_nodes_from(nodes)

# Add Edges and their weights
# Change this section according
# to your specific maps information
G.add_edge("StartingPoint", "A", weight=450)
G.add_edge("A", "B", weight=10)
G.add_edge("A", "C", weight=230)
G.add_edge("B", "E", weight=850)
G.add_edge("C", "D", weight=112)
G.add_edge("C", "H", weight=50)
G.add_edge("E", "FinishingPoint", weight=700)
G.add_edge("D", "F", weight=600)
G.add_edge("F", "E", weight=200)
G.add_edge("D", "J", weight=500)
G.add_edge("J", "FinishingPoint", weight=350)
G.add_edge("D", "H", weight=50)
G.add_edge("H", "FinishingPoint", weight=250)
G.add_edge("B", "C", weight=100)



#position the nodes to resemble mapF
G.nodes["FinishingPoint"]['pos']=(0,0)
G.nodes["J"]['pos']=(0,100)
G.nodes["F"]['pos']=(0,200)
G.nodes["E"]['pos']=(100,200)
G.nodes["D"]['pos']=(-1,200)
G.nodes["C"]['pos']=(-200,200)
G.nodes["H"]['pos']=(-200,100)
G.nodes["B"]['pos']=(-200,300)
G.nodes["A"]['pos']=(-300,300)
G.nodes["StartingPoint"]['pos']=(-400,300)

shortest_route_and_plot(G)



