from venv import create
import matplotlib.pyplot as plt 
import numpy as np 

class RRT: 

    def __init__(self,q_init,K,delta,D): 
        self.q_init=q_init 
        self.K=K 
        self.delta=delta
        self.D=D

        self.G = self.create_RRT(self.q_init,K,delta,D)

    def create_RRT(self,q_init,K,delta,D): 
        G = {} #key: position, value: edges. extend to the edges for nodes it is connected to
        G[q_init]=[]

        for i in range(K): 
            q_rand = self.generate_random_point(D) 
            q_near = self.nearest_vertex(q_rand,G)
            q_new = self.new_configuration(G,q_near,q_rand,delta)

            G[q_new]=[]
            G[q_near].append(q_new)

        return G
        

    #compute eucliean dist bw p1, p2
    def compute_distance(self,p1,p2): 
        p1 = np.array(p1) 
        p2 = np.array(p2) 
        return np.linalg.norm(p1-p2)

    #add a new vertex. go to the nearest vertex, add a distance delta TOWARDS q_rand
    def new_configuration(self,G,q_near,q_rand,delta): 
        x1,y1 = q_near 
        x2,y2 = q_rand 

        v = np.array([(x2-x1),(y2-y1)])
        unit_v = v / np.sqrt(np.sum(v**2))
        q_new = (delta * unit_v[0], delta * unit_v[1])
        return q_new 


    #find vertex in G closest to q_rand
    def nearest_vertex(self,q_rand,G): 
        min=np.inf
        min_dist_vertex=np.inf

        for vertex in G.keys(): #key: position, value: edges. extend to the edges for nodes it is connected to
            dist = self.compute_distance(q_rand,vertex) 
            if dist < min: 
                min=dist 
                min_dist_vertex = vertex 
        
        return min_dist_vertex 


    #generate random point in domain D
    def generate_random_point(self,D): 
        return (np.random.uniform(low=0,high=D[0]),np.random.uniform(low=0,high=D[1]))

def main(): 

    rrt = RRT(q_init=(0,0),K=10,delta=1,D=(50,50))
    print(rrt.G)

main() 