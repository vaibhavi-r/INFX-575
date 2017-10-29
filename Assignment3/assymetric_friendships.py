import MapReduce
import sys

"""
Assymetric Friend Count in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: person
    # value: friend of person
    person = record[0]
    friend = record[1]

    pair = [person, friend]
    pair.sort()
    combined_name = pair[0] + pair[1]

    mr.emit_intermediate(combined_name, record)

def reducer(key, list_of_values):
    # key: person,friend pair
    # value: list of records of their friendship

    if len(list_of_values) ==1:
        record = list_of_values[0]
        A = record[0]
        B = record[1]
        mr.emit((B,A))
    else:
        print("Symmetric")

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
