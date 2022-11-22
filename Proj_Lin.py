#import gurobipy as gp
#heure64,demande64=gp.multidict({'1': 16000, '2': 14000, '3': 16000, '4': 30000, '5': 28000, 
#'6': 25000, '7': 24000, '8': 33000, '9': 41000, '10': 32000, '11': 26000, '12': 22000})


#fonctions retournant l'indice de la periode précédente en fonction de l'option
def prev(periode, option):
    l=[i for i in periode]
    indicePeriode=int(l[1])-1
    if option=='cyclique':
        if indicePeriode==0:
            return 4
        else:
            return indicePeriode-1 
    else:
        if indicePeriode==0:
            return 0
        else:
            return indicePeriode-1 

def prev2(heure, option):
    l=[i for i in heure]
    if len(l)>=3:
        indiceheure=int(l[0]+l[1])
    else :
        indiceheure=int(l[0])
    if option=='cyclique':
        if indiceheure==0:
            return 23
        else:
            return indiceheure-1 
    else:
        if indiceheure==0:
            return 0
        else:
            return indiceheure-1 

def prev3(heure, option):
    indiceheure=int(heure)-1
    #l=[i for i in heure]
    #if len(l)>=3:
    #    indiceheure=int(l[0]+l[1])
    #else :
    #    indiceheure=int(l[0])
    #indiceheure=int(indiceheure-(indiceheure/2))
    if option=='cyclique':
        if indiceheure==0:
            return 11
        else:
            return indiceheure-1 
    else:
        if indiceheure==0:
            return 0
        else:
            return indiceheure-1 

#print([prev3(h,'cyclique') for h in heure64])