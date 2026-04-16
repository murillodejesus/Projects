def main():
    overall_min_val = 999.0
    overall_min_country = ""
    overall_min_year = ""
    
    overall_max_val = -1.0
    overall_max_country = ""
    overall_max_year = ""

    year_interest = input("Enter the year of interest: ")

    year_total_life = 0
    year_count = 0
    year_min_val = 999.0
    year_min_country = ""
    year_max_val = -1.0
    year_max_country = ""

    country_interest = input("Enter a country to see its stats: ").strip().lower()
    c_total = 0
    c_count = 0
    c_min = 999.0
    c_max = -1.0

    try:
        with open("life-expectancy.csv") as file:
            next(file)
            
            for line in file:
                parts = line.strip().split(",")
                
                entity = parts[0]
                year = parts[2]
                value = float(parts[3])

                if value < overall_min_val:
                    overall_min_val = value
                    overall_min_country = entity
                    overall_min_year = year
                
                if value > overall_max_val:
                    overall_max_val = value
                    overall_max_country = entity
                    overall_max_year = year

                if year == year_interest:
                    year_total_life += value
                    year_count += 1
                    
                    if value < year_min_val:
                        year_min_val = value
                        year_min_country = entity
                    
                    if value > year_max_val:
                        year_max_val = value
                        year_max_country = entity

                if entity.lower() == country_interest:
                    c_total += value
                    c_count += 1
                    if value < c_min: c_min = value
                    if value > c_max: c_max = value

        print(f"\nThe overall max life expectancy is: {overall_max_val} from {overall_max_country} in {overall_max_year}")
        print(f"The overall min life expectancy is: {overall_min_val} from {overall_min_country} in {overall_min_year}")

        if year_count > 0:
            avg = year_total_life / year_count
            print(f"\nFor the year {year_interest}:")
            print(f"The average life expectancy across all countries was {avg:.2f}")
            print(f"The max life expectancy was in {year_max_country} with {year_max_val}")
            print(f"The min life expectancy was in {year_min_country} with {year_min_val}")
        else:
            print(f"\nNo data found for the year {year_interest}.")

        if c_count > 0:
            c_avg = c_total / c_count
            print(f"\nHistorical stats for {country_interest.capitalize()}:")
            print(f"Min: {c_min} | Max: {c_max} | Avg: {c_avg:.2f}")

    except FileNotFoundError:
        print("Error: The file 'life-expectancy.csv' was not found.")

if __name__ == "__main__":
    main()