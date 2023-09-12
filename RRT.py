import matplotlib.pyplot as plt 
import numpy as np 
from numpy.linalg import norm

class RRT: 

    def __init__(self,q_init,K,delta,D): 

        self.q_init=q_init 
        self.K=K 
        self.delta=delta
        self.D=D
        self.circle_obstacles = []
        self.generate_circle_obstacles(5)
        self.G = self.create_RRT(self.q_init,K,delta)
        
    def create_RRT(self,q_init,K,delta): 
        G = {} #key: position, value: edges. extend to the edges for nodes it is connected to
        G[q_init]=[]

        for i in range(K): 
            q_rand = self.generate_random_point() 
            q_near = self.nearest_vertex(q_rand,G)
            q_new = self.new_configuration(G,q_near,q_rand,delta)

            G[q_new]=[] 
            print(self.check_circle_collision(q_near,q_new))
            if q_new not in G[q_near] and self.check_circle_collision(q_near,q_new):
                G[q_near].append(q_new)
                

        return G
        

    #compute eucliean dist bw p1, p2
    def compute_distance(self,p1,p2): 
        p1 = np.array(p1) 
        p2 = np.array(p2) 
        return np.linalg.norm(p1-p2)

    #add a random new vertex. go to the nearest vertex, add a distance delta TOWARDS q_rand
    def new_configuration(self,G,q_near,q_rand,delta): 

        q_near = np.array(q_near) #src
        q_rand = np.array(q_rand) #dest

        v = q_rand-q_near
        dir = v / np.sqrt(np.sum(v**2))
        q_new = ( q_near[0] + (delta * dir[0]) , q_near[1] + (delta * dir[1]))

        return q_new 


    #find vertex in G closest to q_rand
    def nearest_vertex(self,q_rand,G): 
        min=np.inf
        min_dist_vertex=np.inf

        for vertex in G.keys(): #key: position, value: edges. append to the edges for nodes it is connected to
            dist = self.compute_distance(q_rand, vertex) 
            if dist < min: 
                min=dist 
                min_dist_vertex = vertex 
        
        return min_dist_vertex 


    #generate random point in domain D
    def generate_random_point(self): 
        return (np.random.uniform(low=0,high=self.D[0]),
                np.random.uniform(low=0,high=self.D[1]))
    
    
    #generate n circular obstacles
    def generate_circle_obstacles(self,n): 
        for _ in range(n):
            center = self.generate_random_point()
            r = np.random.uniform(low=2,high=self.D[0]/10)
            self.circle_obstacles.append([center[0],center[1],r])

    def check_circle_collision(self, q_near, q_new): 
        q_near = np.array(q_near)
        q_new = np.array(q_new) 
      
        line = q_new-q_near 
        distances = [] 

        for crc in self.circle_obstacles: 
            d = np.abs(norm(np.cross(q_new-q_near, q_near-crc[2])))/norm(q_new-q_near)
            distances.append(d) 


            if d < crc[2]: 
                print(d,crc[2])
                return False 
            
            qnx, qny = q_new
            qnrx, qnry = q_near
            
            
            
        return True 

        


        


         
    




        



