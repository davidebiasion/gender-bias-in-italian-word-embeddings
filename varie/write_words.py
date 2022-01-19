# open files
file_source = open("../agency-communion/gram_def_mf.txt", "r")
file_dest = open("new.txt", "w")

# read file
lines = file_source.readlines()

# write file
for line in lines:
	words = line.split(',')
	file_dest.write(words[0]+'\n')
	file_dest.write(words[1])

# close files
file_source.close()
file_dest.close()
