#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#

def pythagoras_approves(sides):
    return(sum([i * i for i in sides]) == 2 * max(sides) ** 2)

def triangle_inequalty_rule_one(sides):
    # https://sciencing.com/rules-length-triangle-sides-8606207.html
    return(sum(sides) < 2 * max(sides))

def triangle(a, b, c):
    # DELETE 'PASS' AND WRITE THIS CODE
    sides = [a, b, c]
    if 0 in sides:
        raise TriangleError('Zero length sides prohibited.')
    if min(sides) < 0:
        raise TriangleError('Negative length sides prohibited.')
    if (triangle_inequalty_rule_one(sides)):
        raise TriangleError('The sum of the two shorter sides must be exceed the longer.')
    return ['point', 'equilateral', 'isosceles', 'scalene'][len(set(sides))]


# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
