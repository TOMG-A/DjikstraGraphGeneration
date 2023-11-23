import djikstra
import generator

graph,end,start=generator.GenerateGraph(200,0.1,20)
a,b,overall_time=djikstra.Dijkstra(graph,graph[0])
print(a)

print(f"Graph Generation Runtime: {(end)*100} ms")
print(f"Total Runtime: {(overall_time-start)*100} ms")