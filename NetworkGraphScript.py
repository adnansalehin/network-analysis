import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.pylab as plot
from networkx.algorithms import community
from networkx.algorithms import cluster
from networkx.algorithms import assortativity
from networkx.algorithms.centrality import betweenness
import networkx.algorithms as alg
import numpy
from collections import OrderedDict
from networkx.algorithms import reciprocity

import itertools

'''
# Documentation:
https://networkx.github.io/documentation/latest/

useful graphs so far:
clustering coefficient bar graph for all nodes
    For unweighted graphs, the clustering of a node u is the fraction of possible triangles through that node that exist

'''

# graph = nx.read_edgelist("gplus_combined.txt", nodetype=int)

# nx.write_gexf(graph, "gplus.gexf")

# NETWORK = "twitter_"
NETWORK = "gplus_"


REDUCED_GEXF_FILE_NAME = NETWORK + "reduced.gexf"
graph = nx.read_gexf(REDUCED_GEXF_FILE_NAME, node_type=int)
# print(nx.info(graph))
# print(nx.degree_assortativity_coefficient(graph))

REDUCED_GEXF_FILE_NAME = NETWORK + "reduced_2.gexf"
graph2 = nx.read_gexf(REDUCED_GEXF_FILE_NAME, node_type=int)
# print(nx.info(graph))
# print(nx.degree_assortativity_coefficient(graph2))

REDUCED_GEXF_FILE_NAME = NETWORK + "reduced_3.gexf"
graph3 = nx.read_gexf(REDUCED_GEXF_FILE_NAME, node_type=int)
# print(nx.info(graph3))

# deg = [item[1] for item in graph.degree()]
# deg.sort()
# print(deg)

# Assortativity calculated:
# print(nx.degree_assortativity_coefficient(graph))
# print(nx.degree_assortativity_coefficient(graph2))
# print(nx.degree_assortativity_coefficient(graph3))
# Gplus: -0.14170952014515537, whole set: -0.08442274414025219
# Twitter: 0.19634890963252885

# avg clustering:
# print(cluster.average_clustering(graph))
# print(cluster.average_clustering(graph2))
# print(cluster.average_clustering(graph3))

# Gplus: 0.372609697038667, avg: 0.3160119141410101
# Twitter: 0.4349088962095986, avg: 0.40417451374667873

# Overall Reciprocity:
# print(nx.overall_reciprocity(graph))
# Gplus: 0.2834563629751221
# Twitter: 0.5668640683101501


# Eigenvector:
# data = nx.eigenvector_centrality(graph)
# data2 = nx.eigenvector_centrality(graph2)
# data3 = nx.eigenvector_centrality(graph3)



# values = [(list(data.values())[x] + list(data2.values())[x] + list(data3.values())[x])/3 for x in range(len(data.values()))]
# values.sort()

# names = list(data.keys())
# names = deg
# keys = data.keys()
# values = list(data_avg.values())

# neighbor_deg = OrderedDict(sorted(data.items()))
# neighbor_deg2 = OrderedDict(sorted(data2.items()))
# neighbor_deg3 = OrderedDict(sorted(data3.items()))
# neighbor_deg_avg = [(list(neighbor_deg.values())[x] + list(neighbor_deg2.values())[x] + list(neighbor_deg3.values())[x])/3 for x in range(len(neighbor_deg.values()))]

# # Degree Distribution Calculation
# deg_dict = OrderedDict(sorted(graph.degree(), key=lambda x: x[0]))
# deg_dict2 = OrderedDict(sorted(graph2.degree(), key=lambda x: x[0]))
# deg_dict3 = OrderedDict(sorted(graph3.degree(), key=lambda x: x[0]))
# deg_dict_avg = [(list(deg_dict.values())[x] + list(deg_dict2.values())[x] + list(deg_dict3.values())[x])/3 for x in range(len(deg_dict.values()))]
#
# deg_count_avg = [list(deg_dict_avg).count(x) for x in deg_dict_avg]
#
# # Degree Distribution Plot
# plt.scatter(deg_dict.values(), deg_count_avg, marker=".")
# plt.xlabel('Degree')
# plt.ylabel('Degree count')
# plt.show()


# print("len val:", len(values), "len deg:", len(deg))
# print(data)
# plt.bar(range(len(data)),values,tick_label=names)

# # Betweenness Centrality Data
# data = betweenness.betweenness_centrality(graph)
# data2 = betweenness.betweenness_centrality(graph2)
# data3 = betweenness.betweenness_centrality(graph3)

# # Betweenness Centrality Calculation
# values = [(list(data.values())[x] + list(data2.values())[x] + list(data3.values())[x])/3 for x in range(len(data.values()))]
# values.sort()
# keys = data.keys()
#
# # Betweenness Centrality Plot
# plt.scatter(values, range(len(keys)), marker=".")
#
# plt.xlabel('Betweenness Centrality of Nodes')
# plt.ylabel('Cumulative frequency of Nodes')
# # Twitter Annotation:
# plt.annotate('Median value at 0.00092 and 500', xytext=(0.01, 500), xy=(0.00092, 500), arrowprops = {'facecolor':'red'})
# # Google+ Annotation:
# plt.annotate('Median value at 0.0007 and 500', xytext=(0.0035, 500), xy=(0.0007, 500), arrowprops = {'facecolor':'red'})
# plt.show()

# Eigenvector Centrality:
# plt.scatter(values, range(len(keys)), marker=".")

# plt.xlabel('Eigenvector Centrality of Nodes')
# plt.ylabel('Cumulative frequency of Nodes')
# # plt.annotate('Median value at 0.00185 and 500', xytext=(0.0075, 500), xy=(0.00185, 500), arrowprops = {'facecolor':'red'}) # twitter
# plt.annotate('Median value at 0.0137 and 500', xytext=(0.045, 500), xy=(0.0137, 500), arrowprops = {'facecolor':'red'}) # gplus
# plt.show()


# # Assortativity Data
# data = assortativity.average_neighbor_degree(graph)
# data2 = assortativity.average_neighbor_degree(graph2)
# data3 = assortativity.average_neighbor_degree(graph3)
# # Assortativity Calculation
# neighbor_deg = OrderedDict(sorted(data.items()))
# neighbor_deg2 = OrderedDict(sorted(data2.items()))
# neighbor_deg3 = OrderedDict(sorted(data3.items()))
# neighbor_deg_avg = [(list(neighbor_deg.values())[x] + list(neighbor_deg2.values())[x] + list(neighbor_deg3.values())[x])/3 for x in range(len(neighbor_deg.values()))]
#
# deg_dict = OrderedDict(sorted(graph.degree(), key=lambda x: x[0]))
# deg_dict2 = OrderedDict(sorted(graph2.degree(), key=lambda x: x[0]))
# deg_dict3 = OrderedDict(sorted(graph3.degree(), key=lambda x: x[0]))
# deg_dict_avg = [(list(deg_dict.values())[x] + list(deg_dict2.values())[x] + list(deg_dict3.values())[x])/3 for x in range(len(deg_dict.values()))]
#
# # Assortativity Plot
# plt.scatter(deg_dict_avg, neighbor_deg_avg, marker=".")
# plt.xlabel('Degree')
# plt.ylabel('Average neighbour degree')
# plt.show()
# # Pearson Correlation of Plot:
# print(numpy.corrcoef(list(deg_dict_avg), list(neighbor_deg_avg))[0, 1])


# Clustering Data
data = OrderedDict(sorted((cluster.clustering(graph)).items()))
data2 = OrderedDict(sorted((cluster.clustering(graph2)).items()))
data3 = OrderedDict(sorted((cluster.clustering(graph3)).items()))

# Clustering Calculation
values = [(list(data.values())[x] + list(data2.values())[x] + list(data3.values())[x])/3 for x in range(len(data.values()))]
values.sort()
keys = data.keys()

# Clustering Plot
plt.scatter(values, range(len(keys)), marker=".")
plt.ylabel('Cumulative frequency of Nodes')
plt.xlabel('Local Clustering Coefficient Value of Nodes')
# Twitter Annotation:
plt.annotate('Median value at 0.4 and 500', xytext=(0.45, 500), xy=(0.402, 500), arrowprops = {'facecolor':'red'})
# # Google+ Annotation:
plt.annotate('Median value at 0.3 and 500', xytext=(0.35, 500), xy=(0.302, 500), arrowprops = {'facecolor':'red'})
plt.show()


'''
older code

'''

# plt.bar(range(len(D)), list(D.values()), align='center')
# plt.xticks(range(len(D)), list(D.keys()))
# plt.show()

# print(cluster.transitivity(graph))
# print(nx.degree_assortativity_coefficient(graph))
# cGraph = clique.make_max_clique_graph(graph)
# print(nx.info(cGraph))

# communities
# lists = sorted(data.items()) # sorted by key, return a list of tuples

# x, y = zip(*lists) # unpack a list of pairs into two tuples

# plt.scatter(x, y)
# plt.show()
# communities_generator = community.girvan_newman(graph)
# # print(communities_generator)
# for communities in communities_generator:
#     print(list(communities))


# print()


# graph = nx.Graph()
# nodes = nx.path_graph(10**3)
# graph.add_nodes_from(nodes)
# print(nx.eigenvector_centrality(graph))
# communities_generator = community.girvan_newman(graph)

# print(tuple(sorted(c) for c in next(communities_generator)))

# k = 2
# for communities in itertools.islice(communities_generator, k):
#     print(tuple(sorted(c) for c in communities))

# nx.write_gexf(graph, "facebook.gexf")

# spring_layout = nx.spring_layout(graph)
# plot.axis("off")

# nx.draw_networkx(graph, pos = spring_layout, with_lavels=False, node_size=35)

# plot.show()
