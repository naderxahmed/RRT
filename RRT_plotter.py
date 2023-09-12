
from RRT import * 
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection


class Plotter:

    def __init__(self,rrt):
        self.rrt = rrt 
        self.fig,self.ax = plt.subplots()
        self.plot_vertices()
        self.plot_edges() 
        plt.show()

    
    def plot_vertices(self): 
        for v in self.rrt.G: 
            plt.plot(v[0],v[1],'bo')
    
    def plot_edges(self):
        segs = [] 
        for v in self.rrt.G.keys():
            v_primes = self.rrt.G[v] 
            if len(v_primes) > 0: 
                for vp in v_primes: 
                    segs.append(np.array([v,vp]))
        
        line_segments = LineCollection(segs, linewidths=(1),
                                colors='black', linestyle='solid')
        self.ax.add_collection(line_segments)


def main(): 

    rrt = RRT(q_init=(50,50),K=100,delta=1,D=(100,100))
    plotter = Plotter(rrt)

main() 

    


