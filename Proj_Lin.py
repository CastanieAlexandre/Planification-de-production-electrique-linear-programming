
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