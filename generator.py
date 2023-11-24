from djikstra.node import *
import random
import math
import time

def GenerateGraph(n:int,P:float,maxWeight:int) -> Graph:
    
    start_time=time.time()
    ## Clamps probability value between 0->1
    P=max(0,min(P,1))

    ## Generates Graph with n amount of nodes
    graph=Graph([Node(f"{chr(65+i-(26*(i//26)))}_{chr((65)+i//26)}") for i in range(n)])

    for x in graph:
        ## Initially used x!=y to assure edge isn't created between a node and itself
        ## [1:] reduces graph generation time by ~13ms
        for y in graph[1:]:
            if random.random()<P:
                weight=random.randint(1,maxWeight)
                # print(f"Create Edge Between {x} and {y} with weight {weight}")
                x.append(y,weight)
    return graph,(time.time()),start_time