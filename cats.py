print('how many cats?')
numCats = input()
try:
    if int(numCats) >= 4:
        print('That is a lot of Cats!')
    elif int(numCats) < 0:
        print('You cannot enter an negative number')
    else:
        print('That is not that many cats')
except ValueError:
           print('You did not enter a number')
