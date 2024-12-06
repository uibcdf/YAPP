cpps = []
non_cpps = []

path_dbs = '/home/diego/repos@uibcdf/YAPP/yapp/data/DBs'
db = 'C2Pred'

filename = path_dbs+'/'+db+'/all_cpps.txt'
with open(filename, 'r') as fff:
    for line in fff:
        cpps.append(line.strip())

filename = path_dbs+'/'+db+'/all_noncpps.txt'
with open(filename, 'r') as fff:
    for line in fff:
        non_cpps.append(line.strip())

