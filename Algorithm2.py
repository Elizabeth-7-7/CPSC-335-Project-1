
#Algorithm 2 Greedy Approach to Hamiltonian Problem
#Name: Monorandoll Im, Sehaj Dhaliwal, and Elizabeth Philip
#Email: monorandoll@csu.fullerton.edu, dhaliwalsehaj36@csu.fullerton.edu, eliza_philip@csu.fullerton.edu

def preferred_starting_city(distances, fuel, mpg):

    n = len(distances)
    start = 0
    tank = 0
    total = 0

    for i in range(n):#O(n)
        gain = fuel[i] * mpg - distances[i]# Calculate net gain/loss of gas at city i
        tank += gain # Update current gas in tank

        # If tank becomes negative, reset start position
        if tank < 0:
            start = i + 1 #city i is distance[i] away from city i + 1
            tank = 0# tank always starts out empty

    return start

# ---------------- MAIN PROGRAM ----------------

def main():
    # Sample input
    city_distances = [5, 25, 15, 10, 15]
    fuel = [1, 2, 1, 0, 3]
    mpg = 10

    print("The Preferred starting city for the sample above is city: ",
          preferred_starting_city(city_distances, fuel, mpg))


if __name__ == "__main__":
    main()

