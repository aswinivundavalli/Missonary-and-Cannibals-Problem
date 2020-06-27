missionariesNumber = int()
cannibalsNumber = int()


def get():
    """
    Gather the inputs from user

    @return: None
    """
    global missionariesNumber, cannibalsNumber
    missionariesNumber = int(input("Enter no.of missionaries to cross the river= "))
    cannibalsNumber = int(input("Enter no.of cannibals to cross the river= "))


def displayPosition():
    """
    Display the position of Missionaries and cannibals on each side
    of the river

    @return: None
    """
    global left, right, boatDirection, side
    print("\nleft side\tright side\n")
    print(left[0], left[1], left[2], "\t\t", right[0], right[1], right[2])
    print(left[3], left[4], left[5], "\t\t", right[3], right[4], right[5])
    if boatDirection % 2 == 0:
        side = True
        print("\nBoat on right side of river\n")
    else:
        side = False
        print("\nBoat on leftside of river\n")

def boat_lr():
    global ml_count, mr_count, cl_count, cr_count, left, right
    for i in range(0, missionariesNumber):
        if left[0] == 'M':
            left[0] = ' '
            right[0] = 'M'
            ml_count -= 1
            mr_count += 1
        elif left[1] == 'M':
            left[1] = ' '
            right[1] = 'M'
            ml_count -= 1
            mr_count += 1
        elif left[2] == 'M':
            left[2] = ' '
            right[2] = 'M'
            ml_count -= 1
            mr_count += 1
    for i in range(0, cannibalsNumber):
        if left[3] == 'C':
            left[3] = ' '
            right[3] = 'C'
            cl_count -= 1
            cr_count += 1
        elif left[4] == 'C':
            left[4] = ' '
            right[4] = 'C'
            cl_count -= 1
            cr_count += 1
        elif left[5] == 'C':
            left[5] = ' '
            right[5] = 'C'
            cl_count -= 1
            cr_count += 1


def boat_rl():
    global ml_count, mr_count, cl_count, cr_count, left, right
    for i in range(0, missionariesNumber):
        if right[0] == 'M':
            right[0] = ' '
            left[0] = 'M'
            ml_count += 1
            mr_count -= 1
        elif right[1] == 'M':
            right[1] = ' '
            left[1] = 'M'
            ml_count += 1
            mr_count -= 1
        elif right[2] == 'M':
            right[2] = ' '
            left[2] = 'M'
            ml_count += 1
            mr_count -= 1
    for i in range(0, cannibalsNumber):
        if right[3] == 'C':
            right[3] = ' '
            left[3] = 'C'
            cl_count += 1
            cr_count -= 1
        elif right[4] == 'C':
            right[4] = ' '
            left[4] = 'C'
            cl_count += 1
            cr_count -= 1
        elif right[5] == 'C':
            right[5] = ' '
            left[5] = 'C'
            cl_count += 1
            cr_count -= 1


# Flag to indicate the boat side
# odd no. indicates boat is on left side and even no. indicates boat is on right side
boatDirection = 1
ml_count = cl_count = 3
mr_count = cr_count = 0
left = ['M', 'M', 'M', 'C', 'C', 'C']
right = [' ', ' ', ' ', ' ', ' ', ' ']
side = False
while True:
    if (cl_count > ml_count > 0) or (cr_count > mr_count > 0):
        print("\n\n~~~~~~~~~~~~~~~~YOU LOST!!~~~~~~~~~~~~~~~~\n")
        break
    elif (cr_count == mr_count) and (cr_count == 3 and mr_count == 3):
        print("\n\n~~~~~~~~~~~~~~~~YOU WON!!~~~~~~~~~~~~~~~~\n")
        break
    else:
        displayPosition()
        get()
        if missionariesNumber >= 3 or cannibalsNumber >= 3 or missionariesNumber < 0 or cannibalsNumber < 0:
            print("number not in range")
            continue
        elif (missionariesNumber + cannibalsNumber) > 2 or (missionariesNumber + cannibalsNumber == 0):
            print("boat should have atleast 1 person and atmost 2 persons")
            continue
        if not side:
            boat_lr()
        else:
            boat_rl()
    boatDirection += 1