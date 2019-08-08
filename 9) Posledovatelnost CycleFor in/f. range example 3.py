winners = ['Max', 'Leo', 'Kate']

# prostoi perebor
for winner in winners:
    print(winner)

# use the range
for i in range (1, len(winners)+1):
    print(i+1, ')', winners[i-1])