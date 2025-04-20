#!/bin/python3

import math
import sys

def calculate_rsr(size_meters):
    if size_meters <= 0:
        raise ValueError("Ship size must be greater than 0 meters.")
    return 42 - 10 * math.log10(size_meters)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python rsr_calc.py <ship_size_in_meters>")
        sys.exit(1)

    try:
        size = float(sys.argv[1])
        rsr = calculate_rsr(size)
        print(f"Ship Size: {size} meters")
        print(f"RSR: {rsr:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
