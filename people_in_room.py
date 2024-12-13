def f(detector):
#Returns True if at least 3 people were in the room at the same time, False otherwise.

#NOBODY WAS IN THE ROOM WHEN IT HAPPEN AHHH MOMENT 
    people_in_room = 0
    
    for action in detector:
        if action == "+":
            people_in_room += 1
        elif action == "-":
            people_in_room -= 1
        
        # Check if at least 3 people are in the room
        if people_in_room >= 3:
            return True
    
    return False
