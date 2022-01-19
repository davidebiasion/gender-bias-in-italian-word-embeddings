def read_simlex_set(file_path):
    file = open(file_path, 'r')
    lines = file.readlines()

    l = []
    for line in lines:
    	words = line.split(",")
    	l.append([words[0], words[1][:-1]])

    return l


lis = read_simlex_set('MSimLex999_Italian_d.txt')

print(lis)

