import MapReduce
import sys

"""
Relational Join in the Simple Python MapReduce Framework
Orders, LineItems
order, line_item
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: source table identifier
    # value: document contents
    source = record[0]
    order_id = record[1]

    mr.emit_intermediate(order_id, record)

def reducer(key, list_of_values):
    # key: order_id
    # value: list of records with order_id

    orders = []
    line_items = []

    for record in list_of_values:
        source = record[0]
        if source == "order":
            orders.append(list(record))
        elif source =="line_item":
            line_items.append(list(record))

    #print("ORDERS",len(orders) )
    #print("LINE ITEMS",len(line_items) )

    for order in orders:
        for item in line_items:
            mr.emit(order + item)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
