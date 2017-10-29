import MapReduce
import sys

"""
Unique Trims in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: sequence_id
    # value: nucleotides
    sequence_id = record[0]
    nucleotides = record[1]

    if len(nucleotides) > 10:
        trimmed_nucleotides  = nucleotides[:-10]
        mr.emit_intermediate(trimmed_nucleotides, sequence_id) #value doesn't matter


def reducer(key, list_of_values):
    # key: trimmed_nucleotides
    # value: list of source sequence_id

    #print all unique trimmed
    mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
