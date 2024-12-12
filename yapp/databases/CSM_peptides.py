cpps = []
non_cpps = []

path_dbs = '/home/diego/repos@uibcdf/YAPP/yapp/data/DBs'
db = 'CSM-peptides'

filename = path_dbs+'/'+db+'/CPP_train.csv'
with open(filename, 'r') as fff:
    for line in fff:
        _, pep, pep_type, _, _ = line.strip().split(',')
        if pep_type.lower()=='positive':
            cpps.append(pep)
        else:
            non_cpps.append(pep)

filename = path_dbs+'/'+db+'/CPP_test_main.csv'
with open(filename, 'r') as fff:
    for line in fff:
        _, pep, pep_type, _, _ = line.strip().split(',')
        if pep_type.lower()=='positive':
            cpps.append(pep)
        else:
            non_cpps.append(pep)

filename = path_dbs+'/'+db+'/CPP_test_alternative.csv'
with open(filename, 'r') as fff:
    for line in fff:
        _, pep, pep_type, _, _ = line.strip().split(',')
        if pep_type.lower()=='positive':
            cpps.append(pep)
        else:
            non_cpps.append(pep)




