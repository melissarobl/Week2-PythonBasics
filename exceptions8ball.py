import requests
question = input('Enter your question for the magic 8 ball:')
magic_8_ball_url = f'https://magic-8-ball-mctc.uc.r.appspot.com/magic/JSON/{question}'

try:
    response = requests.get(magic_8_ball_url).json()
    answer = response['magic']['answer']  # magic and answer refer to json fields (dictionary). Magic is top tier and answer is info within upper tier
    print(f'The magic 8 ball says.... {answer}')
except Exception as e:
    print(e) #if you as developer wants to know what went wrong
    print('Sorry, can\'t contact the magic 8 ball right now.')

    """this is a doc string (documentation string). Program can generate documents based on doc strings in code """