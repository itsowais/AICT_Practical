# uncomment lines 97 87 85 42 4 to see graph if you have matplotlib installed
import networkx as nx
import queue as Q
#import matplotlib.pyplot as plt
 
def getPriorityQueue(G, v):
	q = Q.PriorityQueue()
	for node in G[v]:
		q.put(Ordered_Node(float(heuristics[node])+float(G[node][v]['length']),node))
	return q,len(G[v])

def aStarSearchUtil(G, v, visited, final_path, dest, goal): 
	if goal == 1:
		return goal
	visited[v] = True
	final_path.append(v)
	if v == dest:
		goal = 1
	else:
		pq_list = []
		pq,size = getPriorityQueue(G, v)
		for i in range(size):
			#print(pq.get().description)
			pq_list.append(pq.get().description)
		for i in pq_list:
			if goal != 1:
				#print ("current city:", i)
				if visited[i] == False :
					goal = aStarSearchUtil(G, i, visited, final_path, dest, goal)
	return goal
 
def aStarSearch(G, source, dest, heuristics, pos): 
	visited = {}
	for node in G.nodes():
		visited[node] = False
	final_path = []
	goal = aStarSearchUtil(G, source, visited, final_path, dest, 0)
	#print(final_path)
	prev = -1
	for var in final_path:
		#print(var)
		if prev != -1:
			curr = var
			#nx.draw_networkx_edges(G, pos, edgelist = [(prev,curr)], width = 2.5, alpha = 0.8, edge_color = 'black')
			prev = curr
		else:
			prev = var
	return final_path

class Ordered_Node(object):
	def __init__(self, priority, description):
		self.priority = priority
		self.description = description
		return
	def __lt__(self, other):
		return self.priority < other.priority

def getHeuristics(G):
	heuristics = {}
	f = open('heuristic.txt')
	for i in G.nodes():
		node_heuristic_val = f.readline().split()
		heuristics[node_heuristic_val[0]] = node_heuristic_val[1]
	#print(heuristics)
	return heuristics

#takes input from the file and creates a weighted graph
def CreateGraph():
	G = nx.Graph()
	f = open('Graph.txt')
	n = int(f.readline())
	for i in range(0,23):
		graph_edge_list = f.readline().split()
		if len(graph_edge_list)==3:
			G.add_edge(graph_edge_list[0], graph_edge_list[1], length = graph_edge_list[2])
	source, dest= f.read().splitlines()
	#print(source)
	#print(dest)
	return G, source, dest

def DrawPath(G, source, dest):
	pos = nx.spring_layout(G)
	val_map = {}
	val_map[source] = 'green'
	val_map[dest] = 'red'
	values = [val_map.get(node, 'blue') for node in G.nodes()]
	#nx.draw(G, pos, with_labels = True, node_color = values, edge_color = 'b' ,width = 1, alpha = 0.7)  #with_labels=true is to show the node number in the output graph
	edge_labels = dict([((u, v,), d['length']) for u, v, d in G.edges(data = True)])
	#nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels, label_pos = 0.5, font_size = 11) #prints weight on all the edges
	#print(pos)
	return pos

#main function
if __name__ == "__main__":
	G, source,dest = CreateGraph()
	heuristics = getHeuristics(G)
	pos = DrawPath(G, source, dest)
	print(aStarSearch(G, source, dest, heuristics, pos))
#	plt.show()
# uncomment lines 97 87 85 42 to see graph if you have matplotlib installed