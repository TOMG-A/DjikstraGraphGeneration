import djikstra
import generator
import networkx as NX
import random


graph,end,start=generator.GenerateGraph(10,2/10,20)
startPoint=generator.getReachableNode(graph)
a,b,overall_time=djikstra.Dijkstra(graph,startPoint)
print(a)

print(f"Graph Generation Runtime: {end-start} ms")
print(f"Djikstra's Algorithm Runtime: {overall_time-end} ms")
print(f"Total Runtime: {overall_time-start} ms")

print(start)
print(overall_time)
print(overall_time-end)
#### EDGELIST CONVERSION ---- TEST ####
convert={}
for a,x in enumerate(graph):
    convert[a]=[]
    for y in x.children:
        convert[a].append(graph._Vertices.index(y[0]))
# G=NX.from_dict_of_lists(convert)
#### TO STRING FOR ONLINE GRAPH GENERATOR ####
new=""
for a,x in enumerate(graph):
    for y in x.children:
        new=new+f"\n{x} {y[0]} {y[1]}"
# print(new)