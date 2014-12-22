from __future__ import print_function, division
from pylab import rcParams
import seaborn as sns
sns.set(style="white")

def _mm_to_inches(*mms):
    return [mm / 25.4 for mm in mms]

FONTSIZE = 8
params = {'figure.figsize': _mm_to_inches(180, 80), # 180 or 88mm wide for Scientific Data
          'axes.labelsize': FONTSIZE, # FONTSIZE for x and y labels (was FONTSIZE)
          'axes.titlesize': FONTSIZE,
          'text.fontsize': FONTSIZE, # was FONTSIZE
          'legend.fontsize': FONTSIZE, # was FONTSIZE
          'xtick.labelsize': FONTSIZE,
          'ytick.labelsize': FONTSIZE,
          'font.family': 'Bitstream Vera Sans'
}

rcParams.update(params)


def format_axes(ax):
    for axis in [ax.xaxis, ax.yaxis]:
        axis.set_tick_params(direction='out', color='k', size=4)    

    return ax
