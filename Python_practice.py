print("Hello World")

counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])
if "El Paso" in counties:
    print("El Pass is in the list of Counties.")
else:
    print("El Paso is not in the list of counties")
if "Jefferson" not in counties:
    print("Oselobuan!")
elif "Denver" in counties:
    print("Here we go!")
else:
    print("Huh huh")
if "Denver" in counties and "Enugu" not in counties:
    print("We the Boss!")
else:
    print("Dodo don don")
for county in counties:
    print(county)
for i in range(len(counties)):
    print(counties[i])
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

