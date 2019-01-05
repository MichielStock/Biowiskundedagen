
# Eiwitten beter begrijpen met kansberekening

- [ ] ==abstract==

[toc]

## Een beetje achtergrond

### De wereld van eiwitten en hun opbouw

Eiwitten vormen één van de meest belangrijke klassen van biologische moleculen. Waar DNA een grotendeels passieve drager is van informatie, vervullen eiwitten vaak een meer actieve rol. Zo zijn eiwitten essentieel voor zowat alle biologische processen: ze staan in voor het verteren van voedsel, zorgen voor detoxificatie, geven informatie door, maken beweging mogelijk en nog veel meer. Ze vormen een fundamenteel onderdeel van elk levend organisme.

De opbouw van een eiwit is relatief simpel. Net zoals DNA is een eiwit een *polymeer*: een lange streng van meer eenvoudige moleculen. Voor de meeste organismen bestaan eiwitten uit een specifieke opeenvolging van 20 mogelijke *aminozuren*, elk voorgesteld door een hoofdletter. Deze aminozuren verschillen in hun grootte, lading en flexibiliteit. De opvolging van deze aminozuren wordt ook wel de *primaire structuur* van een eiwit genoemd. Deze primaire structuur bepaalt hoe het eiwit zich verder zal opvouwen en legt de biologische functie van een eiwit vast.

Uit de primaire structuur van eiwitten volgt de *secundaire structuur*. Deze structuren onstaan door waterstofbruggen (niet-covente bindingen tussen vrije waterstoffen en hydroxylgroepen) tussen naburige aminozuren. De belangrijkste secundaire structuren zijn *$\alpha$-helices* en $*\beta$-platen* (Engels: $\beta$-sheets). Gegeven dat deze secundaire structuur enkel door de primaire structuur bepaald wordt, kunnen we wiskunde gebruiken om de secundaire structuur te voorspellen[^structuur].

[^structuur]: Naast de primaire en secundaire structuur hebben eiwitten doorgaans ook en *tertiaire* en *quaternaire* structuur. De tertiaire structuur is de globale opvouwing van het eiwit en is veel (veeeeeeeeel) moeilijker om computationeel te bepalen. De quaternaire structuur omvat hoe verschillende eiwitten samen een groter complex vormen.

![(boven) Eiwitsequenties vormen secundaire structuren via niet-covalente waterstofbindingen. (onder) Een eiwit is slechts een aaneenschakeling van aminozuren die zich zelfstandig opvouwen tot een drie-dimensionale conformatie.](../figuren/sec_struct.png)

### Stoute bacteriën en goede virussen

Zelfs de allerkleinste biologische entiteiten, de virussen, gebruiken eiwitten voor infectie en aldus om zich te kunnen repliceren. Een zeer interessante groep virussen zijn de bacteriofagen of kortweg fagen. Dit zijn virussen die bacteriën infecteren en aldus ook kunnen afdoden. Bacteriën, en dus ook fagen, komen overvloedig voor in ons lichaam. Vele bacteriën zijn goedaardig, en helpen ons lichaam optimaal functioneren. Soms echter dringen pathogene bacteriën ons lichaam binnen en maken ze ons ziek. *Salmonella enterica* is zo’n bacterie. *Salmonella* dringt ons lichaam binnen via besmet voedsel: de bacterie kan overleven op onvoldoende verhitte eieren en vlees, alsook op rauwe groenten en fruit. Eens de bacterie zich in onze darmen bevindt kan ze ons ernstig ziek maken.

- [ ] figuur van Salmonella en haar faag

Een bijkomend probleem is dat *Salmonella* en andere bacteriën ook steeds meer resistent worden tegen antibiotica. Gelukkig kunnen we ook fagen inzetten om bacteriën te bestrijden! Cruciaal voor een faag bij het infecteren van zijn bacteriële gastheer zijn specifieke eiwitten die componenten van de *Salmonellabacterie* herkennen. Verschillende *Salmonella* fagen kunnen verschillende componenten van de bacterie herkennen door variaties in die specifieke eiwitten. Deze eiwitten hebben daarnaast ook wel vaak een geconserveerd eiwitdomein: een ß-helicaal domein. Dit domein vormt als het ware een *moleculaire boor* die de celwand van de bacterie kan doorboren, wat nodig is om de infectie te starten. Door deze eiwitten beter te begrijpen kunnen we ze daarna ook beter inzetten tegen gevaarlijke bacteriën.

Een voorbeeld van zo'n eiwit is het staarteiwit van Salmonella faag P22: [P12528](https://www.uniprot.org/uniprot/P12528). Tussen aminozuur 140 en 543 bevindt zich een groot ß-helicaal domein (bestaande uit parallele ß-platen) dat een puntig einde heeft rond aminozuur 113. De aanwezigheid van die ß-platen is aldus belangrijk voor de specifieke functie van het eiwit. Deze secundaire structuren (de ß-platen) kunnen we bestuderen via wiskunde en computers. Dit onderzoeksdomein noemen we *bio-informatica*. In bio-informatica wordt wiskunde gecombineerd met computerkracht om interessante biologische fenomenen te bestuderen en biologische problemen op te lossen.

![Het P12528 eiwit, ook wel Salmonella faag P22 *tail spike* eiwit genoemd. Dit eiwit bestaat uit een uitzonderlijk groot aantal $\beta$-platen die samen een complexe boorkop vormen. Regenboogkleuring in volgorde van de sequentie.](../figuren/P12528.png)

In dit project zetten we de computer aan het werk om eiwitten te bestuderen. Zo'n eiwitten bestuderen wetenschappers vaak op basis van de aminozuursequentie van het eiwit. Door specifieke instructies te geven aan de computer kunnen we voorspellingen maken voor ß-platen om zo de ß-helicae domeinen te vinden! In dit project zullen we de computer leren om dergelijke voorspellingen te maken. Hieronder bekijken we eerst welke wiskunde je daar net voor nodig hebt.

## Rekenen met kansen en de regel van Bayes

### Kansrekening in een notendop

Kansrekening of probabiliteitstheorie is de tak van de wiskunde die zich bezig houdt met *kansen*. Met kansen kom je dagelijks in contact, denk maar aan gezelschapsspellen waarbij je moet dobbelen of Frank Deboosere die aangeeft dat er een 60%[^procent] kans op neerslag is voor morgen. Er zijn nog vele andere voorbeelden, en net omdat kansberekenen zo belangrijk is in het dagelijkse leven, is het interessant om dit te bestuderen.

[^procent]: Vergeet niet bij het rekenen dat 60% = 0.60.

Er zijn enkele fundamentele regels die steeds opgaan in het berekenen van kansen. De figuur eronder stelt deze kansen visueel voor:

1. De kans van een gebeurtenis is een positief getal of 0[^positievekansen].
2. De totale kans dat er *een* gebeurtenis plaatsvindt is 1 (honderd procent)[^normaliserenkans].
3. (**somregel**) De kans dat er een van twee elkaar uitsluitendende gebeurtenissen plaatsvindt is de som van de kansen van die gebeurtenissen[^uitsluitendekansen].
4. (**productregel**) Zijn twee gebeurtenissen echter *onafhankelijk* van elkaar dan is de kans dat beide gebeurtenissen samen plaatsvinden het product van die kansen[^onafhkansen].
5. Er bestaan *conditionele* kansen, dit is de kans dat een gebeurtenis $A$ plaatsvindt gegeven een gebeurtenis $B$. De conditionele kans[^condkansen] wordt berekend als: $$P(A\mid B) = \frac{P(A \text{ en } B)}{P(B)}\,.$$
7. Met de *regel van Bayes* kunnen we via de informatie van een gebeurtenis kansen berekenen voor een andere gebeurtenis. De formule wordt hieronder gegeven voor gebeurtenissen A en B: $$
P(A\mid B) = \frac{P(B \mid A) P(A)}{P(B)}\,.
$$

[^positievekansen]: Bijvoorbeeld, de kans op een 6 gooien met zesogige dobbelsteen is 1/6.
[^normaliserenkans]: De som van de kansen van alle mogelijke uitkomsten van een worp van een dobbelsteen is 1/6+1/6+...+1/6=1.
[^uitsluitendekansen]: Bijvoorbeeld, met een dobbelsteen gooien kan je nooit én een even getal gooien (kans van 3/6=1/2) én een drie gooien (kans van 1/6). De kans op één van beide gebeurtenissen is 3/6+1/6=4/6=2/3.
[^onafhkansen]: Bijvoorbeeld, de kans dat je bij twee opeenvolgende worpen van een dobbelsteen twee keer een zes gooit is $1/6\cdot1/6=1/36$.
[^condkansen]: Bijvoorbeeld, de kans dat we met een dobbelsteen een zes gooien gegeven dat het een even getal was is $(1/6)/(1/2)=1/3$.

![Voorstelling van de basisregels kans kansrekening. Kansen voor beurtenissen worden voorsteld door niet-negatieve waarden die samen to 1 sommeren. Onderaan een illustratie van de rekenregels voor kansen.](../figuren/probabiliteit.png)

> **Oefening 1:** Je wordt op een nacht rillend van de koorts wakker. Je geeft over en hebt overal jeuk. Er zijn twee ziekten met deze symptomen: blauwkoorts en groenzucht. De ene ziekte komt vaker voor dan de andere: wie ziek is heeft in 75% van de gevallen last van blauwkoorts, terwijl groenzucht slechts in 25% van de gevallen voorkomt. Zoals de naam doet vermoeden, hebben deze ziekten nog een ander symptoom van chromatische aard. Mensen met blauwkoorts krijgen doorgaans een blauw gezicht en deze met groenzucht een groen gezicht. **In 10% van de gevallen is het echter andersom!** Je spoedt je naar de spiegel en iemand met een groen gezicht staart terug. Welke ziekte heb je? Bekijk onderstaande figuur en vul de ontbrekende kansen in de tabel verder aan.

- [ ] pas tekening en oefening aan!

![Twintig individuen met blauwkoorts en groenzucht. Sommigen hebben een blauwe gezichtskleur, anderen een groene.](https://i.imgur.com/zj4Tdhc.png)


$$
P(\text{blauwkoorts}) = \ldots \quad\quad P(\text{groenzucht}) = \ldots
$$

<br>

  | ziekte     | kans blauw gezicht   | kans groen gezicht |
| :------------- | :------------- | :-|
| blauwkoorts      |   ...    | ... |
| groenzucht   |  ... | ... |

<br>

$$
P(\text{blauw gezicht}) = \ldots \quad\quad P(\text{groen gezicht}) = \ldots
$$

$$
P(\text{blauwkoorts} \mid \text{groen gezicht}) = \ldots\quad\quad P(\text{groenzucht} \mid \text{groen gezicht}) = \ldots
$$

### Naïeve Bayes

- [ ] TODO: knip logaritmes weg
- [ ] Orden tabel alfabetish
- [ ] Vul tabel in.

Nu we de regel van Bayes intuïtief begrijpen, kunnen we deze toepassen voor het voorspellen van ß-platen in eiwitten. De *naïeve Bayes*-methode kan hiervoor gebruikt worden. Deze methode maakt gebruik van de regel van Bayes om voorspellingen te maken o.b.v. een gegeven input. In dit project willen we een ß-plaat voorspellen o.b.v. de eiwitsequentie (de input).

De regel van Bayes kan voor dit geval als volgt geschreven worden:

$$
P(\beta\text{-plaat}\mid \text{eiwitsequentie}) = \frac{P(\text{eiwitsequentie} \mid \beta\text{-plaat})P(\beta\text{-plaat}) }{P(\text{eiwitsequentie})}
$$

De eerste kans in de breuk kunnen we wat herschrijven als:

$$
P(\text{eiwitsequentie} \mid \beta\text{-plaat})=P(A_1A_2\ldots A_n\mid \beta\text{-plaat})\,.
$$

Hierboven schrijven we dus de eiwitsequentie gewoon als de opeenvolging van de $n$ aminozuren. Hier stelt $A_i$ de identiteit voor van het aminozuur op positie $i$. Hoe berekenen we de kans op een gegeven sequentie? Voor een stukje van een lengte $n=10$ hebben we $20^{10}= 10240000000000\approx 10^{13}$ unieke sequenties. In een probabilistisch model moeten we dus een vereenvoudiging doorvoeren!

> **Vereenvoudiging:** We gaan er van uit dat de kans dat een bepaald aminozuur op een bepaalde plaats voorkomt **onafhankelijk is van de aminozuren op elke andere plaats**[^vereenvoudiging].

[^vereenvoudiging]: Ergens huilt er een moleculair bioloog.

Deze vereenvoudiging is natuurlijk volstrekt biologisch onrealistisch! De aminozuren zijn in werkelijk juist erg afhankelijk, bijvoorbeeld omdat twee aminozuurtjes met elkaar in contact komen en een waterstofbrug vormen. Hoe fout deze vereenvoudig ook is, ze is echter wel nuttig! Het laat ons toe om de kansen voor een $\beta$-plaat redelijk goed te benaderen! In formulevorm is deze veronderstelling voor ons probleem[^conditioneelvereenvoudiging][^productnotatie]:

[^conditioneelvereenvoudiging]: On helemaal precies te zijn, de veronderstelling zegt dat $P(A_1A_2\ldots A_n)\approx P(A_1)P(A_2)\ldots P(A_n)$, terwijl wij nu eerst de identiteit $P(A_1A_2\ldots A_n\mid \beta\text{-plaat})\approx P(A_1\mid \beta\text{-plaat})P(A_2\mid \beta\text{-plaat})\ldots P(A_n\mid \beta\text{-plaat})$ gebruiken. De eerste veronderstelling zegt dat de aminozuren onafhankelijk zijn, terwijl de tweede identiteit zegt dat ze onafhankelijk zijn binnen een $\beta$-plaat. Deze twee uitspraken zijn **niet** inwisselbaar!

[^productnotatie]: Hier maken we gebruik van de notatie voor een product:$$\prod_{i=1}^n x_i=x_1 x_2\ldots x_n\,,$$ bijvoorbeeld $\prod_{i=2}^4 i = 2\times 3\times 4=24$.

$$
P(\text{eiwitsequentie} \mid \beta\text{-plaat})\approx P(A_1\mid\beta\text{-plaat})P(A_2\mid\beta\text{-plaat})\ldots P(A_n\mid\beta\text{-plaat})
$$
$$
= \prod_{i=1}^n P(A_i\mid\beta\text{-plaat})
$$

We kunnen de berekeningen vereenvoudigen door de logaritme van de kansen te nemen. Dit verandert het product in een som[^logaritme]:

[^logaritme]: De logaritme met basis 10 wordt gedefineerd als $$\log_{10}x=y \Longleftrightarrow 10^y=x\,.$$ Herinner je dat voor positieve getallen $a$ en $b$ geldt dat $\log(ab)=\log(a) + \log(b)$ en $\log(a/b)=\log(a) - \log(b)$. Wetenschappers gebruiken logaritmes vaak om vermenigvuldigingen in sommen om te zetten. De logaritmische transformatie heeft ook als voordeel dat de heel kleine getallen die je bekomt door de vermenigvuldiging in negatieve waarden omgezet worden.

$$
\log_{10}(P(\text{eiwitsequentie} \mid \beta\text{-plaat})) \approx \sum_{i=1}^n \log_{10} (P(A_i\mid\beta\text{-plaat}))
$$

en

$$
\log_{10}(P(\text{eiwitsequentie})) \approx \sum_{i=1}^n \log_{10} (P(A_i))\,.
$$


Uiteindelijk kunnen we de regel van Bayes dus als volgt noteren om ß-platen te voorspellen:

$$
\log_{10}(P( \beta\text{-plaat} \mid \text{eiwitsequentie} )) \approx \sum_{i=1}^n \log_{10} (P(A_i\mid\beta\text{-plaat})) + \log_{10}(P(\beta\text{-plaat}))- \sum_{i=1}^n \log_{10} (P(A_i))\,.
$$

Laat ons dit nog even herschrijven als

$$
\log_{10}(P( \beta\text{-plaat} \mid \text{eiwitsequentie} )) \approx \log_{10}(P(\beta\text{-plaat})) +\sum_{i=1}^n \log_{10}\left(\frac{P(A_i\mid \beta\text{-plaat})}{P(A_i)}\right)\,.
$$

We kunnen de logaritme van de kans op een $\beta$-plaat dus schrijven als een som van termen voor het aminozuur op iedere positie $i$, namelijk de logaritme van de kans dat het aminozuur voorkomt in een $\beta$-plaat gedeeld door de kans dat dat aminozuur überhaubt voorkomt! Deze term wordt de **log-odds** genoemd[^odds].

[^odds]: Sorry, er is geen Nederlandse term voor...

### Een eenvoudig voorbeeld met de hand uitwerken

Nu kunnen we de bovenstaande formule gebruiken om voorspellingen te maken voor eiwitten. Vooraleer we deze formule doorgeven aan de computer zullen we ze eerst zelf op papier eens toepassen. Hiervoor hebben we aldus volgende kansen nodig (rechterlid van de bovenstaande formule):

- $P(A_i)$: de probabiliteiten van het voorkomen van elk aminozuur $A_i$.
- $P(\beta\text{-plaat})$: de kans om een $\beta$-plaat waar te nemen.
- $P(A_i\mid\beta\text{-plaat})$: de kans om een bepaald aminozuur waar te nemen, gegeven dat de sequentie een $\beta$-plaat is.


> **Oefening 2:** Onderstaande tabel bevat empirisch bepaalde aminozuur (AZ) aantallen uit staart eiwitten van fagen die we zullen gebruiken om voorspellingen te maken. Op basis van de aantallen en het totaal aantal AZ kan je de ontbrekende kansen in de tabel berekenen, alsook de kans op een $\beta$-plaat. Deze kansen heb je nodig om de formule uit te werken.


|  AZ  | totaal aantal | $\mathbf{P(A_i)}$ | aantal in $\beta$-plaat | $\mathbf{P(A_i\mid\beta\text{-plaat})}$ | $\mathbf{\log_{10}\left(\frac{P(A_i\mid \beta\text{-plaat})}{P(A_i)}\right)}$ |
|:---|:----|:----------|:-----|:-----|:----|
| W  |  64 | ... | 21 | ... | ... |
| C  |  56 | ... | 23 | ...| ... |
| H  |  95 | ... | 39 | ...| ... |
| M  |  87 | ... | 34 | ...| ... |
| Y  |  177 | ... | 92 | ...| ... |
| F  |  166 | ... | 73 | ...| ... |
| Q  |  154 | ... | 35 | ...| ... |
| N  |  318 | ... | 91 | ...| ... |
| P  |  188 | ... | 27 | ...| ... |
| T  |  357 | ... | 133 | ...| ... |
| D  |  309 | ... | 77 | ...| ... |
| R  |  233 | ... | 87 | ...| ... |
| K  |  215 | ... | 54 | ...| ... |
| I  |  327 | ... | 158 | ...| ... |
| S  |  427 | ... | 122 | ...| ... |
| E  |  252 | ... | 79 | ...| ... |
| V  |  369 | ... | 182 | ...| ... |
| G  |  506 | ... | 174 | ...| ... |
| A  |  389 | ... | 104 | ...| ... |
| L  |  323 | ... | 135 | ...| ... |
| **Totaal** |  **5012** | - | **1740** | -|-

<br>

$$
P(\beta\text{-plaat}) = \ldots
$$

> **Oefening 3:** Volgende korte sequentie is een klein deeltje van het P22 staarteiwit: 'YSIEADKK'. Experimenteel werd reeds bepaald dat dit geen $\beta$-plaat is, maar een $\alpha$-helix. Bereken nu via de laatst geziene formule de kans dat die sequentie een $\beta$-plaat bevat (deze kans zou klein moeten zijn). Maak gebruik van de tabel met probabiliteiten die je net hebt ingevuld.

|$i$| $A_i$ | $\log_{10}\left(\frac{P(A_i\mid \beta\text{-plaat})}{P(A_i)}\right)$ |
|:-|:--|:---|
|1|...|...|
|2|...|...|
|3|...|...|
|4|...|...|
|5|...|...|
|6|...|...|
|7|...|...|
|8|...|...|

$$
\log_{10}(P(\beta\text{-plaat}\mid\text{eiwitsequentie}))\approx \ldots
$$
dus:
$$
P(\beta\text{-plaat}\mid\text{eiwitsequentie}) \approx\ldots
$$

## Naïeve Bayes op de computer

### Glijdende vensters en drempelwaarden

- [ ] figuur glijdend venster
- [ ] controleer logica

In het computerdeel van dit practicum gaan we nu de naïeve Bayes methode toepassen op het volledige P22 eiwit dat we eerder besproken hebben. Het doel is om te ontdekken waar de $\beta$-platen zich in het eiwit bevinden. We zullen $\beta$-platen voorspellen met behulp van de naïeve Bayes methode en de voorspellingen (i.e. de kansen) dan voorstellen via een grafiek. Hiervoor bewegen we aminozuur voor aminozuur over het eiwit via een *glijdend venster* van lengte $k$. In dit glijdend venster kijken we naar de aminozuren op elke positie van $i$ tot $i+k$ en tellen alle odds op voor elk aminzozuur. We noteren dit als

$$
s^k_i = \sum_{j=i}^{i+k}\log_{10}\left(\frac{P(A_i\mid\beta\text{-plaat})}{P(A_i)}\right)\,.
$$

In elke stap (voor elk glijdend venster) maken we een voorspelling die we later visueel kunnen voorstellen in een plot.

Daarenboven kunnen we onze voorspellingen nog vereenvoudigen. De kans op een bepaalde eiwitsequentie $P(\text{eiwitsequentie})$ is onafhankelijk van de kans op een $\beta$-plaat $P(\beta\text{-plaat})$. Hun quotiënt vormt een constante term die we hier kunnen wegdelen uit de regel van Bayes. Hierdoor kunnen we stellen dat een sequentie voorspeld wordt als een $\beta$-plaat als:

$$
\log_{10}(P(\text{eiwitsequentie}\mid\beta\text{-plaat})) > θ
$$

of, equivalent, als

$$
P(\text{eiwitsequentie}\mid\beta\text{-plaat}) > 10^θ
$$

Hier is $\theta$ een zorgvuldig gekozen *drempelwaarde* (Engels: threshold). De keuze van θ heeft gevolgen voor de correctheid van onze voorspellingen:
- als we θ te hoog kiezen is onze drempelwaarde te streng en zullen we dus bepaalde regio's niet als $\beta$-platen voorspellen terwijl dit eigenlijk wel $\beta$-platen zijn.
- als we θ te laag kiezen zijn we niet streng genoeg. We zullen dus regio's voorspellen als $\beta$-plaat dat eigenlijk geen $\beta$-plaat zijn.

Je kan dus inzien dat we de waarde van θ net goed willen kiezen zodat we het aantal foute voorspellingen tot een minimum beperken. Dit beperken van foute voorspellingen is altijd gewenst bij het gebruik van wiskundige modellen, en om deze fouten te bestuderen doen we aan *modelevaluatie*.

### Modelevaluatie: op welke manier is je model fout?

Wiskundige modellen maken zelden perfecte voorspellingen. Toch is het in de praktijk belangrijk dat modellen zeer accurate voorspellingen maken. Als bijvoorbeeld een zelfrijdende auto een foute voorspelling maakt over waar hij moet rijden kan dat mogelijks fataal zijn voor personen in de wagen en/of in de omgeving. Wanneer een wiskundig model voorspelt dat jij een kankergezwel hebt terwijl dat eigenlijk niet zo is krijg je onnodig dure chemotherapie (die vaak ook slechte bijwerkingen heeft). Er zijn natuurlijk ook minder ernstige voorbeelden: wanneer het algoritme van Netflix je weer een serie aanraadt die je niet goed vindt, ga je naar die serie simpelweg niet beginnen kijken. Maar uiteraard wil ook Netflix zijn klanten de meest relevante films en series aanraden, en dat doen ze door continu voorspellingen te maken o.b.v. de series en films die jij al bekeken hebt en de grote hoeveelheid data die ze over hun andere klanten hebben.

Om inzicht te krijgen in hoe goed of hoe slecht een model voorspellingen maakt, zullen we het model evalueren: we bepalen hoe goed het model werkt op nieuwe data. Bij het voorspellen van secundaire structuren kan ons model slechts twee soorten voorspellingen maken: ofwel is de beschouwde regio onderdeel van een $\beta$-plaat ofwel is die dat niet. Het eerste noemen we een *positieve voorspelling*, het tweede een *negatieve voorspelling*. Deze terminologie is afkomstig uit de geneeskunde: een diagnostische test is positief als de persoon ziek is, en negatief als de persoon gezond is. In onze context hebben we echter geen voorkeur voor een positieve of negatieve voorspelling, we willen enkel correcte voorspellingen! Ons model kan twee soorten foute voorspellingen maken:

- Er werd foutief voorspeld dat een regio deel uit maakt van een $\beta$-plaat. Dit heet een **vals positieve** voorspelling (Engels: *false positive*).
- Een regio werd voorspeld als deel van een $\beta$-plaat terwijl dit niet zo is. Dit is een **vals negatieve** voorspelling (Engels: *false negative*).

De correcte en foute voorspellingen kunnen we eenvoudig voorstellen in een compacte tabel:

|                                  | **Voorspeld als $\beta$-plaat** | **Voorspeld als geen $\beta$-plaat** |
|:-------------------------------- |:------------------------- |:------------------------------ |
| **Regio is deel van $\beta$-plaat**      | echt positief             | vals negatief                  |
| **Regio is geen deel van $\beta$-plaat** | vals positief             | echt negatief                  |

<br>

Beide foute voorspellingen zijn nauw verbonden met de keuze van de drempelwaarde θ, alsook de grootte van het glijdend venster. In een laatste stap zullen we daarom de drempelwaarde θ en de grootte van het glijdend venster manueel aanpassen en het effect bestuderen op het aantal foute voorspellingen. Op die manier kunnen we θ en de grootte van het venster optimaal kiezen, om de foute voorspellingen tot een minimum te beperken.

### Stappenplan

Concreet zullen we de computer dus instructeren om het volgende te doen:
1. Startend bij het begin van een eiwitsequentie maakt de computer een eerste voorspelling voor het stukje van de sequentie dat zich in het glijdend venster bevindt. Dit doet hij door Naïeve Bayes toe te passen en het stukje sequentie als ß-plaat te voorspellen wanneer de berekende kans groter is dan de vooropgestelde drempelwaarde θ.
2. Daarna schuift de computer het glijdend venster één aminozuur op in de sequentie en maakt een nieuwe voorspelling voor dit glijdend venster. Dit proces herhaalt de computer tot het einde van de eiwitsequentie bereikt is.
3. Voor elk glijdend venster slaat de computer de voorspelling op, zodat die later visueel voorgesteld kan worden.
4. We laten de computer de voorspellingen vergelijken met de werkelijke secundaire structuren, zodat we het model kunnen evalueren o.b.v. vals positieven en vals negatieven.
5. Als laatste stap veranderen we manueel de drempelwaarde θ en de grootte van het glijdend venster, om op die manier te proberen de vals positieven en vals negatieven tot een minimum te houden.


- [ ] *voeg exacte locatie toe waar ze de notebook kunnen vinden*

## En verder...

De concepten die je in deze praktische sessie geleerd hebt zijn eenvoudig en kunnen zeer nuttig zijn in de praktijk, maar er bestaan ook veel complexere methoden om eiwitten te bestuderen. Daarenboven staat onderzoek in de bio-informatica nooit stil en zijn er zelfs grote bedrijven in geïnteresseerd, net omdat computers ons veel kunnen bijleren over biologie. Een zeer recent voorbeeld is Deepmind, een bedrijf dat onder Google werkt. Recent werk van hen gebruikt complexe artificiële intelligentie om de tertiaire structuur van een eiwit accuraat te voorspellen. Hun ontwikkelde methode [AlphaFold](https://deepmind.com/blog/alphafold/) is de eerste in zijn soort, maar zal waarschijnlijk niet de laatste zijn. Ook deze complexe methoden zijn gebasseerd op wiskundige concepten, en het is net daarom dat bio-informatica zo krachtig kan zijn. Als je dus slechts een ding onthoudt van deze praktische sessie moet het wel het volgende zijn: wiskunde zit écht overal.
