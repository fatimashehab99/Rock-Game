import random

running=True
choices=('Rock','Scissor','Paper')

#Starting the game
while running:
 user=None
 #Computer Choices
 computer=random.choice(choices)

#Rechoosing an input if it is not available in the choices 
 while user not in choices:
  user=input('Enter a choice(Rock,Scissor,Paper):')

#Printing the results
 print({'User':user,'Computer':computer})
 
 #When choosing the same choice
 if(user==computer):
     print('It is a tie')
#Evaluting the Winnner   
 elif(user=='Rock'):
    if(computer=='Scissor'):
        print('User win')
    else:
        print('Computer wins')
        
 elif(user=='Paper'):
    if(computer=='Rock'):
        print('User win')
    else:
        print('Computer wins')
        
 elif(user=='Scissor'):
    if(computer=='Paper'):
        print('User win')
    else:
        print('Computer wins')
        
#Asking the user if he want to play again 
 play_again=input('PLay again(y/n):').lower()
 if not play_again=='y':
     running=False
     
 print('Thanks for playing')