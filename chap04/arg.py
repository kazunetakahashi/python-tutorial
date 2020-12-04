def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def keyword_only_arg(*, arg):
    print(arg)

def combined(pos_only, /, standard, *, keyword_only):
    print(pos_only, standard, keyword_only)

standard_arg(2)
standard_arg(arg=2)

pos_only_arg(2)
# pos_only_arg(arg=2)

# keyword_only_arg(2)
keyword_only_arg(arg=3)

combined(1, 2, keyword_only=3)
combined(1, standard=2, keyword_only=3)

numbers = [(1, 'One'), (2, 'Two'), (3, 'Three'), (4, "Four")]
numbers.sort(key=lambda pair: pair[1])
print(numbers)
