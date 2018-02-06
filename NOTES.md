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
