#!/bin/env python

import matplotlib.pyplot as plt
import random
import sys
import numpy


def plotfile(filepath, outpath):
    with open(filepath, 'r') as fp:
        x = []
        y = []

        for line in fp.readlines():
            runtime, user, pid, cpu, mempct, virt, real, tt, status, time, cputime, cmd = line.split(
                ',')
            mem_mb = float(virt) / 1024 / 1024
            runtime_minutes = float(runtime) / 60

            if runtime < 100:
                continue

            x.append(runtime_minutes)
            y.append(mem_mb)

        plt.xlabel('Runtime (Minutes)')
        plt.ylabel('Memory (MB)')
        plt.plot(x, y)
        plt.savefig(outpath)


plotfile(sys.argv[1], sys.argv[2])
