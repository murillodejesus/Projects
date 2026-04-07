# open the file
with open("week 06/web_traffic.csv") as web_file:

# read through the file line by line
    for line in web_file:
        print(line)

#split the line into parts
parts = line.split(",")


# store each part into a separate variable
page = parts[0]
time = parts[1]
referring_page = parts[2]



# print the result
print(f"Page '{page}' referred by '{referring_page}'was visited for '{time}' seconds")
