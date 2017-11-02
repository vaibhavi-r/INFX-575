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

    m = 5 #Rows in A
    p = 5 #Cols in B

    c_key = 1

    #Send each row of A to multiple reducers
    if source== "a":
        for k in range(p): #number of cols in C
            c_key = (i,k)
            mr.emit_intermediate(c_key, record)

    #Send each column of B to multiple reducers
    if source =="b":
        for k in range(m): #number of rows in C
            c_key = (k,j)
            mr.emit_intermediate(c_key, record)

def reducer(key, list_of_values):
    # key:  tupleof form (i,j) addressing cell in result matrix
    # value: all elements from A of form A[i][*] and from B of form B[*][j]

    A = {}
    B = {}

    for record in list_of_values:
        source = record[0]
        i = record[1]
        j = record[2]
        value = record[3]

        if source =="a":
            A[j]= value  #storing by col, all are from same row
        elif source =="b":
            B[i]= value #indexing by row, all are from same col


    n = 5  # Cols in A  = Rows in B
    sum = 0
    for k in range(n):
        if k not in A or k not in B:
            sum+=0
        else:
            sum+= A[k]*B[k]

    #Separate out row, col
    i,j = key
    mr.emit((i,j, sum))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
