# open the file
with open("week 06/web_traffic.csv") as web_file:

    total_time = 0

    # read through the file line by line
    for line in web_file:
        print(line)

    #split the line into parts
    parts = line.split(",")


    # store each part into a separate variable
    page = parts[0].strip()
    time = float(parts[1].strip())
    referring_page = parts[2].strip()

    total_time += time

    # print the result
    print(f"Page '{page}' referred by '{referring_page}'was visited for '{time}' seconds")

    print(f"The total time was {total_time}")