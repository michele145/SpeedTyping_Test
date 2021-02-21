#SPEEDTYPINGTEST v1.0

from easygui import *
import time as tm
import sqlite3 as sql
import os


def create_db(): ##check if the database has already been created
    db_filename = "database.db"
    db_is_new = not os.path.exists(db_filename)

    if db_is_new:
        conn = sql.connect ("database.db")
        conn.execute("CREATE TABLE tempi (parole_al_minuto text);")
        conn.close()

def insert_into_db(words_per_minute): #with this function I add the times to the database
    conn = sql.connect ("database.db")
    conn.execute("INSERT INTO tempi (parole_al_minuto) VALUES (" + str(words_per_minute) + ");")
    conn.commit()
    conn.close()

def print_times(title): #with this function I extract from the database all the times of the user and print them
    time_list = []
    conn = sql.connect ("database.db")
    user_times = conn.execute("SELECT parole_al_minuto FROM tempi;")

    for x in user_times:
        time_list.append(x)

    conn.close()

    msgbox("Ecco la tua lista tempi:\n\n" + str(time_list) + "", title, "Exit")



title = "SpeedTyping Test v1.0"
text = "superare gamba terzo forma isola a rapido lasciare niente oppure punta certo durante presso studio università qui ah confronto differenza colpa"
choices = ["OK", "Cancel"]

create_db()

#with this 'if' I control if, to the initial screen the user has continued or decided to exit
if ccbox("Un semplice SpeedTyping Test sviluppato in Python :)\nAppena premerai OK, il timer inizierà!\n\n(ATTENTO AGLI INVIO, ANCHE QUELLI CONTANO!)", title, choices):
    pass

    start = tm.time() #I start counting time
    words = textbox(text, title)

    if words == text:
        end = tm.time() #I finish counting time
        time = round(end - start, 2)
        words_per_minute = round(21 * 60 / time, 2)

        insert_into_db(words_per_minute)

        text_2 = "Bravo, hai scritto le parole con una velocità di " + str(words_per_minute) + " parole al minuto"
        msgbox(text_2, title, "OK")
    else:
        end = tm.time()
        msgbox("Ops, non hai scritto bene le parole!", title, "OK")
    
    print_times(title)

else:
    msgbox("A presto!", title, "Exit")