import matplotlib
import brewer2mpl

def keynote_figs():
	matplotlib.rcParams['lines.color'] = 'white'
	matplotlib.rcParams['patch.edgecolor'] = 'white'
	matplotlib.rcParams['text.color'] = 'white'
	matplotlib.rcParams['axes.facecolor'] = 'black'
	matplotlib.rcParams['axes.edgecolor'] = 'white'
	matplotlib.rcParams['axes.labelcolor'] = 'white'
	matplotlib.rcParams['xtick.color'] = 'white'
	matplotlib.rcParams['ytick.color'] = 'white'
	matplotlib.rcParams['grid.color'] = 'white'
	matplotlib.rcParams['figure.facecolor'] = 'black'
	matplotlib.rcParams['figure.edgecolor'] = 'black'
	matplotlib.rcParams['savefig.facecolor'] = 'black'
	matplotlib.rcParams['savefig.edgecolor'] = 'black'
	cols = (brewer2mpl.get_map('Set1', 'qualitative', 7)).mpl_colors
	cols.insert(0,(1.,1.,1.))
	matplotlib.rcParams['axes.prop_cycle'] = matplotlib.cycler('color', cols)
	matplotlib.rcParams['font.size'] = 14
	matplotlib.rcParams['lines.linewidth'] = 2.0
	matplotlib.rcParams['font.family'] = 'sans-serif'
	matplotlib.rcParams['text.usetex'] = False

def latex_figs():
	matplotlib.rcParams['lines.color'] = 'black'
	matplotlib.rcParams['patch.edgecolor'] = 'black'
	matplotlib.rcParams['text.color'] = 'black'
	matplotlib.rcParams['axes.facecolor'] = 'white'
	matplotlib.rcParams['axes.edgecolor'] = 'black'
	matplotlib.rcParams['axes.labelcolor'] = 'black'
	matplotlib.rcParams['xtick.color'] = 'black'
	matplotlib.rcParams['ytick.color'] = 'black'
	matplotlib.rcParams['grid.color'] = 'black'
	matplotlib.rcParams['figure.facecolor'] = 'white'
	matplotlib.rcParams['figure.edgecolor'] = 'white'
	matplotlib.rcParams['savefig.facecolor'] = 'white'
	matplotlib.rcParams['savefig.edgecolor'] = 'white'
	cols = (brewer2mpl.get_map('Set1', 'qualitative', 7)).mpl_colors
	cols.insert(0,(0.,0.,0.))
	matplotlib.rcParams['axes.prop_cycle'] = matplotlib.cycler('color', cols)
	matplotlib.rcParams['font.size'] = 8
	matplotlib.rcParams['lines.linewidth'] = 1.0
	matplotlib.rcParams['font.family'] = 'serif'
	matplotlib.rcParams['text.usetex'] = True
