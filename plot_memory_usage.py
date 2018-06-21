#!/bin/env python

import sys

from statictics_server import plotter


if __name__ == "__main__":
    plotter.generate_plot(sys.argv[1], sys.argv[2])

