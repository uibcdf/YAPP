cpps = []
non_cpps = []

path_dbs = '/home/diego/repos@uibcdf/YAPP/yapp/data/DBs'
db = 'AiCPP'

filename = path_dbs+'/'+db+'/S1_Test_Set.csv'
with open(filename, 'r') as fff:
    for line in fff:
        pep, pep_type = line.strip().split(',')
        if pep_type.lower()=='cpp':
            cpps.append(pep)
        else:
            non_cpps.append(pep)

filename = path_dbs+'/'+db+'/S2_Train_Set.csv'
with open(filename, 'r') as fff:
    for line in fff:
        pep, pep_type = line.strip().split(',')
        if pep_type.lower()=='cpp':
            cpps.append(pep)
        else:
            non_cpps.append(pep)

