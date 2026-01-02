countries =['India', 'United states', 'Australia', 'Ireland', 'Sri Lanka', 'Iceland', 'Cuba', 'Iran', 'Poland']
# count countries started with I
# prepare listedCountry of them


listedCountry =[]
count =0
for country in countries:
    if country.startswith('I'):
        listedCountry.append(country)
        count += 1

print(f"There are {count} countries started with initial I")
print(listedCountry)