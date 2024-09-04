from datetime import datetime, date, time

today = date.today()
print(today)

tomorrow = date(2020, 8, 19)
print(tomorrow)

next_week = date.fromisoformat('2020-08-24')
print(next_week)

right_now = datetime.now()
print(right_now)


print(right_now.timestamp())  # seconds since 1970

my_date = datetime.fromtimestamp(1800000000) #convert timestamp to useful date
print(my_date)

# tuples can't be changed

city_state = [ ('Seattle', 'WA'), ('Portland', 'OR'), ('San Francisco', 'CA')]
print(len(city_state))

first_city_state = city_state[0]
print(first_city_state)

print(first_city_state[0])
print(first_city_state[1])

city, state = first_city_state  # unpacks each individual value in tuple
print(city)

animals = ('lion', 'puma', 'tiger')
lion, puma, tiger = animals
(print(tiger))

def get_distance():
    miles = 1000
    km = miles * 1.6
    return miles, km # returns tuple
distances = get_distance()
print(distances[0])

miles, km = get_distance()
print(km)




