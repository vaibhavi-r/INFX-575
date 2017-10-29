import MapReduce
import sys

"""
Friend Count in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: person
    # value: person's friend
    person = record[0]
    friend = record[1]

    mr.emit_intermediate(person, friend)

def reducer(key, list_of_values):
    # key: person
    # value: list of friends

    total_friends = 0
    unique_friends = list(set(list_of_values))
    num_friends = len(unique_friends)

    mr.emit((key,num_friends ))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
