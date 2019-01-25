# PDF gids en comments

1. De pdf files van deze notas werden gemaakt via pandoc en het [Eisvogel](https://github.com/Wandmalfarbe/pandoc-latex-template) template. Om de markdown files te kunnen omzetten naar pdf heb je aldus [pandoc](http://pandoc.org/) en LaTeX nodig.
2. Neem de Eisvogel.latex template in deze map en zet hem in de correcte folder:
- Unix, Linux, macOS: ~/.pandoc/templates/
- Windows XP: C:\Documents And Settings\USERNAME\Application Data\pandoc\templates
- Windows Vista or later: C:\Users\USERNAME\AppData\Roaming\pandoc\templates
2. Open een terminal, begeef je naar de correcte map met de markdown files in en voer volgend commando uit:  
  - `pandoc -N --latex-engine=xelatex cover.md voorwoord.md secundairestructuur.md ziekteverspeiding.md -o bwd2019.pdf --from markdown --template eisvogel -V lang=nl` (voor PDF)
  - - `pandoc -N --latex-engine=xelatex cover.md voorwoord.md secundairestructuur.md ziekteverspeiding.md -o bwd2019.tex --from markdown --template eisvogel -V lang=nl` (voor .tex)

Checklist voor TeX:
- [x] inhoudstafel: `\tableofcontents`
- [x] taal: `\usepackage[dutch]{babel}`
- [ ] grootte figuren handmatig goedzetten

TO DO feedback aanpassingen:
- p9 - de 5e kansregel (conditionele kans): Strikt genomen definieer je onafhankelijkheid via de conditionele kans: "B levert geen informatie over A" en van daaruit zie je dan dat de kans op de doorsnijding het product van de kansen is.
- p12 - de vereenvoudiging: Het gaat hier over conditionele onafhankelijkheid, dus onafhankelijkheid gegeven een specifieke beta-plaat: dit komt niet tot uiting in de omschrijving van de vereenvoudiging
- p13 - bijhorende voetnoot die dat uitlegt: Ik vind dit toch wel een belangrijk onderscheid, door het in een voetnoot te plaatsen is het precies alsof dit maar om en "detail" gaat.
- p21 - 1000 miljoen? 100 miljoen of 1 miljard? Ik vond hier niet direct een cijfer van terug
- p23 - S, I en R zijn relatieve aantallen? Hoe moet dit geïnterpreteerd worden, zijn bv.  percentages mogelijk (reeel getal tussen 0 en 1)?
- p24 - onderschrift van figuur 7: Ik vind het wat vreemd dat dit in de titel van de figuur wordt besproken. Ik zou de tijd nemen om deze figuur expliciet toe te lichten. Bv: de pijlen stellen een tijdsstap voor enzoverder...
- p25 - gebruik van 'kans' in de 1e lijn: Ik zou het woord kans hier opnieuw vermijden...
- p30 - vraag 5: kunnen ze op dit moment deze vraag al beantwoorden? Er is nog niet echt gezegd wat het betekent dat twee personen met elkaar "verbonden" zijn.
- p31 - formule D(k) en oef 2: Mss een lijn toevoegen in de tabel waar ze het relatief aantal moeten weergeven? Dat het 'normalizeren' nog duidelijker is?
- p32 - Figuur 14: Boven de figuur wordt "willekeurig" gebruikt, in de figuur "random" -> waarom maak je gebruik van twee woorden van hetzelfde?
- p34 - paragraaf onder ziektedynamiek op een netwerk: De notatie N_i^t is nergens gedefinieerd. Definieer dit!
- p34 - oef 3: zou het zin hebben om een specifiek persoon mee te geven waarmee ze moeten beginnen? Dit is mogelijks makkelijker om tijdens die namiddag te helpen bij vragen omdat we dan maar "1 oplossing" moeten beredeneren? Waar moeten ze plotten?
- p40 - sectie 2.7: Ik heb het gevoel dat deze sectie iets meer context/duiding nodig heeft met een duidelijke kernboodschap die je hier wil meeggeven. Als ik het nu de eerste keer lees, komt het voor mij een beetje over als losstaande dingen die snel nog eens vermeld moeten worden.
