
#James Filip
#12/22/2021

#this program performes circle, sphere, square, and cube calculations depending on user input

#thi function collects and stores user inputs for number and measurment type
def getUserInput():
    userSize = float(input("Enter Size for radius/side: "))
    userMeasure = input("Enter Unit of measure, e.g., inches: ")
    return userSize, userMeasure

#this function handles all displaying and formatting of calculations
def displayCircleResults(size, measure):


# this imports our "geometry.py" file
    import geometry
    print ()
    
    print ("Circle results")
    print ("-" * 14)
    
    print (format("Circumference: ", "20s"), geometry.circleCircum(size), measure)
    print (format("Area: ", "20s"), geometry.circleArea(size), measure)
    print ()
    
   
def displaySphereResults(size, measure):
    import geometry
    print ("Sphere Results")
    print ("-" * 14)

    print (format("Volume: ", "20s"), geometry.sphereVolume(size), measure)
    print (format("Surface Area: ", "20s"), geometry.sphereArea(size), measure)
    print ()


def displaySquareResults(size, measure):
    import geometry
    print ("Square Results")
    print ("-" * 14)

    print (format("Perimeter: ", "20s"), geometry.squarePerimiter(size), measure)
    print (format("Area: ", "20s"), geometry.squareArea(size), measure)
    print ()

    print ("Cube Results")
    print ("-" * 14)

def displayVolumeResults(size, measure):
    import geometry

    print (format("Volume: ", "20s"), geometry.cubeVolume(size), measure)
    print (format("Area: ", "20s"), geometry.cubeArea(size), measure)
    print ()
    

#test 1: I was recieving errors during my first tests, this was because I had
    # not added userSize, userMeasure = getUserInput() to the function
    
#test 2: calculations were slightly off, edited with round() and correct math, working now

#test 3: outputs are all correct, but formatting is off, two new lines instead of 1..hmmm

#test 4: after replacing print("\n") with print(), function now only prints 1 new line.    

#I approached this project by trying to simplify the steps without coding too mucn,
    # I wanted to make sure that one calculation would work, and next to see if would return correctly.
        # worrying about the formatting last 
# I tested my program with long numbers beofore and after the decimal.
    # output was identical to google calcualtor

#complex scripts can be easily broken down into steps,
    # validating one feature at a time before moving on.

    
def main():
    # this is our returned data give by the user,
    size, measure = getUserInput()
    
   
    displayCircleResults(size, measure)
    displaySphereResults(size, measure)

    displaySquareResults(size, measure)
    displayVolumeResults(size, measure)
    
main()

