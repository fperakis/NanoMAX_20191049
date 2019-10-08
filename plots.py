import h5py
import numpy as np
import matplotlib.pyplot as plt
plt.ion()

scans = (4, 10, 11)

fig, ax = plt.subplots(ncols=5, nrows=3, figsize=(10, 6))
plt.subplots_adjust(left=.05, top=.9, bottom=.01, right=.99, hspace=.1, wspace=.1)

for i, scan in enumerate(scans):
	with h5py.File('%06u.h5' % scan, 'r') as fp:
		for ii, j in enumerate((0, 5, 10, 15, 20)):
			data = fp['entry/measurement/pilatus/%06u' % j][:, :, :200]
			data = np.mean(data, axis=0)
			ax[i, ii].imshow(np.log10(data), vmin=0, vmax=4)
			plt.setp(ax[i, ii], xticks=[], yticks=[])

for i in range(5):
	ax[0, i].set_title('position %u' % i, fontsize=18)

ax[0, 0].set_ylabel('in focus', fontsize=18)
ax[1, 0].set_ylabel('400 um out', fontsize=18)
ax[2, 0].set_ylabel('1 mm out', fontsize=18)

plt.savefig('plots.png')