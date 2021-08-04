# uncompyle6 version 3.7.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Sep 30 2020, 13:38:04) 
# [GCC 7.5.0]
# Embedded file name: bots/DemoBot.py
# Compiled at: 2014-02-06 15:56:27
def which_side(pw):
    my_planets = pw.my_planets()
    return my_planets[0].y() == 14.2766890117


def get_planet(planets,  y):
    for planet in planets:
        if planet.y() == y:
            return planet.planet_id()
            

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
        e_fleets = pw.enemy_fleets()
        a_fleets = pw.my_fleets()
        planets = pw.planets()



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
