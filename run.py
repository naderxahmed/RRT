from RRT import RRT
from RRT_plotter import Plotter

def main():
    rrt = RRT(q_init=(10,10),K=500,delta=1,D=(50,50), num_circle_obstacles=10)
    plotter = Plotter(rrt)
    plotter.show()

if __name__ == "__main__":
    main()