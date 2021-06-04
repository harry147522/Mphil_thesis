import matplotlib.pyplot as plt
import yt
import numpy as np
import matplotlib.gridspec as gridspec
from mpl_toolkits.axes_grid1 import AxesGrid
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica'],'size':15})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)

def gamma(field, data):
    return  np.sqrt( 1.0 + (data['W_vel1']**2 + data['W_vel2']**2 + data['W_vel3']**2) )
def veloc1(field, data):
    return data['W_vel1'] / data['gamma']
def veloc2(field, data):
    return data['W_vel2'] / data['gamma']
def veloc3(field, data):
    return data['W_vel3'] / data['gamma']

# Load the dataset
ds_initial = yt.load('output0000.dat', unit_system='code')
ds_initial.add_field( ('amrvac','gamma'), function=gamma, sampling_type='cell')
ds_initial.add_field( ('amrvac','veloc1'), function=veloc1, sampling_type='cell')
ds_initial.add_field( ('amrvac','veloc2'), function=veloc2, sampling_type='cell')
ds_initial.add_field( ('amrvac','veloc3'), function=veloc2, sampling_type='cell')
x_projection_initial= yt.LineBuffer( ds_initial, (-15.0,0.0,0.0), (15.0,0.0,0.0), 256 )
y_projection_initial= yt.LineBuffer( ds_initial, (0.0,-15.0,0.0), (0.0,15.0,0.0), 256 )
z_projection_initial= yt.LineBuffer( ds_initial, (0.0,0.0,-15.0), (0.0,0.0,15.0), 256 )

ds_final = yt.load('output0987.dat', unit_system='code')
ds_final.add_field( ('amrvac','gamma'), function=gamma, sampling_type='cell')
ds_final.add_field( ('amrvac','veloc1'), function=veloc1, sampling_type='cell')
ds_final.add_field( ('amrvac','veloc2'), function=veloc2, sampling_type='cell')
ds_final.add_field( ('amrvac','veloc3'), function=veloc2, sampling_type='cell')
x_projection_final= yt.LineBuffer( ds_final, (-15.0,0.0,0.0), (15.0,0.0,0.0), 256 )
y_projection_final= yt.LineBuffer( ds_final, (0.0,-15.0,0.0), (0.0,15.0,0.0), 256 )
z_projection_final= yt.LineBuffer( ds_final, (0.0,0.0,-15.0), (0.0,0.0,15.0), 256 )

fig, axs = plt.subplots(3,1, sharex='col',sharey='row')
# x projection
axs[0].plot(x_projection_initial[('amrvac', 'x')], x_projection_initial[('amrvac', 'rho')], color='black', linestyle='-', linewidth = 1)
axs[0].plot(x_projection_final[('amrvac', 'x')], x_projection_final[('amrvac', 'rho')],'r.',markersize=3)
axs[0].set_xlim(-15.0, 15.0)
axs[0].set( xlabel='$x$')
axs[0].set( ylabel='$\\rho$')
axs[0].set_yscale('log')
axs[0].grid(True)

# y projection
axs[1].plot(y_projection_initial[('amrvac', 'y')], y_projection_initial[('amrvac', 'rho')], color='black', linestyle='-', linewidth = 1)
axs[1].plot(y_projection_final[('amrvac', 'y')], y_projection_final[('amrvac', 'rho')],'r.',markersize=3)
axs[1].set_xlim(-15.0, 15.0)
axs[1].set( xlabel='$y$')
axs[1].set_yscale('log')
axs[1].set( ylabel='$\\rho$')
axs[1].grid(True)

# z projection
axs[2].plot(z_projection_initial[('amrvac', 'z')], z_projection_initial[('amrvac', 'rho')], color='black', linestyle='-', linewidth = 1)
axs[2].plot(z_projection_final[('amrvac', 'z')], z_projection_final[('amrvac', 'rho')],'r.',markersize=3)
axs[2].set_xlim(-15.0, 15.0)
axs[2].set( xlabel='$z$')
axs[2].set_yscale('log')
axs[2].set( ylabel='$\\rho$')
axs[2].grid(True)

fig.tight_layout()

plt.subplots_adjust(hspace=0.3, wspace=0.0)

plt.savefig('../../fig_HD_BU0_3d_slices.pdf', bbox_inches="tight")
