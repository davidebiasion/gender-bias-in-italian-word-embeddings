# functions to be used in bias_in_italian_WEs notebook
# Davide Biasion
# 1204521
# Ingegneria Informatica - UniPD


import codecs
import numpy as np
from numpy import linalg as LA
from sklearn.decomposition import PCA


# Hila Gonen's functions
# *********************************************************************

def load_embeddings_from_w2vf(filename):
    print ('loading w2vf...')
    
    wv = np.load(filename + '.npy')
    with codecs.open(filename + '.vocab', 'r', 'utf-8') as f_embed:
        vocab = f_embed.read().split()
    
    w2i = {w: i for i, w in enumerate(vocab)}

    return vocab, wv, w2i


def normalize(wv):
    # normalize vectors
    norms = np.apply_along_axis(LA.norm, 1, wv)
    wv = wv / norms[:, np.newaxis]
    return wv


def load_and_normalize(lang, filename, vocab, wv, w2i):
    vocab_muse, wv_muse, w2i_muse = load_embeddings_from_w2vf(filename)
    wv_muse = normalize(wv_muse)
    vocab[lang] = vocab_muse 
    wv[lang] = wv_muse
    w2i[lang] = w2i_muse
    print ('done')
    
# Hila Gonen's functions
# *********************************************************************



# PCA
def myPCA(pairs, embedding, num_components = 10):
    matrix = []
    for a, b in pairs:
        center = (embedding[a] + embedding[b])/2
        matrix.append(embedding[a] - center)
        matrix.append(embedding[b] - center)
    matrix = np.array(matrix)
    pca = PCA(n_components = num_components)
    pca.fit(matrix)
    
    return pca


# read profession list
def read_professions(file_path, mode):
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
            
    else:
        print("!!! unknown mode")

    file.close()
    
    return l


# compute projections for male-female professions
def prof_proj(embedding, l, g, mode):
    proj = []
    
    if mode=='m':
        for w in l:
            try:
                v = embedding[w]
                pr = np.dot(v,g)
                proj.append([w,pr])
            except KeyError:
                pass        
    
    elif mode=='mf':
        for pair in l:
            try:
                v1 = embedding[pair[0]]
                v2 = embedding[pair[1]]
                proj1 = np.dot(v1,g)
                proj2 = np.dot(v2,g)
                proj.append([pair[0],proj1,pair[1],proj2])
            except KeyError:
                pass
                
    elif mode=='istat':
        for triple in l:
            try:
                v = embedding[triple[0]]
                pr = np.dot(v,g)
                proj.append([triple[0],pr,triple[1],triple[2]])
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
def simlex_set_dist(embedding, l):
    s = 0 # sum
    n = len(l) # number of pairs
    
    for pair in l:
        try:
            v1 = embedding[pair[0]]
            v2 = embedding[pair[1]]
            s = s + np.dot(embedding[pair[0]],embedding[pair[1]])
        except KeyError: # words not in E
            n = n - 1

    return s/n
