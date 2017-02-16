# Forum - Initiation à l'Informatique
##### Auteur: Florian Dambrine (@Lowess)
##### Date: 16/02/2017
----------------------------------------

L'idée du projet `Forum` est de découvrir les différents aspects de l'informatique à travers plusieurs ateliers qui sont:

## __0. La Découverte et la mise en place d'outils sur son poste de travail:__
  - Les outils pour coder?
    * Système de gestion de version: `git`
    * Un éditeur de code source: `sublime-text`
    * Un environnement de développement: `virtualbox` et `vagrant`
   

## __1. Une approche de la programmation par la mise en place d'un site web:__
  - Dans un premier temps comprendre qui sert à quoi:
    + `HTML`   -> La représentation de la page web
    + `CSS`    -> La présentation et mise en forme du document
    + `nginx`  -> Le serveur de requête
    + `python` -> Le moteur permettant d'intégrer du dynamisme aux pages

### 1.1. Exploration de `HTML` et `CSS` par la création d'une simple page:

  + Apprentissage des [balises de bases](https://openclassrooms.com/courses/apprendre-asp-net-mvc/introduction-au-html) `HTML` 
  + Le `CSS` et son utilisation avec `HTML`
  + Un petit tour chez [Bootstrap](http://getbootstrap.com/)

### 1.2. Tutoriel LINUX:

### 1.3. Mise en place d'un server web `nginx`:

  + Installer un server `nginx` et le faire servir une page d'index `index.html`
  + Manipuler quelques paramètres `nginx`:
    * Le concept de `port` (`listen`)
    * Le concept de `routage` (`location`)

### 1.4. Les base de données et le langage `SQL`:
  - Pourquoi une base de donnée ?
  - Opérations de bases `CRUD` (create, read, update, delete).

### 1.5. Page web plus dynamique:

### 1.5. L'Administration système 2.0:
  - Installation manuelle des logiciels dans un premier temps.
  - Dans un second temps, introduction à l'automatisation avec `ansible`
  - Automatiser la mise à jour du site web et par la suite son installation complète.

## __2. Pour aller plus loin...__
  - Introduction à l'infrastructure (Chaque serveur à un role).
  - Mettre en place le site web et la base de donnée sur des serveurs dédiés.
  - Introduction à la répartition de charge avec `nginx` utilisé en frontal.
  - Mettre en place une infrastructure de type:

 ```
                                      --------------
 -----------------------        - - >| Site web 1 | - - -
 |                     |        |    --------------      |          ---------
 | Nginx Load Balancer | - - - -|                        | - - - -> | Mysql |
 |                     |        |    --------------      |          ---------
 -----------------------        - - >| Site web 2 | - - -
                                      --------------
 ``` 

