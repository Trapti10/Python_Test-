
# Ramesh and Suresh playing a simple game. they have to put some number of Stones from one place to another and started doing their work. They decided, they end up with a fun challenge who will put the last Stone.

# They to follow a simple rule, In the i'th round, Ramesh puts i stones whereas Suresh puts ix2 stones.
# There are only N stones, you need to help find the challenge result to find who put the last stone.

# Input:
# The first line contains an integer N.

# Output:
# Output Ramesh(without the quotes) if Ramesh puts the last Stones, "Suresh"(without the quotes) otherwise.

# Example:
# Input:
# 13

# Output:
# Suresh

# Explanation:
# 13 Stones are there :
# Ramesh Suresh
# 1 2
# 2 4
# 3 1 ( Only 1 remain)
# Hence, Suresh puts the last one.

n = int(input("Enter number of stones: "))
i = 1

while n > 0:
    n1 = i       
    n2 = 2 * i  

   
    if n - n1 <= 0:
        print("Ramesh")
        break
    n -= n1

  
    if n - n2 <= 0:
        print("Suresh")
        break
    n -= n2

    i += 1

 