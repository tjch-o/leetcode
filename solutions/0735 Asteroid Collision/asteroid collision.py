def will_collide(a1, a2):
    return a1 > 0 and a2 < 0

def asteroid_collision(asteroids):
    stack = []

    for asteroid in asteroids:
        while stack and will_collide(stack[-1], asteroid):
            if abs(stack[-1]) == abs(asteroid):
                stack.pop()
                break
            elif abs(asteroid) > abs(stack[-1]):
                stack.pop()
            else:
                break
        
        else:
            stack.append(asteroid)
    return stack
