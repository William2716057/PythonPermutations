
def perms(lst):

    #check if list is empty
    if len(lst)  == 0:
        return[[]]

    #check if there is only one item in list and return one
    if len(lst) == 1:
        return [lst]

    #list to store permutations
    a = []

    #iterations
    for i in range(len(lst)):

        index = lst[i]

        #get lst[i] or a from list
        remaining = lst[:i] + lst[i+1:]

        #generate all permutations 
        for p in perms(remaining):
            a.append([index] + p)
    return a

inputs = list('123456')
for p in perms(inputs):
    print(p)



