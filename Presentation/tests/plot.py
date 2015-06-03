import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.backends.backend_pdf import PdfPages

argc = len(sys.argv)

if argc < 3:
  print('\nERROR! Specify command line arguments in a correct way.')
  print('USAGE: draw_plots_to_pdf file1 file2 ... outputfile\n')
  sys.exit()

inputFileCount = argc - 1

for i in range(1, inputFileCount):
  x = []
  y = []
  for str in open(sys.argv[i], 'r'):
    coords = str.split(" ")
    x.append(coords[0])
    y.append(coords[1])
  
  #plt.title('1 CPU')
  plt.xlabel('2-d grid linear size (nodes)')
  plt.ylabel(r'Perfomance ($10^6$ nodes / s)')
  
  #plt.plot(x, y, label=sys.argv[i].split(".")[0])
  
  
  #plt.plot(x, y)
  plt.plot(x, y, 'o-', label=sys.argv[i].split(".")[0])
  x = np.linspace(0, 10)
  
ax = plt.gca()
ax.set_xscale('log')

# show legend
legend = plt.legend(loc='upper left', shadow=True, prop={'size':16})
legend.get_frame().set_facecolor('#ffffff')

# export to pdf
filename = '' + sys.argv[argc - 1] + '.pdf'
pp = PdfPages(filename)
plt.savefig(pp, format='pdf')
pp.close()

print('\nFinished\n')