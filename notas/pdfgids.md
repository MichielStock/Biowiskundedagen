# PDF gids

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
