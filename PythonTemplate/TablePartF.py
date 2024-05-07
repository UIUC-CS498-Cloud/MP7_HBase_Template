import happybase as hb

# DON'T CHANGE THE PRINT FORMAT, WHICH IS THE OUTPUT
# OR YOU WON'T RECEIVE POINTS FROM THE GRADER

#1. update the data in a particular cell using the put() method
#2. retrieve all versions of all columns, with the most recent version coming first

# The solution to this part should be fairly straightforward if the right functions are used in the loops below. There should be no need to
# manually sort the results to be printed. 
# If your solution requires you to sort your results, we are expecting the following order of rows:
# color(updated), color(original), hero, power, name, xp
                                                                                     
row = ???
for ???, ??? in row.items():

    cells = ???
    for ???, ??? in cells:
        print("row: {}, column family:qualifier: {}, value: {}, timestamp: {}".format(???, ???, ???, ???))


