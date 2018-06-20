import os

import matplotlib.pyplot as plt

from statistics_server import paths


def generate_plot(pid, output_path, start=None, end=None):
    file_path = os.path.join(paths.DATA_DIR, pid + ".txt")

    with open(file_path, 'r') as fp:
        x = []
        y = []

        for line in fp.readlines():
            runtime, user, pid, cpu, mempct, virt, real, tt, status, time, cputime, cmd = line.split(
                ',')
            runtime_seconds = float(runtime)

            if start is not None and runtime_seconds < start:
                continue

            if end is not None and runtime_seconds > end:
                continue

            mem_mb = float(virt) / 1024 / 1024
            runtime_minutes = runtime_seconds / 60

            x.append(runtime_minutes)
            y.append(mem_mb)

        plt.xlabel('Runtime (Minutes)')
        plt.ylabel('Memory (MB)')
        plt.plot(x, y)
        plt.savefig(output_path)