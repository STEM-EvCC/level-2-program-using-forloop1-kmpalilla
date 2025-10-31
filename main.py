## Program with For Loop ##

# Show total number of missions
# Show number of successful missions
# Show success rate as a percentage
# Show names of missions launched before the year 2000

mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]

print("Total number of missions: " + str(len(mission_names)))
count = 0
for x in mission_success:
    if x:
        count += 1


print("Number of successful missions: " + str(count))
success_rate = count / len(mission_success) * 100
print("Success rate: " + str(round(success_rate,2)) + "%")
print("Missions launched before the year 2000: ")
for x in range(len(mission_names)):
   if mission_years[x] < 2000:
    print("- " + mission_names[x])
   




