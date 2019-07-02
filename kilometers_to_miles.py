# kilometers_to_miles.py
# A program to convert Kilometers to Miles
# by: Mike Gilson, for ITC110 Summer Qtr 2019

def main () :
        # Explain purpose of program to user
    
    print ("This program converts kilometers to miles.")

        # ask user to input the kilometer measurement they wish to convert to miles
        # for value of "kilometers", save user input as decimal.
    
    kilometers = float(input ("Enter the kilometers: ") )

        # process user's input with the formula to convert to miles
    
    miles = 1.62 * kilometers

        # provide a space to make answer easier to read,
        # and give converted miles, rounded to 2 decimal places.
    
    print (" ")
    print ("That is approximately", round(miles, 2), "miles.")

main ()


