cpps = []
non_cpps = []

path_dbs = '/home/diego/repos@uibcdf/YAPP/yapp/data/DBs'
db = 'BChemRF-CPPred'

filename = path_dbs+'/'+db+'/independent_test_cpps.txt'
with open(filename, 'r') as fff:
    for line in fff:
        cpps.append(line.strip())

filename = path_dbs+'/'+db+'/training_cpps.txt'
with open(filename, 'r') as fff:
    for line in fff:
        cpps.append(line.strip())

filename = path_dbs+'/'+db+'/independent_test_no_cpps.txt'
with open(filename, 'r') as fff:
    for line in fff:
        non_cpps.append(line.strip())

filename = path_dbs+'/'+db+'/training_non_cpps.txt'
with open(filename, 'r') as fff:
    for line in fff:
        non_cpps.append(line.strip())

