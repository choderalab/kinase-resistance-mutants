#!/bin/env python

import numpy as np
import sys

filename = sys.argv[1]
times = np.loadtxt(filename)
nodes_reporting = len(times)
nodes_requested = 200
print(times)
mean_time = times.mean()
ns_per_day = 0.005 / mean_time * 24 * 60 * 60
print('%d nodes reporting an average time/iteration of %.3f s (%.3f ns/day) : %.3f ns/day aggregate (%.3f%% of perfect scaling)' % (nodes_reporting, mean_time, ns_per_day, ns_per_day * nodes_reporting, 100*nodes_reporting/float(nodes_requested)))
