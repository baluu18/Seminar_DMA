import numpy
import glob, os

# settings
load_max_files = 3
max_rows = 100

class GrainsizeSet(object):
    name = ""
    data = []

    # def __init__(self, name, data):
    #     self.name = name
    #     self.data = data



# declare global variables
grainsize_sets = []
selected_files = []
index = 0

# Look for dat files
for root, dirs, files in os.walk("U:/Other_Stuff/Seminar_DMA/dem_reach/"):

    # Get data for each file
    for file in files:
        if file.endswith(".dat") and (index < load_max_files):

            index += 1

            filename = os.path.join(root, file)
            print(filename)

            data = numpy.genfromtxt(filename, delimiter=' ', max_rows=max_rows)
            grainsize_set = GrainsizeSet()
            grainsize_set.name = os.path.basename(file)
            grainsize_set.data = data

            print("Loaded" + filename)

            grainsize_sets.append(grainsize_set)

    print("finished")