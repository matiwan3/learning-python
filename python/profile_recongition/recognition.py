from deepface import DeepFace
from IPython.display import Image

stalone_path = r'profile_recongition\sylvester stallone.png'
oliwia_path = r'profile_recongition\oliwia brazil.jpg'
ariana_path = r'profile_recongition\ariana grande.jpg'
olga_path = r'profile_recongition\Olga ciemielewska.jpg'
people_list = {stalone_path: 'Sylvester Stallone',oliwia_path: 'Olivia Brazil',ariana_path: 'Ariana Grande',olga_path: 'Olga Ciemielewska'}

counter = 1
for x in people_list:
    print(f'person {counter}: {people_list[x]}')
    Image(filename=x)

    obj = DeepFace.analyze(
        img_path=x,
        actions = ['age','gender','race','emotion'],
        prog_bar = False
    )
    #Recognize gender and print
    print('Gender: ' + obj['gender'])
    
    #Recognize age and print
    get_age = str(obj['age'])
    print('Age: ' + get_age)
    
    #Recognize emotions and print
    emotions = obj['emotion']
    print('Emotion: ' + max(emotions, key=emotions.get))

    #Recognize race and print
    races = obj['race']
    print('Race: ' + max(races, key=races.get))
    counter += 1
    print(f'\n')
    