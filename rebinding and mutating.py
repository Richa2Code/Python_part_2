# Rebinding means what the variable starts to point to another object.

nums = [1, 2, 3]
nums = [10, 20, 30]

print(nums)

# Mutating means you changes the existing one instead of making new one 

lst = [1, 2, 3]
print(lst)
lst.append(44)
print(lst)

# here, list remain same only the elements are getting changed so this is what mutating looks like.

'''
If you see:

=

It is usually rebinding.

If you see methods like:

append()
remove()
pop()
clear()
sort()
reverse()
extend()

or

nums[0] = 100

It is mutating.
'''

one = [23, 1, 56, 78, 90, 34, 54, 22, 10]
print(one)
one.pop()
print(one)