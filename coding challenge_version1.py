import random
import math
import matplotlib.pyplot as plt

# define the value of alpha
alpha = 0.4

# define the function to check if a point is valid
def checkvalid(positions, alphapos):
    # initialize a flag to indicate if the point is valid
    valid = True
    # loop through the existing positions
    for pos in positions:
        # calculate the distance between the point and the existing position using the Pythagorean theorem
        pythagoras = math.sqrt(abs(pos[0] - alphapos[0])**2 + abs(pos[1] - alphapos[1])**2)
        # calculate the maximum distance between the point and the existing position based on the value of alpha
        alphad = alpha * (pos[2] + alphapos[2])
        # if the distance between the point and the existing position is less than or equal to the maximum distance, the point is not valid
        if (pythagoras) <= (alphad):
            valid = False
    # return the validity of the point
    return valid

# print the available options for the mixture
print ("1. Monodisperse (single-size) mixture")
print ("2. Bidisperse mixture 50/50")
print ("3. Additional bidisperse mixture 80/20")

# loop until the user enters a valid choice
while True:
    # get the user's choice for the mixture
    choice = int(input("Write the number that corresponds to which solution you want: "))
    # if the user selects the first option
    if choice == 1:
        # calculate the radius of the particles in the mixture
        R1 = (1/math.sqrt(math.pi))
        R2 = 0
        # print the radius of the particles
        print( "The particles in solution have radius of {0:.3f}".format(R1))
        u = 4
        f = 6
        b = 3
        break
    elif choice == 2:
        R1 = math.sqrt(3/(2*(math.pi)))
        R2 = math.sqrt(1/(2*(math.pi)))
        print( "The 50 % of the particles in solution have radius of {0:.3f} and the other 50% have a radius  of {1:.3f} ".format(R1, R2))
        u = 0
        f = 2
        b = 2
        break
    elif choice == 3:
        R1 = math.sqrt(15/(16*(math.pi)))
        R2 = math.sqrt(5/(4*(math.pi)))
        print( "The 80 % of the particles in solution have radius of {0:.3f} and the other 20% have a radius  of {1:.3f} ".format(R1, R2))
        u = 0
        f = 5
        b = 5
        break
    else:
        print("Solution corresponding to the number you have inputted doesn't exist please try again")
N = int(input("Enter a integer number N: "))
positions = [] # inside is [x,y,radii]

fig = plt.gcf() #Defines a figure object
ax = fig.gca() #Defines an axis object
plt.xlim(0,20)
plt.ylim(0,20)

while len(positions) != N:
    add = True
    p = random.randint(u,f)
    position = [(random.randint(0,200) / 10),(random.randint(0,200) / 10)]
    if p < b:
        for x in position:
            R2variant = random.randint(0,1)
            if x + R2variant > 20 or x - R2variant < 0:
                add = False
        valid = checkvalid(positions, [position[0],position[1],R2variant])
        if add == True and valid == True :
            ax.add_patch( plt.Circle(( position[0], position[1] ), radius=R2variant, color = "red" ) )
            positions.append([position[0],position[1],R2variant])
    else:
        for x in position:
            if x + R1 > 20 or x - R1 < 0:
                add = False
        valid = checkvalid(positions, [position[0],position[1],R1])
        if add == True and valid == True :
            ax.add_patch( plt.Circle(( position[0], position[1] ), radius=R1, color = "blue" ) )
            positions.append([position[0],position[1],R1])
  #show the plot
plt.show()

# define the number of random points to generate/ N_sample
num_points = int(input("please input the number of random points you want to generate"))

# initialize counters for valid and invalid points
num_valid = 0
num_invalid = 0

# loop through the specified number of random points
for i in range(num_points):
    # generate a random point within the defined space
    x = random.uniform(0, 20)
    y = random.uniform(0, 20)

    # initialize a flag to check if the point is inside any of the circles
    inside = False

    # loop through the circles in the mixture
    for circle in positions:
        # calculate the distance between the point and the center of the circle
        pythagoras = math.sqrt((x - circle[0]) ** 2 + (y - circle[1]) ** 2)
        # if the distance is less than the radius of the circle, the point is inside the circle
        if pythagoras <= circle[2]:
            inside = True
            break

    # update the counters based on whether the point was inside a circle or not
    if inside:
        num_valid += 1
    else:
        num_invalid += 1

# print the results
print("Number of valid points:", num_valid)
print("Number of invalid points:", num_invalid) 
