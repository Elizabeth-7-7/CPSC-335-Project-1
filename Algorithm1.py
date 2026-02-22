# Algorithm 1: Greedy Approach to Couple sitting next to each other problem
 # Name: Monorandoll Im, Elizabeth Philip
 # Email: monorandoll@csu.fullerton.edu, eliza_philip@csu.fullerton.edu

def swap(row, a,b):
    row[a], row[b] = row[b], row[a]

def swappingCouples(row):

    n = len(row)

    #storing the position in the index of the person
    position = [0] * n 

    #build the position array with the baseline swap amount performed
    for i in range(len(row)):
        position[row[i]] = i
    swaps = 0


    #function to process seating arrangement for two at a time
    for i in range (0, n , 2):
        

        partner = row[i]^1 

        #checking to see if it's the right partner
        if row[i+1] != partner:

            #finding where the correct partner is at
            partner_pos = position[partner]
            wrong_partner = row[i+1]

            
            swap (row, i+1, partner_pos)

            #update position after swap
            position[wrong_partner] = partner_pos
            position[partner] = i+1

            swaps += 1

    return swaps

            

def main(): 
    user= input("Enter the seating with space in between: ")
    row = list(map(int, user.split()))

    result = swappingCouples(row)
    print("Minimum swaps needed: ", result)
    print("New Seating: ", row)

if __name__ == "__main__":
    main()
    input("Press Enter to exit")

