# py_keynote_figs
Python matplotlib script to toggle between the figure formatting for keynote and manuscripts

Using the matplotlib.rcParams[] function within python, changes to the figure formatting can be made for the duration of the existing python session. The major change is the swapping of a color palatte from black on white to white on black. Other improvements are made to improve legibility on terrible projectors. The author has seen far too many terrible attrocities committed with keynote talks on default white backgrounds. The line must be drawn here.

##Detailed changes (Manuscript -> Keynote)
- Line color : Black to white
- Text color : Black to white
- Axes face color : White to black
- Axes edge color : Black to white
- Axes label color : Black to white
- Tick color : Black to white
- Grid color : Black to white
- Figure face color : White to black
- Figure edge color : White to black
- Default plot line color : Black to white
- Line width : 1.0 to 2.0
- Font size : 8 to 14
- Font family : Serif to sans-serif
- LaTeX : On to off
 
##Things to-do
- Include transparency options by default for keynote figures
- Adjust rendering of math to avoid serifed LaTeX fonts in keynote mode
