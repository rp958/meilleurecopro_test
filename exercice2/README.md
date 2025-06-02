# Test technique MeilleurCopro, Exercice 2

## Choses qui ne marchent pas

* dans le main, on essaye de créer un tank avec une armure de type 'steel' or ce n'est pas un type valide. Il faudrait
soit ajouter 'steel' dans la liste des choix acceptés dans le constructeur de Tank (ainsi que ses caractéristiques dans
vulnerable), soit change le type d'armure du tank que l'on crée dans le main (pour un type valide : 'chobham',
'composite' ou 'ceramic').

* l'attribut 'name' n'est pas initialisé dans le constructeur. Dans __repr__, il est donc possible d'avoir une erreur si
le nom n'a pas été rempli (par exemple via set_name). Il faudrait initialiser le nom dans le constructeur ou vérifier
dans __repr__ que le nom est renseigné avant de faire des opérations dessus.

* Dans test_tank_safe, le paramètre test_vehicles n'est pas appelé. J'imagine qu'il s'agit peut-être d'une erreur avec
le nom 'test' dans la boucle for.

* Dans test_tank_safe, le paramètre shooter n'est pas utilisé non plus. Etant donné que le test "if t:" ne semble pas
correct, je suppose que le shooter doit être utilisé lors de ce test.

* dans le main, la boucle while est infinie car index n'est jamais incrémenté. Pour parser la liste tanks, il vaut mieux
utiliser une boucle for comme lorsque l'on donne des noms aux tanks, un peu plus haut.

* La ligne suivante:
m1_2 = Tank(620, 670, 'chobham')
semble erronée. Etant donné le message "Vulnerable to self", il semblerait que l'on veuille tester la vulnérabilité du
tank m1 contre lui-même, or m1_1 et m1_2 n'ont pas les mêmes points d'armure. Si c'est le cas, on pourrait aussi tester m1 contre
lui-même sans créer une deuxième instance, de cette façon :
if m1.vulnerable(m1):
Mais dans ce cas, la ligne qui appelle swap_armor ne sert à rien.

* la liste test n'est plus utilisée après avoir été remplie. Aussi elle boucle pour savoir quels tanks sont vulnérables
contre m1_1, ce qui est aussi fait dans l'appel test_tank_safe plus bas.

* lorsque l'on crée un liste de tanks, on leur donne le même type d'armure et les mêmes valeurs d'armure à chaque fois.
L'issue du programme sera donc toujours la même et le résultat de vulnerable contre m1 identique pour chaque autre tank.
Je ne connais pas les spécificactions du programme, mais sans doute qu'on l'on pourrait randomiser la génération des autres
tanks. Peut-être que l'ont pourrait aussi tester la vulnérabilité de m1 contre les autres tanks.

## Choses qui peuvent être simplifiées ou font partie des bonnes pratiques

* utilisation des F-string plutôt que la notation en %s et la concaténation avec l'opérateur +.

* utiliser des pattern matching plutôt que des if/elif.

* dans le constructeur de tank, on pourrait ajouter les armor_type valides dans une liste plutôt que de les comparer
individuellement à chaque valeur

* ne pas mettre des fonctions au milieu du code main

* mettre le code main dans un if (if __name__ == "__main__":)

* eventuellement mettre test_tank_safe en tant que méthode statique de la classe Tank

* Les manipulations de string dans __repr__ peuvent être écrites en une seule ligne et sans passer par une variable
temporaire

* plutôt que de parser plusieurs fois les tanks (une fois pour les créer et une fois pour les nommer) il est possible
de le faire en une seule étape.

* dans test_tank_safe, on peut s'arrêter de parcourir la boucle dès qu'un tank en sécurité a été trouvé.

* vulnerable retourne True ou False. Dans le main, le 'is True' n'est donc pas nécessaire dans le if suivant :
if m1_1.vulnerable(m1_1) is True:

* quelques utilisations de simple 'quotes' à la place de doubles.

* quelques instructions sur une seule ligne lorsque'il faudrait mettre un retour à la ligne