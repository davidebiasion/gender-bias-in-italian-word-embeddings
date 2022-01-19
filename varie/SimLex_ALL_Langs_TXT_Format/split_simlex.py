# leggerò il file modificato da me: di fronte ad ogni coppia ci sarà la lettera "S"
# se le parole della coppia hanno lo stesso genere, "D" altrimenti.

# open files
file_source_ita = open("MSimLex999_Italian_split_noverbs.txt", "r")
file_source_en = open("MSimLex999_English.txt", "r")
file_dest_ita_s = open("MSimLex999_Italian_s.txt", "w")
file_dest_ita_d = open("MSimLex999_Italian_d.txt", "w")
file_dest_en_s = open("MSimLex999_English_s.txt", "w")
file_dest_en_d = open("MSimLex999_English_d.txt", "w")


# reading files
lines_ita = file_source_ita.readlines()
lines_en = file_source_en.readlines()


# lists
ita_s = []
ita_d = []
en_s = []
en_d = []

for i in range(len(lines_ita)):
	words_ita = lines_ita[i].split(",")
	words_en = lines_en[i].split(",")
	
	# if same gender
	if words_ita[0]=="S": 
		ita_s.append(words_ita[1]+","+words_ita[2])
		en_s.append(words_en[0]+","+words_en[1])
	else:
		ita_d.append(words_ita[1]+","+words_ita[2])
		en_d.append(words_en[0]+","+words_en[1])


# write files
for pair in ita_s:
	file_dest_ita_s.write(pair+"\n")

for pair in ita_d:
	file_dest_ita_d.write(pair+"\n")

for pair in en_s:
	file_dest_en_s.write(pair+"\n")

for pair in en_d:
	file_dest_en_d.write(pair+"\n")


# close files
file_source_ita.close()
file_source_en.close()
file_dest_ita_s.close()
file_dest_ita_d.close()
file_dest_en_s.close()
file_dest_en_d.close()