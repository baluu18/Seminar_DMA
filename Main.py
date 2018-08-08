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

            # create new plot with absolute data (not calculated data=relative data)
            fig, ax = plt.subplots()
            fig.set_size_inches(20.5, 12.5)
            x = np.arange(max_rows)
            plt.ylabel('% of certain grainsize', fontsize=14)
            plt.xlabel('years', fontsize=14)
            plt.title(grainsize_set.name, fontsize=18)
            plt.suptitle('Absolute grainsize distribution during scenario', fontsize=18)  # if Possible loop over scenarios name

            # dashes format: 2pt line, 2pt break, 10pt line, 2pt break
            y = data[:,1]
            ax.plot(x, y, color='fuchsia', label='0.0001m')

            y = data[:, 2]
            ax.plot(x, y, color='purple', label='0.005m')

            y = data[:, 3]
            ax.plot(x, y, color='blue', label='0.02m')

            y = data[:, 4]
            ax.plot(x, y, color='cyan', label='0.04m')

            y = data[:, 5]
            ax.plot(x, y, color='green', label='0.08m')

            y = data[:, 6]
            ax.plot(x, y, dashes=[2, 2, 10, 2], color='gold', label='0.12m')

            y = data[:, 7]
            ax.plot(x, y, color='orange', label='0.2m')

            y = data[:, 8]
            ax.plot(x, y, dashes=[2, 2, 10, 2], color='red', label='0.4m')

            y = data[:, 9]
            ax.plot(x, y, dashes=[2, 2, 10, 2], color='black', label='1.5m')

            # add legend
            ax.legend()

            # save as image
            plt.savefig(os.path.join("C:\LocalDrive\Seminar_DMA2\output", "absolute-" + grainsize_set.name + ".png"))



            # create new plot with relative data (calculated data)
            fig, ax = plt.subplots()
            fig.set_size_inches(20.5, 12.5)
            x = np.arange(max_rows)
            plt.ylabel('% of certain grainsize', fontsize= 14)
            plt.xlabel('years', fontsize=14)
            plt.suptitle('Relative grainsize distribution during scenario', fontsize=18)
            plt.title(grainsize_set.name, fontsize=18)

            # dashes format: 2pt line, 2pt break, 10pt line, 2pt break
            y = calculated[:, 1]
            ax.plot(x, y, color='fuchsia', label='0.0001m')

            y = calculated[:, 2]
            ax.plot(x, y, color='purple', label='0.005m')

            y = calculated[:, 3]
            ax.plot(x, y, color='blue', label='0.02m')

            y = calculated[:, 4]
            ax.plot(x, y, color='cyan', label='0.04m')

            y = calculated[:, 5]
            ax.plot(x, y, color='green', label='0.08m')

            y = calculated[:, 6]
            ax.plot(x, y, dashes=[2, 2, 10, 2], color='gold', label='0.12m')

            y = calculated[:, 7]
            ax.plot(x, y, color='orange', label='0.2m')

            y = calculated[:, 8]
            ax.plot(x, y, dashes=[2, 2, 10, 2], color='red', label='0.4m')

            y = calculated[:, 9]
            ax.plot(x, y, dashes=[2, 2, 10, 2], color='black', label='1.5m')

            # add legend
            ax.legend()

            # save as image
            plt.savefig(os.path.join("C:\LocalDrive\Seminar_DMA2\output", "relative-" + grainsize_set.name + ".png"))

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