# py_keynote_figs
Python matplotlib script to toggle between the figure formatting for keynote and manuscripts

Using the matplotlib.rcParams[] function within python, changes to the figure formatting can be made for the duration of the existing python session. The major change is the swapping of a color palatte from black on white to white on black. Other improvements are made to improve legibility on terrible projectors. The author has seen far too many terrible attrocities committed with keynote talks on default white backgrounds. The line must be drawn here.

##Detailed changes (Manuscript -> Keynote (black) / Keynote (grey))
- Line color : Black to white / black
- Text color : Black to white / black
- Axes face color : White to black / grey
- Axes edge color : Black to white / black
- Axes label color : Black to white / black
- Tick color : Black to white / black
- Grid color : Black to white / black
- Figure face color : White to black / grey
- Figure edge color : White to black / grey
- Default plot line color : Black to white / black
- Line width : 1.0 to 2.0 / 2.0
- Font size : 8 to 14 / 14
- Font family : Serif to sans-serif / sans-serif
- LaTeX : On to off / off
 
##Things to-do
- Include transparency options by default for keynote figures
- Adjust rendering of math to avoid serifed LaTeX fonts in keynote mode
- Slightly darken label colors, etc, to bring out the data first and foremost
