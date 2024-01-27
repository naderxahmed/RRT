from RRT import RRT
from RRT_plotter import Plotter

def main():
    rrt = RRT(q_init=(10,10), q_goal=(40,40),K=1000,delta=1.75,D=(50,50), num_circle_obstacles=5)
    plotter = Plotter(rrt)
    plotter.show()

if __name__ == "__main__":
    main()