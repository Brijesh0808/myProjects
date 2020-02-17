'''
Python code to ESTIMATE the value of mathematical pi
Method: Monte Carlo
File Name: pi_Monte_carlo.py
Author: Brijesh
Taking origin as center of the circle
'''


from random import uniform
import math

n = int(input('Enter number of itterations you want: '))

radius = 1  #units
total_drops_in_circle = 0
total_drops_in_square = 0

for i in range(n):
    x, y = uniform(-1, 1), uniform(-1, 1)       #(x,y) pt. from origin
    pt_dist_from_origin = (x*x + y*y)**0.5

    if(pt_dist_from_origin <= 1):
        total_drops_in_circle += 1
    total_drops_in_square += 1

pi = 4*(total_drops_in_circle)/(total_drops_in_square)

print('Estimated pi: ',pi)
print('Original pi : ', math.pi)
