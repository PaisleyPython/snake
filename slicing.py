# SLICING

# manipulating lists and tuples.

piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
piano_tuple = ("do", "re", "me", "fa", "so", "la", "ti", "do")


# It's important to remeber that the slicing happens between the
# items in the list. So 0 is just before a, and 1 is inbetween a and b.. etc

print(piano_keys[2:5])  # This prints ["c", "d", "e"]
print(piano_keys[2:])  # This prints "c" through to the end.
print(piano_keys[:5])  # This prints everything up to pos 5.
print(piano_keys[2:5:2])  # Adding a third number sets the increment.
print(piano_keys[::2])  # This prints every 2nd item.
print(piano_keys[::-1])  # This reverses the list in it's entirety

# The slicing works exactly the same for the tuples.
print(piano_tuple[2:5])  # This prints 'me', 'fa', 'so'
