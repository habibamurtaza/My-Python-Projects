
Gryffindor=0
Ravenclaw=0
Hufflepuff=0
Slytherin=0

print('===============')
print('The Sorting Hat')
print('===============')

q1=int(input('''Q1) Do you like Dawn or Dusk?
                        1) Dawn
                        2) Dusk
    '''))
if q1== 1:
        Gryffindor +=1
        Ravenclaw +=1
elif q1==2:
        Hufflepuff +=1
        Slytherin +=1
else:
    print("Wrong input.")


q2=int(input('''Q2) When I’m dead, I want people to remember me as:
                        1) The Good
                        2) The Great
                        3) The Wise
                        4) The Bold
    '''))

if q2==1:
    Hufflepuff += 2
elif q2==2:
    Slytherin +=2
elif q2==3:
    Ravenclaw +=2
elif q2==4:
    Gryffindor +=2
else:
    print("Wrong input.")

q3=int(input('''Q3) Which kind of instrument most pleases your ear?
                        1) The violin
                        2) The trumpet
                        3) The piano
                        4) The drum
    '''))

if q3==1:
    Slytherin +=4
elif q3==2:
    Hufflepuff +=4
elif q3==3:
    Ravenclaw +=4
elif q3==4:
    Gryffindor +=4
else:
    print("Wrong input.")

      
print("Gryffindor: ", Gryffindor)
print("Ravenclaw: ", Ravenclaw)
print("Hufflepuff: ", Hufflepuff)
print("Slytherin: ", Slytherin)

if Gryffindor >= Ravenclaw and Gryffindor >= Hufflepuff and Gryffindor >= Slytherin:
  print('🦁 Gryffindor!')
elif Ravenclaw >= Hufflepuff and Ravenclaw >= Slytherin:
  print('🦅 Ravenclaw!')
elif Hufflepuff >= Slytherin:
  print('🦡 Hufflepuff!')
else:
  print('🐍 Slytherin!')
