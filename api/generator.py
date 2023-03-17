def group_by_type(pokemon_list):
    if pokemon_list == {}:
        return None

    my_groups = {}

    for key in pokemon_list:
        my_groups[pokemon_list[key]['type']] = [pokemon_list[key]['name']]

    return my_groups


def group_by_type_generator(pokemon_list):
    my_groups = {}

    for key in pokemon_list:
        if pokemon_list[key]['type'] in my_groups:
            my_groups[pokemon_list[key]['type']].append(
                pokemon_list[key]['name'])
        else:
            my_groups[pokemon_list[key]['type']] = [pokemon_list[key]['name']]

        yield my_groups


a = group_by_type_generator({0: {"name": "Charizard", "type": "Fire/Flying"}, 1: {
    "name": "Charmander", "type": "Fire"}, 2: {"name": "Bulbasaur", "type": "Grass"}, 3: {"name": "Incineroar", "type": "Fire"}})

assert (next(a) == {'Fire/Flying': ['Charizard']})
assert (next(a) == {'Fire/Flying': ['Charizard'], 'Fire': ['Charmander']})
assert (next(a) == {'Fire/Flying': ['Charizard'],
        'Fire': ['Charmander'], 'Grass': ['Bulbasaur']})
assert (next(a) == {'Fire/Flying': ['Charizard'],
        'Fire': ['Charmander', 'Incineroar'], 'Grass': ['Bulbasaur']})


# Is {} a set or an empty dict? Is empty dict
assert (group_by_type({}) == None)
assert (group_by_type({0: {"name": "Charizard", "type": "Fire/Flying"}, 1: {
        "name": "Charmander", "type": "Fire"}}) == {"Fire/Flying": ["Charizard"], "Fire": ["Charmander"]})


# Complete the generator
