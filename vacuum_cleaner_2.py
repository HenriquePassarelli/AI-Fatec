""" 
    ## requirements

    linux users - sudo apt install python3-tk
    pip3 install matplotlib
    Reference - https://github.com/mawippel/python-vacuum/blob/master/complex-agent-robot.py

    run - python3 vacuum_cleaner_2.py

 """

import matplotlib.pyplot as plt
import random
from tkinter import messagebox
from copy import copy, deepcopy


    # Node Object, represents a position in the matrix array
class Node:
    def __init__(self, x, y, parent=None):
        self.x = x
        self.y = y
        self.parent = parent

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_parent(self, parent):
        self.parent = parent

    def get_parent(self):
        return self.parent

# 0 -> clean
# 1 -> wall
# 2 -> dirt
matrix = [
    [1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1]
]

presentationMatrix = [
    [1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1]
]

# The robot always starts at matrix[1][1]
currLine = 1
currCol = 1
stack = [Node(1, 1)]
solution = [Node(1, 1)]
process_map = []


def mapNotClean():
    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[i]) - 1):
            if (matrix[i][j] == 2):
                return True
    return False


def renderMatrix(matrix):
    plt.imshow(matrix, 'pink')
    plt.show(block=False)
    plt.plot(currCol, currLine, '*r', 'LineWidth', 5)
    plt.pause(0.5)
    plt.clf()


def createWorld(m):
    for mI in range(1, 5):
        for aI in range(1, 5):
            if (mI == 1 and aI == 1):
                continue
            number = random.randint(0, 3)
            m[mI][aI] = 2 if number == 1 else 0
    renderMatrix(matrix)
    global process_map
    global presentationMatrix
    process_map = deepcopy(matrix)
    presentationMatrix = deepcopy(matrix)


def hasPosition(x, y):
    if (matrix[x][y] == 1):
        return False
    return True


def lookLeft(x, y, node):
    if (hasPosition(x - 1, y)):
        new_node = Node(x - 1, y, node)
        if (process_map[x - 1][y] == 2):
            return new_node
        if (process_map[x - 1][y] != 4):
            stack.append(new_node)
            process_map[x - 1][y] = 4


def lookRight(x, y, node):
    if (hasPosition(x + 1, y)):
        new_node = Node(x + 1, y, node)
        if (process_map[x + 1][y] == 2):
            return new_node
        if (process_map[x + 1][y] != 4):
            stack.append(new_node)
            process_map[x + 1][y] = 4


def lookAbove(x, y, node):
    if (hasPosition(x, y - 1)):
        new_node = Node(x, y - 1, node)
        if (process_map[x][y - 1] == 2):
            return new_node
        if (process_map[x][y - 1] != 4):
            stack.append(new_node)
            process_map[x][y - 1] = 4


def lookDown(x, y, node):
    if (hasPosition(x, y + 1)):
        new_node = Node(x, y + 1, node)
        if (process_map[x][y + 1] == 2):
            return new_node
        if (process_map[x][y + 1] != 4):
            stack.append(new_node)
            process_map[x][y + 1] = 4


def discoverPath():
    while (len(stack) != 0):
        node = stack.pop(0)
        x = node.get_x()
        y = node.get_y()

        auxNode = lookLeft(x, y, node)
        if (auxNode):
            return auxNode

        auxNode = lookAbove(x, y, node)
        if (auxNode):
            return auxNode

        auxNode = lookRight(x, y, node)
        if (auxNode):
            return auxNode

        auxNode = lookDown(x, y, node)
        if (auxNode):
            return auxNode


def main():
    global matrix
    global process_map
    global stack
    global currCol
    global currLine
    
    createWorld(matrix)

    while (mapNotClean()):
        path = discoverPath()
        x = path.get_x()
        y = path.get_y()

        aux_list = []
        while (path.get_parent() is not None):
            process_map[path.get_x()][path.get_y()] = 3
            aux_list.append(path)
            path = path.get_parent()
        aux_list.reverse()
        solution.extend(aux_list)

        matrix[x][y] = 0
        stack = [Node(x, y)]
        process_map = deepcopy(matrix)

    for path in solution:
        currCol = path.get_y()
        currLine = path.get_x()
        renderMatrix(presentationMatrix)
        if (presentationMatrix[currLine][currCol] == 2):
            presentationMatrix[currLine][currCol] = 0
    renderMatrix(presentationMatrix)
    messagebox.showinfo(
        "Vacuum Problem", "The vacuum took %s steps" % (len(solution) - 1))

if __name__ == "__main__":
    main()


