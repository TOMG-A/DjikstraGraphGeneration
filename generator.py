from djikstra.node import *
import random
import math
import time

def GenerateGraph(n:int,P:float,maxWeight:int) -> Graph:
    ## Clamps probability value between 0->1
    start_time=time.process_time()
    P=max(0,min(P,1))
    graph=Graph([])

    for x in range(n):
        ## Name Format: [A-Z]_[A-]
        ## First half increments every node
        ## Second half increments every 26 nodes
        name=f"{chr(65+x-(26*(x//26)))}_{chr((65)+x//26)}"

        ## New node added to the graph
        graph.append(Node(name))
    for x in graph:
        for y in graph:
            if x!=y and random.randrange(0,int(math.pow(P,-1)))==1:
                weight=random.randrange(1,maxWeight)
                print(f"Create Edge Between {x} and {y} with weight {weight}")
                x.add_child(y,weight)
    return graph,(time.process_time()),start_time