#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

     Author: Hsieh, Li-Yi (lyshie@tn.edu.tw)
       Date: 2016-09-20 21:32:00
Description: Brute-force method to find the longest chain of
             factors-and-multiples game.

             Factors and Multiples Game
             https://nrich.maths.org/5468

'''

from __future__ import print_function
import sys

MAX = 100     # 1..100 numbers
LONGEST = 0   # record the current length of longest chain
NODES = []    # numbers that have been chosen
TABLES = []   # factors and multiples relational matrix
PATH = []     # longest chain


def init(t, n, p):
    '''
    two-dimensional matrix to represent factors and multiples relations
    '''
    global MAX

    # all to zero
    for i in xrange(0, MAX + 1):
        n.append(0)
        row = []
        for j in xrange(0, MAX + 1):
            row.append(0)
        t.append(row)

    # factors-and-multiples relation
    for i in xrange(1, MAX + 1):
        for j in xrange(i, MAX + 1, i):
            if i != j and i not in [1, 2, 3] and j not in [1, 2, 3]:
                t[i][j] = t[j][i] = 1


def mark_node(n, p, node):
    n[node] = 1
    p.append(node)


def unmark_node(n, p, node):
    n[node] = 0
    p.pop()


def find_path(t, n, p, node):
    global LONGEST

    more = 0
    for i in xrange(1, MAX + 1):
        # backward may get better results
        j = MAX + 1 - i
        if n[j] == 0 and t[node][j] == 1:
            more = j
            mark_node(n, p, node)
            find_path(t, n, p, j)
            unmark_node(n, p, node)

    # no more path to go, just print
    if more == 0:
        t = len(PATH)
        if t > LONGEST:
            LONGEST = t
            print(t)  # length
            print(p)  # chain


def main():
    init(TABLES, NODES, PATH)

    start = int(sys.argv[1])
    print(start)
    find_path(TABLES, NODES, PATH, start)

if __name__ == '__main__':
    main()
