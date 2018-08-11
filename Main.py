import numpy as np
import glob, os
import numpy as np
import matplotlib.pyplot as plt

# packages:
# python 2.7.0
# numpy 1.15.0
# matplotlib 2.2.2

# settings
load_max_files = 1
max_rows = 8760*20  # 8760 -> 1y; 17520 -> 2y;  35040 -> 4y
load_cols = range(4, 14)
skiprows = 10
use_cols = range(0, 4)
max_rows = max_rows / skiprows

# declare custom objects
class GrainsizeSet(object):
    name = ""
    data = []

grainsizes = []
class Grainsize(object):
    name = ""
    scenario = ""
    max_grainsize = 0

labels = []
class Label(object):
    name = ""
    color = ""

# declare global variables
selected_files = []
index = 0

# chart style
defaultFontSize = 14
headerFontSize = 18

# define labels and colors for each column
label = Label()
label.name = "0.0001m"
label.color = "fuchsia"
labels.append(label)
label = Label()
label.name = "0.005m"
label.color = "purple"
labels.append(label)
label = Label()
label.name = "0.02m"
label.color = "blue"
labels.append(label)
label = Label()
label.name = "0.04m"
label.color = "cyan"
labels.append(label)
label = Label()
label.name = "0.08m"
label.color = "green"
labels.append(label)
label = Label()
label.name = "0.12m"
label.color = "gold"
labels.append(label)
label = Label()
label.name = "0.2m"
label.color = "orange"
labels.append(label)
label = Label()
label.name = "0.4m"
label.color = "red"
labels.append(label)
label = Label()
label.name = "1.5m"
label.color = "black"
labels.append(label)

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
            data = np.genfromtxt(filename, delimiter=' ', max_rows=max_rows*skiprows, usecols=load_cols)

            # filter data set
            data = data[0::skiprows]

            # create new grainsize set
            grainsize_set = GrainsizeSet()
            grainsize_set.name = os.path.basename(file)

            print ("Processing: " + grainsize_set.name)

            # load one column
            column = np.array(data)
            total_row = data[:,0]
            calculated = column / total_row[:,None] * 100

            # declare figure for plot charts
            fig, ax = plt.subplots()
            fig.set_size_inches(20.5, 12.5)

            # chart specific settings
            title = 'Absolute grainsize distribution during scenario ' + grainsize_set.name[:-4]

            # create new plot with absolute data (not calculated data=relative data)
            x = np.arange(max_rows)

            plt.ylabel('absolute amount of certain grainsize', fontsize=defaultFontSize)
            plt.xlabel('years', fontsize=defaultFontSize)
            plt.title(title, fontsize=headerFontSize)
            plt.xticks(np.arange(0, max_rows, step=8760/skiprows), np.arange(0, max_rows / (8760/skiprows)))

            # add data
            for count in use_cols:
                # skip the first column with total values
                y = data[:, count+1]
                ax.plot(x, y, color=labels[count].color, label=labels[count].name)

            # add legend
            ax.legend()

            # save as image
            plt.savefig(os.path.join("C:\LocalDrive\Seminar_DMA2\output", "absolute-" + grainsize_set.name + ".png"))

            # declare figure for plot charts
            fig, ax = plt.subplots()
            fig.set_size_inches(20.5, 12.5)

            # chart specific settings
            title = 'Relative grainsize distribution during scenario ' + grainsize_set.name[:-4]

            # create new plot with relative data (calculated data)
            x = np.arange(max_rows)

            plt.ylabel('% of certain grainsize', fontsize=defaultFontSize)
            plt.xlabel('years', fontsize=defaultFontSize)
            plt.title(title, fontsize=headerFontSize)
            plt.xticks(np.arange(0, max_rows, step=8760 / skiprows), np.arange(0, max_rows / (8760 / skiprows)))

            # add data
            for count in use_cols:
                # skip the first column with total values
                y = calculated[:, count+1]
                ax.plot(x, y, color=labels[count].color, label=labels[count].name)

            # add legend
            ax.legend()

            # save as image
            plt.savefig(os.path.join("C:\LocalDrive\Seminar_DMA2\output", "relative-" + grainsize_set.name + ".png"))

            # clear figure
            plt.close('all')

            # get max value for each grainsize column
            for count in use_cols:
                grainsize = Grainsize()
                grainsize.name = labels[count-1].name
                grainsize.scenario = grainsize_set.name
                grainsize.max_grainsize = np.max(data[:, count])
                grainsizes.append(grainsize)


print("finished")
