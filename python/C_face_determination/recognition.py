from deepface import DeepFace
from IPython.display import Image

stalone_path = r'sylvester stallone.png'
oliwia_path = r'oliwia brazil.jpg'
ariana_path = r'ariana grande.jpg'
olga_path = r'Olga C.jpg'
mateusz_path = r'Mateusz W.jpg'
seba_path = r'seba ch.png'
people_list = {
            stalone_path: 'Sylvester Stallone',
            oliwia_path: 'Olivia Brazil',
            ariana_path: 'Ariana Grande',
            olga_path: 'Olga C',
            mateusz_path: 'Mateusz W',
            seba_path: 'Sebastian Ch'
}
total_man = 0
total_woman = 0
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
    sex = obj['gender']
    print('Gender: ' + sex)
    if sex == 'Man':
        total_man +=1
    else:
        total_woman += 1
        
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

print(f'Total man: {total_man}\nTotal woman: {total_woman}')