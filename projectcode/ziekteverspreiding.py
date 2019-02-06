"""
Created on Tuesday 18 December 2018
Last update: Saturday 19 January 2019

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
import matplotlib.pyplot as plt

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

def update_toestand(A, x, resistent=[]):
    """
    Voor een gegeven verbindingsmatrix A en een binaire toestandsvector x
    (0: vatbaar/resitent, 1: geinfecteerd) op tijdstip t, bereken de toestandsvector op
    tijdstip t+1. Optioneel kan je een lijst met indices van resistente individuen
    geven.
    """
    # update x
    x[:] = (x + A @ x) > 0
    # resitente worden niet ziek
    if resistent:
        x[resistent] = 0
    return x

def simuleer_uitbraak(n, initgeinf, netwerk, fractie_gevac, strategie):
    similatiestappen = 10
    if netwerk == "willekeurig":
        p = 4 / n
        G = nx.binomial_graph(n=n, p=p)
    elif netwerk == "schaalvrij":
        G = nx.barabasi_albert_graph(n=n, m=2)
    else:
        raise(AttributeError("Netwerk is ofwel 'willekeurig' of 'schaalvrij'"))
    A = geef_verbindingsmatrix(G)
    posities = nx.spring_layout(G)
    x = np.zeros((n, 1), dtype=int)
    x[:initgeinf] = 1  # eerste persoon is geinfecteerd
    resistent = []
    if strategie=="willekeurig":
        resistent = random.sample(range(initgeinf, n), int(n * fractie_gevac))
    elif strategie=="best connecteerd":
        if fractie_gevac > 0:
            D = -A.sum(0)
            resistent = D.argsort(1).tolist()[0][:int(n * fractie_gevac)]
            resistent = list(set(resistent) - set(range(initgeinf)))
    else:
        raise(AttributeError("strategie is ofwel 'willeurig' of 'best connecteerd'"))
    geinfecteerd = [sum(x) / n]
    for t in range(similatiestappen):
        update_toestand(A, x, resistent)
        geinfecteerd.append(sum(x) / n)
    # plot resultaat
    fig, axes = plt.subplots(ncols=2, figsize=(15, 10))
    # plot het netwerk
    knoopkleuren = [blauw] * initgeinf
    for i in range(initgeinf, n):
        if i in resistent:
            knoopkleuren.append(groen)
        elif x[i]:
            knoopkleuren.append(rood)
        else:
            knoopkleuren.append(geel)
    nx.draw_networkx_nodes(G, posities, node_size=10, alpha=0.8,
                                    node_color=knoopkleuren, ax=axes[0])
    nx.draw_networkx_edges(G, posities, ax=axes[0], edge_color=blauw,
                                                        width=0.5, alpha=0.8)
    deax(axes[0])
    axes[0].set_title("Eindtoestand van de het netwerk na {} stappen".format(similatiestappen))

    # plot nu de toestanden
    vatbaar = 1 - np.array(geinfecteerd) - fractie_gevac
    axes[1].plot(geinfecteerd, color=rood, ls="--", lw=2, label="geinfecteerd")
    axes[1].plot([0, similatiestappen], [fractie_gevac, fractie_gevac], color=groen, ls=":",
                            lw=2, label="resistent")
    axes[1].plot(vatbaar, color=geel, lw=2, label="vatbaar")
    axes[1].legend(loc=1)
    axes[1].set_xlabel(r"$t$")
    axes[1].set_ylabel(r"Fractie van de knopen")
    axes[1].set_title("Evolutie van de toestanden.")


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

def printtoestandtabel(n, t):
    """Print tabel voor toestand transities"""
    print("| knoop |" + " ".join([" $t={}$ |".format(i) for i in range(t+1)]))
    print("|" + ":--|" * (t+2))
    for knoop in range(n):
        print("| ${}$ |".format(knoop+1) + " ... |" * (t+1))
    print("| **totaal aantal geinfecteerden** |".format(knoop+1) + " ... |" * (t+1))

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    #plt.xkcd()

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
                                            label="willekeurig netwerk")

    netwerk_schaalvrij = nx.barabasi_albert_graph(n=1000, m=10)
    ax.plot(bereken_gradenverdeling(netwerk_schaalvrij), color=rood, ls=':',
                                            label="schaalvrij netwerk")
    """
    netwerk_grid = nx.grid_2d_graph(n=50, m=20)
    ax.plot(bereken_gradenverdeling(netwerk_grid), color=oranje, ls=":",
                                            label="grid netwerk")
    """
    ax.set_xlabel(r"Graad $k$")
    ax.set_ylabel(r"Relatief aantal knopen $D(d)$")
    ax.set_title("Gradenverdeling van twee netwerken\n met 1000 knopen")
    ax.legend(loc=0)
    #ax.set_xticks([1, 10, 100, 1000])
    #ax.set_yticklabels([0.001, 0.01, 0.1, 1], map(str, [0.001, 0.01, 0.1, 1]))
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
