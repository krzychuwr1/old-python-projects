from averages_files.get_data import arithmetic_list,\
    geometric_list, harmonic_list, rms_list, wages_list
from averages_files.averages import arithmetic,\
    geometric, harmonic, rms


count_again = True
while count_again:   # checking for another counting
    ingredients = []
    wages = []
    averages = ('arithmetic', 'geometric', 'harmonic', 'rms')

    print('Which average do you want to count?')  # check which average
    for i in range(4):
        print(str(i) + ':' + averages[i])
    get = 10
    while get not in range(0, len(averages)):
        print('Give number in range 0 to ' + str(len(averages)-1))
        try:
            get = int(input())
        except ValueError:
            print('Give the number.')

    print('Give me the ingredients to count the average')  # count average
    if get == 0:
        ingredients = arithmetic_list()
        wages = wages_list(ingredients)
        print(arithmetic(ingredients, wages))
    elif get == 1:
        ingredients = geometric_list()
        wages = wages_list(ingredients)
        print(geometric(ingredients, wages))
    elif get == 2:
        ingredients = harmonic_list()
        wages = wages_list(ingredients)
        print(harmonic(ingredients, wages))
    elif get == 3:
        ingredients = rms_list()
        wages = wages_list(ingredients)
        print(rms(ingredients, wages))

    print('Do you want to count another average? (type yes or no)')
    again = ''
    while again != 'yes' and again != 'no':
        print('Type yes or no')
        again = input()
        again.lower()
    if again == 'yes':
        count_again = True
    else:
        count_again = False
