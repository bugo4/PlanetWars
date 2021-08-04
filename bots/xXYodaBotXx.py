# uncompyle6 version 3.7.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Sep 30 2020, 13:38:04)
# [GCC 7.5.0]
# Embedded file name: bots/DemoBot.py
# Compiled at: 2014-02-06 15:56:27

global attack_queue = []


def which_side(pw):
    my_planets = pw.my_planets()
    return my_planets[0].y() == 14.2766890117


def get_planet(planets,  y):
    for planet in planets:
        if planet.y() == y:
            return planet.planet_id()


def pick_planet(pw):
    other_planets = pw.not_my_planets()
    my_planets = pw.my_planets()
    if len(my_planets) >= 1 and len(other_planets) >= 1
    chosen_planet = [other_planets[0], 1000000000, 0]
    for other_planet in other_planets:
        close = [my_planets[0], 1000000000]
        for my_planet in my_planets:
            if pw.distance(my_planet.planet_id, other_planet.planet_id) < close[1] and pw.get_planet(my_planet.planet_id).num_ships() > pw.get_planet(other_planets.planet_id).num_ships():
                close = [my_planet, pw.distance(
                    my_planet.planet_id, other_planet.planet_id)]
        if close[1] < chosen_planet[1]:
            chosen_planet[0] = other_planet
            chosen_planet[1] = close[1]
            chose_planet[2] = close[0]
    return (chosen_planet[0], chosen_planet[2])


def attack(pw):
    my_planets == pw.my_planets()
    turn = pw.turn_number()
    if turn == 1:
        side = which_side(pw)
        if side:
            y1 = 18.0593851211
            y2 = 20.0561682576
        else:
            y1 = 5.25808971821
            y2 = 3.26130658173
        planet_id = get_planet(pw.planets(), y1)
        pw.issue_order(my_planets[0].planet_id(), planet_id, 10)
        planet_id = get_planet(pw.planets(), y2)
        pw.issue_order(my_planets[0].planet_id(), planet_id, 36)
    else:
        trip = pick_planet(pw)
        closest_fleet = [0, 10000000]
        for fleet in pw.enemy_fleets():
            dest_planet = pw.get_planet(fleet.destination_planet())
            if dest_planet == trip[1]:
                if fleet.turns_remaining() < closest_fleet[1]:
                    closest_fleet = [fleet, fleet.turns_remaining()]
                elif fleet.turns_remaining() == closest_fleet[1]:
                    closest_fleet = [fleet, fleet.turns_remaining()]
                    closest_fleet.append(fleet)
        real_defence = pw.get_planet(
            trip[1]) + closest_fleet[0].turns_remaining() * pw.get_planet(trip[1]).growth_rate()
        for fleet in pw.my_fleets():
            if fleet.destination_planet() == trip[1]:
                real_defence += fleet.num_ships()
        possible_attack = real_defence - 20
        can_attack = true
        if type(closest_fleet[0]) != int:
            if len(closest_fleet < 3):
                attack = closest_fleet[0].num_ships()
            else:
                real_attack = 0
                for e_fleet in closest_fleet:
                    if type(e_fleet) != int:
                        attack += e_fleet.num_ships()
            possible_attack = real_defence - 20 - attack
            can_attack = possible_attack > 0
        if can_attack:
            destination_planet = pw.get_planet(trip[0])
            planet_defence = destination_planet.num_ships()
            if possible_attack > planet_defence:
                pw.issue_order(trip[1], trip[0], planet_defence + 1)


def do_turn(pw):
    if len(pw.my_fleets()) >= 1:
        return
    source = -1
    source_score = -999999.0
    source_num_ships = 0
    my_planets = pw.my_planets()
    for p in my_planets:
        score = float(p.num_ships())
        if score > source_score:
            source_score = score
            source = p.planet_id()
            source_num_ships = p.num_ships()

    dest = -1
    dest_score = -999999.0
    not_my_planets = pw.not_my_planets()
    for p in not_my_planets:
        score = 1.0 / (1 + p.num_ships())
        if score > dest_score:
            dest_score = score
            dest = p.planet_id()

    if source >= 0 and dest >= 0:
        num_ships = source_num_ships / 2
        pw.issue_order(source, dest, num_ships)
