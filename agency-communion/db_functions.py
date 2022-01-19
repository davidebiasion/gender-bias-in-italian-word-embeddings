# functions to be used in bias_in_italian_WEs notebook
# Davide Biasion
# 1204521
# Ingegneria Informatica - UniPD


# read profession list
def read(file_path, mode):
    file = open(file_path, 'r')
    lines = file.readlines()
    l = []
    
    # read professions.txt with only male professions
    if mode=='m':
        for line in lines:
            l.append(line[:-1])

    # read professions_female.txt with both male-female professions
    elif mode=='mf':
        for line in lines:
            words = line.split(',')
            if len(words)>1: # pairs of male-female professions
                l.append([words[0], words[1][:-1]])
                
    elif mode=='istat':
        for line in lines:
            words = line.split(',')
            l.append([words[0], float(words[1]), float(words[2][:-1])])
            
    elif mode=='truth':
        for line in lines[1:]:
            words = line.split(',')
            l.append([words[0], 100-float(words[1]), float(words[1])])
            
    elif mode=='truth-mf':
        for line in lines[1:]:
            words = line.split(',')
            l.append([words[0], words[1], 100-float(words[2]), float(words[2])])
    
    elif mode=='ag-com':
        for line in lines:
            words = line.split(',')
            l.append([words[0], float(words[1])])
            
    elif mode=='ag-com-mf':
        for line in lines:
            words = line.split(',')
            l.append([words[0], words[1], float(words[2]), float(words[3])])
            
    elif mode=='ag-com-en':
        for line in lines:
            words = line.split(',')
            l.append([words[0], float(words[1]), float(words[2])])
    else:
        print("!!! unknown mode")

    file.close()
    
    return l


# compute projections for male-female professions
def prof_proj(E, l, g, mode):
    proj = []
    
    if mode=='m':
        for w in l:
            try:
                v = E.v(w)
                pr = v.dot(g)
                proj.append([w,pr])
            except KeyError:
                pass        
    
    elif mode=='mf':
        for pair in l:
            try:
                v1 = E.v(pair[0])
                v2 = E.v(pair[1])
                proj1 = v1.dot(g)
                proj2 = v2.dot(g)
                proj.append([pair[0],proj1,pair[1],proj2])
            except KeyError:
                pass
                #print(pair[0]+","+pair[1]+" not in E")
                
    elif mode=='istat':
        for triple in l:
            try:
                v = E.v(triple[0])
                pr = v.dot(g)
                proj.append([triple[0],pr,triple[1],triple[2]])
            except KeyError:
                pass
            
    elif mode=='istat-mf':
        for quadruple in l:
            try:
                v1 = E.v(quadruple[0])
                v2 = E.v(quadruple[1])
                proj1 = v1.dot(g)
                proj2 = v2.dot(g)
                proj.append([quadruple[0],proj1,quadruple[1],proj2,quadruple[3]])
            except KeyError:
                pass

    elif mode=='ag-com':
        for pair in l:
            try:
                v = E.v(pair[0])
                pr = v.dot(g)
                proj.append([pair[0],pr,pair[1]])
            except KeyError:
                pass
            
    elif mode=='ag-com-f':
        for t in l:
            try:
                v = E.v(t[1])
                pr = v.dot(g)
                proj.append([t[1],pr,t[2],t[3]])
            except KeyError:
                pass
            
    elif mode=='ag-com-m':
        for t in l:
            try:
                v = E.v(t[0])
                pr = v.dot(g)
                proj.append([t[0],pr,t[2],t[3]])
            except KeyError:
                pass
            
    elif mode=='ag-com-mf':
        for t in l:
            try:
                v1 = E.v(t[0])
                v2 = E.v(t[1]) 
                pr = (v1.dot(g)+v2.dot(g))/2
                proj.append([t[0],pr,t[2],t[3]])
            except KeyError:
                pass

    elif mode=='ag-com-en':
        for t in l:
            try:
                v = E.v(t[0]) 
                pr = v.dot(g)
                proj.append([t[0],pr,t[1],t[2]])
            except KeyError:
                pass
            
    else:
        print("!!! unknown mode") 

    return proj


# read the SimLex splits
def read_simlex_set(file_path):
    file = open(file_path, 'r')
    lines = file.readlines()

    l = []
    for line in lines:
        words = line.split(",")
        l.append([words[0], words[1][:-1]])
    
    file.close()

    return l


# compute average cosine distance between words in a set
def simlex_set_dist(E, l):
    s = 0 # sum
    n = len(l) # number of pairs
    
    for pair in l:
        try:
            v1 = E.v(pair[0])
            v2 = E.v(pair[1])
            s = s + E.v(pair[0]).dot(E.v(pair[1]))
        except KeyError: # words not in E
            n = n - 1

    return s/n
