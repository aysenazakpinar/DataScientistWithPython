# Create a variable savings
savings = 100

# Create a variable growth_multiplier
growth_multiplier = 1.1
result = savings * growth_multiplier ** 7
print(result)

# Calculate result


# Print out result

# Create a variable desc
desc = "compound interest"

# Create a variable profitable
profitable = True

#Guess the type
#To find out the type of a value or a variable that refers to that value,
# you can use the type() function. Suppose you've defined a variable a, but you forgot the type of this variable.
# To determine the type of a, simply execute:
#  type(a)
#We already went ahead and created three variables: a, b and c.
# You can use the IPython shell to discover their type. Which of the following options is correct?

#Instructions
#Possible Answers
# 1- a is of type int, b is of type str, c is of type bool
# 2- a is of type float, b is of type bool, c is of type str
# 3- a is of type float, b is of type str, c is of type bool
# 4- a is of type int, b is of type bool, c is of type str

savings = 100
growth_multiplier = 1.1

# Assign product of growth_multiplier and savings to year1
year1 = savings * growth_multiplier

# Print the type of year1
print(type(year1))

# Assign sum of desc and desc to doubledesc
doubledesc = desc + desc

# Print out doubledesc
print(doubledesc)
result = 100 * 1.10 ** 7

# Fix the printout
print("I started with $" + str(savings) + " and now have $" + str(result) + ". Awesome!")

# Definition of pi_string
pi_string = "3.1415926"

# Convert pi_string into float: pi_float

pi_float = float(pi_string)

# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas
areas = [hall, kit, liv, bed, bath]
print(areas)

# Print areas
# Adapt list areas
areas = ["hallway", hall, "kitchen", kit, "living room", liv, "bedroom", bed, "bathroom", bath]

# Print areas
print(areas)
# house information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]

# Print out house
print(house)

# Print out the type of house
print(type(house))
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas[1])

# Print out last element from areas
print(areas[-1])

# Print out the area of the living room
print(areas[5])


# Sum of kitchen and bedroom area: eat_sleep_area
eat_sleep_area = areas[3] + areas[-3]

# Print the variable eat_sleep_area
print(eat_sleep_area)
# Use slicing to create downstairs
downstairs = areas[:6]

# Use slicing to create upstairs
upstairs = areas[6:10]

# Print out downstairs and upstairs
print(downstairs)
print(upstairs)
# Alternative slicing to create downstairs
downstairs = areas[:6]

# Alternative slicing to create upstairs
upstairs = areas[6:]
# Correct the bathroom area
areas[-1] = 10.50

# Change "living room" to "chill zone"
areas[4] = "chill zone"

# Create the areas list and make some changes
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ["poolhouse", 24.5]

# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage", 15.45]

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Create areas_copy
areas_copy = areas[:]

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)

