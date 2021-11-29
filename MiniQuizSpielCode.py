print('Wilkommen im QuizSpiel')
answer=input('Möchtest du das Spiel starten ? (Ja/Nein) :')
score=0
total_questions=3
 
if answer.lower()=='Ja':
    answer=input('Frage 1: Von wem stammt das Gemälde von Mona Lisa')
    if answer.lower()=='Leonardo Da Vinci':
        score += 1
        print('Richtig!')
    else:
        print('Leider Falsch :(')
 
 
    answer=input('Frage 2: Wie hieß der erste deutsche Bundeskanzler? ')
    if answer.lower()=='Konrad Adenauer':
        score += 1
        print('Richtig!')
    else:
        print('Leider Falsch :(')
 
    answer=input('Frage 3: Wie lautete der frühere Name Istanbul?')
    if answer.lower()=='Konstantinopel':
        score += 1
        print('Richtig!')
    else:
        print('Leider Falsch :(')

# Fragen können im Code beliebig angepasst werden!
 
print('Danke, dass du mitgespielt hast! Du hast ',score,"richtig beantwortet!")
mark=(score/total_questions)*100
print('Marks obtained:',mark)
print('Auf Wiedersehen!')