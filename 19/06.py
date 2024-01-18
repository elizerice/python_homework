def find_farthest_orbit(list_of_orbits):
    orbits_sq_list= []
    orbits_list = []
    [orbits_sq_list.append((orbit[0] * orbit[1])) for orbit in filter(lambda x: x[0] != x[1], list(list_of_orbits)) if orbit[0] != orbit[1]]
    [orbits_list.append(i) for i in list_of_orbits if sorted(orbits_sq_list, reverse=True)[0] == i[0] * i[1]]
    return orbits_list
