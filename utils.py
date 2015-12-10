with open("sorted_data.csv", "r") as file:
    data = file.read().replace('\r\n', '')
    
POKEMON_COUNT = 811
COLUMNS = 8
T_order = []#[POKEMON_COUNT]
T_id = []#[POKEMON_COUNT]
T_name = []#[POKEMON_COUNT]
T_species_id = []#[POKEMON_COUNT]
T_height = []#[POKEMON_COUNT]
T_weight = []#[POKEMON_COUNT]
T_base_experience = []#[POKEMON_COUNT]
T_is_default = []#[POKEMON_COUNT]


c1 = 0 #counts to POKEMON_COUNT * COLUMNS
c2 = 0 #counts to POKEMON_COUNT
data = data.split(",")
data_length = len(data)



while c1 < POKEMON_COUNT*COLUMNS -1:
    T_order.append(data[c1])
    T_id.append(data[c1+1])
    T_name.append(data[c1+2])
    T_species_id.append(data[c1+3])
    T_height.append(data[c1+4])
    T_weight.append(data[c1+5])
    T_base_experience.append(data[c1+6])
    T_is_default.append(data[c1+7])
    c2+=1
    c1+=7

print T_name
    
        
        



         
