import random
sticks = random.randint(10,50)
print('there are', sticks,'sticks to remove')

# turn initialized to start the process of turns

turn = 0
while turn >= 0 :

    # checks for remainder
    
    if turn % 2 == 0:
        turn += turn
        remove = int(input('it is your turn! pick one or two sticks to remove: '))
        sticks = sticks - remove
        print(sticks,'remain')

    # while statements to prevent cheating from the player

    while remove < 1 or remove > 2:
        print('hey! you cant take more than 2 sticks, or less that 1 stick.')
        sticks = sticks + remove
        remove = int(input('it is your turn! pick one or two sticks to remove: '))
        sticks = sticks - remove
        print(sticks, 'remain')
    while sticks < 0:
        print('you cant take more sticks than what is there!')
        sticks = sticks + remove
        remove = int(input('it is your turn! pick one or two sticks to remove: '))
        sticks = sticks - remove
        print(sticks, 'remain')

    # checks to see if the player wins

    if sticks == 0:
        print('the player wins!')
        break

    # checks for remainder, shouldn't be this way, but it works, so I don't really care that much.

    if turn % 2 == 0:
        remove = random.randint(1,2)
        print ('the computer decides to take',remove, 'sticks')
        sticks = sticks - remove
        print(sticks,'remain')

    # computer does not have an actual algorithm (yet), can sometimes take 2 sticks when 1 is left.

    while sticks < 0:
        print('you cant take more sticks than what is there!')
        sticks = sticks + remove
        remove = random.randint(1,2)
        print('the computer decides to take', remove, 'sticks')
        sticks = sticks - remove
        print(sticks, 'remain')

    # checks to see if the computer wins

    if sticks == 0:
        print('the computer wins!')
        break