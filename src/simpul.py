import copy
import _pickle as cPickle
from heapq import heappush, heappop
from queue import PriorityQueue
import enum
from util import *
# creating enumerations using class
class Directions(enum.Enum):
    DOWN = [1,0]
    LEFT = [0,-1]
    UP = [-1,0]
    RIGHT = [0,1]

class PrioQueue:
    def __init__(self):
        self.heap = []
    # Insert new element
    def push(self, k):
        heappush(self.heap, k)
    # Remove minimum element
    def pop(self):
        return heappop(self.heap)
    # Check if the Queue is empty
    def isEmpty(self):
        if not self.heap:
            return True
        else:
            return False

def solve(pq, tracker) :
    # If initial node is solution
    count = 0
    while not pq.empty() :
        simpul = pq.get()
        if (isSolution(simpul[1])) : 
            printPath(simpul[0], tracker)
            return count

        for move in Directions :
            if (move.name == getCounterMove(simpul[5])) : 
                continue
            new_tilekosong = [simpul[2][0] + move.value[0], simpul[2][1] + move.value[1]]
            if (isValidMove(new_tilekosong)) :
                new_matrix = cPickle.loads(cPickle.dumps(simpul[1], -1))

                x1 = simpul[2][0]
                y1 = simpul[2][1]
                x2 = new_tilekosong[0]
                y2 = new_tilekosong[1]
                new_matrix[x1][y1], new_matrix[x2][y2] = new_matrix[x2][y2], new_matrix[x1][y1]
                if (new_matrix in tracker) :
                    continue
                tracker.append(new_matrix)
                new_cost = countMisplacedTiles(new_matrix)
                count += 1
                new_simpul = [count, new_matrix, new_tilekosong, new_cost, simpul[4] + 1, move]
                pq.put(new_simpul)
    

# class TreeNode:
#     def __init__(self, parent, matrix, tilekosong, cost, moves, prev_move):
#         self.parent = parent
#         self.matrix = matrix
#         self.tilekosong = tilekosong
#         self.cost = cost
#         self.moves = moves
#         self.prev_move_enum = prev_move

#     def isBetter(self, other):
#         return self.cost < other.cost

#     def isSolution(self):
#         return (countMisplacedTiles(self.matrix) == 0)

#     def getParent(self):
#         return self.parent

# def createTreeNode(parent, matrix, tilekosong, new_tilekosong, moves) :
#     new_matrix = copy.deepcopy(matrix)

#     x1 = tilekosong[0]
#     y1 = tilekosong[1]
#     x2 = new_tilekosong[0]
#     y2 = new_tilekosong[1]
#     # Swap
#     matrix[x1][y1], matrix[x2][y2] = matrix[x2][y2], matrix[x1][y1]

#     # Set number of misplaced tiles
#     cost = countMisplacedTiles(matrix)

#     simpulBaru = (parent, matrix, new_empty_tile_pos, cost, moves, None)
#     return simpulBaru