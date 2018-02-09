#!/usr/bin/env python
# -*- coding: utf-8 -

import mysql.connector

mysql_host = '192.168.55.55'
mysql_user = 'forum'
mysql_passwd = 'stage'
mysql_db = 'forum'

conn = mysql.connector.connect(host=mysql_host,
      user=mysql_user,
      passwd=mysql_passwd,
      db=mysql_db)

cursor = conn.cursor()

def select_database():
    cursor.execute("""SELECT id, sujet, auteur, date_sujet FROM forum""")
    rows = cursor.fetchall()
    # for row in rows:
    #     print('{0} : {1} - {2}'.format(row[0], row[1], row[2]))
    return rows

def count_database():
    cursor.execute("""SELECT COUNT(sujet) FROM forum""")
    rows = cursor.fetchall()
    # for row in rows:
    #     print('{0}'.format(row[0]))
    return rows[0][0]

def dernier_sujet_database():
    cursor.execute("""SELECT MAX(date_sujet), sujet FROM forum """)
    rows = cursor.fetchall()
    # for row in rows:
    #     print('{0} : {1}'.format(row[0], row[1]))
    return rows[0]

def auteur_actif_database():
    cursor.execute("""SELECT COUNT(sujet) AS nb_sujet, auteur FROM forum GROUP BY auteur ORDER BY nb_sujet DESC LIMIT 1""")
    rows = cursor.fetchall()
    print rows
    for row in rows:
        print('{0} : {1}'.format(row[0], row[1]))
    return rows[0]

def formulaire_auteur_database(sujet, auteur, date_sujet):
    cursor.execute("""INSERT INTO forum (sujet, auteur, date_sujet)
                      VALUES ("{0}", "{1}", "{2}")""".format(sujet.encode('utf-8'), auteur.encode('utf-8'), date_sujet))

def suppression_database(id_suppression):
    cursor.execute("""DELETE FROM forum WHERE id={0}""".format(id_suppression))