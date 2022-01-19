# open files
file_source = open("ag_com_ita.txt", "r")
file_ag = open("ag_ita_thresh_2.txt", "w")
file_com = open("com_ita_thresh_2.txt", "w")

# read file
lines = file_source.readlines()[1:]

# write file
for line in lines:
	words = line.split(',')
	if float(words[1]) > float(words[2]): # agency-score > communion-score
		if float(words[1]) > 2:
			#file_ag.write(words[0]+','+words[1]+'\n')
			file_ag.write(words[0]+','+words[1]+','+words[2])
	else:
		if float(words[2]) > 2:
			#file_com.write(words[0]+','+words[2])
			file_com.write(words[0]+','+words[1]+','+words[2])


# close files
file_source.close()
file_ag.close()
file_com.close()