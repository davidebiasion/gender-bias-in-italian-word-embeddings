# open files
file_source = open("aggettivi.txt", "r")
file_dest = open("aggettivi_mf.txt", "w")

# read file
lines = file_source.readlines()

# write file
for line in lines:
	words = line.split(',')
	if len(words)>1:
		file_dest.write(line)

# close files
file_source.close()
file_dest.close()