#sets - they are not ordered!

from pkg_resources import non_empty_lines

cats = set() #creates empty set
cats.add('Lion')
cats.add('Tiger')
print(cats)

cats.add('Cheetah')
print(cats)


birds = {'owl', 'robin', 'swan'}
print(birds)
birds.add('robin')
print(birds)
birds.remove('owl')
birds.add('cardinal')
print(birds)

for bird in birds:
    print(bird)

#lists are ordered, changeable and allow duplicate values
bird_list = ['robin', 'swan', 'swan', 'eagle', 'cardinal', 'swan', 'robin']
bird_list_no_duplicates = list(set(bird_list)) #duplicates not allowed in sets
print(bird_list_no_duplicates)  #will lose order though


cats = {'Leopard', 'Tiger', 'Cheetah'}
print (cats) # {'Tiger', 'Leopard', 'Cheetah'} Why? Sets are not ordered

for cat in cats:
    print(cat)

cats.add('Puma')
cats.remove('Cheetah')
print(cats) #{'Leopard', 'Puma', 'Tiger'}

cats.add('Puma') #{'Leopard', 'Puma', 'Tiger'} no duplicates


#catching errors/exceptions:
def get_random_cat_and_pattern():
    return 'tiger', 'stripes' #return a tuple

# upack your tuple to conveniently get both values in a separate variable
cat, pattern = get_random_cat_and_pattern() # cat = 'tiger', pattern = 'stripes'

data = get_random_cat_and_pattern() # can do this, but usually more work

try:
    print(data[10]) #tiger
except:
    print('oops, that does not exist.')
