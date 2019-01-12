"""
Created on Tuesday 18 December 2018
Last update: -

@author: Michiel Stock
michielfmstock@gmail.com

Code nodig voor het practicum 'ziekteverspreiding' van de Biowiskundedagen
editie 2018-2018. Maakt sterk gebruik van netwerkx.
"""

# KLEUREN
# -------

blue = blauw = '#264653'
green = groen = '#2a9d8f'
yellow = geel = '#e9c46a'
orange = oranje = '#f4a261'
red = rood= '#e76f51'
black = zwart = '#50514F'

# laadt enkele nuttige pakketten
import networkx as nx
from collections import Counter
import numpy as np
import random

# maak de figuren reproduceerbaar
seed = 2
np.random.seed(seed)
random.seed(seed)

def bereken_gradenverdeling(G, norm=True):
    """
    Bereken de gradenverdeling van een graaf G. Geeft de gradenverdeling als
    een lijst weer. Norm=True berekent de relatieve verdeling (standaard).
    """
    # tel de graden
    c = Counter(dict(G.degree()).values())
    # geef weer
    gradenverdeling = np.zeros(len(G) + 1)
    for i, d in c.items():
        gradenverdeling[i] = d
    return gradenverdeling / gradenverdeling.sum()

def geef_verbindingsmatrix(G):
    """
    Geef de verbindingsmatrix van een netwerk als een binaire Numpy matrix.
    """
    return nx.adj_matrix(G).todense()

def deax(ax):
    "Verwijder lelijke assen."
    ax.set_xticks([])
    ax.set_yticks([])

def printdegreetable(n):
    """Print de tabel voor gradenverdeling"""
    print("| $k$ | $D(k)$ |")
    print("|:--|:--|")
    for i in range(n):
        print("| ${}$ | ... |".format(i+1))

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    plt.xkcd()

    # Voorbeeld netwerk
    # -----------------

    netwerk_voorbeeld = nx.barabasi_albert_graph(n=15, m=2)
    # note: n=20, n=1 is ook leuk, geeft een boom

    posities = nx.spring_layout(netwerk_voorbeeld)
    labels = {i : str(i + 1) for i in range(len(netwerk_voorbeeld))}

    fig, ax = plt.subplots(figsize=(8, 6))

    nx.draw_networkx_nodes(netwerk_voorbeeld, posities, nodesize=1000,
                                                        node_color=geel, ax=ax)
    nx.draw_networkx_edges(netwerk_voorbeeld, posities, ax=ax, edge_color=blauw,
                                                        width=4, alpha=0.8)
    nx.draw_networkx_labels(netwerk_voorbeeld, posities, labels=labels, ax=ax,
                                                        label_color=zwart)

    deax(ax)

    fig.savefig("figuren/socialnetwerk.png")

    # Figuur gradenverdeling standaard netwerken
    # ------------------------------------------

    fig, ax = plt.subplots(figsize=(10, 8))

    netwerk_random = nx.binomial_graph(n=1000, p=0.05)
    ax.plot(bereken_gradenverdeling(netwerk_random), color=groen,
                                            label="random netwerk")

    netwerk_schaalvrij = nx.barabasi_albert_graph(n=1000, m=10)
    ax.plot(bereken_gradenverdeling(netwerk_schaalvrij), color=rood, ls=':',
                                            label="schaalvrij netwerk")

    netwerk_grid = nx.grid_2d_graph(n=50, m=20)
    ax.plot(bereken_gradenverdeling(netwerk_grid), color=oranje, ls=":",
                                            label="grid netwerk")

    ax.set_xlabel(r"Graad $k$")
    ax.set_ylabel(r"Relatief aantal knopen $D(d)$")
    ax.set_title("Gradenverdeling van drie netwerken\n met 1000 knopen")
    ax.legend(loc=0)
    ax.loglog()
    fig.tight_layout()

    fig.savefig('figuren/gradenverdelingen.png')

    # Plot voor gradenverdeling
    # -------------------------

    fig, ax = plt.subplots(figsize=(10, 8))

    ax.plot(bereken_gradenverdeling(netwerk_voorbeeld), color='w')
    ax.grid(color='g', linestyle=':', linewidth=0.25)
    ax.set_xlabel(r"Graad $k$")
    ax.set_ylabel(r"Relatief aantal knopen $D(d)$")

    fig.savefig('figuren/gradenverdelingenleeg.png')
