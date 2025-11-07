## Program with For Loop ##

# Show total number of missions
# Show number of successful missions
# Show success rate as a percentage
# Show names of missions launched before the year 2000
# Data shown to user must match what was given to keep uniformity

mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
# All missions by name

mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
# All years missions happened

mission_success = [True, False, True, True, True, True, False]
# Success status of missions

print("Total number of missions: " + str(len(mission_names))) # Show the user the total amount of missions

count = 0
for x in mission_success: # Will get the amount of successful missions by finding all True entries
    if x == True: # if x: also works, need to look up reasoning for why it works. This is adding to the count for each True in the misssion_success variable
        count += 1 # Count goes up for every True the for loop finds
print("Number of successful missions: " + str(count)) # Display to user number of successful mission based off the count in prior for loop

success_rate = count / len(mission_success) * 100 # Acquire the percentage of the successful missions by getting the number of entries in mission_success
# Then dividing the count by the entries and multiply the result by 100 to get success_rate into desired format

print("Success rate: " + str(round(success_rate,2)) + "%") # Show user the success rate in a percentage. Uses round to show only 2 decimal places for percentage
# Could have used the string formatting from the provided example in the "Help! My code doesn't work" section instead to get desired output

print("Missions launched before the year 2000: ")
for x in range(len(mission_names)): # Using the range of the mission names to allow use in case more data entries is added. Similar to fizzbuzz example
   if mission_years[x] < 2000: # Checking through the mission years (x being the index) to see what missions are before year 2000
    print("- " + mission_names[x]) # Using this format to match the provided output.
    # Using x as the index it will pair mission names with mission years as long as the data correlate based off position in index
    # And keep looping until it checks all mission names
   


