with open("sorted_data.csv", "r") as file:
    data = file.read().replace('\r\n', ',')
    
POKEMON_COUNT = 811
COLUMNS = 8


T_order = []
T_id = []
T_name = []
T_species_id = []
T_height = []
T_weight = []
T_base_experience = []
T_is_default = []


c1 = 0 #counts to POKEMON_COUNT * COLUMNS
c2 = 0 #counts to POKEMON_COUNT
data = data.split(",")
data_length = len(data)


while c1 < data_length:
    T_order.append(data[c1])
    T_id.append(data[c1+1])
    T_name.append(data[c1+2])
    T_species_id.append(data[c1+3])
    T_height.append(data[c1+4])
    T_weight.append(data[c1+5])
    T_base_experience.append(data[c1+6])
    T_is_default.append(data[c1+7])
    c2+=1
    c1+=8


def search_id(number):
    '''
    input the pokemon's id number(unique) parse for exact match
    returns the index
    '''
    c1 = 0
    while c1 < POKEMON_COUNT:
        if T_id[c1] == str(number):
            return c1
        c1+=1

def search_name(name):
    '''
    input string
    return list of indices that fit the string
    '''
    c1 = 0
    index_list = []
    while c1 < POKEMON_COUNT:
        if name in T_name[c1]:
            index_list.append(c1)
        c1+=1
    return index_list

if __name__=="__main__":
    #test search_id(n)
    print T_name[search_id(124)]
    print T_name[search_id(204)]
    #test search_name(name)
    c1 = 0
    search_list = search_name("mew")
    while c1 < len(search_list):
        print T_name[search_list[c1]]
        c1+=1


    

        
        



         
