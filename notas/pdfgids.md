# PDF gids

1. De pdf files van deze notas werden gemaakt via pandoc en het [Eisvogel](https://github.com/Wandmalfarbe/pandoc-latex-template) template. Om de markdown files te kunnen omzetten naar pdf heb je aldus [pandoc](http://pandoc.org/) en LaTeX nodig.
2. Neem de Eisvogel.latex template in deze map en zet hem in de correcte folder:
- Unix, Linux, macOS: ~/.pandoc/templates/
- Windows XP: C:\Documents And Settings\USERNAME\Application Data\pandoc\templates
- Windows Vista or later: C:\Users\USERNAME\AppData\Roaming\pandoc\templates
3. Open een terminal, begeef je naar de correcte map met de markdown files in en voer volgend commando uit: pandoc --latex-engine=xelatex cover.md secundairestructuur.md ziekteverspeiding.md -o bwd2019.pdf --from markdown --template eisvogel
