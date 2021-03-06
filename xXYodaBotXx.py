# uncompyle6 version 3.7.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Sep 30 2020, 13:38:04) 
# [GCC 7.5.0]
# Embedded file name: bots/DemoBot.py
# Compiled at: 2014-02-06 15:56:27


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
