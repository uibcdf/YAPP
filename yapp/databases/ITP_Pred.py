cpps = []
non_cpps = []

path_dbs = '/home/diego/repos@uibcdf/YAPP/yapp/data/DBs'
db = 'ITP-Pred'

filename = path_dbs+'/'+db+'/CPPs_Testing.txt'
with open(filename, 'r') as fff:
    for line in fff:
        pep = line.strip()
        cpps.append(pep)

filename = path_dbs+'/'+db+'/CPPs_Training.txt'
with open(filename, 'r') as fff:
    for line in fff:
        pep = line.strip()
        cpps.append(pep)

filename = path_dbs+'/'+db+'/Non_CPPs_Testing.txt'
with open(filename, 'r') as fff:
    for line in fff:
        pep = line.strip()
        non_cpps.append(pep)

filename = path_dbs+'/'+db+'/Non_CPPs_Training.txt'
with open(filename, 'r') as fff:
    for line in fff:
        pep = line.strip()
        non_cpps.append(pep)

