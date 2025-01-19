def lemonade_change(bills):
    tens, fives = 0, 0

    for bill in bills:
        if bill == 20:
            if tens > 0:
                tens -= 1
                fives -= 1
            else:
                fives -= 3
        elif bill == 10:
            tens += 1
            fives -= 1
        else:
            fives += 1

        if fives < 0 or tens < 0:
            return False
    return True
