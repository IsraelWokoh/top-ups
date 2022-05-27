# Purpose
On [ShopTo.net](https://www.shopto.net/en/sony-wallet-topup/), top-up cards (with values ranging from £5 to £100) for the PlayStation Store can be bought at a discount from their nominal price. However, the discount isn't consistent across the board, meaning that the savings aren't consistent depending on the amount you choose to top-up your Wallet with AND the combination of cards you buy.

This program solves that for you.

# Getting it working
No additional files required!

The only thing you will probably need to do is change the prices in the list `costs`. It's simple, though. The cost of `topups[x]` = `costs[x]`. I've ordered the top-up values in descending order by default, but they can be changed around. All that matters is that the corresponding top-up and cost are in the same index of `topups` and `costs`.

**It is *imperative* that this is done carefully.**

## How to use it
Just input the amount you to wish to top-up your Wallet with (no currency signs!) and let the program work it out for you. It'll tell you the cost of what you're buying, and how much you're saving, both in cash and as a percentage of the standard price.

This will continually loop until you close the program.

# Things to watch out for
- This only works for **multiples of £5**.
	- I will update this so it works for any positive non-zero input up to two decimal points, even non-integral inputs.

- No exception handling. I mean, I'll implement it later, but you can input a number correctly, right? :P

- Massive slowdown past £100 or so. Without removing duplicates, adding another £5 doubles the combinations. (£90 gives 130K combinations, £105 gives 1.04M, £120 gives 8.3M.)
	- If I don't dedupe `matches` (containing all combinations), it slows down `lowest()` in calculating the total cost of each combination in `matches` because there are **so many** redundant ones.
	- Even if I dedupe `matches`, which shrinks `len(matches)` by _several orders of magnitude_, that just slows it down in a different place by a similar amount. I'll run loop testing to see which is faster. I imagine the latter would place less strain on memory, so I'll default to that method.
	- Maybe running it on a 12-inch MacBook (2017) with a 1.4GHz Dual-Core i7 is the actual problem...

# Future
I'm considering making a separate revision that scrapes [ShopTo.net](https://www.shopto.net/). Benefits would be threefold:

- Bonus points for functional complexity!
- QoL: the user wouldn't have to hard code in the current values (they change regularly).
- Erases possibility for human error messing up the code itself when adjusting `costs`.
