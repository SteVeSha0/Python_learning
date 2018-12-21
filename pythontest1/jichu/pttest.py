a = 0

def factory(pos):
    def traveler_move(step):
        nonlocal pos
        new_pos = pos + step
        pos = new_pos
        return pos
    return traveler_move
        

travel = factory(a)
print(travel(2))
print(travel(5))
print(travel(8))