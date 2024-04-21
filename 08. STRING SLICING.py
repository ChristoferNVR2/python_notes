# slicing = create a substring by extracting elements from another
#           string indexing[] or slice()
#           [start:stop:step]

name = "Christofer Vega"

first_name = name[:10]  # if start is not defined, it's 0
last_name = name[11:]  # if stop is not defined, it goes to the end
funky_name = name[::2]

print(first_name)
print(last_name)
print(funky_name)

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice_ = slice(7, -4)
print(website1[slice_])
print(website2[slice_])
