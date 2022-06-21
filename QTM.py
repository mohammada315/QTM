#!/usr/bin/env python3
import sys
from decimal import Decimal


def format_float(f):
    return "{0:f}".format(Decimal(f).quantize(Decimal("1.0000000")).normalize())


def main(infile, outfile):
    with open(infile) as ins:
        inputs = ins.read()

    lines = []
    for line in inputs.split("\n"):
        if not line or line.startswith("#"):
            continue
        vehicle_id, component_id, name, value, type = line.split("\t")
        v = value
        if type == "9":
            v = format_float(float(value))
        lines.append(f"{name},{v}\n")

    with open(outfile, "wt") as outs:
        outs.writelines(lines)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
