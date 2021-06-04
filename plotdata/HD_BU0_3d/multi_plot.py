import matplotlib
import yt
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import AxesGrid
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica'],'size':15})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)

savepath = '../../'

units_override = dict( 
length_unit=(1.0, 'cm'),
time_unit=(1.0, 's'),
mass_unit=(1.0, 'g'),
)

fig = plt.figure()
grid = AxesGrid(fig, (0.075,0.075,0.85,0.85),
                nrows_ncols = (2, 2),
                axes_pad = 1.5,
                label_mode = "each",
                share_all = False,
                cbar_location="right",
                cbar_mode="each",
                cbar_size="5%",
                cbar_pad="1%")

# Load the dataset
ds = yt.load('output0249.dat', unit_system='code')

cuts=['z','x','z','x']
fields=['rho','rho','alp','alp']
annotate_flag=[False,False,True,True]

for i, (direction, field, annotate) in enumerate(zip(cuts, fields, annotate_flag)):
    # Load the data and create a single plot
    p = yt.SlicePlot(ds, direction, field)
    p.zoom(3)
    p.set_cmap(field="rho", cmap='hot')
    p.set_cmap(field="eps", cmap='RED TEMPERATURE')
    p.set_log('alp', False)
    p.set_log('psi', False)
    p.set_log('beta1', False)
    p.set_log('beta2', False)
    p.set_log('beta3', False)
    #if (annotate and direction == 'z'):
        #p.annotate_streamlines('W_vel1', 'W_vel2', density = 0.5, factor = 16)
    #elif (annotate and direction == 'x'):
        #p.annotate_grids()

    if (annotate ):
        p.annotate_grids()

    if (direction == 'z'):
        if (field == 'rho'):
            p.hide_colorbar()
        p.set_xlabel('$x$')
        p.set_ylabel('$y$')
    else:
        p.set_xlabel('$y$')
        p.set_ylabel('$z$')

    p.set_colorbar_label('rho', '$ \\rho $')
    p.set_colorbar_label('eps', '$ \\epsilon $')
    p.set_colorbar_label('alp', '$ \\alpha $')
    #p.set_colorbar_label('W_vel1', '$ W v^r $')
    #p.set_colorbar_label('W_vel2', '$ W v^\\theta $')

    # This forces the ProjectionPlot to redraw itself on the AxesGrid axes.
    plot = p.plots[field]
    plot.figure = fig
    plot.axes = grid[i].axes
    plot.cax = grid.cbar_axes[i]

    # Since there are only two colorbar axes, we need to make sure we don't try
    # to set the temperature colorbar to cbar_axes[4], which would if we used i
    # to index cbar_axes, yielding a plot without a temperature colorbar.
    # This unnecessarily redraws the Density colorbar three times, but that has
    # no effect on the final plot.
    #if field == "rho":
    #    plot.cax = grid.cbar_axes[0]
    #elif field == "temperature":
    #    plot.cax = grid.cbar_axes[1]

    # Finally, redraw the plot.
    p._setup_plots()

plt.savefig(savepath + "HD_BU0_3d.pdf")
