# All possible top-ups
topups = [100, 90, 80, 50,
          45, 40, 35, 30,
          25, 20, 15, 10,
          5]

# Their prices on ShopTo.net
costs = [88.05, 76.29, 68.45, 41.99,
         39.04, 35.13, 30.23, 26.31,
         22.39, 18.47, 13.57, 9.65,
         4.75]

assigned = dict(zip(topups, costs))

def combos(balance = 100, choices = topups, current = []): # Create all combinations
    for x in choices:
        if balance >= x: # if target not exceeded
            if balance == x: # target reached
                if sorted(current + [x]) not in matches: # sort to avoid duplicates - RATE-LIMITING STEP
                    matches.append(sorted(current + [x])) # append sorted combo
            else: # If below target
                combos(balance - x, [y for y in choices if y <= balance - x], current + [x]) # filtering choices improves performance

def lowest(matches): # Calculate cheapest match
    minPrice = None
    minList = None
    for elem in matches: # Checks each combo
        cost = sum([assigned[y] for y in elem]) # Calculates combo's price
        # print(cost)
        if minPrice == None or cost < minPrice: # If cheapest
            minPrice, minList = cost, elem

    # Presentation, after best combo found
    print(f'== BEST COMBINATION FOR £{target} ==')
    for i in set(minList):
        print(f'{minList.count(i)} × £{i} costs £{minList.count(i) * assigned[i]:.2f}') # How many of each to buy
    print(f'\nTotal cost: £{minPrice:.2f}') # Rounded to two decimal places
    print(f'Money saved: £{target - minPrice:.2f} ({100 * (1 - minPrice / target):.2f}%)\n') # Saving

while True: # Loop continually
    matches = []
    print("--------------------------")
    target = int(input('Desired total (multiple of 5): ')) # Custom target

    combos(target, [q for q in topups if q <= target]) # Ascertain all possible combinations of top-ups for a given value
    print(f'{len(matches)} possible combinations.\n')
    lowest(matches)
