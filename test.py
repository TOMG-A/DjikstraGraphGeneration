import djikstra
import generator

graph,end,start=generator.GenerateGraph(200,0.1,20)
a,b,overall_time=djikstra.Dijkstra(graph,graph[0])
print(a)

print(f"Graph Generation Runtime: {round(end-start,3)*100} ms")
print(f"Djikstra's Algorithm Runtime: {round(overall_time-end,3)*100} ms")
print(f"Total Runtime: {round(overall_time-start,3)*100} ms")