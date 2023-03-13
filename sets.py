#!/usr/bin/env python3.10
#Reference URL: https://www.youtube.com/watch?v=vzGllw18DkA&t=257s - 3:25:50

# If you don't care about the order of the elements and you know the values will be unique, you can use a set.
s = set()

s.add(1)
s.add(2)
s.add(3)
s.add(4)

# Even though I add 3 again to the set, it does not show up twice when I run the program. In math, no element shows up more than once in a set.
s.add(3)

s.remove(2)

print(s)

print(f"The set has {len(s)} elements.")