import numpy as np
import matplotlib.pyplot as plt

def make_some_data_i_believe(x, a, f, po):
    return a*np.sin(2 * np.pi * x * f + po)

x = np.linspace(0, 2, 1000)

plt.style.use('dark_background')

fig, ax = plt.subplots()

ax.plot(x, make_some_data_i_believe(x, 0.3, 1, 0))
ax.plot(x, make_some_data_i_believe(x, 0.2, 2, np.pi/2), linestyle='--')
ax.plot(x, make_some_data_i_believe(x, 0.15, 3, 0), linestyle=':')
ax.plot(x, make_some_data_i_believe(x, 0.1, 4, np.pi/2), linestyle='-.')

ax.minorticks_on()
ax.xaxis.set_ticks_position('both')
ax.yaxis.set_ticks_position('both')
ax.tick_params(axis='x',which='major',direction='in',length=5,labelsize=10)
ax.tick_params(axis='y',which='major',direction='in',length=5,labelsize=10)
ax.tick_params(axis='x',which='minor',direction='in',length=3,labelsize=10)
ax.tick_params(axis='y',which='minor',direction='in',length=3,labelsize=10)

plt.savefig('plot_example.pdf', transparent=True, bbox_inches='tight', dpi=300)
