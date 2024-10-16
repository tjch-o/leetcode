def will_collide(r1, r2):
    return r1 > 0 and r2 < 0


def asteroid_collision(asteroids):
    stack = [asteroids[0]]
    n = len(asteroids)
    i = 1

    while i < n:
        curr = asteroids[i]
        while stack and will_collide(stack[-1], curr):
            if abs(stack[-1]) == abs(curr):
                stack.pop()
                break
            elif abs(stack[-1]) < abs(curr):
                stack.pop()
            else:
                break

        else:
            stack.append(curr)
        i += 1
    return stack
