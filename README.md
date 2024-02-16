RRT, or Rapidly-exploring Random Tree, is a probabilistic algorithm used for pathfinding and motion planning in robotics and computer graphics. It efficiently explores the configuration space of a robot or an agent to find a feasible path from a start point to a goal point amidst obstacles.

To see a demo of the tree expansion around an obstacle, clone the repository and run `python run.py`!

<p align="center">
    <img src="assets/RRT.gif" alt="Motion Model" width="500" height="300"/>
</p>

Here's how RRT works:

    Initialization: The algorithm starts with a tree containing only the start node.

    Expansion: In each iteration, a random point is generated within the configuration space. This point is then connected to the nearest node in the existing tree. The new node becomes part of the tree if the path to it is obstacle-free.

    Goal Check: At each iteration, the algorithm checks if the newly added node is close to the goal state. If it is, a path has potentially been found.

    Termination: The algorithm continues to expand the tree until a specified number of nodes are added, or until a path to the goal is found.

    Path Extraction: Once the goal is reached or the maximum number of iterations is reached, the algorithm traces back from the goal node to the start node, extracting the path that connects them.

RRT is particularly useful in scenarios where the configuration space is complex or high-dimensional, and where traditional grid-based methods become inefficient. Its probabilistic nature allows it to efficiently explore the space without exhaustive searching, making it suitable for real-time applications.