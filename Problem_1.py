# Davos wants to build a game and he wants to build a staircase in the game.
# The staircase must be in the form of

#
##
###
####

n  = int(input("Enter number: "))

for i in range(1, n+1):
    print(i * "#")
    