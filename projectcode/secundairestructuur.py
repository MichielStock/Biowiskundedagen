"""
Created on Wednesday 09 Janary 2018
Last update: Tuesday 05 February 2019

@author: Michiel Stock
michielfmstock@gmail.com

Basic python module for project secondary protein structure.
"""

from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import random as rd
rd.seed(1)

sequentie = P22eiwit = "MTDITANVVVSNPRPIFTESRSFKAVANGKIYIGQIDTDPVNPANQIPVYIENEDGSHVQITQPLIINAAGKIVYNGQLVKIVTVQGHSMAIYDANGSQVDYIANVLKYDPDQYSIEADKKFKYSVKLSDYPTLQDAASAAVDGLLIDRDYNFYGGETVDFGGKVLTIECKAKFIGDGNLIFTKLGKGSRIAGVFMESTTTPWVIKPWTDDNQWLTDAAAVVATLKQSKTDGYQPTVSDYVKFPGIETLLPPNAKGQNITSTLEIRECIGVEVHRASGLMAGFLFRGCHFCKMVDANNPSGGKDGIITFENLSGDWGKGNYVIGGRTSYGSVSSAQFLRNNGGFERDGGVIGFTSYRAGESGVKTWQGTVGSTTSRNYNLQFRDSVVIYPVWDGFDLGADTDMNPELDRPGDYPITQYPLHQLPLNHLIDNLLVRGALGVGFGMDGKGMYVSNITVEDCAGSGAYLLTHESVFTNIAIIDTNTKDFQANQIYISGACRVNGLRLIGIRSTDGQGLTIDAPNSTVSGITGMVDPSRINVANLAEEGLGNIRANSFGYDSAAIKLRIHKLSKTLDSGALYSHINGGAGSGSAYTQLTAISGSTPDAVSLKVNHKDCRGAEIPFVPDIASDDFIKDSSCFLPYWENNSTSLKALVKKPNGELVRLTLATL"

beta_platen = ["SRSF", "KIYIGQ", "VYIE", "HVQI", "QPLII", "IVY", "IVTVQ",
                "SMAIY", "QVDYIA", "SVK", "YPT", "VDGLLI", "TVD", "TIEC",
                "AKFI", "DGNLIFT", "RIAG", "FME", "WVI", "KTDGY", "STLEIRE",
                "EVHR", "SGLMAGFLFRG", "KMVD", "NNPSG", "IITFE", "LSGD", "YVIG",
                 "RTSY", "SAQFLRNN", "GVIG", "TSYR", "GVKT", "GTV", "NYN",
                 "QFRDSVVIY", "GFDL", "DMN", "LIDNLLVR", "LGVGFGMDGKG",
                 "YVSNITVED", "AGSGAYLLTHE", "VFTNIAIID", "QIYI", "RVNGLRL",
                 "TIDAPNSTVSGITG", "INVANL", "NIRANS", "GYDSAAIKL", "KTL",
                 "SGALYSHI", "AYTQLTAIS", "TPDAVSLKVN", "GAE", "VPD",
                 "DSSCFLPYWE", "SLKALVK", "LVRLTLA"]

# locaties beta-platen (start, stop)
regios = []
beta_masker = np.zeros(len(P22eiwit), dtype=bool)
for bp in beta_platen:
    start = P22eiwit.find(bp)
    regios.append((start, start + len(bp)))
    beta_masker[start:start+len(bp)] = True

AZ_aantal = Counter(P22eiwit)
AZ_beta_platen_aantal = Counter()
for beta_plaat in beta_platen:
    AZ_beta_platen_aantal.update(beta_plaat)

aminozuren = list(AZ_aantal.keys())

AZ_totaal = sum(AZ_aantal.values())
AZ_beta_platen_totaal = sum(AZ_beta_platen_aantal.values())

prior_beta = AZ_beta_platen_totaal / AZ_totaal

AZ_prob = {}
AZ_prob_beta = {}
AZ_prob_geen_beta = {}
AZ_odds = {}
for AZ in sorted(aminozuren):
    AZ_prob[AZ] = AZ_aantal[AZ] / AZ_totaal
    AZ_prob_beta[AZ] = AZ_beta_platen_aantal[AZ] / AZ_beta_platen_totaal
    AZ_prob_geen_beta[AZ] = (AZ_aantal[AZ] - AZ_beta_platen_aantal[AZ]) / (AZ_totaal - AZ_beta_platen_totaal)
    AZ_odds[AZ] = AZ_prob_beta[AZ] / AZ_prob[AZ]

# Genereer een random eiwit met bepaalde structuur
# AZ per regio gesampelt volgens geoberveerde distributies

p_beta = [AZ_prob_beta[az] for az in aminozuren]
p_niet_beta = [AZ_aantal[az] - AZ_beta_platen_aantal[az] for az in aminozuren]

def genereer_seq_van_distributie(n, p_vect):
    return "".join(rd.choices(aminozuren, weights=p_vect, k=n))

# geneer een eiwit volgens die distributie

if True:  # genereer nieuwe sequentie
    sequentie = ""
    regios = []
    beta_masker = []

    while len(sequentie) < 700:
        niet_beta_plaat = genereer_seq_van_distributie(rd.randint(20, 100), p_niet_beta)
        sequentie += niet_beta_plaat
        beta_plaat = genereer_seq_van_distributie(rd.randint(15, 50), p_beta)
        regios.append((len(sequentie), len(sequentie) + len(beta_plaat) - 1))
        beta_masker += [False] * len(niet_beta_plaat) + [True] * len(beta_plaat)
        sequentie += beta_plaat

def confusiematrix(y, p):
    n=len(y)
    print(
    """
                                    | Voorspeld als beta | Voorspeld als geen beta |
    --------------------------------------------------------------------------------
    regio is deel van beta-plaat    |       {tp}         |           {fn}             |
    regio geen deel van beta-plaat  |       {fp}         |           {tn}            |
    """.format(tp=sum([p[i]==True for i in range(n) if y[i]]),
            fn=sum([p[i]==False for i in range(n) if y[i]]),
            fp=sum([p[i]==True for i in range(n) if not y[i]]),
            tn=sum([p[i]==False for i in range(n) if not y[i]])
    )

    )

def glijdendvenster(sequentie, k=5):
    # FIX: kansen groter dan 1?
    # DOC
    assert k > 0  and k % 2  # lengte van het venster is oneven
    n = len(sequentie)
    w = (k - 1) // 2
    posterior_kans = np.ones(n) * prior_beta
    likelihood_beta = np.array([AZ_prob_beta[AZ] for AZ in sequentie])
    likelihood_geen_beta = np.array([AZ_prob_geen_beta[AZ] for AZ in sequentie])
    for i in range(w, n-w):
        p_seq_beta = np.prod([likelihood_beta[i-w:i+w+1]]) * prior_beta
        p_seq_geen_beta = np.prod([likelihood_geen_beta[i-w:i+w+1]]) * (1 - prior_beta)
        posterior_kans[i] = p_seq_beta / (p_seq_beta + p_seq_geen_beta)
    return posterior_kans

def plot_glijdend_venster_ax(ax, threshold=0.5, k=5):
    """
    Maak een plot van het glijdend venster.

    Parameters:
        - sequentie : eiwitsequentie
        - threshold
        - k
    """
    ax.set_ylim([1e-4, 1.2])
    ax.set_xlim([0, len(sequentie)])
    gv = glijdendvenster(sequentie, k)
    ax.plot(gv, zorder=2, color="#2a9d8f",
                            label=r'P($\beta$-plaat | regio)')
    ax.plot([0, len(sequentie)], [threshold, threshold], zorder=2, ls="--",
                    color="#e76f51", label=r'$\theta$={:.4f}'.format(threshold))
    for start, stop in regios:
        ax.fill_between(np.linspace(start, stop, 10), 2 * np.ones(10), color="#e9c46a",
                        zorder=1, alpha=0.6)
    ax.legend(loc=1)
    ax.set_xlabel(r"positie $i$")
    ax.set_title("Glijdend venster met k={}".format(k))
    confusiematrix(beta_masker, gv > threshold)

def plot_glijdend_venster(threshold, k):
    fig, ax = plt.subplots(figsize=(15, 5))
    plot_glijdend_venster_ax(ax, threshold, k)
    #return fig


if __name__ == '__main__':

    # PRINT TABEL KANSEN
    #peptide = "YSIEADKK"
    peptide = "MLIDIAR"

    print("|  AZ  | totaal aantal | aantal in $\\beta$-plaat |  aantal niet in $\\beta$-plaat | $\\mathbf{P(A_i\\mid\\beta\\text{-plaat})}$ | $\\mathbf{P(A_i\\mid\\text{geen $\\beta$-plaat})}$ |")
    print("|:---|:----|:----------|:-----|:-----|:----|")
    for AZ in sorted(aminozuren):
        odds = AZ_prob_beta[AZ] / AZ_prob[AZ]
        AZ_odds[AZ] = odds
        if True: #AZ not in peptide:
            print("| {AZ} | {n_AZ} | {n_AZ_beta} | {n_AZ_geen_beta} | {p_AZ_beta:.4f} | {p_AZ_geen_beta:.4f} |".format(
                    AZ=AZ,
                    n_AZ=AZ_aantal[AZ],
                    n_AZ_beta=AZ_beta_platen_aantal[AZ],
                    n_AZ_geen_beta=AZ_aantal[AZ] - AZ_beta_platen_aantal[AZ],
                    p_AZ_beta=AZ_prob_beta[AZ],
                    p_AZ_geen_beta=AZ_prob_geen_beta[AZ]
                    ))
        else:
            print("| {AZ} | {n_AZ} | ... | {n_AZ_beta} | ... | ... |".format(
                    AZ=AZ,
                    n_AZ=AZ_aantal[AZ],
                    n_AZ_beta=AZ_beta_platen_aantal[AZ],
                    ))
    print("| **Totaal** |  **{AZ_totaal}** | **{AZ_beta_platen_totaal}** | **{AZ_geen_beta_platen_totaal}**|**1**| **1**| ".format(
                AZ_totaal=AZ_totaal,
                AZ_beta_platen_totaal=AZ_beta_platen_totaal,
                AZ_geen_beta_platen_totaal=AZ_totaal-AZ_beta_platen_totaal
            ))
    l_beta = 1
    l_geen_beta = 1
    for AZ in peptide:
        l_beta *= AZ_prob_beta[AZ]
        l_geen_beta *= AZ_prob_geen_beta[AZ]
    kans_beta = prior_beta * l_beta / (prior_beta * l_beta + (1 - prior_beta) * l_geen_beta)
    print("Kans dat {peptide} een beta-plaat is: {kans_beta:.4f}".format(
                peptide=peptide,
                kans_beta=kans_beta
            ))

    # maak plot glijdendvenster
    fig, ax = plt.subplots(figsize=(15, 5))
    plot_glijdend_venster_ax(ax=ax)
    fig.savefig("../figuren/glijdendvenstervoorbeeld.png")
