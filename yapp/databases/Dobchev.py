cpps = []
non_cpps = []

path_dbs = '/home/diego/repos@uibcdf/YAPP/yapp/data/DBs'
db = 'Dobchev2010Prediction'

filename = path_dbs+'/'+db+'/training.dat'
with open(filename, 'r') as fff:
    for line in fff:
        pep, pep_type = line.strip().split()
        pep=pep.removesuffix('-NH2')
        if pep_type.lower()=='cpp':
            cpps.append(pep)
        else:
            non_cpps.append(pep)

filename = path_dbs+'/'+db+'/validation.dat'
with open(filename, 'r') as fff:
    for line in fff:
        pep, pep_type = line.strip().split()
        pep=pep.removesuffix('-NH2')
        if pep_type.lower()=='cpp':
            cpps.append(pep)
        else:
            non_cpps.append(pep)

