import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

fig = plt.figure()
ax = fig.add_subplot(111)

## the data
perfomance = [1900.3, 1068, 2048.3, 3617.6, 3462.6]
devNumber =  [1, 2, 3, 4, 5]
N = 5

ind = np.arange(N)
width = 0.5

ax.bar(ind, perfomance, width, color='blue')

# axes and labels
ax.set_xlim(-width, len(ind))
ax.set_ylim(0, 3700)
ax.set_ylabel(r'Perfomance ($10^6$ nodes / s)')
#ax.set_title('Device type')
xTickMarks = ['1 CPU', '1 GPU', '2 GPU', '2 CPU', '1 CPU\n3 GPU']
ax.set_xticks(ind + width / 2)
xtickNames = ax.set_xticklabels(xTickMarks)
plt.setp(xtickNames, rotation=0, fontsize=16)

#plt.show()

filename = 'hist.pdf'
pp = PdfPages(filename)
plt.savefig(pp, format='pdf')
pp.close()