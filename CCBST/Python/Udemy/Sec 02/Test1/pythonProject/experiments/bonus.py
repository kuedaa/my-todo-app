contents = ["L'hommme est un loup pour l'homme depuis la nuit des temps, donc mefier vosud e vos prochains",
            "Il aime trop les figures de style dans ses propos, donc il faut faire face a ces contournements de langages",
            "Il aime lire les bouquins tres mistiques tels ques les aventures misterieuses ecrites par Patrick Ngema Ndong"]
filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for content, filename in zip (contents, filenames) :
    file = open(rf"..\files\{filename}", 'w')
    file.write(content)

filestoedit = open(rf"..\files\doc.txt", 'r')
contenus =  filestoedit.readlines()
contenus.append("Serge")
print(contenus)
alpha = 0

for contenu in contenus :
    print(contenu)
    alpha = alpha +1
    print(alpha)