def power_set(s):
    
    if len(s) == 0:
        return [[]]  # if s is an empty set, its power set is a set containing the empty set
    else:
        elem = s[0]
        rest = s[1:]
        ps = power_set(rest)
        return ps + [[elem] + subset for subset in ps]

user_input = input("Enter a set of elements separated by commas: ")
s = user_input.split(",")  

ps = power_set(s)
print("Power set of", s, "is:")
for subset in ps:
    print(subset)
    
    
    
OUTPUT:
    Enter a set of elements separated by commas: 1,2,3
Power set of ['1', '2', '3'] is:
[]
['3']
['2']
['2', '3']
['1']
['1', '3']
['1', '2']
['1', '2', '3']
