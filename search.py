# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

from game import Directions
import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def expand(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (child,
        action, stepCost), where 'child' is a child to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that child.
        """
        util.raiseNotDefined()

    def getActions(self, state):
        """
          state: Search state

        For a given state, this should return a list of possible actions.
        """
        util.raiseNotDefined()

    def getActionCost(self, state, action, next_state):
        """
          state: Search state
          action: action taken at state.
          next_state: next Search state after taking action.

        For a given state, this should return the cost of the (s, a, s') transition.
        """
        util.raiseNotDefined()

    def getNextState(self, state, action):
        """
          state: Search state
          action: action taken at state

        For a given state, this should return the next state after taking action from state.
        """
        util.raiseNotDefined()

    def getCostOfActionSequence(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def graphSearch(problem, frontier):
    """
    Algoritmo genérico para la búsqueda en grafos.
    Recibe la clase asociada al problema y el manejo de la frontera.
    """
    expanded = [] # Lista que almacena todos los nodos que se hayan expandido (explorado)
    path = [] # Lista que almacena el camino recorrido
    while not frontier.isEmpty():
        """
        Mientras podamos explorar, utilizamos node para obtener, en base a algún criterio,
        el nodo a analizar para comprobar si es el goal, o si podemos seguir explorando.
        """
        node = frontier.pop()
        if problem.isGoalState(node[0]):
            path.append(node)
            path_to_node = path_to_goal(problem, path)
            return path_to_node

        if node[0] not in expanded:
            expanded.append(node[0])
            if (node[1]):
                path.append(node)
            for child in problem.expand(node[0]):
                frontier.push( (child[0], child[1]) )
    return [Directions.STOP]

def path_to_goal(problem, path):
    """
    Cuando se encuentra el goal en el algoritmo de búsqueda, se reconstruye el camino para poder
    llegar a él
    """
    start = problem.getStartState()
    to_goal = []
    temp = path.pop()
    flag = 0
    while flag < len(path):
        if temp[1] in problem.getActions(start):
            if problem.getNextState(start, temp[1]) == temp[0]:
                to_goal.append(temp[1])
                break
        for move in path:
            if temp[1] in problem.getActions(move[0]):
                if problem.getNextState(move[0], temp[1]) == temp[0]:
                    to_goal.append(temp[1])
                    temp = move
                    break
        flag = flag + 1
    return list(reversed(to_goal))
        

def depthFirstSearch(problem):
    """
    Implementación de DFS. Utiliza un Stack para manejar la frontera.
    """
    frontier = util.Stack()
    frontier.push( (problem.getStartState(), False) )
    return graphSearch(problem, frontier)
def breadthFirstSearch(problem):
    """
    Implementación de BFS. Utiliza una Queue para manejar la frontera.
    """
    frontier = util.Queue()
    frontier.push( (problem.getStartState(), False) )
    return graphSearch(problem, frontier)

    # util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic = nullHeuristic):
    """
    Implementación de A*. Utiliza una Priority Queue para manejar la frontera, donde cada
    prioridad se maneja a través de una heurística.
    """
    
    frontier = util.PriorityQueue()
    start = problem.getStartState()
    frontier.push( (problem.getStartState(), False), 0 + heuristic(start, problem) )
    expanded = []
    path = []
    while not frontier.isEmpty():
        node = frontier.pop()
        if problem.isGoalState(node[0]):
            path.append(node)
            path_to_node = path_to_goal(problem, path)
            return path_to_node

        if node[0] not in expanded:
            expanded.append(node[0])
            if (node[1]):
                path.append(node)
            for child in problem.expand(node[0]):
                frontier.push( (child[0], child[1]), child[2] + heuristic(child[0], problem) )
    return [Directions.STOP]

    # util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
