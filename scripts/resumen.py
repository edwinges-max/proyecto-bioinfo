import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(output_file, "w") as f:
    f.write("id\tlongitud\n")
    f.write("seq1\t100\n")