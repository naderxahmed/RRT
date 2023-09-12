
from RRT import * 
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

class RRT_plotter: 
    # RRT.g: key: position tuple, value: vertices which an edge needs to be drawn to

    def __init__(self,RRT): 
        self.RRT = RRT 
        self.plot_RRT()
        self.fig, self.ax = plt.subplots()

        # ax.set_xlim(0,100)
        # ax.set_ylim(0,100)

     
    def plot_vertices(self): 

        for v in self.RRT.G: 
            # print(v)
            plt.plot(v[0],v[1],'bo')
            
    
    def plot_edges(self): 

        #each vertex with list of points it is connected to 
        #v connects to v'

        x_values = []
        y_values = [] 
        segs = [] 

        line_segments = LineCollection(segs, linewidths=(.5),
                               colors='red', linestyle='solid')
        

        for v in self.RRT.G.keys():
    
            v_primes = self.RRT.G[v] 

            if len(v_primes) > 0: 
                for vp in v_primes: 
                    segs.append(np.array([v,vp]))
        

           
        self.ax.add_collection(line_segments)
        

        
    def plot_RRT(self): 
        self.plot_vertices() 
        self.plot_edges()
        self.ax.xlabel("X") 
        self.ax.ylabel("Y") 
        self.ax.show() 

def main(): 

    rrt = RRT(q_init=(50,50),K=50,delta=.001,D=(100,100))

    fig,ax = plt.subplots()
    for v in rrt.G: 
        plt.plot(v[0],v[1],'bo')

    segs = [] 
    for v in rrt.G.keys():

        v_primes = rrt.G[v] 

        if len(v_primes) > 0: 
            for vp in v_primes: 
                segs.append(np.array([v,vp]))
    
    line_segments = LineCollection(segs, linewidths=(1),
                            colors='black', linestyle='solid')
    
    ax.add_collection(line_segments)


    plt.show()

main() 

    


