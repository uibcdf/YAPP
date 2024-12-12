cpps = []
non_cpps = []

path_dbs = '/home/diego/repos@uibcdf/YAPP/yapp/data/DBs'
db = 'Hallbrink_2005'

filename = path_dbs+'/'+db+'/functional_CPPs.txt'
with open(filename, 'r') as fff:
    for line in fff:
        pep = line.strip()
        cpps.append(pep)

filename = path_dbs+'/'+db+'/non_functional_CPPs.txt'
with open(filename, 'r') as fff:
    for line in fff:
        pep = line.strip()
        non_cpps.append(pep)

