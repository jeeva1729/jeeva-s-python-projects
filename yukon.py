import random
gnum=random.randrange(100)
chances=7
while chances>0:
    mnum=int(input('enter a no:'))
    if mnum==gnum and chances>0:
        print('congratulations')
        break
    elif mnum!=gnum and chances>0:
        print('better luck next time')
        chances=chances-1
    elif chances<=0:
        print('u loose')
        
        
    
