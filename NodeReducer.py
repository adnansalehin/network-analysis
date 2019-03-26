
# specify gplus or twitter file names here:

EXISTING_FILE_NAME = "gplus_combined.txt"
REDUCED_GEXF_FILE_NAME = "gplus_reduced"
NUMBER_OF_NODES = 1000

import networkx as nx
import random

def readFile():
    edgelist = open(EXISTING_FILE_NAME)
    return edgelist

# edgelist = readFile()
nodeSet = set()
while len(nodeSet)<NUMBER_OF_NODES:
    # line = edgelist.readline()
    fl=open(EXISTING_FILE_NAME)
    lines = fl.read().splitlines()
    line = random.choice(lines)
    node = (line.split(" ")[0]).strip()
    nodeSet.add(node)
    fl.close()
# edgelist.close()

# edgelist = readFile()
nodeSet2 = set()
while len(nodeSet2)<NUMBER_OF_NODES:
    fl=open(EXISTING_FILE_NAME)
    lines = fl.read().splitlines()
    line = random.choice(lines)
    node = (line.split(" ")[0]).strip()
    if node not in nodeSet:
        nodeSet2.add(node)
# edgelist.close()

# edgelist = readFile()
nodeSet3 = set()
while len(nodeSet3)<NUMBER_OF_NODES:
    fl=open(EXISTING_FILE_NAME)
    lines = fl.read().splitlines()
    line = random.choice(lines)
    node = (line.split(" ")[0]).strip()
    if node not in nodeSet and node not in nodeSet2: 
        nodeSet3.add(node)
# edgelist.close()

graph = nx.read_edgelist(EXISTING_FILE_NAME, create_using=nx.DiGraph, nodetype=int)

subgraph = graph.subgraph(list(map(int, nodeSet)))
subgraph2 = graph.subgraph(list(map(int, nodeSet2)))
subgraph3 = graph.subgraph(list(map(int, nodeSet3)))

nx.write_gexf(subgraph, REDUCED_GEXF_FILE_NAME+"_r.gexf")
nx.write_gexf(subgraph2, REDUCED_GEXF_FILE_NAME+"_2_r.gexf")
nx.write_gexf(subgraph3, REDUCED_GEXF_FILE_NAME+"_3_r.gexf")
