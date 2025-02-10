import random
import time
sticks = random.randint(10, 1000)
time.sleep(1)
print('there are', sticks, 'sticks to remove')
time.sleep(1)

# added this so you can see what you and the computer do without it blazing past quickly

max_Remove = int(input('pick the max amount of sticks to remove (cannot pick more than a quarter of the sticks): '))
if max_Remove > sticks/4:
    print('hey, you can not remove more sticks than the amount of sticks here!')
    time.sleep(1)
    max_Remove = int(input('pick the max amount of sticks to remove: '))

turn = 0
while turn >= 0:

    # checks for remainder

    if turn % 2 == 0:
        turn += turn
        print('it is your turn! pick one through', max_Remove, 'sticks to remove: ')
        remove = int(input('pick the amount of sticks you want to remove: '))
        sticks = sticks - remove
        time.sleep(1)
        print(sticks, 'remain')

    while remove < 1 or remove > max_Remove:
        time.sleep(1)
        print('hey! you cant take more than', max_Remove, 'sticks, or less that 1 stick.')
        time.sleep(1)
        sticks = sticks + remove
        print('it is your turn! pick one through', max_Remove, 'sticks to remove: ')
        remove = int(input('pick the amount of sticks you want to remove: '))
        time.sleep(1)
        sticks = sticks - remove
        print(sticks, 'remain')
    while sticks < 0:
        print('you cant take more sticks than what is there!')
        time.sleep(1)
        sticks = sticks + remove
        print('it is your turn! pick one through', max_Remove, 'sticks to remove: ')
        remove = int(input('pick the amount of sticks you want to remove: '))
        time.sleep(1)
        sticks = sticks - remove
        print(sticks, 'remain')

    # checks to see if the player wins

    if sticks == 0:
        print('the player wins!')
        time.sleep(1)
        print('good job!')
        break

    # checks for remainder, shouldn't be this way, but it works, so I don't really care that much.

    if turn % 2 == 0:
        remove = random.randint(1, max_Remove)
        time.sleep(1)
        print('the computer decides to take', remove, 'sticks')
        time.sleep(1)
        sticks = sticks - remove
        print(sticks, 'remain')

    # computer does not have an actual algorithm (yet), can sometimes take 2 sticks when 1 is left.

    while sticks < 0:
        print('you cant take more sticks than what is there!')
        sticks = sticks + remove
        remove = random.randint(1, max_Remove)
        time.sleep(1)
        print('the computer decides to take', remove, 'sticks')
        time.sleep(1)
        sticks = sticks - remove
        print(sticks, 'remain')
        time.sleep(1)

    # checks to see if the computer wins

    if sticks == 0:
        print('the computer wins!')
        time.sleep(1)
        print('better luck next time!')
        break