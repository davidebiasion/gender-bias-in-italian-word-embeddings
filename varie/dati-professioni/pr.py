file_dest = open("professions.txt", "r")

lines = file_dest.readlines()
l = []
for line in lines:
	l.append(line[:-1])

print(l)
file_dest.close()