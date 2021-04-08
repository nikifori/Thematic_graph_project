import networkx as nx
import networkx.algorithms.community as nx_comm
import matplotlib.pyplot as plt

def plot_degree_dist(G):
    degrees = [G.degree(n) for n in G.nodes()]
    plt.figure(num='Degree Distribution')
    plt.hist(degrees, bins= 240)
    plt.show()
    


themnet = nx.read_gml("Thematic_graph_gmlformat.gml")

print(nx.info(themnet))

nodes = len(themnet.nodes)
edges = len(themnet.edges)


density = nx.density(themnet)               # Piknotita akmwn 
print("Density: ", density)

triadic_closure = nx.transitivity(themnet)  # Metavatikothta
print("Triadic closure: ", triadic_closure)

selfloops = nx.number_of_selfloops(themnet)     # Self loops
print("Number of selfloops: ", selfloops)

average_clustering = nx.average_clustering(themnet)                 # Mesos sintelestis omadopoihshs
print("Average clustering coefficient: ", average_clustering)


# CENTRALITIES
degree_centrality = nx.degree_centrality(themnet)    # degree centrality
sorted_degree_centrality = {k: v for k, v in sorted(degree_centrality.items(), key=lambda item: item[1], reverse=True)[:10]}
print("\n","=" * 15, "Top 10 degree centrality vertices", "=" * 15, "\n" )
for x,y in sorted_degree_centrality.items():
    print(x,y)
print("-" * 75)

eigenvector_centrality = nx.eigenvector_centrality(themnet)    # eigenvector centrality
sorted_eigenvector_centrality = {k: v for k, v in sorted(eigenvector_centrality.items(), key=lambda item: item[1], reverse=True)[:10]}
print("\n","=" * 15, "Top 10 eigenvector centrality vertices", "=" * 15, "\n" )
for x,y in sorted_eigenvector_centrality.items():
    print(x,y)
print("-" * 75)

closeness_centrality = nx.closeness_centrality(themnet)   # closeness centrality h sta ellinika shmantikothta apostashs
sorted_closeness_centrality = {k: v for k, v in sorted(closeness_centrality.items(), key=lambda item: item[1], reverse=True)[:10]}
print("\n","=" * 15, "Top 10 closeness centrality vertices", "=" * 15, "\n" )
for x,y in sorted_closeness_centrality.items():
    print(x,y)
print("-" * 75)

betweenness_centrality = nx.betweenness_centrality(themnet)   # betweenness centrality h sta ellinika simantikotita thesews
sorted_betweenness_centrality = {k: v for k, v in sorted(betweenness_centrality.items(), key=lambda item: item[1], reverse=True)[:10]}
print("\n","=" * 15, "Top 10 betweenness centrality vertices", "=" * 15, "\n" )
for x,y in sorted_betweenness_centrality.items():
    print(x,y)
print("-" * 75)


plot_degree_dist(themnet)
# average_node_connectivity = nx.average_node_connectivity(themnet)    # Kanei ligi wra gia ton ipologismo
# print("Average node connectivity: ", average_node_connectivity)      # = 2.8751493428912784