import MapReduce
import sys

"""
Matrix Multiply in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: source matrix identifier
    # value: i, j , value  contents of matrix
    source = record[0]
    i = record[1]
    j = record[2]
#    value = record[3]

    n_row = 5
    n_col = 5

    #Send each row of A to multiple reducers
    if source== "a":
        for k in range(n_col):
            c_key = "row"+str(i) + "col"+str(k)
            mr.emit_intermediate(c_key, record)

    #Send each column of B to multiple reducers
    if source =="b":
        for k in range(n_row):
            c_key = "row"+str(k) + "col"+str(j)
            mr.emit_intermediate(c_key, record)

def reducer(key, list_of_values):
    # key:  index of form a1b2 addressing cell in result matrix
    # value: all elements from A of form A[i][*] and from B of form B[*][j]

    A = {}
    B = {}

    for record in list_of_values:
        source = record[0]
        i = record[1]
        j = record[2]
        value = record[3]

        if source =="a":
            A[j]= value #storing by k
        elif source =="b":
            B[i]= value #indexing by k

    n_row = 5
    n_col = 5







    # Send each row of A to multiple reducers
    if source == "a":
        for k in range(n_col):
            c_key = "a" + str(i) + "b" + str(k)
            mr.emit_intermediate(c_key, record)

    # Send each column of B to multiple reducers
    if source == "b":
        for k in range(n_row):
            c_key = "a" + str(k) + "b" + str(j)
            mr.emit_intermediate(c_key, record)

    total = 0
    for v in list_of_values:
      total += v
    mr.emit((key, total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
