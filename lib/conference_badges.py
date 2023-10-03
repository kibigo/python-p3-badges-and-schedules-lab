def badge_maker(name):
    return (f"Hello, my name is {name}.")

def batch_badge_creator(names):
    return [f"Hello, my name is {name}." for name in names]

def assign_rooms(names):
    rooms = []
    for i, name in enumerate(names, start=1):
        rooms.append(f"Hello, {name}! You'll be assigned to room {i}!")
    return rooms

def printer(names):
    badges = batch_badge_creator(names)
    assigned_rooms = assign_rooms(names)

    for badge in badges:
        print (badge)
    for room in assigned_rooms:
        print(room)
