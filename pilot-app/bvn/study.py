from matplotlib import pyplot

machine_counts = [18,4,2]

machine_names = ['pc','mac','linux']

pyplot.pie(machine_counts, labels = machine_names)

pyplot.show()