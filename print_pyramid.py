# Implement a program that prints out a half-pyramid of a specified height.

# Example: pyramid(6)
# input: (6) number of levels high
# output:
     #
    ##
   ###
  ####
 #####
######


# Challenge
# Implement a program that prints out a full-pyramid of a specified height.

# Example: pyramid(6)
# input: (6) number of levels high
# output:
     # #
    ## ##
   ### ###
  #### ####
 ##### #####
###### ######


# *** your code here ***

def pyramidder(num):
    counter = 1
    while counter <= num:
        print(" " * (num - counter) + "#" * counter, "#" * counter + " " * (num - counter))
        counter += 1

pyramidder(1)
pyramidder(9)
