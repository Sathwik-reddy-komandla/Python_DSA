# return tehe position of the query element in the cards list
tests=[]

tests.append({
    'input':{
    'cards':[13,12,10,7,4,3,1,0],
    'query':7
    },
    'output':3
})

tests.append({
    'input':{
    'cards':[13,12,10,7,4,3,1,0],
    'query':10
    },
    'output':2
})

tests.append({
    'input':{
    'cards':[13,12,10,7,4,3,1,0],
    'query':13
    },
    'output':0
})


tests.append({
    'input':{
    'cards':[13,12,10,0,-4,-13,-21,-30],
    'query':0
    },
    'output':3
})


tests.append({
    'input':{
    'cards':[2,0,-2,-4,-13,-21,-30],
    'query':-30
    },
    'output':6
})


tests.append({
    'input':{
    'cards':[],
    'query':0
    },
    'output':-1
})

tests.append({
    'input':{
    'cards':[2,0,-2,-4,-13,-21,-30],
    'query':-1
    },
    'output':-1
})


tests.append({
    'input':{
    'cards':[2,2,0,0,0,-1,-2,-2,-4,-13,-21,-30],
    'query':-4
    },
    'output':8
})


tests.append({
    'input':{
    'cards':[2,0,-2,-2,-2,-4,-13,-21,-30],
    'query':-2
    },
    'output':2
})

# test cases
'''
1=> Some where in the middle
2=> first ele
3=> last ele
4=> only one ele
5=> list is empty
6=> repetaing eles
7=> query is repeating
8=> does not contain
'''


'''
BRUTE FORCE APPROACH
'''
# def locate_card(cards,query):
#     len_inputs=len(cards)
#     if len_inputs>0:
#         if query in cards:
#             return cards.index(query)
#         else:
#             return -1
#     else:
#         return -1 

# num_times=0
def locate_card(cards,query):
    global num_times
    position=0
    while position<len(cards):
        num_times+=1
        if cards[position] ==query:
                return position
        position+=1
    return -1 

# for test in tests:  
#     print(test)
#     print(locate_card(**(test['input'])),test['output'])
#     print("num times Looped is :",num_times)
#     print('*'*10)


# print(num_times)

# The runtime of the Brute Force Algorithm is of order O(N)
'''
Lets try an Efficient Method
=> Binary Search Method
'''

def binary_search_method(cards,query):
    lo,hi=0,len(cards)-1
    while lo<=hi:
        mid=(lo+hi)//2
        mid_number=cards[mid]
        print("lo :",lo, " hi :",hi," mid : ",mid," mid_number :",mid_number)
        if mid_number==query:
            if mid-1>0 and cards[mid-1]==query:
                hi=mid-1
            else:
                return mid
        elif mid_number<query:
            hi=mid-1
        else:
            lo=mid+1
    return -1

for test in tests:
    print(binary_search_method(**test['input']),test['output'])
    
#  This method takes time of the order O(logn)