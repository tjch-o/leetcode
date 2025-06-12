def collide(a1, a2):
    return a1 > 0 and a2 < 0


def asteroid_collision(asteroids):
    stack = []

    for asteroid in asteroids:
        while stack and collide(stack[-1], asteroid):
            if abs(stack[-1]) > abs(asteroid):
                break
            elif abs(stack[-1]) == abs(asteroid):
                stack.pop()
                break
            else:
                stack.pop()
                continue
        else:
            stack.append(asteroid)
    return stack
