def find_farthest_orbit(list_of_orbits):
    list_of_orbits = filter(lambda x: x[0] != x[1], list(list_of_orbits))
    max_area = 0
    orbits_list = list()
    for orbit in list_of_orbits:
        orbits_list.append((orbit[0], orbit[1]))
        if max_area < orbit[0] * orbit[1] * 3.14:
            max_area = orbit[0] * orbit[1] * 3.14
            max_orbit = (orbit[0], orbit[1])
    return max_orbit
