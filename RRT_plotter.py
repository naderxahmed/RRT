
from RRT import * 
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

class RRT_plotter: 
    # RRT.g: key: position tuple, value: vertices which an edge needs to be drawn to

    def __init__(self,RRT): 
        self.RRT = RRT 
        self.plot_RRT()
        fig, ax = plt.subplots()
        # ax.set_xlim(0,100)
        # ax.set_ylim(0,100)

     
    def plot_vertices(self): 

        for v in self.RRT.G: 
            print(v)
            plt.plot(v[0],v[1],'bo')
            
    
    def plot_edges(self): 

        #each vertex with list of points it is connected to 
        #v connects to v'


        x_values = []
        y_values = [] 

        for v in self.RRT.G.items(): 
            for v_prime in v: 
                if len(v_prime)>0: 
                   
                   x_values.append(v[0])
                   x_values.append(v_prime[0])

                   y_values.append(v[1])
                   y_values.append(v_prime[1])

        plt.plot(x_values,y_values,'o') 
        
    def plot_RRT(self): 
        self.plot_vertices() 
        self.plot_edges()
        plt.xlabel("X") 
        plt.ylabel("Y") 
        plt.show() 

def main(): 

    rrt = RRT(q_init=(0,0),K=50,delta=1,D=(100,100))
    # print(rrt.G)
    plotter = RRT_plotter(rrt) 
    plotter.plot_vertices

main() 

    


