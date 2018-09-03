# declaring lists
multiples_3 = []
multiples_5 = []
# declaring sets
set_3 = ()
set_5 = ()

# defining a function to obtain a list of multiples of 3 less than 1000
def multiples_of_3():
    num1 = 1
    while num1 < 1000:
        if num1%3==0:
            multiples_3.append(num1)
            num1+=1
            continue
        else:
            num1+=1
            continue
    print (multiples_3)

# defining a function to obtain a list of multiples of 5 less than 1000
def multiples_of_5():
    num1 = 1
    while num1 < 1000:
        if num1%5==0:
            multiples_5.append(num1)
            num1+=1
            continue
        else:
            num1+=1
            continue
    print (multiples_5)


# calling the function multiples_of_3

multiples_of_3()

# converting the list into a set to perform set operations
set_3 = set(multiples_3)
print(set_3)

# calling the function multiples_of_5
multiples_of_5()

# converting the list into a set to perform set operations
set_5 = set(multiples_5)
print(set_5)

# performing a union operation on the set to eliminate duplicates between 2 sets
new_set = set_3.union(set_5)

# sorting the set to see if all desired values are in the set
print(sorted(new_set))

# using the sum operation to sum all the values in the set
print(sum(new_set))