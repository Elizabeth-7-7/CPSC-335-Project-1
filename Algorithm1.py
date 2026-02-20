# Algorithm 1. Connecting Pairs of Persons

def connect_pairs(row):#Input: row = [0, 2, 1, 3]
    n = len(row)
    
    pos = {}
    for i in range(n):
        person = row[i]
        pos[person] = i
        """"
        person sitting at 'i'
        time complexity: O(1)
        (i = 0 to n-1) and space complexity: O(n)
        each dictionary is  O(1)
        """""

    swaps = 0
    i = 0#checker for the first person in the pair & time O(1)

    
    while i < n:
        first_person = row[i]#O(1)

        if first_person % 2 == 0:#if the first person is even, their partner is the next odd number vice versa
            partner = first_person + 1
        else:
            partner = first_person - 1#O(1)

        if row[i + 1] != partner:#if the partner is not sitting next to the first person then swap
            partner_index = pos[partner]

            # Swap the person at i+1 with the partner
            temp = row[i + 1]
            row[i + 1] = row[partner_index]
            row[partner_index] = temp

            """
            positions in dictionary
            update position of the person who was swapped to the partner's position
            """
            pos[temp] = partner_index
            pos[partner] = i + 1

            swaps += 1
        i += 2
        """
        number of swaps needed to connect the pair
        move to the next pair
        time complexity: O(n) since we are iterating through the row once
        """

    return swaps#and this one is to return the total number of swaps needed to connect all pairs


# ---------------- MAIN PROGRAM ----------------

if __name__ == "__main__":
    print("Enter the numbers separated by spaces:")
    row = []
    user_input = input()
    values = user_input.split()#splits the string which is based on spaces to get a list of strings
    for value in values:#integer
        row.append(int(value))#adds the integer value to the row list

    result = connect_pairs(row)
    print("Minimum swaps required:", result)
