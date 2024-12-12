cpps = []
non_cpps = []

path_dbs = '/home/diego/repos@uibcdf/YAPP/yapp/data/DBs'
db = 'CellPPD'

filename = path_dbs+'/'+db+'/CPPset1_cpps.txt'
with open(filename, 'r') as fff:
    for line in fff:
        pep = line.strip()
        cpps.append(pep)

filename = path_dbs+'/'+db+'/CPPset2_cpps.txt'
with open(filename, 'r') as fff:
    for line in fff:
        pep = line.strip()
        cpps.append(pep)

filename = path_dbs+'/'+db+'/CPPset3_cpps.txt'
with open(filename, 'r') as fff:
    for line in fff:
        pep = line.strip()
        cpps.append(pep)

filename = path_dbs+'/'+db+'/independent_cpps.txt'
with open(filename, 'r') as fff:
    for line in fff:
        pep = line.strip()
        cpps.append(pep)

filename = path_dbs+'/'+db+'/CPPset1_non_cpps.txt'
with open(filename, 'r') as fff:
    for line in fff:
        pep = line.strip()
        non_cpps.append(pep)

filename = path_dbs+'/'+db+'/CPPset2_non_cpps.txt'
with open(filename, 'r') as fff:
    for line in fff:
        pep = line.strip()
        non_cpps.append(pep)

filename = path_dbs+'/'+db+'/CPPset3_non_cpps.txt'
with open(filename, 'r') as fff:
    for line in fff:
        pep = line.strip()
        non_cpps.append(pep)

filename = path_dbs+'/'+db+'/independent_non_cpps.txt'
with open(filename, 'r') as fff:
    for line in fff:
        pep = line.strip()
        non_cpps.append(pep)

