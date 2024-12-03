import pandas as pd

for line in open("test_input.txt"):
    print(repr(line))

schematic = pd.read_table("test_input.txt", header=None, lineterminator="\n", delim_whitespace=True)
print(schematic)

