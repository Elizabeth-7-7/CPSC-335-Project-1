
#Algorithm 2 Greedy Something
#Name: Elizabeth Philip
#Email: eliza_philip@csu.fullerton.edu


def brute_force_preferred_city(distances, fuel, mpg):
    """
    Brute Force Solution
    Time Complexity: O(n^2)
    """
    n = len(distances)

    for start in range(n):
        tank = 0
        valid = True

        for step in range(n):
            city = (start + step) % n

            tank += fuel[city]
            required_fuel = distances[city] / mpg

            if tank < required_fuel:
                valid = False
                break

            tank -= required_fuel

        if valid:
            return start

    return -1


def greedy_preferred_city(distances, fuel, mpg):
    """
    Greedy Solution
    Time Complexity: O(n)
    """
    n = len(distances)
    start = 0
    tank = 0
    total = 0

    for i in range(n):
        gain = fuel[i] - (distances[i] / mpg)
        tank += gain
        total += gain

        # If tank becomes negative,
        # reset start position
        if tank < 0:
            start = i + 1
            tank = 0

    return start


def main():
    # Sample Input
    city_distances = [5, 25, 15, 10, 15]
    fuel = [1, 2, 1, 0, 3]
    mpg = 10

    print("Brute Force Result:",
          brute_force_preferred_city(city_distances, fuel, mpg))

    print("Greedy Result:",
          greedy_preferred_city(city_distances, fuel, mpg))


if __name__ == "__main__":
    main()