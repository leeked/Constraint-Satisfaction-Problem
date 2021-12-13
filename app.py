"""
CS-UY 4613
Source Code for Project 2: Map Coloring Problem

Author: Kevin Lee (KL3642)

Description: Implement the Backtracking algorithm
for solving the Map Coloring Problem.
"""

# Standard Libraries
import sys
import copy

# Node Class for each variable
class Node:
    def __init__(self, name, adj, domain):
        self.name = name
        self.adj = adj
        self.domain = domain

# Problem Class
class Problem:
    def __init__(self, num_var, num_domain, var_names, var_list):
        self.num_var = num_var
        self.domain = num_domain
        self.var_names = var_names
        self.var_list = var_list

def search(csp):

def main():
    # Grab filename and w from stdin
    filename = sys.argv[1]

    # Open File and parse input
    f = open(filename)
    lines = f.readlines()

    print(lines)

    # Init problem variables
    num_var = 0
    num_domain = 0
    var_names = []
    var_list = []

    # Init node variables
    domain = []

    # Assign values
    num_var, num_domain = int(lines[0][0]), int(lines[0][2])
    
    for name in lines[1].strip().split(' '):
        var_names.append(name)

    for domain_val in lines[2].strip().split(' '):
        domain.append(domain_val)

    # Parsing adjacency list
    ind = 0
    for line in lines[3:-1]:
        new_adj_list = []
        adj_ind = 0
        for adj in line.strip().split(' '):
            if int(adj) == 1:
                new_adj_list.append(var_names[adj_ind])

            adj_ind += 1
        var_list.append(Node(var_names[ind], new_adj_list, copy.deepcopy(domain)))
        ind += 1

    # Create problem
    problem = Problem(num_var, num_domain, var_names, var_list)

    #res = search(problem)

if __name__=='__main__':
    main()