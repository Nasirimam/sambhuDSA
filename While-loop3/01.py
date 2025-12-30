# Write a java program to take a user input and print each
# digits of the number one by one from right to left.
# Input:
# N=43705;
# Output:5 0 7 3 4

i = 43705

while i > 0:
    print(i % 10)
    i = i // 10
