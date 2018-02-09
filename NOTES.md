# Notes:

## Commandes:

* cd: Change Directory: Se déplacer dans les dossiers
* ls: Lister les dossiers et fichiers

Lien pour site HTML Accueil: file:///home/enzo/workspace/Forum/1_webapp/index.html
<p> = Faire un paragraphe
<br /> = Passer une lignePanel footer
Lien Forum Site HTML: file:///home/enzo/workspace/Forum/1_webapp/forum.html

Linux: Commandes de base:

Changer de répertoire

Ex : cd /home/username

Lister un répertoire

Ex : ls /home/username

Supprimer un fichier

Ex : rm /home/username/filename

Créer un dossier

Ex : mkdir /home/username/new_dir

Copier un fichier

Ex : cp /tmp/file /etc/file_copy

Déplacer un fichier

Ex : mv /old/dir/file /new/dir/file_copy

Ex : Lister un répertoire avec ses fichiers invisibles : ls -a

Ex : Se connecter à mysql avec l'utilisateur root (demande le pass) : mysql -u "root" -p


Faire un lien symbolique

Ex : ln -s /path/file /path/link

Lire le contenu d'un fichier

Ex : cat home/username/filename

Créer un fichier vide

Ex : touch /home/username/new_file

Changer d'utilisateur

Ex : su new_user

Trouver les fichiers qui contiennent une chaîne

Ex : grep -r 'chaine' /path/to/repository

Remplacer une chaîne "search" par "replace" dans tous les fichiers ".php" d'un répertoire

Ex : find ./ -type f -exec sed -i '' 's#search#replace#' *.php {} \;

adresse serveur site internet: 192.168.33.33

Commandes pour mettre à jour mon projet GitHub depuis ma machine:

 Vous pouvez proposer un changement (l'ajouter à l'Index) en exécutant les commandes
git add <filename>
git add *
C'est la première étape dans un workflow git basique. Pour valider ces changements, utilisez
git commit -m "Message de validation"
Le fichier est donc ajouté au HEAD, mais pas encore dans votre dépôt distant.
envoyer des changements

Vos changements sont maintenant dans le HEAD de la copie de votre dépôt local. Pour les envoyer à votre dépôt distant, exécutez la commande
git push origin master
Remplacez master par la branche dans laquelle vous souhaitez envoyer vos changements.

Zone de texte multiligne

Pour créer une zone de texte multiligne, on change de balise : nous allons utiliser<textarea> </textarea>

on peut modifier la taille du<textarea>de deux façons différentes.

En CSS : il suffit d'appliquer les propriétés CSSwidthetheightau<textarea>.
Avec des attributs : on peut ajouter les attributsrowsetcolsà la balise<textarea>. Le premier indique le nombre de lignes de texte qui peuvent être affichées simultanément, et le second le nombre de colonnes.

E-mail

Vous pouvez demander à saisir une adresse e-mail :

<input type="email" /> 

Nombre

Ce champ permet de saisir un nombre entier :

<input type="number" />

Une URL

Avec le typeurl, on peut demander à saisir une adresse absolue (commençant généralement parhttp://) :

<input type="url" />

Numéro de téléphone

Ce champ est dédié à la saisie de numéros de téléphone :

<input type="tel" />

Un curseur

Le typerangepermet de sélectionner un nombre avec un curseur (aussi appelé slider), comme à la figure suivante :

<input type="range" />

Couleur

Ce champ permet de saisir une couleur :

<input type="color" />


Date

Différents types de champs de sélection de date existent :

date: pour la date (05/08/1985 par exemple) ;
time: pour l'heure (13:37 par exemple) ;
week: pour la semaine ;
month: pour le mois ;
datetime: pour la date et l'heure (avec gestion du décalage horaire) ;
datetime-localpour la date et l'heure (sans gestion du décalage horaire).
Exemple :

<input type="date" />

Recherche

On peut créer un champ de recherche comme ceci :

<input type="search" />


Les cases à cocher

Créer une case à cocher ? Rien de plus simple ! Nous allons réutiliser la balise<input />, en spécifiant cette fois le typecheckbox:

<input type="checkbox" name="choix" />
Rajoutez un<label>bien placé, et le tour est joué !


Enfin, sachez que vous pouvez faire en sorte qu'une case soit cochée par défaut avec l'attributchecked:

<input type="checkbox" name="choix" checked />



Les zones d'options

Les zones d'options vous permettent de faire un choix (et un seul) parmi une liste de possibilités. Elles ressemblent un peu aux cases à cocher mais il y a une petite difficulté supplémentaire : elles doivent être organisées en groupes. Les options d'un même groupe possèdent le même nom (name), mais chaque option doit avoir une valeur (value) différente.

La balise à utiliser est toujours un<input />, avec cette fois la valeurradiopour l'attributtype.

Les choses seront plus claires sur l'exemple ci-dessous :

<form method="post" action="traitement.php">
   <p>
       Veuillez indiquer la tranche d'âge dans laquelle vous vous situez :<br />
       <input type="radio" name="age" value="moins15" id="moins15" /> <label for="moins15">Moins de 15 ans</label><br />
       <input type="radio" name="age" value="medium15-25" id="medium15-25" /> <label for="medium15-25">15-25 ans</label><br />
       <input type="radio" name="age" value="medium25-40" id="medium25-40" /> <label for="medium25-40">25-40 ans</label><br />
       <input type="radio" name="age" value="plus40" id="plus40" /> <label for="plus40">Encore plus vieux que ça ?!</label>
   </p>
</form>


Si vous avez deux zones d'options différentes, il faut donner unnameunique à chaque groupe, comme ceci :

<form method="post" action="traitement.php">
   <p>
       Veuillez indiquer la tranche d'âge dans laquelle vous vous situez :<br />
       <input type="radio" name="age" value="moins15" id="moins15" /> <label for="moins15">Moins de 15 ans</label><br />
       <input type="radio" name="age" value="medium15-25" id="medium15-25" /> <label for="medium15-25">15-25 ans</label><br />
       <input type="radio" name="age" value="medium25-40" id="medium25-40" /> <label for="medium25-40">25-40 ans</label><br />
       <input type="radio" name="age" value="plus40" id="plus40" /> <label for="plus40">Encore plus vieux que ça ?!</label>
   </p>
   <p>
       Sur quel continent habitez-vous ?<br />
       <input type="radio" name="continent" value="europe" id="europe" /> <label for="europe">Europe</label><br />
       <input type="radio" name="continent" value="afrique" id="afrique" /> <label for="afrique">Afrique</label><br />
       <input type="radio" name="continent" value="asie" id="asie" /> <label for="asie">Asie</label><br />
       <input type="radio" name="continent" value="amerique" id="amerique" /> <label for="amerique">Amérique</label><br />
       <input type="radio" name="continent" value="australie" id="australie" /> <label for="australie">Australie</label>
   </p>
</form>
L'attributcheckedest, là aussi, disponible pour sélectionner une valeur par défaut.


Les listes déroulantes

Les listes déroulantes sont un autre moyen élégant de faire un choix parmi plusieurs possibilités. Le fonctionnement est un peu différent. On va utiliser la balise<select> </select>qui indique le début et la fin de la liste déroulante. On ajoute l'attributnameà la balise pour donner un nom à la liste.

Puis, à l'intérieur du<select> </select>, nous allons placer plusieurs balises<option> </option>(une par choix possible). On ajoute à chacune d'elles un attributvaluepour pouvoir identifier ce que le visiteur a choisi.

Voici un exemple d'utilisation :

<form method="post" action="traitement.php">
   <p>
       <label for="pays">Dans quel pays habitez-vous ?</label><br />
       <select name="pays" id="pays">
           <option value="france">France</option>
           <option value="espagne">Espagne</option>
           <option value="italie">Italie</option>
           <option value="royaume-uni">Royaume-Uni</option>
           <option value="canada">Canada</option>
           <option value="etats-unis">États-Unis</option>
           <option value="chine">Chine</option>
           <option value="japon">Japon</option>
       </select>
   </p>
</form>


Si vous voulez qu'une option soit sélectionnée par défaut, utilisez cette fois l'attributselected:

<option value="canada" selected>Canada</option>



Vous pouvez aussi grouper vos options avec la balise<optgroup> </optgroup>. Dans notre exemple, pourquoi ne pas séparer les pays en fonction de leur continent ?

<form method="post" action="traitement.php">
   <p>
       <label for="pays">Dans quel pays habitez-vous ?</label><br />
       <select name="pays" id="pays">
           <optgroup label="Europe">
               <option value="france">France</option>
               <option value="espagne">Espagne</option>
               <option value="italie">Italie</option>
               <option value="royaume-uni">Royaume-Uni</option>
           </optgroup>
           <optgroup label="Amérique">
               <option value="canada">Canada</option>
               <option value="etats-unis">Etats-Unis</option>
           </optgroup>
           <optgroup label="Asie">
               <option value="chine">Chine</option>
               <option value="japon">Japon</option>
           </optgroup>
       </select>
   </p>
</form>


Regrouper les champs

Si votre formulaire grossit et comporte beaucoup de champs, il peut être utile de les regrouper au sein de plusieurs balises<fieldset>. Chaque<fieldset>peut contenir une légende avec la balise<legend>. Regardez cet exemple :

<form method="post" action="traitement.php">
 
   <fieldset>
       <legend>Vos coordonnées</legend> <!-- Titre du fieldset --> 

       <label for="nom">Quel est votre nom ?</label>
       <input type="text" name="nom" id="nom" />

       <label for="prenom">Quel est votre prénom ?</label>
       <input type="text" name="prenom" id="prenom" />
 
       <label for="email">Quel est votre e-mail ?</label>
       <input type="email" name="email" id="email" />

   </fieldset>
 
   <fieldset>
       <legend>Votre souhait</legend> <!-- Titre du fieldset -->
 
       <p>
           Faites un souhait que vous voudriez voir exaucé :

           <input type="radio" name="souhait" value="riche" id="riche" /> <label for="riche">Etre riche</label>
           <input type="radio" name="souhait" value="celebre" id="celebre" /> <label for="celebre">Etre célèbre</label>
           <input type="radio" name="souhait" value="intelligent" id="intelligent" /> <label for="intelligent">Etre <strong>encore</strong> plus intelligent</label>
           <input type="radio" name="souhait" value="autre" id="autre" /> <label for="autre">Autre...</label>
       </p>
 
       <p>
           <label for="precisions">Si "Autre", veuillez préciser :</label>
           <textarea name="precisions" id="precisions" cols="40" rows="4"></textarea>
       </p>
   </fieldset>
</form>



Sélectionner automatiquement un champ

Vous pouvez placer automatiquement le curseur dans l'un des champs de votre formulaire avec l'attributautofocus. Dès que le visiteur chargera la page, le curseur se placera dans ce champ.

Par exemple, pour que le curseur soit par défaut dans le champprenom:

<input type="text" name="prenom" id="prenom" autofocus />



Rendre un champ obligatoire

Vous pouvez faire en sorte qu'un champ soit obligatoire en lui donnant l'attributrequired.

<input type="text" name="prenom" id="prenom" required />


Le bouton d'envoi

Il ne nous reste plus qu'à créer le bouton d'envoi. Là encore, la balise<input />vient à notre secours. Elle existe en quatre versions :

type="submit": le principal bouton d'envoi de formulaire. C'est celui que vous utiliserez le plus souvent. Le visiteur sera conduit à la page indiquée dans l'attributactiondu formulaire.
type="reset": remise à zéro du formulaire.
type="image": équivalent du boutonsubmit, présenté cette fois sous forme d'image. Rajoutez l'attributsrcpour indiquer l'URL de l'image.
type="button": bouton générique, qui n'aura (par défaut) aucun effet. En général, ce bouton est géré en JavaScript pour exécuter des actions sur la page. Nous ne l'utiliserons pas ici.
On peut changer le texte affiché à l'intérieur des boutons avec l'attributvalue.
Pour créer un bouton d'envoi on écrira donc par exemple :

<input type="submit" value="Envoyer" />


