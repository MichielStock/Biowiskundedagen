"""
Created on Sunday 27 January 2019
Last update: -

@author: Michiel Stock
michielfmstock@gmail.com

Animaties BWD SIR model.
"""

# Animaties
# ---------

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from sklearn.metrics.pairwise import pairwise_distances
from sklearn.neighbors import BallTree
import numpy as np
from random import sample

# KLEUREN
# -------

blue = blauw = '#264653'
green = groen = '#2a9d8f'
yellow = geel = '#e9c46a'
orange = oranje = '#f4a261'
red = rood = '#e76f51'
black = zwart = '#50514F'

np.random.seed(10)

n_points = 100
r_big = 3
r_small = 0.25
neighbors = 3
coordinates = []
while len(coordinates) < n_points:
    x = (np.random.rand(2) - 0.5) * r_big * 4
    r = np.sum(x**2)**0.5
    if r < r_big and r > r_small:
        coordinates.append(x.tolist())
coordinates = np.array(coordinates)
balltree = BallTree(coordinates)
d, ind = balltree.query(coordinates, neighbors+1)
A = np.zeros((n_points, n_points), dtype=bool)
for i in range(n_points):
    for j in ind[i,:]:
        A[i,j] = True
        A[j,i] = True

def draw_nodes(ax, colors):
    ax.scatter(coordinates[:,0], coordinates[:,1], color=colors, zorder=2)

def plot_sir_step(filename, t, colors):
    fig, ax = plt.subplots()
    # draw edges
    for i in range(n_points-1):
        for j in range(i+1, n_points):
            if A[i,j]:
                ax.plot(coordinates[[i,j],0], coordinates[[i,j],1], zorder=1, color=blauw,
                        lw=2, alpha=0.8)
    draw_nodes(ax, colors)
    ax.set_title("Simulatie op tijdstip {} ({} resistent) \n {} / {} geïnfecteerd".format(
            t, colors.count(groen), colors.count(red), n_points))
    ax.set_yticks([])
    ax.set_xticks([])
    ax.axis('off')
    # legende
    ax.scatter([],[], color=geel, label="vatbaar (S)")
    ax.scatter([],[], color=rood, label="geïnfecteerd (I)")
    ax.scatter([],[], color=groen, label="resistent (R)")
    ax.legend(loc=0)
    fig.savefig("figuren/SIRanimatiesplots/{}_{}.png".format(filename, t))
    fig.clf()
    """
    # plot points
    for x1, x2 in coordinates:
        ax.scatter(x1, x2, color=green, s=50, zorder=2)

    # make animation
    return anim
    """


xinit = np.zeros((n_points))
xinit[:5] = 1

x = xinit.copy()
filename = "sir_sim_no_R_"
for t in range(11):
    colors = [geel if x[i] == 0 else red for i in range(n_points)]
    plot_sir_step(filename, t, colors)
    x = A @ x

x = xinit.copy()
filename = "sir_sim_R0.2"
resistent = sample(range(5,  n_points), int(n_points * 0.2))
for t in range(11):
    colors = [geel if x[i] == 0 else red for i in range(n_points)]
    for i in resistent:
        colors[i] = groen
    plot_sir_step(filename, t, colors)
    x = (x + A @ x) > 0
    x[resistent] = 0


x = xinit.copy()
filename = "sir_sim_R0.6"
resistent = sample(range(5,  n_points), int(n_points * 0.6))
for t in range(11):
    colors = [geel if x[i] == 0 else red for i in range(n_points)]
    for i in resistent:
        colors[i] = groen
    plot_sir_step(filename, t, colors)
    x = A @ x > 0
    x[resistent] = 0

x = xinit.copy()
filename = "sir_sim_R0.8"
resistent = sample(range(5,  n_points), int(n_points * 0.8))
for t in range(11):
    colors = [geel if x[i] == 0 else red for i in range(n_points)]
    for i in resistent:
        colors[i] = groen
    plot_sir_step(filename, t, colors)
    x = A @ x > 0
    x[resistent] = 0
