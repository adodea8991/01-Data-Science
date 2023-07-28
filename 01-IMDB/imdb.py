import networkx as nx
import matplotlib.pyplot as plt

# Read the edges from the 'IMDB.edges' file
filename_edges = "IMDB.edges"
with open(filename_edges, "r") as file_edges:
    lines_edges = file_edges.readlines()

# Parse the edge data and create the network
G = nx.Graph()
for line in lines_edges[1:]:  # Skip the header line
    src, tgt = line.strip().split()
    G.add_edge(int(src), int(tgt))

# Read the node labels from the 'IMDB.node_labels' file
filename_labels = "IMDB.node_labels"
node_labels = {}
with open(filename_labels, "r") as file_labels:
    lines_labels = file_labels.readlines()

# Parse the node label data
for line in lines_labels:
    node, label = line.strip().split(',')
    node_labels[int(node)] = int(label)

# Draw the network
plt.figure(figsize=(12, 8))  # Set the figure size for the visualization
pos = nx.spring_layout(G, seed=42)  # Spring layout for node positioning

# Extract unique node labels and assign colors
unique_labels = set(node_labels.values())
num_labels = len(unique_labels)
color_map = plt.get_cmap("tab20", num_labels)  # Use tab20 colormap for distinct colors

for label in unique_labels:
    nodes_with_label = [node for node, lbl in node_labels.items() if lbl == label]
    nx.draw_networkx_nodes(
        G,
        pos,
        nodelist=nodes_with_label,
        node_size=300,
        node_color=[color_map(label % num_labels)],
        label=f"Label {label}",
    )

nx.draw_networkx_edges(G, pos, alpha=0.5)
nx.draw_networkx_labels(G, pos, font_size=8, font_weight="bold")

plt.title("IMDB Network Visualization", fontsize=16)
plt.legend(loc="best", fontsize=10)
plt.axis("off")  # Turn off the axis to remove the bounding box
plt.tight_layout()  # Adjust the layout for better visualization
plt.show()
