file_source = open("professions_female.txt", "r")

lines = file_source.readlines()
l = []
for line in lines:
	words = line.split(',')
	if len(words)>1: # coppia di professioni maschile-femminile
		l.append([words[0], words[1][:-1]])

for el in l:
	print(el)
file_source.close()