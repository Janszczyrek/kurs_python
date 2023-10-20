#!/usr/bin/env python3

line = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n\
Nulla tristique arcu eget orci rutrum, eget condimentum magna dapibus.\n\
Nunc non risus quis nisi laoreet interdum.\n\
Integer ut lacus fringilla, faucibus diam non, accumsan odio.\n\
Donec id malesuada nisl, sed consectetur erat.\n\
Quisque in velit sit amet dui euismod dapibus nec at velit.\n\
Maecenas varius aliquet tincidunt.\n\
Quisque consectetur vitae ante a tincidunt.\n\
Aenean molestie nisi GvRnec laoreet pulvinar.\n\
Proin sed pellentesque ligula, in pretium augue.\n\
Vestibulum sed ullamcorper ipsum.'

word = "Hello"

L = [43, 53, 1, 34, 32, 65, 123]

# 2.10
print(len(line.split()))

# 2.11
print("".join([x + "_" for x in word])[0:-1]) 

# 2.12
print("".join([x[0] for x in line.split()]))
print("".join([x[-1] for x in line.split()]))

# 2.13
print(sum([len(x) for x in line.split()]))

# 2.14
print(max(line.split(),key=len))
print(max(len(x) for x in line.split()))

# 2.15
print("".join([str(x) for x in L]))

# 2.16
print(line.replace("GvR", "Guido van Rossum"))

# 2.17
print(" ".join(sorted(line.split(), key=str.lower)))
print(" ".join(sorted(line.split(), key=len)))

# 2.18
print(str(160000200003000040000).count('0'))

# 2.19
print([str.zfill(str(x),3) for x in L])