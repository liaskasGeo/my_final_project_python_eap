#     *        4spaces 1asterisk
#    ***       3kena   3asterisks
#   *****      2kena   5asterisks
#  *******     1keno   7a
# *********    0kena   9a
#odd = 2n+1

N = 5

for i in range(N):
    print("  " * (N-i-1),end="")
    print("* " * (2*i+1),end="")
    print("")
