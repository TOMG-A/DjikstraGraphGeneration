import djikstra
import generator

graph=generator.GenerateGraph(200,0.1,20)
a,b=djikstra.Dijkstra(graph,graph[0])
print(a)