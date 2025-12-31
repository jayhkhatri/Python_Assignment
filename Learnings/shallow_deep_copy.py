import copy

# l1 = [1, 2.5, [10, 20, 30,], 'python']
l1 = {'id':1010, 'name':'John','Marks':{'eng':71.5,'maths':91.5,'bio':80.0}}

# shallow copy
# will not have any effect if id of internal element changes (reassignment of variable)
# but will have effect if values are altered but not the id
# since it is associated with id of internal items any update operation changes both l1 and l2

l2 = copy.copy(l1)
l3 = copy.deepcopy(l1)

# modifying l1 after creating copy
# l1[0] = 100  # reassignment id changed
# l1[2][2] = 50 # value update id of l1[2] is not changed.
l1['id'] = 1001  # reassignment id changed
l1['Marks']['eng'] = 80 # value update id of l1[2] is not changed.


l2['Marks']['bio'] =85.0 # this is update operation and changes l1 too
print(f"l1 is {l1} and l2 is {l2} and l3 is {l3}")

print(f"memory address of l1 is {id(l1)} and l2 is {id(l2)} and l3 is {id(l3)}")  # both are different