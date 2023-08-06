
card=list(range(10000000,0,-1))
query=1
# using Linear search
output=9999999

# output=log(10000000)
output=7

import binary_search

# print(binary_search.locate_card(card,query))
# for searching in an array of size 100000000 linaer algo tok a time of 13.036 seconds


print(binary_search.binary_search_method(card,query))


# for searching in an array of size 100000000 linaer algo tok a time of 2.886 seconds in tehe worst case {Element is not present in the array}