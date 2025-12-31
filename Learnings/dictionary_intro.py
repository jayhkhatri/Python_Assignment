# comma separated key value pairs enclosed with in {}
# {"key1":val1,"key2":val2,....}

groceries = {'milk': 60, 'biscuits': 20, 'rice': 90, 'bread': 30}
groceries_1 = {'millet': 120, "ice-cream":50,'rice':110}
print(groceries, type(groceries))
print(len(groceries))
print(groceries['milk'])
# updating values of key
groceries['milk'] = 65
print(groceries)

# adding key value pair manually
groceries['Mice1'] = 50
print(groceries)


## operation in dictionaries

marks = {'maths': 80.5, 'end': 76.0, 'phy':89.0}
print(marks)

print(marks['phy'])

print(marks.get('phy',40))

print('maths' in marks)


# removing key value pair
marks.pop('maths')
print(marks)

groceries.update(groceries_1)
print(groceries)

groceries.pop('Mice1')
print(groceries)

# operations in dictionary
# allowed Keys: String, int, float, boolean, tuples  ==> immutable data types
# not allowed keys: List, sets,dict. ==> mutable data type

# fetching of keys from dictionary
print(groceries.keys())

# fetching values
print(groceries.values())

# fetching items
print(groceries.items())
































