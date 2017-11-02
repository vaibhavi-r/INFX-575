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
    combined_name =(pair[0], pair[1])  #alphabetic ordering
    #print(combined_name)

    mr.emit_intermediate((person, friend), 1)
    mr.emit_intermediate((friend, person), 1)


def reducer(key, list_of_values):
    # key: person,friend pair
    # value: list of 1s

    if len(list_of_values) < 2:
         mr.emit(key)

    #elif len(list_of_values)> 1 :
    #    print("Mutual Friends - ", key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
