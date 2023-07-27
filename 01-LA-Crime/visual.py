import networkx as nx
import matplotlib.pyplot as plt
import community  # Python-Louvain community detection library

# Read the edges from the file
filename = "ia-crime-moreno.edges"
with open(filename, "r") as file:
    lines = file.readlines()

# Parse the data and create the network
G = nx.Graph()
for line in lines[3:]:  # Skip the header lines
    src, tgt = line.strip().split()
    G.add_edge(src, tgt)

# Compute the communities using the Louvain algorithm
communities = community.best_partition(G)

# Limit the number of clusters to 6
max_clusters = 6
cluster_mapping = {}
current_cluster = 0

for node, cluster in communities.items():
    if cluster not in cluster_mapping and current_cluster < max_clusters:
        cluster_mapping[cluster] = current_cluster
        current_cluster += 1
    communities[node] = cluster_mapping.get(cluster, max_clusters)

# Draw the network
plt.figure(figsize=(12, 10))  # Increase the figure size for more spacious visualization
pos = nx.fruchterman_reingold_layout(G, seed=42, k=0.01, iterations=100)  # Smaller 'k' for increased spacing

# Assign colors based on the cluster number
colors = ["skyblue", "salmon", "limegreen", "orange", "plum", "gold"]

for cluster in range(max_clusters):
    nodes_in_cluster = [node for node in communities if communities[node] == cluster]
    nx.draw_networkx_nodes(
        G,
        pos,
        nodelist=nodes_in_cluster,
        node_size=1000,
        node_color=colors[cluster],
        label=f"Cluster {cluster + 1}",
    )

nx.draw_networkx_edges(G, pos, alpha=0.5)
nx.draw_networkx_labels(G, pos, font_size=8, font_weight="bold")  # Reduced font size

plt.title("Network Visualization with Clustering", fontsize=16)
plt.legend(loc="best", fontsize=10)
plt.axis("off")  # Turn off the axis to remove the bounding box
plt.tight_layout()  # Adjust the layout for better visualization
plt.show()
