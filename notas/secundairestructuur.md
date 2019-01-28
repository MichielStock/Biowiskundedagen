
# Eiwitten beter begrijpen met kansrekening

In dit project zullen we gebruik maken van kansrekening om de secundaire structuur ($\beta$-platen) van een eiwit te voorspellen. We overlopen eerst de basisregels van kansrekening en dan zullen we de kansformules vereenvoudigen  om eenvoudiger te kunnen rekenen. Zo bekomen we een data-gedreven model om voor een aminozuur de kans te berekenen of dit in een $\beta$-plaat voorkomt of niet. Dit proces zullen we toepassen over volledige eiwitten via de glijdend venster methode. Ten slotte hebben we het kort even over modelevaluatie: hoe betrouwbaar is zo'n model?

## Een beetje achtergrond

### De wereld van eiwitten en hun opbouw

Eiwitten vormen één van de meest belangrijke klassen van biologische moleculen. Eiwitten vervullen actieve rollen en blijken essentieel te zijn voor zowat alle biologische processen in een levend organisme: ze staan in voor het verteren van voedsel, zorgen voor ontgifting, geven informatie door, maken beweging mogelijk en nog veel meer. Zo vormen ze een fundamenteel onderdeel van elk biologisch wezen.

De opbouw van een eiwit is relatief simpel. Net zoals DNA is een eiwit een *polymeer*: een lange streng van meer eenvoudige moleculen. Deze eenvoudige moleculen worden *aminozuren* (AZ) genoemd, waarvan er in de natuur 20 verschillenden voorkomen, elk voorgesteld door een hoofdletter. Een specifieke opeenvolging van dergelijke aminozuren wordt de *primaire structuur* van een eiwit genoemd. Deze primaire structuur bepaalt hoe een eiwit zich verder zal opvouwen (in een functionele 3D-structuur) en legt de biologische functie van een eiwit vast.

Uit de primaire structuur van eiwitten volgt de *secundaire structuur*. Deze structuren onstaan door waterstofbruggen (niet-covalente bindingen tussen vrije waterstoffen en hydroxylgroepen) tussen naburige aminozuren (zie Figuur 1). De belangrijkste secundaire structuren zijn *$\alpha$-helices* en *$\beta$-platen* (Engels: $\beta$-sheets). Gegeven dat deze secundaire structuur enkel door de primaire structuur bepaald wordt, kunnen we wiskunde gebruiken om de secundaire structuur te voorspellen[^structuur].

[^structuur]: Naast de primaire en secundaire structuur hebben eiwitten doorgaans ook en *tertiaire* en *quaternaire* structuur. De tertiaire structuur is de globale opvouwing van het eiwit en is veel (veeeeeeeeel) moeilijker om computationeel te bepalen. De quaternaire structuur omvat hoe verschillende eiwitten samen een groter complex vormen.

![(boven) Eiwitsequenties vormen secundaire structuren via niet-covalente waterstofbindingen. (onder) Een eiwit is slechts een aaneenschakeling van aminozuren die zich zelfstandig opvouwen tot een driedimensionale structuur.](../figuren/sec_struct.png)

### Slechte bacteriën en goede virussen

Zelfs de allerkleinste biologische entiteiten, de virussen, gebruiken eiwitten voor infectie, wat nodig is voor hun vermenigvuldiging. Een zeer interessante groep virussen zijn de bacteriofagen of kortweg fagen. Dit zijn virussen die bacteriën infecteren en ook kunnen afdoden. Bacteriën, en dus ook fagen, komen overvloedig voor in ons lichaam. Vele bacteriën zijn goedaardig en helpen ons lichaam optimaal functioneren. Soms dringen echter pathogene bacteriën ons lichaam binnen en maken ze ons ziek. *Salmonella enterica* is zo’n bacterie (Figuur 2). *Salmonella* dringt ons lichaam binnen via besmet voedsel: de bacterie kan overleven op onvoldoende verhitte eieren en vlees, alsook op rauwe groenten en fruit. Eens de bacterie zich in onze darmen bevindt, kan ze ons ernstig ziek maken.

![(links) Microscopische figuur van de *Salmonellabacterie*. (rechts) Figuur van P22 fagen die *Salmonella* kunnen infecteren.](../figuren/salmonellafaag.png)

Een bijkomend probleem is dat *Salmonella* en andere bacteriën steeds meer resistent worden tegen antibiotica. Gelukkig kunnen we ook fagen inzetten om bacteriën te bestrijden! Cruciaal voor een faag bij het infecteren van zijn bacteriële gastheer zijn specifieke faageiwitten die componenten van de salmonellabacterie herkennen. Deze faageiwitten verschillen vaak tussen verschillende salmonellafagen. Hierdoor kunnen verschillende fagen andere varianten van de salmonellabacterie herkennen. Anderzijds komt er tussen verschillende salmonellafagen ook vaak een geconserveerd eiwitdomein voor. Dit is een stukje van het eiwit dat wel hetzelfde is tussen de verschillende salmonellafagen. Bij salmonellafagen is dit een zogenaamd $\beta$-helicaal domein. Dit domein vormt als het ware een *moleculaire boor* die de celwand van de bacterie kan doorboren, wat nodig is om de infectie te starten. Door zo'n faageiwitten beter te begrijpen kunnen we ze daarna ook beter inzetten tegen gevaarlijke bacteriën.

Een voorbeeld van zo'n faageiwit is het staarteiwit van salmonellafaag P22: [*P12528*](https://www.uniprot.org/uniprot/P12528) (zie rechtse deel van Figuur 2). Tussen aminozuur 140 en 543 bevindt zich een groot $\beta$-helicaal domein (bestaande uit parallele $\beta$-platen) dat een puntig einde heeft rond aminozuur 113 (Figuur 3). De aanwezigheid van die $\beta$-platen is belangrijk voor de specifieke functie van het eiwit. Deze secundaire structuren (de $\beta$-platen) kunnen we bestuderen via wiskunde en computers. Dit onderzoeksdomein noemen we *bio-informatica*. In bio-informatica wordt wiskunde gecombineerd met computerkracht om interessante biologische fenomenen te bestuderen en biologische problemen op te lossen.

![Het P12528 eiwit, ook wel salmonellafaag P22 *tail spike* eiwit genoemd. Dit eiwit bestaat uit een uitzonderlijk groot aantal $\beta$-platen die samen een complexe boorkop vormen. Regenboogkleuring in volgorde van de sequentie.](../figuren/P12528.png)

In dit project zetten we de computer aan het werk om eiwitten te bestuderen. Zo'n eiwitten bestuderen wetenschappers vaak op basis van de aminozuursequentie van het eiwit. Door specifieke instructies te geven aan de computer kunnen we voorspellingen maken voor $\beta$-platen om zo de $\beta$-helicale domeinen te vinden! In dit project zullen we de computer leren om dergelijke voorspellingen te maken. Hieronder bekijken we eerst welke wiskunde je daar net voor nodig hebt.

## Rekenen met kansen en de regel van Bayes

### Kansrekening in een notendop

Kansrekening of probabiliteitstheorie is de tak van de wiskunde die zich bezig houdt met *kansen*. Met kansen kom je dagelijks in contact, denk maar aan gezelschapsspellen waarbij je moet dobbelen of Frank Deboosere die aangeeft dat er 60%[^procent] kans op neerslag is voor morgen. Er zijn nog vele andere voorbeelden, en net omdat kansrekenen zo belangrijk is in het dagelijkse leven, is het interessant om dit te bestuderen.

[^procent]: Vergeet niet bij het rekenen dat 60% = 0.60.

Er zijn enkele fundamentele regels die steeds gelden bij het berekenen van kansen. Figuur 4 stelt deze regels visueel voor:

1. De kans van een gebeurtenis is een niet-negatief getal  (nul inclusief) [^positievekansen].
2. De totale kans dat er *een* gebeurtenis plaatsvindt is 1 (honderd procent)[^normaliserenkans].
3. (**somregel**) De kans dat één van twee elkaar uitsluitendende gebeurtenissen plaatsvindt is de som van de kansen van die gebeurtenissen[^uitsluitendekansen].
4. (**productregel**) Bij twee *onafhankelijke* gebeurtenissen is de kans dat beide gebeurtenissen samen plaatsvinden het product van die kansen[^onafhkansen].
5. Er bestaan *conditionele* kansen, dit is de kans dat een gebeurtenis $A$ plaatsvindt gegeven een gebeurtenis $B$. De conditionele kans[^condkansen] wordt gedefinieerd als: $$P(A\mid B) = \frac{P(A \text{ en } B)}{P(B)}\,.$$
6. (**wet van totale probabiliteit**) Er geldt $$P(B)=P(B\mid A)P(A) + P(B|\text{niet }A)P(\text{niet }A)\,,$$ de kans op gebeurtenis $B$ kan dus berkend worden aan de hand van de kansen dat gebeurtenis $A$ al dan niet plaatsvindt[^wettotprob].
7. Met de *regel van Bayes* kunnen we via de kansen van een gebeurtenis A de kansen berekenen voor een andere gebeurtenis B. De formule wordt hieronder gegeven voor gebeurtenissen $A$ en $B$: $$
P(A\mid B) = \frac{P(B \mid A) P(A)}{P(B)} = \frac{P(B \mid A) P(A)}{P(B\mid A)P(A) + P(B|\text{niet }A)P(\text{niet }A)}\,.
$$

[^positievekansen]: Bijvoorbeeld, de kans op een 6 gooien met een zesogige dobbelsteen is 1/6.
[^normaliserenkans]: De som van de kansen van alle mogelijke uitkomsten van een worp van een dobbelsteen is 1/6+1/6+...+1/6=1.
[^uitsluitendekansen]: Bijvoorbeeld, met een dobbelsteen gooien kan je nooit én een even getal gooien (kans van 3/6=1/2) én een drie gooien (kans van 1/6). De kans op één van beide gebeurtenissen is 3/6+1/6=4/6=2/3.
[^onafhkansen]: Bijvoorbeeld, de kans dat je bij twee opeenvolgende worpen van een dobbelsteen twee keer een zes gooit is $1/6\cdot1/6=1/36$.
[^condkansen]: Bijvoorbeeld, de kans dat we met een dobbelsteen een zes gooien gegeven dat het een even getal was is $(1/6)/(1/2)=1/3$.
[^wettotprob]: Stel, je hebt twee dobbelstenen met zes zijden en één dobbelsteen met acht zijden. Als je een willekeurige dobbelsteen gooit is de kans om een zes te gooien $(1/6)(2/3)+(1/8)(1/3)=11/72$.

![Voorstelling van de basisregels van kansrekening. Kansen voor beurtenissen worden voorsteld door niet-negatieve waarden die samen tot 1 sommeren.](../figuren/probabiliteit.png)

> **Oefening 1:** Je wordt op een nacht rillend van de koorts wakker. Je moet overgeven en hebt overal jeuk. Er zijn twee ziekten met deze symptomen: blauwkoorts en groenzucht. De ene ziekte komt vaker voor dan de andere: wie ziek is heeft in 80% van de gevallen last van blauwkoorts, terwijl groenzucht slechts in 20% van de gevallen voorkomt. Zoals de naam doet vermoeden, hebben deze ziekten nog een ander, duidelijk zichtbaar symptoom. Mensen met blauwkoorts krijgen doorgaans een blauw gezicht en deze met groenzucht een groen gezicht. **In 20% van de gevallen krijgt een persoon met blauwkoorts een groen gezicht en in 30% van de gevallen krijgt iemand met groenkoorts een blauw gezicht!** Je spoedt je naar de spiegel en iemand met een groen gezicht staart terug. Welke ziekte heb je meest waarschijnlijk? Bekijk onderstaande figuur en vul de ontbrekende kansen in de tabel verder aan.

![Honderd individuen met blauwkoorts en groenzucht. Sommigen hebben een blauwe gezichtskleur, anderen een groene.](../figuren/ziektebayes.png)


$$
P(\text{blauwkoorts}) = \ldots \quad\quad P(\text{groenzucht}) = \ldots
$$

<br>

| ziekte      | kans blauw gezicht | kans groen gezicht |
|:------------|:-------------------|--------------------|
| blauwkoorts | ...                | ...                |
| groenzucht  | ...                | ...                |

<br>

$$
P(\text{blauw gezicht}) = \ldots \quad\quad P(\text{groen gezicht}) = \ldots
$$

**Hint**: de kans op een blauw gezicht splitst zich uit in het geval dat je blauwkoorts hebt en het geval dat je groenkoorts hebt.

$$
P(\text{blauwkoorts} \mid \text{groen gezicht}) = \ldots\quad\quad P(\text{groenzucht} \mid \text{groen gezicht}) = \ldots
$$

### Naive Bayes

Nu we de regel van Bayes intuïtief begrijpen, kunnen we deze toepassen voor het voorspellen van $\beta$-platen in eiwitten. De *Naive Bayes*-methode kan hiervoor gebruikt worden. Deze methode maakt gebruik van de regel van Bayes om voorspellingen te maken o.b.v. een gegeven input. In dit project willen we een $\beta$-plaat voorspellen o.b.v. de eiwitsequentie (de input).

De regel van Bayes kan voor dit geval als volgt geschreven worden:

$$
P(\beta\text{-plaat}\mid \text{eiwitsequentie}) = \frac{P(\text{eiwitsequentie} \mid \beta\text{-plaat})P(\beta\text{-plaat}) }{P(\text{eiwitsequentie})}
$$

De eerste kans in de breuk kunnen we wat herschrijven als:

$$
P(\text{eiwitsequentie} \mid \beta\text{-plaat})=P(A_1A_2\ldots A_n\mid \beta\text{-plaat})\,.
$$

Hierboven schrijven we dus de eiwitsequentie gewoon als de opeenvolging van de $n$ aminozuren. Hier stelt $A_i$ de identiteit voor van het aminozuur op positie $i$. Hoe berekenen we de kans op een gegeven sequentie? Voor een stukje met een lengte van tien aminozuren hebben we $20^{10}= 10240000000000\approx 10^{13}$ ofwel 10 biljoen unieke sequenties. In een probabilistisch model moeten we dus een vereenvoudiging doorvoeren!

\bigskip

> **Vereenvoudiging:** We gaan ervan uit dat de kansen voor de verschillende aminozuren **binnen** een bepaalde regio onafhankelijk van elkaar zijn.

\bigskip

Deze vereenvoudiging is natuurlijk volstrekt biologisch onrealistisch! De aminozuren zijn in werkelijkheid juist erg afhankelijk, bijvoorbeeld omdat twee aminozuurtjes met elkaar in contact komen en een waterstofbrug vormen. Hoe fout deze vereenvoudiging ook is, ze is echter wel nuttig! Het laat ons toe om de kansen voor een $\beta$-plaat eenvoudig te herschrijven. In formulevorm is deze veronderstelling voor ons probleem[^productnotatie]:

[^productnotatie]: Hier maken we gebruik van de notatie voor een product: $\prod_{i=1}^n x_i=x_1 x_2\ldots x_n\,,$ (bv. $\prod_{i=2}^4 i = 2\times 3\times 4=24$).

$$
P(\text{eiwitsequentie} \mid \beta\text{-plaat})= P(A_1\mid\beta\text{-plaat})P(A_2\mid\beta\text{-plaat})\ldots P(A_n\mid\beta\text{-plaat})
$$
$$
= \prod_{i=1}^n P(A_i\mid\beta\text{-plaat})\,,
$$

en, analoog, de kans op een sequentie als het geen $\beta$-plaat is:

$$
P(\text{eiwitsequentie} \mid \text{geen $\beta$-plaat})= \prod_{i=1}^n P(A_i\mid \text{geen $\beta$-plaat})\,.
$$

Daarnaast moeten we ook nog de noemer berekenen, namelijk de kans op een eiwitsequentie, deze valt als volgt uiteen (wet van de totale probabiliteit):

\begin{multline*}
P(\text{eiwitsequentie}) = P(\text{eiwitsequentie} \mid \text{$\beta$-plaat})P(\text{$\beta$-plaat})\\+ P(\text{eiwitsequentie} \mid \text{geen $\beta$-plaat}) P(\text{geen $\beta$-plaat})\,.
\end{multline*}

Dit is alles wat we nodig hebben! We kunnen de kans op een $\beta$-plaat gegeven een sequentie dus berekenen aan de hand van termen die we makkelijk uit data kunnen schatten door te tellen:

$$
P(A_i\mid \text{$\beta$-plaat}) = \frac{\text{aantal keer aminozuur $A_i$ in $\beta$-plaat regio's}}{\text{totaal aantal aminozuren in $\beta$-plaat regio's}}\,,
$$

$$
P(A_i\mid \text{geen $\beta$-plaat}) = \frac{\text{aantal keer aminozuur $A_i$ in niet-$\beta$-plaat regio's}}{\text{totaal aantal aminozuren in niet-$\beta$-plaat regio's}}
$$

> **Vraag**: Onder dit model, denk je dat er een verschil is tussen de kans dat 'RGTHHG' of 'GHHTGR' deel uitmaakt van een $\beta$-plaat regio?

### Een eenvoudig voorbeeld met de hand uitwerken

Nu kunnen we de bovenstaande formule gebruiken om voorspellingen te maken voor eiwitten. Vooraleer we deze formule doorgeven aan de computer zullen we ze eerst zelf op papier eens toepassen.

Onderstaande tabel bevat experimenteel bepaalde aminozuur (AZ) aantallen van een staarteiwit van een faag die we zullen gebruiken om voorspellingen te maken. Op basis van die aantallen zijn de verschillende conditionele kansen berekend.

| AZ         | totaal aantal | aantal in $\beta$-plaat | aantal niet in $\beta$-plaat | $P(A_i\mid \beta\text{-plaat})$ | $P(A_i\mid \text{geen } \beta \text{-plaat})$ |
|:-----------|:--------------|:------------------------|:-----------------------------|:--------------------------------|:----------------------------------------------|
| A          | 48            | 21                      | 27                           | 0.0634                          | 0.0804                                        |
| C          | 8             | 2                       | 6                            | 0.0060                          | 0.0179                                        |
| D          | 48            | 19                      | 29                           | 0.0574                          | 0.0863                                        |
| E          | 22            | 11                      | 11                           | 0.0332                          | 0.0327                                        |
| F          | 25            | 13                      | 12                           | 0.0393                          | 0.0357                                        |
| G          | 71            | 29                      | 42                           | 0.0876                          | 0.1250                                        |
| H          | 10            | 4                       | 6                            | 0.0121                          | 0.0179                                        |
| I          | 51            | 36                      | 15                           | 0.1088                          | 0.0446                                        |
| K          | 34            | 12                      | 22                           | 0.0363                          | 0.0655                                        |
| L          | 49            | 30                      | 19                           | 0.0906                          | 0.0565                                        |
| M          | 9             | 6                       | 3                            | 0.0181                          | 0.0089                                        |
| N          | 41            | 18                      | 23                           | 0.0544                          | 0.0685                                        |
| P          | 28            | 7                       | 21                           | 0.0211                          | 0.0625                                        |
| Q          | 22            | 9                       | 13                           | 0.0272                          | 0.0387                                        |
| R          | 23            | 14                      | 9                            | 0.0423                          | 0.0268                                        |
| S          | 50            | 25                      | 25                           | 0.0755                          | 0.0744                                        |
| T          | 46            | 23                      | 23                           | 0.0695                          | 0.0685                                        |
| V          | 48            | 31                      | 17                           | 0.0937                          | 0.0506                                        |
| W          | 7             | 2                       | 5                            | 0.0060                          | 0.0149                                        |
| Y          | 27            | 19                      | 8                            | 0.0574                          | 0.0238                                        |
| **Totaal** | **667**       | **331**                 | **336**                      | **1**                           | **1**                                         |
Dus is de kans op een $\beta$-plaat gelijk aan:

$$
P(\beta\text{-plaat}) = \ldots
$$

en de kans op een geen $\beta$-plaat:

$$
P(\text{geen }\beta\text{-plaat}) = \ldots
$$

<br>

> **Oefening 2:** Volgende korte sequentie is een klein deeltje van het P12528 staarteiwit: 'MLIDIAR'. Experimenteel werd reeds bepaald dat dit een $\beta$-plaat is. Bereken nu via de laatst geziene formule de kans dat die sequentie een stukje van een $\beta$-plaat is (deze kans zou groot moeten zijn).

| $i$ | $A_i$ | $P(A_i\mid \beta\text{-plaat})$ | $P(A_i\mid \text{geen }\beta\text{-plaat})$ |
|:----|:------|:--------------------------------|:--------------------------------------------|
| 1   | ...   | ...                             | ...                                         |
| 2   | ...   | ...                             | ...                                         |
| 3   | ...   | ...                             | ...                                         |
| 4   | ...   | ...                             | ...                                         |
| 5   | ...   | ...                             | ...                                         |
| 6   | ...   | ...                             | ...                                         |
| 7   | ...   | ...                             | ...                                         |
<br>

En dus (vermenigvuldig alle kansen):

$$
P(\text{eiwitsequentie} \mid \text{$\beta$-plaat}) = \ldots
$$

en

$$
P(\text{eiwitsequentie} \mid \text{geen }\text{$\beta$-plaat}) = \ldots
$$

waaruit volgt:

$$
P(\text{eiwitsequentie}) = \ldots
$$

En dus finaal, volgens de regel van Bayes:

$$
P( \text{$\beta$-plaat} \mid \text{eiwitsequentie}) = \frac{\ldots\ldots\times \ldots\ldots}{\ldots\ldots}=\ldots
$$

## Naive Bayes op de computer

### Glijdende vensters en drempelwaarden

In het computerdeel van dit practicum gaan we nu de Naive Bayes-methode toepassen op het volledige P12528 eiwit dat we eerder besproken hebben. Het doel is om te ontdekken waar de $\beta$-platen zich in het eiwit bevinden. We zullen $\beta$-platen voorspellen met behulp van de Naive Bayes-methode en de voorspellingen (i.e. de kansen) dan voorstellen via een grafiek. Hiervoor bewegen we aminozuur voor aminozuur over het eiwit via een *glijdend venster* van lengte $k$. In dit glijdend venster kijken we naar de aminozuren op elke positie van $i$ tot $i+k$ en berekenen we de conditionele kans voor een $\beta$-plaat in dit venster. We noteren dit als

$$
s^k_i = P(\beta\text{-plaat}\mid \text{subsequentie van $i$ tot $i+k$})\,.
$$

![Illustratie van het glijdend venster over een sequentie.](../figuren/glijdendvenster.png)

In elke stap (voor elk glijdend venster) maken we een voorspelling die we later visueel kunnen voorstellen in een plot.

We kunnen stellen dat we een regio als een $\beta$-plaat kunnen classificeren indien

$$
P(\beta\text{-plaat}\mid \text{eiwitsequentie}) > 0.5\,.
$$

We willen dit echter veralgemenen zodat we strenger of minder streng kunnen zijn om secundaire structuren te vinden:

$$
P(\beta\text{-plaat}\mid \text{eiwitsequentie}) > \theta\,.
$$

Hier is $\theta$ een zorgvuldig gekozen *drempelwaarde* (Engels: threshold). De keuze van $\theta$ heeft gevolgen voor de correctheid van onze voorspellingen:

- als we $\theta$ te hoog kiezen is onze drempelwaarde te streng en zullen we dus bepaalde regio's niet als $\beta$-platen voorspellen terwijl dit eigenlijk wel $\beta$-platen zijn.
- als we $\theta$ te laag kiezen zijn we niet streng genoeg. We zullen dus regio's voorspellen als $\beta$-plaat die eigenlijk geen $\beta$-plaat zijn.

Hieronder zie je een voorbeeld van een analyse met een glijdend venster.

![Voorstelling van de resultaten van het glijdend venster. De regio's waar de conditionele kans de drempelwaarde overschrijdt gedurende een bepaalde lengte (bepaald door $k$), worden aangeduid als $\beta$-plaat.](../figuren/glijdendvenstervoorbeeld.png)

Je kan dus inzien dat we de waarde van $\theta$ net goed willen kiezen zodat we het aantal foute voorspellingen tot een minimum beperken. Dit beperken van foute voorspellingen is altijd gewenst bij het gebruik van wiskundige modellen, en om deze fouten te bestuderen doen we aan *modelevaluatie*.

### Modelevaluatie: op welke manier is je model fout?

Wiskundige modellen maken zelden perfecte voorspellingen. Toch is het in de praktijk belangrijk dat modellen zeer accurate voorspellingen maken. Als bijvoorbeeld een zelfrijdende auto een foute voorspelling maakt over waar hij moet rijden kan dat mogelijks fataal zijn voor personen in de wagen en/of in de omgeving. Wanneer een wiskundig model voorspelt dat jij een kankergezwel hebt terwijl dat eigenlijk niet zo is, krijg je onnodig dure chemotherapie (die vaak ook slechte bijwerkingen heeft). Er zijn natuurlijk ook minder ernstige voorbeelden: wanneer het algoritme van Netflix je weer een serie aanraadt die je niet goed vindt, ga je simpelweg niet naar die serie beginnen kijken. Maar uiteraard wil ook Netflix zijn klanten de meest relevante films en series aanraden, en dat doen ze door continu voorspellingen te maken o.b.v. de series en films die jij al bekeken hebt en de grote hoeveelheid data die ze over hun andere klanten hebben.

Om inzicht te krijgen in hoe goed of hoe slecht een model voorspellingen maakt, zullen we het model evalueren: we bepalen hoe goed het model werkt op nieuwe data. Bij het voorspellen van secundaire structuren kan ons model slechts twee soorten voorspellingen maken: ofwel is de beschouwde regio onderdeel van een $\beta$-plaat ofwel is die dat niet. Het eerste noemen we een *positieve voorspelling*, het tweede een *negatieve voorspelling*. Deze terminologie is afkomstig uit de geneeskunde: een diagnostische test is positief als de persoon ziek is, en negatief als de persoon niet ziek is. In onze context hebben we echter geen voorkeur voor een positieve of negatieve voorspelling, we willen enkel correcte voorspellingen! Ons model kan twee soorten foute voorspellingen maken:

- Er werd foutief voorspeld dat een regio deel uitmaakt van een $\beta$-plaat. Dit heet een **vals positieve** voorspelling (Engels: *false positive*).
- Een regio werd voorspeld als geen deel van een $\beta$-plaat terwijl dit in werkelijkheid wel zo is. Dit is een **vals negatieve** voorspelling (Engels: *false negative*).

De correcte en foute voorspellingen kunnen we eenvoudig voorstellen in een tabel:

|                                          | **Voorspeld als $\beta$-plaat** | **Voorspeld als geen $\beta$-plaat** |
|:-----------------------------------------|:--------------------------------|:-------------------------------------|
| **Regio is deel van $\beta$-plaat**      | echt positief                   | vals negatief                        |
| **Regio is geen deel van $\beta$-plaat** | vals positief                   | echt negatief                        |

\bigskip

Beide foute voorspellingen zijn nauw verbonden met de keuze van de drempelwaarde $\theta$, alsook de grootte van het glijdend venster. In een laatste stap zullen we daarom de drempelwaarde $\theta$ en de grootte van het glijdend venster manueel aanpassen en het effect bestuderen op het aantal foute voorspellingen. Op die manier kunnen we $\theta$ en de grootte van het venster optimaal kiezen en zo de foute voorspellingen tot een minimum beperken.

### Stappenplan

Concreet zullen we de computer dus instructies geven om het volgende te doen:

1. Startend bij het begin van een eiwitsequentie maakt de computer een eerste voorspelling voor het stukje van de sequentie dat zich in het glijdend venster bevindt. Dit doet hij door Naive Bayes toe te passen en het stukje sequentie als $\beta$-plaat te voorspellen wanneer de berekende kans groter is dan de vooropgestelde drempelwaarde $\theta$.
2. Daarna schuift de computer het glijdend venster één aminozuur op in de sequentie en maakt een nieuwe voorspelling voor dit glijdend venster. Dit proces herhaalt de computer tot het einde van de eiwitsequentie bereikt is.
3. Voor elk glijdend venster slaat de computer de voorspelling op, zodat die later visueel voorgesteld kan worden.
4. We laten de computer de voorspellingen vergelijken met de werkelijke secundaire structuren, zodat we het model kunnen evalueren o.b.v. vals positieven en vals negatieven.
5. Als laatste stap veranderen we manueel de drempelwaarde $\theta$ en de grootte van het glijdend venster, om op die manier te proberen de vals positieven en vals negatieven tot een minimum te beperken.

> **Computeroefeningen:** Het glijdend venster om secundaire structuur te voorspellen is beschikbaar in een Jupyter notebook. Deze zijn beschikbaar via de website van de biowiskundedagen (http://www.biowiskundedagen.ugent.be/) of door op [*deze link*](https://mybinder.org/v2/gh/michielstock/biowiskundedagen/master) te klikken. Met die notebook kan je experimenteren met de grootte van het venster, de parameter $k$ en de drempelwaarde. Enkele vragen hierbij zijn de volgende:
>
> - Welke invloed heeft de parameter $k$ als die groter wordt?
> - Wat wil $k=1$ zeggen?
> - Welke invloed heeft het verhogen en verlagen van de drempelwaarde op de verschillende types fouten?
> - Kan je het aantal valse positieven (niet-$\beta$-platen die als $\beta$-plaat voorspeld worden) zo laag mogelijk krijgen? Hoe zorg je er voor dat je geen enkele $\beta$-plaat mist? Wat is het nadeel hiervan?

## Naive Bayes programmeren

We illustreren hier hoe de kansen op de computer berekend kunnen worden in de programmeertaal Python.

```python
# volledige eiwitsequentie
P12528eiwit = "MTDITANVVVSNPRPIFTESRSFKAVANGKIYIGQIDTDPVNPANQIPVYIENEDGSHVQITQPLII\
NAAGKIVYNGQLVKIVTVQGHSMAIYDANGSQVDYIANVLKYDPDQYSIEADKKFKYSVKLSDYPTLQDAASAAVDGLL\
IDRDYNFYGGETVDFGGKVLTIECKAKFIGDGNLIFTKLGKGSRIAGVFMESTTTPWVIKPWTDDNQWLTDAAAVVATL\
KQSKTDGYQPTVSDYVKFPGIETLLPPNAKGQNITSTLEIRECIGVEVHRASGLMAGFLFRGCHFCKMVDANNPSGGKD\
GIITFENLSGDWGKGNYVIGGRTSYGSVSSAQFLRNNGGFERDGGVIGFTSYRAGESGVKTWQGTVGSTTSRNYNLQFR\
DSVVIYPVWDGFDLGADTDMNPELDRPGDYPITQYPLHQLPLNHLIDNLLVRGALGVGFGMDGKGMYVSNITVEDCAGS\
GAYLLTHESVFTNIAIIDTNTKDFQANQIYISGACRVNGLRLIGIRSTDGQGLTIDAPNSTVSGITGMVDPSRINVANL\
AEEGLGNIRANSFGYDSAAIKLRIHKLSKTLDSGALYSHINGGAGSGSAYTQLTAISGSTPDAVSLKVNHKDCRGAEIP\
FVPDIASDDFIKDSSCFLPYWENNSTSLKALVKKPNGELVRLTLATL"

# voorbeelden van sequenties van beta-platen
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
```

Via de geavanceerde datastructuur `Counter` kunnen we makkelijk de frequenties van de verschillende aminozuren bepalen.

```python
from collections import Counter

freq_az_P12528 = Counter(P12528eiwit)  # Counter is een dict datastructuur

for AZ, freq in freq_az_P12528.items():
    print(AZ, " : ", freq)

aminozuren = freq_az_P12528.keys()  # alle aminozuren
```

Ditto voor de $\beta$-platen:

```python
freq_az_betaplaat = Counter()  # initieer een counter object

for betaplaat in beta_platen:
    # voeg de individuele platen toe
    freq_az_betaplaat.update(betaplaat)

# kijk voor aminozuur P (proline)
print("P :", freq_az_betaplaat["P"])
```

De frequenties van de aminozuren die niet in een $\beta$-plaat voorkomen berekenen we als volgt.

```python
freq_az_niet_betaplaat = {}  # lege dictionary

for AZ in aminozuren:
    freq_az_niet_betaplaat[AZ] = freq_az_P12528[AZ] - freq_az_betaplaat[AZ]
```

We kunnen makkelijk het aantal aminozuren tellen in de regio's.

```python
totaal_beta = sum(freq_az_betaplaat.values())
totaal_niet_beta = sum(freq_az_niet_betaplaat.values())

print("Aantal aminozuren in beta-platen: ", totaal_beta)
print("Aantal aminozuren in niet-beta-platen: ", totaal_niet_beta)
```

> **Optionele programmmeeropdracht**: Bereken met de computer de conditionele kans op een $\beta$-plaat zoals je op papier gedaan hebt. Bereken de kans dat peptide 'YSIEADKK' een $\beta$-plaat is volgens de Naive Bayes methode.

## En verder...

De concepten die je in deze praktische sessie geleerd hebt zijn eenvoudig en kunnen zeer nuttig zijn in de praktijk. Deze methode is een vereenvoudigede versie van de **Chou-Fasman** methode om secundaire structuren te voorspellen. Er bestaan echter ook veel complexere methoden om eiwitten te bestuderen. Misschien vind je onze methode van het glijdend venster nogal onelegant. Een veel krachtigere methode om secundaire structuren te bepalen is via *verborgen Markovketens* (Engels: Hidden Markov Chains) die op een slimme manier eiwit- en DNA-sequenties kunnen labellen.

Daarenboven staat onderzoek in de bio-informatica nooit stil en zijn er zelfs grote bedrijven in geïnteresseerd, net omdat computers ons veel kunnen bijleren over biologie. Een zeer recent voorbeeld is Deepmind, een bedrijf dat onder Google werkt. Recent werk van hen gebruikt complexe artificiële intelligentie om de tertiaire structuur van een eiwit accuraat te voorspellen. Hun ontwikkelde methode [*AlphaFold*](https://deepmind.com/blog/alphafold/) is de eerste in zijn soort, maar zal waarschijnlijk niet de laatste zijn. Net zoals we in dit project gedaan hebben, werd hierbij een model gefit aan een databank met gelabelde voorbeelden. Wij hebben echter met een model gewerkt met een twintigtal parameters, in de praktijk zijn het er miljoenen of miljarden.

\pagebreak
