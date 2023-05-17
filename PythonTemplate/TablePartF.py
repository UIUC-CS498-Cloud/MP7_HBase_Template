import happybase as hb

# DON'T CHANGE THE PRINT FORMAT, WHICH IS THE OUTPUT
# OR YOU WON'T RECEIVE POINTS FROM THE GRADER

#1. update the data in a particular cell using the put() method
#2. retrieve all versions of all columns, with the most recent version coming first
                                                                                     
row = ???
for ???, ??? in row.items():

    cells = ???
    for ???, ??? in cells:
        print("row: {}, column family:qualifier: {}, value: {}, timestamp: {}".format(???, ???, ???, ???))


