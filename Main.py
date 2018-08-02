import numpy as np
import glob, os

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
usecols = range(4, 13)


# Look for dat files
for root, dirs, files in os.walk("U:/Other_Stuff/Seminar_DMA/dem_reach/"):

    # Get data for each file
    for file in files:
        if file.endswith(".dat") and (index < load_max_files):

            index += 1

            filename = os.path.join(root, file)
            print("Loading: " + filename)

            data = np.genfromtxt(filename, delimiter=' ', max_rows=max_rows, usecols=usecols)
            grainsize_set = GrainsizeSet()

            print ("Processing: " + grainsize_set.name)

            # load one column
            column = np.array(data)
            total_row = data[:,0]
            calculated = column / total_row[:,None] * 100

            # add to grainsize collection
            grainsize_set.name = os.path.basename(file)
            grainsize_set.absolute = data
            grainsize_set.relative = calculated
            scenarios.append(grainsize_set)

    #print("finished")

print("finished")

# print("Find max for each column")
#
# for scenario in scenarios :
#     scenario.