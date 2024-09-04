import requests
question = input('Enter your question for the magic 8 ball:')
magic_8_ball_url = f'https://magic-8-ball-mctc.uc.r.appspot.com/magic/JSON/{question}'

try:
    response = requests.get(magic_8_ball_url).json()
    answer = response['magic']['answer']
    print(f'The magic 8 ball says.... {answer}')
except Exception as e:
    print(e) #if you as developer wants to know what went wrong
    print('Sorry, can\'t contact the magic 8 ball right now.')