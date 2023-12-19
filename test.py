import dijkstra
import generator

#### Generally 2/N returns a reasonable amount of edges,
#### With minimal amount of unreachable nodes
n=int(input("Enter quantity of nodes:\n"))

graph,end,start=generator.GenerateGraph(n,5/n,20)
startPoint=generator.getReachableNode(graph)
a,b,overall_time=dijkstra.Dijkstra(graph,startPoint)
print(f"STARTING NODE: {startPoint}")
print(f"Graph Generation Runtime: {round(end-start,3)*100} ms")
print(f"dijkstra's Algorithm Runtime: {round(overall_time-end,3)*100} ms")
print(f"Total Runtime: {round(overall_time-start,3)*100} ms")
for x in a:
    print(f"Distance to {x} from {startPoint} --> {a[x]}")




#### EDGELIST CONVERSION ---- TEST ####
convert={}
for a,x in enumerate(graph):
    convert[a]=[]
    for y in x.children:
        convert[a].append(graph._Vertices.index(y[0]))
# G=NX.from_dict_of_lists(convert)

#### TO STRING FOR ONLINE GRAPH GENERATOR ####
#### Enter text to https://csacademy.com/app/graph_editor/
Enabled=False
new=""
for a,x in enumerate(graph):
    for y in x.children:
        new=new+f"\n{x} {y[0]} {y[1]}"
if Enabled:
    print(new)
