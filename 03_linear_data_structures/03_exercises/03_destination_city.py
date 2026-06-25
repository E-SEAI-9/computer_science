# Solution one
def destination_city(paths):
    for i in range(len(paths)):
        possible_city = paths[i][1] # Lima
        for j in range(len(paths)):
            if possible_city == paths[j][0]:
                break
        else:
            return possible_city
            

# Solution two
def destination_city_2(paths):
    outgoing_cities = set() # {London, new york, Lima}

    for path in paths:
        outgoing_cities.add(path[0])

    for path in paths:
        if path[1] not in outgoing_cities:
            return path[1]
    
first_city = destination_city_2([["London","New York"], ["New York","Lima"], ["Lima","Sao Paulo"]])
print(first_city)

#----

