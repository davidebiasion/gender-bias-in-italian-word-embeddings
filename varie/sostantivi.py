# open files
file_source = open("lista333sostantivi.txt", "r")
file_dest = open("sostantivi.txt", "w")

# read file
lines = file_source.readlines()

# write file
for line in lines:
	words = line.split()
	file_dest.write(words[2]+'\n')

# close files
file_source.close()
file_dest.close()