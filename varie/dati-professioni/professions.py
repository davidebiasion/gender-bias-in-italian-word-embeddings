# open files
file_source = open("professions_dizy_com.txt", "r")
file_dest = open("professions.txt", "w")

# read file
lines = file_source.readlines()[1:]

# write file
for line in lines:
	words = line.split()
	for word in words:
		file_dest.write(word+'\n')

# close files
file_source.close()
file_dest.close()