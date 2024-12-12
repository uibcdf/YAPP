cpps = []

path_dbs = '/home/diego/repos@uibcdf/YAPP/yapp/data/DBs'
db = 'CPPSite2'
aas = ['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y']

import pickle

with open(path_dbs+'/'+db+'/'+'CPPSite2.pkl', 'rb') as fff:
    data_db = pickle.load(fff)

for ii,jj in data_db.items():
    if jj['LINEAR/CYCLIC']=='Linear':
        if jj['CHIRALITY']=='L':
            seq=jj['PEPTIDE SEQUENCE']
            if all(kk in aas for kk in seq):
                cpps.append(seq)

