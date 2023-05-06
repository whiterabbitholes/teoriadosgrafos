grafos = [
    {1: [2, 3],
    2: [1, 3],
    3: [2, 4, 5],
    4: [1, 3, 5],
    5: [3, 4]},
    {},
    {}
]

mapas = {
    "adjacency_list": {
        'BSB':[('TAG',1),('AP',3),('GO',4)],
        'TAG':[('BSB',1)],
        'AP':[('BSB',3), ('JP',9),('CER',5)],
        'CER':[('AP',5),('JP',8),('GO',3)],
        'GO':[('BSB',4),('CER', 3)],
        'JP':[('AP',9),('CER',4)] 
    },
    "adjacency_matrix": [
        [0, 1, 3, 0, 4, 0],
        [1, 0, 0, 0, 0, 0],
        [3, 0, 0, 5, 0, 9],
        [0, 0, 5, 0, 3, 4],
        [4, 0, 0, 3, 0, 0],
        [0, 0, 9, 4, 0, 0]
    ],
    "adjacency_listNW":{
        'BSB':['TAG','AP','GO'],
        'TAG':['BSB'],
        'AP':['BSB','JP','CER'],
        'CER':['AP','JP','GO'],
        'GO':['BSB','CER'],
        'JP':['AP','CER'] 
    }
}