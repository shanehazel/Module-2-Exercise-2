# pseudocode

# make a method
def process ():

    # open students.txt file (read)
    with open("students.txt") as input_file:

        # assign variables for highest GWA and the student with highest grade
        high_gwa = 2
        high_student = ""

        # read students.txt line by line
        for line in input_file:

            # separate the names and their respective GWA
            names, gwa = line.strip().split(" = ")

            # make the GWA a float
            gwa = float(gwa)

            # if the current gwa is higher than the highest gwa, update the variables
            if gwa < high_gwa:
                high_gwa = gwa
                high_student = names

        # print output
        print(high_student, "got the highest GWA of", high_gwa)

# end of method
process ()