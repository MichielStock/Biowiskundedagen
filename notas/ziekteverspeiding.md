# Ziekteverspreiding

- [ ] ==abstract==

In dit project zullen we bestuderen hoe ziektes kunnen verspreiden via een (sociaal) netwerk. We zullen onderzoeken hoe de structuur van een netwerk een invloed kan hebben hoe snel een ziekte doorgegeven wordt. Ten slotte zullen we het effect van vaccinatie bekijken.

[toc]

## Besmettelijke ziektes

In de geschiedenis van de mensheid[^niethumaneziekten] heeft niets zoveel mensen gedood als besmettelijke ziekten. De ziekte die de meeste mensen heeft gedood is waarschijnlijk tuberculose, waarbij 1000 miljoen mensen in alleen de 19de en 20ste eeuwen werden gedood. De ziekte die het snelst gedood heeft, is de 'Spaanse griep' epidemie die tussen 1918-1920 50-100 miljoen mensen heeft gedood. De ziekte met het grootste evenredige dodental blijkt de Zwarte Dood, die 20% van de wereldbevolking en zelfs 50% van de Europese bevolking in de 14e eeuw doodde. Nog erger dan die ramp was het dodental in het Amerikaanse continent na de Europese kolonisatie, die op veel plaatsen de inheemse bevolking met meer dan 90% verminderde.

[^niethumaneziekten]: In deze nota's leggen we de nadruk op de verspreiding van humane ziektes. Dezelfde modellen worden echter ook gebruikt om ziektes tussen dieren (zoals verspreiding van *Myxomatosis* bij konijnen) of zelfs tussen planten (bijvoorbeeld verspreiding van *Phytophthora infestans*, een aardappelziekte die verantwoordelijk was voor de Ierse hongersnood).

Tegenwoordig veroorzaakt besmettelijke ziektes minder doden door betere medische kennis, technieken en middelen. Echter blijven ze een ernstig probleem voor de volksgezondheid. Toch zijn 3 van de 10 belangrijkste doodsoorzaken wereldwijd besmettelijke ziekten. Naast de verbeteringen van de moderne wereld zijn er ook nieuwe uitdagingen voor het stoppen van epidemieën. Nu kan een besmette persoon op een vliegtuig stappen en in een paar uur tijd een ziekte naar een ander continent verspreiden.


![](https://i.imgur.com/TC1h64w.jpg)

- [ ] bron figuur?
- [x] technieken => link naar ander labo!

## Ziekteverspreidingsmodellen

Bij de uitbraak van een besmettelijke ziekte is het belangrijk om inzicht te krijgen in hoe deze ziekte zich de volgende dagen en weken kunnen verspreiden. Dit zal helpen om het optimale gebruik van middelen en mensen te plannen om de ziekteverspreiding een halt toe te roepen. Bovendien, voordat we deze maatregelen ten uitvoer leggen, moeten we weten hoe ze het verloop van de ziekte kunnen beïnvloeden, zodat de meest efficiënte en goedkoopste maatregelen eerst geïmplementeerd kunnen worden.

Om deze en andere belangrijke vragen te beantwoorden, zijn *ziektespreidingsmodellen* vaak gebruikt. Deze modellen zijn gebaseerd op wiskundige vergelijkingen die beschrijven hoe een besmettelijke ziekte zich doorheen de tijd en/of ruimte verspreidt. Ze kunnen worden gebruikt om relevante vragen te beantwoorden, zoals:

- Zonder tussenkomst, zal de ziekte uitsterven of ongecontroleerd verspreiden?
- Hoeveel mensen moeten gevaccineerd worden om de verspreiding te stoppen?
- Hoe beïnvloedt het gedrag van mensen of dieren de verspreiding van ziektes?
- Welk effect zullen verschillende quarantainemaatregelen hebben?

Aangezien het verloop doorheen de tijd cruciaal is in het geval van ziekteverspreiding, zijn bijna alle ziektespreidingsmodellen *dynamisch*[^dynamisch] van aard. Maar sinds de ontwikkeling van de eerste ziektespreidingsmodellen in de eerste helft van de 20e eeuw, bijna alle mogelijke modeltypes zijn gebruikt om de dynamiek van besmettelijke ziektes te beschrijven.

[^dynamisch]: Een dynamisch model wil zeggen dat het een verandering in de tijd modelleert.

In dit project zullen we twee van de belangrijkste en meest gebruikte types van ziektespreidingsmodellen bestuderen.

## Het SIR model

Een van de eenvoudigste manieren om ziekteverspreiding in een gemeenschap te modelleren is aan de hand van het SIR model. SIR staat voor *Susceptible* (vatbaar), *Infected* (geïnfecteerd) en *Resistant* (resistent of hersteld), de drie types van individuen die in een gemeenschap voorkomen. Meestal zijn de individuen gewoon mensen, maar dit model kan ook aangewend worden om ziekteuitbraak bij knaagdieren, vogels of zelfs planten te modelleren. Het SIR model bestaat uit drie vergelijkingen die de veranderingen van het aantal individuen in een bepaalde groep beschrijven. De variabelen die de toestand beschrijven zijn:

-  $S(t)$: het (relatief) aantal vatbare individuen op tijdstip $t$;
-  $I(t)$: het (relatief) aantal geinfecteerde individuen op tijdstip $t$;
-  $R(t)$: het (relatief) aantal resistente individuen op tijdstip $t$.

In deze beschrijving maken we een eerste grote vereenvoudiging van de werkelijkheid. We nemen aan dat elk van deze variablen reëelwaardig zijn en dat het aantal individuen in elke groep continu kan variëeren. In werkelijkheid is het aantal geïnfecteerden of vatbare individuen een geheel getal, je bent immers besmet of je bent het niet. Modelleerders werken echter graag met continue variablen omdat ze dan de technieken van wiskundige analyse kunnen gebruiken.

> **Vraag 1**: Onder welke omstandigheden gaat deze continue benadering ongeveer op? Wanneer niet?

![Visule voorstelling van het SIR model. Een vatbaar individu (toestand $S$) kan geïnfecteerd worden (toestand $I$), weergegeven door de volle pijlen. Een gïnfecteerd individu kan immuun worden en vatbare individuen kunnen  geimmuniseerd worden, weergegeven door de pijlen met stippellijnen. In dit project zullen we deze overgangen niet beschouwen.](../figuren/SIRtoestanden.png)

Deze drie variabelen worden aan elkaar gelinkt aan de hand van drie vergelijkingen. Hierin nemen we aan dat de grootte van de populatie ongewijzigd blijft. In de tijdspanne die het model beschrijft gebeuren er dus geen geboortes, noch sterven er mensen. We zullen ons hier dus betrekken tot de verspreiding van een relatief onschuldige ziekte zoals een verkoudheid. De drie vergelijkingen zijn als volgt:

$$
\frac{\text{d}S(t)}{\text{d}t} = -\beta S(t)I(t)
$$

$$
\frac{\text{d}I(t)}{\text{d}t} = \beta S(t)I(t) - \gamma I(t)
$$

$$
\frac{\text{d}R(t)}{\text{d}t} = \gamma I(t)
$$

Elke vergelijking vertelt ons hoeveel mensen  op een bepaald moment bevinden zich in dat groep. De vergelijkingen zijn gekoppeld via de *overgangssnelheiden*, die vertellen ons de waarschijnlijkheid om van het ene naar het andere groep te gaan.

De overgangssnelheid van vatbaar naar geïnfecteerd hangt af van het contact tussen een vatbare persoon en een geïnfecteerd persoon. We noemen deze contactsnelheid als $\beta$. Dus de kans dat de ziekte  overgedragen wordt tijdens een contact tussen een vatbare en een geïnfecteerde persoon is $\beta I$. Dan vermindert het totale aantal vatbare personen met deze snelheid op elke tijdstip.

De overgangssnelheid van geïnfecteerd naar resistent hangt alleen af van de snelheid van herstel, die we $\gamma$ noemen. Dus het aantal geïnfecteerde personen vermindert met deze snelheid op else tijdstip.

> **Vraag 1**: Kan je aantonen dat het totaal aantal individuen in de populatie $(S(t)+I(t)+R(t))$ constant zal blijven?
>

Bij het vaststellen van deze overgangssnelheiden hebben we een andere belangrijke vereenvoudiging gemaakt. We nemen aan dat elke persoon in de populatie een gelijke waarschijnlijkheid heeft om in contact te komen met elke andere persoon. Anders gezegd, nemen we aan dat de populatie perfect gemengd is. In sommige gevallen kan deze vereenvoudiging passen bij de realiteit, bijvoorbeeld als we willen bijhouden hoe een griep zich door een fuif verspreidt.

Het SIR-model kan niet exact worden opgelost, zoals veel differentiaalvergelijkingen die optreden in de biologische wetenschappen. Dus we moeten een *numerieke benadering* van de oplossing vinden. Dit betekent dat we een algoritme zullen gebruiken om een geschatte maar nauwkeurige oplossing te vinden. Er zijn verschillende mogelijkheiden om dit te doen. We zouden ons continue probleem kunnen vervangen door een discrete tegenhanger. Dit zou ons toelaten bepaalde numerieke methoden te gebruiken om een benaderende oplossing te krijgen. Anders kunnen we een iteratieve methode gebruiken. Uitgaande van een initiële schatting, maken iteratieve methoden opeenvolgende benaderingen die stapsgewijs convergeren naar de exacte oplossing.

Met behulp van computers is het gemakkelijk om op deze manier een numerieke oplossing voor het SIR-model te vinden. Vanuit deze oplossing kunnen we leren hoe de verschillende variabelen in de loop van de tijd veranderen. Om dit te doen, vertrekken we van een beginvoorwaarde: het is logisch om te beginnen met een populatie met zero resistente personen, een paar geïnfecteerde personen en de rest vatbaar. Vervolgens kunnen we onze numerieke oplossing gebruiken om het aantal mensen in elke groep bij elke tijdstap te berekenen. Als we een plot maken, zullen we de dynamiek zien die in de onderstaande figuur wordt getoond.

![](https://i.imgur.com/M0NVPcz.png)

> **Vraag 2**: Een epidemie wordt **uitbreidend** genoemd als het aantal geïnfecteerden toeneemt. Wanneer is de epidemie uitbreidend? Op het moment wanneer $I$ verandert van toenemend naar afnemend, wat kun je zeggen over de verandering van $I$? (**hint**: kijk naar de vorm van $\frac{dI}{dt}$)
>

## Sociale netwerken

Het standaard SIR model maakt de onrealistische veronderstelling dat twee willekeurige individuen telkens de zelfde kans hebben om met elkaar in contact te komen en zo mogelijks een ziekte door te geven [^contact]. In werkelijk gaat natuurlijk niet iedereen met dezelfde mensen om. We hebben allemaal mensen waar we meer mee omgaan dan anderen, sommigen komen meer in contact met anderen. Het geheel van wie met wie in contact staat wordt een *sociaal netwerk* genoemd (denk aan Facebook). Het lijkt evident dat de structuur van zo'n netwerk een sterke invloed zal hebben op de dynamiek van de ziekteverspreiding. In deze sectie zullen we bekijken hoe we een netwerk wiskundig kunnen beschrijven.

[^contact]: Welk type contact hier ook voor nodig zou zijn.

### Een voorbeeld

Hieronder zie je een voorbeeld van een twee netwerken. Laten we ons voorstellen dat het het sociale netwerk van een schoolklas vertegenwoordigt. De punten vertegenwoordigen de studenten en worden *knopen* genoemd. De contacten tussen studenten worden weergegeven door lijnsegmenten tussen knopen, en worden *bogen* genoemd. We zeggen dat twee knopen met elkaar *verbonden* zijn als er een boog tussen zit. Hier gaan we er van uit dat een knoop niet verbonden kan zijn met zichzelf[^selfconnectance]. Ook is er maar maximaal één boog mogelijk tussen twee knopen. De *graad* van een knoop is het aantal bogen dat ermee verbonden zijn.

![](https://i.imgur.com/AozX7EL.jpg)
([source](https://royalsocietypublishing.org/doi/full/10.1098/rspb.2010.1807))

Zoals je ziet wordt een network of een graaf vaak voorgesteld in een figuur waar cirkels (of andere elementen) de knopen voorstellen die geconnecteerd zijn door lijnen, de bogen. Deze figuren zijn niet uniek: eenzelfde netwerk kan vaak op verschillende manieren voorgesteld worden. Soms hebben de knopen ook een kleur, bijvoorbeeld om geslacht te duiden in een sociaal netwerk. In dat geval spreekt men van een *gekleurde graaf*.

[^selfconnectance]: We gaan er van uit dat je niet kan bevriend zijn met jezelf.

> **Vraag 2**: Beschrijf het verschil tussen de sociale netwerken tussen kinderen van verschillende leeftijden.

Een figuur is nuttig om te bekijken hoe het netwerk er uit ziet. Om er berekeningen mee te doen zijn er echter andere representaties nodig. Een graaf kan wiskundig voorgesteld worden in een matrix die heet en *bogenmatrix* (Engels: adjacency matrix). Als de aantal knopen in de graaf $n$ is, dan is de bogenmatrix een vierkante matrix met dimensies $n \times n$. Het element $A_{ij} = 1$ als de knopen $i$ en $j$ verbonden zijn, en $A_{i,j} = 0$ als ze niet verbonden zijn[^verbindingslijst]. Hoewel we hier niet zo ver zullen gaan, linkt de bogenmatrix graaftheorie met matrixtheorie!

[^verbindingslijst]: In het echte leven hebben de meeste mensen in een populatie geen contact met elkaar (denk aan het sociaal netwerk van een  hele stad). Dus de graaf is verre van *volledig verbonden* (elk paar knopen is verbonden) en de elementen van de bogenmatrix bestaat grotendeels uit nullen. In deze gevallen kan het soms beter zijn om een *verbindingslijst* te gebruiken. Dit is een lijst met dimensies $m \times 2$ waarbij $m$ het aantal bogen is, en elke rij bevat een koppel knopen die verbonden zijn. Afhankelijk van het specifieke netwerk dat we bestuderen en wat we ermee willen doen, kan de ene of de andere van deze datastructuren efficiënter zijn.

Het sociaal netwerk dat we beschouwen wordt weergegeven in onderstaande figuur. De knopen (hier personen) zijn genummerd voor ons gemak. We houden geen rekening met geslacht of andere attributen. We zullen hier een ziekteuitbraak op simuleren!

![Een sociaal netwerk tussen vijftien personen.](../figuren/socialnetwerk.png)


> **Oefening 1**: voltooi de bogenmatrix en de verbindingslijst voor het sociale netwerk.

|      | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    | 9    | 10   | 11   | 12   | 13   | 14   | 15  |
:---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---| :---|:--|
| **1** | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |
| **2** | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |
| **3** | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |
| **4** | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |
| **5** | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |
| **6** | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |
| **7** | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |
| **8** | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |
| **9** | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |
| **10** | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |
| **11** | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |
| **12** | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |
| **13** | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |
| **14** | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |
| **15** | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |

- [x] maak netwerk + plot
- [x] verbindingmatrix

### Gradenverdeling

> **Vraag 5**: Wie zal er eerder een verkoudheid oplopen: persoon 3 of 15 ?

Een graaf is een complexe wiskundige structuur. Een gegeven knoop in een graaf wordt gekarakteriseerd door zijn bogen en dus ook graad. Echter, belangrijke eigenschappen van de graaf zijn *emergent*, dit wil zeggen dat ze enkel te verklaren zijn door de graaf in zijn geheel en niet enkel de individuele onderdelen.

Als we iets willen leren over een netwerk, welke informatie kunnen we bekijken? Het zou zeer interessant zijn om te weten hoe verbonden het netwerk is. Hoe kunnen we bepalen tot welke mate de knopen met elkaar verbonden zijn? We zouden naar de gemiddelde knoopgraad kunnen kijken, maar dit zou ons niet veel zeggen. In plaats daarvan kunnen we tellen voor elk nummer $x$ het aantal $y$ van knopen met graad $x$. Deze plot wordt de *gradenverdeling*  (Engels: *degree distribution*) genoemd en kan ons veel vertellen over de structuur van een netwerk. Wiskundig drukken we de gradenverdeling uit als

$$
D(k)=\text{fractie van de knopen met $k$ bogen}\,.
$$

> **Oefening 2**: Bereken en plot de gradenverdeling van het sociaal netwerk. Vul eerst onderstaande tabel in en teken dan de plot.

| $k$ | $D(k)$ |
|:--|:--|
| $1$ | ... |
| $2$ | ... |
| $3$ | ... |
| $4$ | ... |
| $5$ | ... |
| $6$ | ... |
| $7$ | ... |
| $8$ | ... |
| $9$ | ... |
| $10$ | ... |
| $11$ | ... |
| $12$ | ... |
| $13$ | ... |
| $14$ | ... |
| $15$ | ... |

![](../figuren/gradenverdelingenleeg.png)

### Drie types van netwerken

![Illustraties van gradenverdelingen van verschillende types van netwerken.](../figuren/gradenverdelingen.png)

- [ ] inleiding

#### Willekeurige netwerken

Een *willekeurig netwerk* heeft eigenschappen die willekeurig worden bepaald, zoals het aantal knopen, het aantal bogen en de verbindingen tussen knopen en bogen. We kunnen een dergelijk netwerk beschrijven als $G(n, p)$ waarbij $n$ het aantal knopen is en $p$, een getal tussen 0 en 1, de kans dat er een boog tussen een willekeurig paar knopen is.

Bij een willekeurig netwerk is het verwacht aantal graden per knoop gelijk aan

$$
n\cdot p\,.
$$

De meeste knopen hebben een graad dicht bij dit gemiddelde. **In een (groot) willekeurig netwerk vind je zelden een knoop met extreem veel of extreem weinig bogen**[^gradenrn].

[^gradenrn]: Om precies te zijn, de kans dat een knoop in een netwerk met $n$ knopen exact $m$ bogen heeft wordt gegeven door $$p^m(1-p)^{{n \choose 2} - M},,$$. Dit volgt uit de Binomiale verdeling. Hier is ${n \choose 2}$ de binomiaalcoëfficient $${n \choose 2}=\frac{n(n-1)}{2}\,,$$ dit is het aantal mogelijke manier je twee knopen kan kiezen uit $n$.

> **Oefening** Een sociaal netwerk van een school telt 1000 leerlingen. Ga er van uit dat dit beschreven kan worden als een willekeurig netwerk met $p=0.01$. Hoeveel vrienden heeft een persoon gemiddeld? Denk je dat het waarschijnlijk is dat er iemand rond loopt die slechts twee of minder vrienden heeft?

$$
\text{Gemiddeld aantal vriendschappen} = \ldots \quad
$$

$$
P(\text{Geen vrienden})= \ldots
$$

$$
P(\text{Eén vriend})= \ldots
$$

$$
P(\text{Twee vrienden})= \ldots
$$

$$
P(\text{Twee of minder vrienden})= \ldots
$$

> **Vraag** Binnen een random netwerk heeft elke knoop ongeveer hetzelfde aantal graden (iedereen heeft ongeveer evenveel vrienden in een sociaal netwerk). Denk je dat dit een realistische assumptie is voor veel netwerken?


#### Schaalvrije netwerken

Een netwerk wordt *schaalvrij* (Engels: scale-free)  genoemd als de gradenverdeling ongeveer aan volgdende vorm voldoet aan een zogenaamde *power law*[^propto]

[^propto]: $\propto$ wil zeggen 'evenredig aan'.

$$
d(k) \propto \frac{1}{k^a}\,,
$$

met $a$ een exponent die verschild van network tot netwerk. **In een schaalvrij netwerk hebben enkele knopen een hoge graad en zijn er veel knopen met een lage graad.** Schaalvrije netwerken onstaan door een aggregatieproces waarbij 'the rich get richer': wanneer nieuwe knopen aan een netwerk toegevoegd worden, gaan deze preferentieel verbindingen aan met  knopen met een reeds hoge graad.

Schaalvrije netwerken komen overal voor:

- netwerken van filmsterren (knopen) die samen in een film gespeeld hebben (bogen);
- netwerken van het internet: links (bogen) tussen websites (knopen);
- netwerken die interacties (bogen) weergeven tussen eiwitten (knopen).

> **Vraag**: Stel je een sociaal netwerk voor van drie vrienden waar gradueel nieuwe mensen aan geïntroduceerd worden. Kan je je een scenario voorstellen waarbij een schaalvrij netwerk bekomen zou worden?

#### Ruimtelijke netwerken

Soms zijn we niet alleen geïnteresseerd in de individuen en hun contacten in een netwerk, maar ook in de onderliggende ruimte. We kunnen grafen ook gebruiken om een *ruimtelijk* proces te beschrijven. Stel dat de knopen punten zijn die evenredig verspeid liggen op een grid. Er is een boog die twee punten verbindt als die naburig zijn, zoals op onderstaande figuur te zien is. We noemen dit een *gridnetwerk*.

- [ ] figuur
- [ ] notas:
    - [ ] graden
    - [ ] verspreiding

> **PICTURE?**

> **Vraag**: Kun je de gradenverdeling van een regelmatig gridnetwerk met $m$ rijen en $n$ kolommen afleiden? **Hint** Stel dat $n$ en $m$ erg groot zijn.


## Verspreiding van een ziekte doorheen een netwerk

Laat ons nu kijken hoe we het SIR ziekteverspreidingsmodel kunnen vertalen naar de taal van netwerken. Aan de hand van een algemeen netwerk zullen we een veel realistischer model opstellen, geen continue benadering meer! Vreemd genoeg sluit dit model niet enkel dichter aan bij de werkelijkheid, het is ook veel eenvoudiger om te bevatten en te simuleren. We kunnen een exacte oplossing bekomen zonder zelfs maar afgeleiden of andere geavanceerde wiskundige technieken nodig te hebben!

### Ziektedynamiek op een netwerk

In plaats van het aantal $S$, $I$ en $R$ individuen doorheen de tijd bij te houden zoals bij het standaard SIR model zullen we voor elke knoop in het netwerk zijn of haar toestand bijhouden. Ook de tijd zal niet meer continu varieren maar zal nu in discrete stappen wegtikken: $t \in 0, 1, 2, 3, \ldots$. De toestanden van het model worden dus beschreven door $N_i^t\in \{S, I, R\}$, dit wil zeggen dat knoop $i$ op tijdstip $t$ de toestand $S$ (vatbaar), $I$ (geïnfecteerd) of $R$ (resistent) kan hebben. De verandering in toestanden voor de knopen beschrijven we aan de hand van enkele eenvoudige regels.

#### Vatbare en geinfecteerde mensen

Laten we ons eerst beperken tot vatbare en geïnfecteerde individuen. We gaan er van uit dat vatbare individuen ziek kunnen worden, maar zieke individuen niet meer kunnen genezen. Beschouw volgende regels:

1. Indien een knoop in tijdstip $t$ in toestand $S$ zit en al zijn buren eveneens in toestand $S$ zitten, blijft de knoop in tijdstip $t+1$ in toestand $S$.
2. Indien een knoop in tijdstip $t$ in toestand $S$ zit en minstend één van zijn buren eveneens in toestand $I$ zit, verandert de knoop in tijdstip $t+1$ naar toestand $I$.
3. Indien een knoop in tijdstip $t$ in toestand $I$ zit blijft de knoop in tijdstip $t+1$ in toestand $I$.


![Overzicht van de regels voor het SIR model op een netwerk.](../figuren/SIRregels.png)


> **Oefening 3**: Gebruik het sociale netwerk dat je hebt gekregen om de verspreiding van een ziekte te modelleren.
>1. Elk individu begint als vatbaar. Kies een persoon om de eerste geïnfecteerde te worden en kleurt deze in.
>2. Bij elke tijdstip, ga een voor een door de buren van een geïnfecteerde persoon en laat hen ook geïnfecteerde raken volgens de bovenstaande regels. Vul de tabel in om de spreiding over de tijd te volgen.
>3. Herhaal totdat het netwerk niet meer verandert.
>4. Volgens de tabel, plot het aantal geïnfecteerden bij elke tijdstip.


| knoop | $t = 0$   | $t = 1$ |
| :------------- | :------------- | :-|
| A      |    $S^0_A$    |$S^1_A$
| B      |    $S^0_B$    |$I^1_B$

> **OEFENING**: Herhaal de laatste oefening met een ander startpunt: kies een persoon met minder of meer contacten. Vul de tabel in en plot het aantal geïnfecteerden bij elke tijdstip. Hoe verandert de ziekteverspreiding ?
>

| knoop | $t = 0$   | $t = 1$ |
| :------------- | :------------- | :-|
| A      |    $S^0_A$    |$S^1_A$
| B      |    $S^0_B$    |$I^1_B$

### Immuniteit en vaccinatie

Het bovenstaande voorbeeld geeft ons een idee hoe we ziekteverspreiding op een netwerk kunnen modelleren, maar nu kunnen we enkele vereenvoudigingen verwijderen. Laten we nu *immuniteit* in onze populatie toestaan. Dit betekent dat sommige mensen niet geïnfecteerd kunnen worden. Hun immuniteit kan natuurlijk zijn (door een herstelling van een eerdere infectie) of kunstmatig (door een vaccin te krijgen).  Dus nu kunnen individuen in het netwerk ook in toestand $R$ (resistent) zitten.

Beschouw nu de volgende regels:

1. Indien een knoop in tijdstip $t$ in toestand $S$ of $R$ zit en al zijn buren eveneens in toestand $S$ of $R$ zitten, verandert de knoop zijn toestand niet in tijdstip $t+1$.
2. Indien een knoop in tijdstip $t$ in toestand $S$ zit en minstend één van zijn buren eveneens in toestand $I$ zit, verandert de knoop in tijdstip $t+1$ naar toestand $I$.
3. Indien een knoop in tijdstip $t$ in toestand $I$ zit blijft de knoop in tijdstip $t+1$ in toestand $I$.
4. Een knoop in toestand $R$ blijft altijd in toestand $R$.

> **Oefening**: Simuleren we nu een epidemie in een populatie met een bepaalde  niveau van *natuurlijke immuniteit*.
>1. Elk individu begint als vatbaar. Kies een persoon om de eerste geïnfecteerde te worden en kleurt deze in.
>2. Ga een voor een door de buren van een geïnfecteerde persoon. Voor elke knoop gooi een dobbelsteen: als het **1 of 2** is, wordt die persoon ook geïnfecteerd. Als het **een ander nummer** is, zijn ze resistent.
>3. Herhaal voor de nieuwe geïnfecteerde mensen en ga door totdat je de dobbelstenen gegooid hebt voor de buren van elke geïnfecteerde persoon.
>4. Tel hoeveel mensen in de populatie zijn geïnfecteerd en hoeveel stappen je hebt genomen om ze allemaal te infecteren. Maak een plot.
>5. Herhaal de oefening met verschillende startpunten.

> **Oefening**: Nu herhalen we de oefening, maar met *gerichte vaccinatie*.
>1. Elk individu begint als vatbaar. Vaccineer **50% van de populatie**: verander hun toestand in resistent.
>2. Kies een persoon om de eerste geïnfecteerde te worden en kleurt deze in.
>2. Ga een voor een door de buren van een geïnfecteerde persoon en laat hen ook geïnfecteerde raken volgens de bovenstaande regels.
>3. Herhaal voor de nieuwe geïnfecteerde mensen en ga door totdat je de dobbelstenen gegooid hebtvoor de buren van elke geïnfecteerde persoon.
>4. Tel hoeveel mensen in de populatie zijn geïnfecteerd en hoeveel stappen je hebt genomen om ze allemaal te infecteren. Maak een plot.
>5. Herhaal de oefening: deze keer vaccineer **75% van de populatie**.

> **VRAAG**: Wat zou je doen als je slechts 3 doses van het vaccin had? Kies je om de meest populaire mensen te vaccineren, of zou je op bepaalde plaatsen proberen het netwerk te doorbreken? Waarom?


### Kudde-immuniteit

Sommige mensen kunnen door verschillende redenen niet immuun worden. Bijvoorbeeld, vaccins kunnen niet gegeven worden aan jonge baby's of mensen met ernstige medische aandoeningen. In deze groep is *kudde-immuniteit* dus een belangrijke beschermingsmethode.

Kudde immuniteit betekent een indirecte bescherming tegen besmettelijke ziekten. Deze komt voor wanneer een groot percentage van de populatie immuun is tegen een infectie (door natuurlijke immuniteit of vaccinatie) en daardoor beschermen ze mensen die niet immuun zijn. Dit gebeurt omdat het grote aantal immune mensen de ziekteverspreiding vertraagt of zelfs stopt, want de transmissieverbindingen zijn verbroken.

> **PICTURE**

[example of nice figures](https://www.reddit.com/r/dataisbeautiful/comments/5v72fw/how_herd_immunity_works_oc/)

Als een bepaalde grenslijn kan bereikt worden, zal de kudde-immuniteit een ziekte uit een populatie elimineren. Als deze eliminatie over de hele wereld bereikt wordt, kan het aantal infecties permanent tot nul teruggebracht worden. Dan kunnen we spreken van de *uitroeiing* van de ziekte. Het moet duidelijk zijn dat volledige uitroeiing zeer moeilijk te bereiken is. Veel ziekten zijn regionaal uitgeroeid (bijvoorbeeld cholera in België), terwijl slechts twee ziekten wereldwijd uitgeroeid zijn: pokken en runderpest.


## Wat je geleerd hebt over ziekteverspreidingsmodellen

![example in a high profile scientific study of exactly what the students have done](https://i.imgur.com/jEJJ3fJ.jpg)[^PNAS]

[^PNAS]: Source: Cauchemez et al., "Role of social networks in shaping disease transmission during a community outbreak of 2009 H1N1 pandemic influenza," PNAS 108 (7): 2825-2830 (2011).


## Meer informatie

- https://www.gleamproject.org/news
