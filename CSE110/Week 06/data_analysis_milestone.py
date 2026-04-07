min_life_expectancy = 9999.0
max_life_expectancy = -1.0

with open("week 06/life-expectancy.csv") as data_file:
    next(data_file)
    
    for line in data_file:
        parts = line.strip().split(",")
        
        life_expectancy = float(parts[3])
        
        if life_expectancy > max_life_expectancy:
            max_life_expectancy = life_expectancy
            
        if life_expectancy < min_life_expectancy:
            min_life_expectancy = life_expectancy
            
print(f"The overall max life expectancy is: {max_life_expectancy}")
print(f"The overall min life expectancy is: {min_life_expectancy}")