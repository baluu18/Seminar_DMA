import numpy as np
import glob, os
import numpy as np
import matplotlib.pyplot as plt

# packages:
# python 2.7.0
# numpy 1.15.0
# matplotlib 2.2.2

# settings
load_max_files = 3
max_rows = 100

class GrainsizeSet(object):
    name = ""
    data = []
    max_grainsizes = []

# declare global variables
scenarios = []
selected_files = []
index = 0
usecols = range(4, 14)


# Look for dat files
for root, dirs, files in os.walk("C:\LocalDrive\Seminar_DMA2\input"):

    # Get data for each file
    for file in files:
        if file.endswith(".dat") and (index < load_max_files):

            index += 1

            # get filename
            filename = os.path.join(root, file)
            print("Loading: " + filename)

            # load data
            data = np.genfromtxt(filename, delimiter=' ', max_rows=max_rows, usecols=usecols)
            grainsize_set = GrainsizeSet()
            grainsize_set.name = os.path.basename(file)

            print ("Processing: " + grainsize_set.name)

            # load one column
            column = np.array(data)
            total_row = data[:,0]
            calculated = column / total_row[:,None] * 100

            # create new plot
            fig, ax = plt.subplots()
            fig.set_size_inches(18.5, 10.5)
            x = np.arange(max_rows)

            # dashes format: 2pt line, 2pt break, 10pt line, 2pt break
            y = data[:,1]
            ax.plot(x, y, dashes=[2, 2, 10, 2], label='0.0001m')

            y = data[:, 2]
            ax.plot(x, y, dashes=[6, 2], label='0.005m')

            y = data[:, 3]
            ax.plot(x, y, dashes=[1, 1], label='0.02m')

            y = data[:, 4]
            ax.plot(x, y, dashes=[1, 1], label='0.04m')

            y = data[:, 5]
            ax.plot(x, y, dashes=[1, 1], label='0.08m')

            y = data[:, 6]
            ax.plot(x, y, dashes=[1, 1], label='0.12m')

            y = data[:, 7]
            ax.plot(x, y, dashes=[1, 1], label='0.2m')

            y = data[:, 8]
            ax.plot(x, y, dashes=[1, 1], label='0.4m')

            y = data[:, 9]
            ax.plot(x, y, dashes=[1, 1], label='1.5m')

            # add legend
            ax.legend()

            # save as image
            plt.savefig(os.path.join("C:\LocalDrive\Seminar_DMA2\output", grainsize_set.name + ".png"))

            # add to grainsize collection

            grainsize_set.absolute = data
            grainsize_set.relative = calculated
            scenarios.append(grainsize_set)

    #print("finished")

print("finished")

# print("Find max for each column")
#
# for scenario in scenarios :
#     scenario.