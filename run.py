from RRT import RRT
from RRT_plotter import Plotter

def main():
    rrt = RRT(q_init=(40,40), q_goal=(60,60),K=5000,delta=1.25,D=(100,100), num_circle_obstacles=0, 
              image_path="N_map.png")
    
    plotter = Plotter(rrt)
    plotter.show()
    
if __name__ == "__main__":
    main()