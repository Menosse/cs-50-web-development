ppl = [ {"name":"harry", "house" : "gryffindor"}, 
		{"name":"cho", "house" : "ravendlaw"}, 
		{"name":"draco", "house" : "slytherin"} ]


def f(person):
	return person["name"]

ppl.sort(key=lambda person: person["name"])

print(ppl)

