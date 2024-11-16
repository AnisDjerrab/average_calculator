import tkinter as tk

fenetre = tk.Tk()
fenetre.geometry("1000x800")
fenetre.title("fenetre d'essai tkinter")
canvas = tk.Canvas(width=1000, height=650, bg="lightgray")
canvas.pack(side="bottom", padx=5, pady=5)
canvas2 = tk.Canvas(width=1000, height=150, bg="lightgray")
canvas2.pack(side="top", padx=5, pady=5)


canvas2.create_rectangle(10, 10, 500, 50)
canvas2.create_rectangle(530, 10, 700, 50)
canvas2.create_rectangle(730, 10, 980, 50)
canvas2.create_rectangle(10, 60, 250, 110)
canvas2.create_rectangle(270, 60, 400, 110)
canvas2.create_rectangle(410, 60, 550, 110)
canvas2.create_rectangle(560, 60, 690, 110)
canvas2.create_rectangle(700, 60, 800, 110)
canvas2.create_rectangle(820, 60, 980, 110)
canvas2.create_text(250, 30, text="Bienvenue sur la plateforme de calcul de moyenne !", font=("arial", 14), fill="darkblue")
canvas2.create_text(615, 30, text="Classe : 4AM2", font=("arial", 14), fill="darkblue")
canvas2.create_text(855, 30, text="Elève : AnisDJE_voyager1", font=("arial", 14), fill="darkblue")
canvas2.create_text(135, 85, text="Matières", font=("arial", 16), fill="darkblue")
canvas2.create_text(335, 85, text="Controle", font=("arial", 16), fill="darkblue")
canvas2.create_text(480, 85, text="Devoir", font=("arial", 16), fill="darkblue")
canvas2.create_text(625, 85, text="Examen", font=("arial", 16), fill="darkblue")
canvas2.create_text(750, 85, text="Coeff", font=("arial", 16), fill="darkblue")
canvas2.create_text(900, 85, text="Moyenne locale", font=("arial", 16), fill="darkblue")



matieres = ["arabe", "math", "francais", "anglais", "histoire geo", "education civique", "islam", "physique", "SVT", "sport", "informatique"]
coefficient = [5, 4, 3, 2, 3, 1, 1, 2, 2, 1, 1]
devoirs = [None] * len(matieres)
examen = [None] * len(matieres)
controle = [None] * len(matieres)
def recuperer_nombre(entry, index):
    try:
        devoirs[index] = float(entry.get())
        print(f"Devoirs[{index}] mis à jour : {devoirs[index]}")
    except ValueError:
        nombre = None
        print("entrée invalide")

def recuperer_nombre_examen(entry, index):
    try:
        examen[index] = float(entry.get())
        print(f"Examen[{index}] mis à jour : {examen[index]}")
    except ValueError:
        nombre = None
        print("entrée invalide")

def recuperer_nombre_controle(entry, index):
    try:
        controle[index] = float(entry.get())
        print(f"Controle[{index}] mis à jour : {controle[index]}")
    except ValueError:
        nombre = None
        print("entrée invalide")
x = 10

while x <= 550:
    canvas.create_rectangle(50 ,x  , 250 , x + 50)
    x += 50

x = 10
for i in matieres:
    canvas.create_text(150, x + 25, text=f"{i}", font=("Arial", 14), fill="darkblue")
    x += 50
y = 10

u = 10
while u <= 550:
    canvas.create_rectangle(700 ,u , 800 , u + 50)
    u += 50
u = 10

canvas.create_rectangle(700, 570, 950, 620) 
canvas.create_rectangle(50, 570, 685, 620)
while u <= 550:
    canvas.create_rectangle(820 ,u , 950 , u + 50)
    u += 50
for i in coefficient:
    canvas.create_text(750, y + 25, text=f"{i}", font=("Arial", 14), fill="darkblue")
    y += 50
x = 10
for i in range(len(matieres)):
    entry = tk.Entry(fenetre, font=("Arial", 14), width=10)
    button = tk.Button(fenetre, text="ok", font=("Arial", 10), width=4,
                       command=lambda e=entry, idx=i: recuperer_nombre(e, idx))
    canvas.create_window(480, x + 25, window=entry)  
    canvas.create_window(530, x + 25, window=button)
    x += 50

x = 10
for i in range(len(matieres)):
    entry = tk.Entry(fenetre, font=("Arial", 14), width=10)
    button = tk.Button(fenetre, text="ok", font=("Arial", 10), width=4,
                       command=lambda e=entry, idx=i: recuperer_nombre_examen(e, idx))
    canvas.create_window(620, x + 25, window=entry)  
    canvas.create_window(670, x + 25, window=button)
    x += 50

u = 10
for i in range(len(matieres)):
    entry = tk.Entry(fenetre, font=("Arial", 14), width=10)
    button = tk.Button(fenetre, text="ok", font=("Arial", 10), width=4,
                       command=lambda e=entry, idx=i: recuperer_nombre_controle(e, idx))
    canvas.create_window(330, u + 25, window=entry)  
    canvas.create_window(380, u + 25, window=button)
    u += 50

def verifier_listes():
    if all(v is not None for v in devoirs) and all(o is not None for o in examen) and all(s is not None for s in controle):
        print("Toutes les notes ont été saisies.")
        print("Devoirs :", devoirs)
        print("Examen :", examen)
        print("Controle :", controle)
        p = 0
        moyenne_matieres = []
        for i in range(len(matieres)):
            c = controle[p]
            d = devoirs[p]
            m = examen[p]
            N = (c+d+2*m)/4
            moyenne_matieres.append(N)
            print(moyenne_matieres)
            p +=1
        y = 10
        for i in moyenne_matieres:
            canvas.create_text(870, y + 25, text=f"{i:.2f}", font=("Arial", 14), fill="darkblue")
            y += 50

        moyenne_generale = (moyenne_matieres[0]*5+moyenne_matieres[1]*4+moyenne_matieres[2]*3+moyenne_matieres[3]*2+moyenne_matieres[4]*3+moyenne_matieres[5]+moyenne_matieres[6]+moyenne_matieres[7]*2+moyenne_matieres[8]*2+moyenne_matieres[9]+moyenne_matieres[10])/25
        canvas.create_text(800, 595, text=f"Moyenne : {moyenne_generale:.2f}", font=("Arial", 14), fill="darkblue")
        if moyenne_generale == 15 or moyenne_generale > 15:
            canvas.create_text(390, 595, text="Excellent ! Avec les felicitation du jury !", font=("Arial", 14), fill="darkblue")
        elif moyenne_generale == 10 or moyenne_generale > 10:
            canvas.create_text(390, 595, text="""Note moyenne. Nous esperons de votre part 
                                    plus d'efforts la prochaine fois.""", font=("Arial", 14), fill="darkblue")
        elif moyenne_generale > 0:
            canvas.create_text(390, 595, text="""Notes catastrophiques. cependant tous n'est pas perdu, 
                    il faudra travailler dur la prochaine fois.""", font=("Arial", 14), fill="darkblue")
        else:
            canvas.create_text(390, 595, text="Erreur ! moyenne non valide.", font=("Arial", 14), fill="darkblue")
    else:
        fenetre.after(500, verifier_listes)


verifier_listes()



fenetre.mainloop()