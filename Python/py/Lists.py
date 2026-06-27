#reverse indexing

lst = [2,222,333,45,56]
i = -1

while i>=-5:
	print(lst[i])
	i +=-1

print("---------------------------------------------------")

# del and remove

del lst[0]

print(lst)

lst.remove(45)

print(lst)

print("----------------------------------------------------")

#sort

lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst)

print("----------------------------------------------------")

#inserting elements list

lst.append(000)
print(lst)
lst.extend([999,888,777,36,96])
print(lst)
lst.insert(3,3456789)
print(lst)

print("----------------------------------------------------")
# del vs clear

lst.clear()
print(lst)
del lst
print(lst)


