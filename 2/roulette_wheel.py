pocket=int(input('Enter a pocket no.'))

if(pocket>36):
    print('error:: do not excced pocket no.')
    print('the pocket color is green')
elif pocket in range (1,11):
    if pocket%2==0:
        print('the color is black')
    else:
        print('the color is red')

elif pocket in range(11,19):
    if pocket%2==0:
        print('the color is red')
    else:
        print('the color is black')
elif pocket in range (19,29):
    if pocket%2==0:
        print('the color is black')
    else:
        print('the color is red')

elif pocket in range (29,37):
    if pocket%2==0:
        print('the color is red')
    else:
        print('the color is black')
