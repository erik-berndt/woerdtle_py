#!/usr/bin/env python3
from appdata.json_funcs import check_name, create_json, create_log, halt
import os
import re
import json
from pathlib import Path
from os import system
from datetime import date, datetime
from random import random
system("cls")

# P F A D E
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

score_path = BASE_DIR + '/appdata/scores.json'
log_path   = BASE_DIR + '/appdata/log.json'

dict_path = BASE_DIR+'/appdata/woerter_3_7.txt'

R="\033[1;31m"
G="\033[1;32m"
Y="\033[1;33m"
B="\033[0;34m"
P="\033[0;35m"
LB="\033[1;34m"
E="\033[00m"

# L I S T E N
results = []
is_out = []
words = []
is_right = []

# Z U F A L L S W O R T
with open(dict_path) as f:
    for wort in f:
        words.append(wort.strip().upper())

def ratewort(l):
    w = 0
    if l ==3:
        wort = words[int(random() * len(words))]
        w = len(wort)
        return wort 
    else:
        while w != l:
            wort = words[int(random() * len(words))]
            w = len(wort)
            print(wort,type(l),l,type(w),w)
        return wort 

# G R A F I K
pipe  =B+ "|" +E
pipe3  =B+ "|   " +E
spc = " " * 5   
# newLine = " " * 36

header = LB+"\n\n    W O R D T L E        "+"—" * 29 + Y
header += "\n" + " " * 28 + "ein Spiel zum Verzweifeln" + LB
header += "\n   " + "—" * 36 + "" + E
footer = "\n   " + B + ("—" * 53) + E



# S C O R I N G
def scoring(email, i):
    with open(score_path, 'r') as previous_scores:
        scores = json.load(previous_scores)
    for person in scores['Spieler']:
        if person['email'] == email:
            person['last'] = heute 
            person['total'] += 1
            if i < 7:
                person['score'] += ((7-i)*len(wort))
                person['trys'][i-1] += 1
                person['win'] += 1
            else: 
                person['score'] -= len(wort)
            new_score = person    
    with open(score_path, 'w') as f:
        json.dump(scores, f, indent=2)
    return new_score

def logging(email, trys):
    with open(log_path,'r') as prev_logs:
        logs = json.load(prev_logs)
    for person in logs['players']:
        if person['email'] == email:
            person['trys'].append((trys))
            person['word'].append(wort)
            person['log_time'].append(log_time)
    with open(log_path, 'w') as f:
        json.dump(logs, f, indent=2)

def highscore():
    high = -1111111
    champs = []
    with open(score_path, "r") as players:
        best = json.load(players)
    for person in best["Spieler"]:
        champs.append([person["score"], person["name"]])
        champs = sorted(champs)
    champs.reverse()
    return champs[:3]

def loglist(email):
    prev_date = []
    c = 0
    COL2 = LB
    with open(log_path ,'r') as prev_logs:
        logs = json.load(prev_logs)
    for person in logs['players']:
        if person['name'] == name:
            system ('cls')
            print(header)
            print("\n\n")
            print(G + f"   {person['name']}:\n" + E)
            for  j in range(len(person['trys'])):
                i = len(person['trys']) - (j+1)
                logsplit = person['log_time'][i].split(" ")
                
                logdate = logsplit[0].split("-")
                logdate = logdate[2] + "." + logdate[1] + "." + logdate[0]
                
                logtime = logsplit[1].split(":")
                logtime = logtime[0] + " Uhr " + logtime[1]
                
                if prev_date != []:
                    if logdate != prev_date:
                        if c % 2 == 0:
                            COL2 = E 
                            c += 1
                        else:
                            COL2 = LB
                            c += 1

                print (COL2 + f"   {logdate} um {logtime}  : " + E, end="")
                v = person['trys'][i]
                if v > 0:
                    if  v in [1,2,3]:
                        COL = G
                    elif v in [4,5,6]:
                        COL = Y
                    else:
                        COL = E
                    print(COL + f" Runde {v}" + E, end="")
                else:
                    print(R + "VERLOREN" + E, end="")
                print(f" — {person['word'][i]}")
                prev_date = logdate

def all_players():
    with open(score_path, 'r') as f:
        all_players = json.load(f)
    system('cls')
    print(header + "\n\n")
    print("   Alle Spieler:\n")
    persons = []
    champs = []
    for person in all_players['Spieler']:
        persons.append(person)
    for person in persons:
        champs.append([
            person['score'],
            person['name'],
            person['total'],
            person['win'],
            person['last']
            ])
    champs = sorted(champs)
    champs.reverse()
    print("   Score| Name            | Win  | Plays | Last Play")
    print("   " + "¯" * 50)
    for person in champs:
        spc3 = " " * (5 - len(str(person[0])))
        sp   = " " * (15 - len(person[1]))
        spc1 = " " * (4 - len(str(person[3])))
        spc2 = " " * (4 - len(str(person[2])))
        
        score = spc3 + str(person[0])
        name  = person[1] + sp
        win   = spc1 + str(person[3])
        plays = spc2 + str(person[2])
        date  = person[4][2] + "." + person[4][1] + "." + person[4][0] 
        
        print(G + f"   {score}|", end="")
        print(f" {name} |", end="")
        print(G + f"  {win}|   " + E, end = "")
        print(Y + f"{plays}| " + E, end="")
        print(Y + f"{date}" + E)
    return

# S T A T I S T I K
def statistics(score):
    champs = highscore()
    proz = 0
    total = score['total']
    win = float(score['win'])
    lost = total - win
    if total == 0:
        return
    elif score['win'] == 0: 
        print("\n   ... und gib dir mal ein bisschen Mühe!\n")
        factor = 0
    else:
        proz = win * 100 / float(total)    
        peak = float(max(score['trys']))
        factor = 36 / peak
    first = score['first'][2]+"."+score['first'][1]+"."+score['first'][0]
    last = score['last'][2]+"."+score['last'][1]+"."+score['last'][0]
    print("\n   Highscores:\n")
    for champ in champs:
        champ[0] = str(champ[0])
        champ[0] = "0" * (4 - len(champ[0])) + G+ champ[0] + E
        champ[1] = champ[1] + " " * (12 - len(champ[1]))
        print(Y + f"   {champ[1]}:" + E + f" {champ[0]} Punkte")
    
    print(G + f"\n   {name}, {score['score']}:" + E)
    print("   Auswertung vom "+Y+f"{first}"+E+" bis "+Y+f"{last}\n"+E)
    print("   Spiele gesamt: "+Y+ f"{score['total']}\n"+E)
    print("   Erfolg : ", end="")
    r = int(36 * lost / total)
    g = 36 - r
    print(G + "—" * g + R + "—" * r + E +f":{int(proz)}%\n")
    for i in range(6):
        print(f"   {i+1}.Runde: "+G+"—"*(int(score['trys'][i]*factor))+E, end="")
        print(f":{score['trys'][i]}")
    l = "x"
    while l != "":
        l = halt(2)
        if l == "l":
            loglist(email)
        elif l == "a":
            all_players()
        else:
            continue
    return

# S H O W   R A T E F E L D
def show(table,out, lost=0):
    system("cls")
    print(header)
    print(G + f"   {name}" + E)
    print(f"\n            Wort mit " + Y + f"{w}" + E, end="")
    print(" Buchstaben! " + Y + "6 " + E + "Versuche!\n")
    # print (wort) # S P I C K E R
    # spc = " " * (9 + int((40 - (w * 2)) / w))
    spc = " " * (13 + 8 - w)
    print (spc + strich)
    for b in range (len(results)):
        print(spc + pipe ,end="")
        for a in range (w):
            print(results[b][a]+ pipe, end="")
        print("\n" + spc + strich)
    for l in range(6-len(results)):
        print (spc + pipe3 * w + pipe)
        print (spc + strich)
    if lost != 0:
        print()
        return
    if out:
        abc=["\n         ","Q","W","E","R","T","Z","U","I","O","P","Ü","\n",
             "         ","A","S","D","F","G","H","J","K","L","Ö","Ä","\n",
              "          ","Y","X","C","V","B","N","M","\n"]
        for c in range(len(abc)):
            if abc[c] in out:
                print(R+" " + abc[c] + E, end=" ")
            else:
                print(G + " "+abc[c] + E, end=" ")
        print (footer)
    else:
        print(G+"\n   - GRÜN  "+E+" = richtig richtig")
        print(Y+"   - GELB  "+E+" = is drinne")
        print("   - BLASS  = is nich drinne")
        print("   - ohne groß/klein aber Fremdwörter und so")
        print(footer)

# W O R D   T O   L I S T
def word_to_list(wtl):
    lword = []
    for letter in wtl:
        lword.append(letter)
    return lword


# S P I E L E R I N F O
heute = str(date.today()).split('-')
log_time = str(datetime.now())

print (header)
name = input("\n\n\n   Wer bist du denn? "+Y)
print (E)
name = name.capitalize()
if name != "":
    email = "definiert"
    r_mail = re.compile(r'.+\@.+\..+')
    while not r_mail.match(email):
        email = input("   Und die email   : "+Y)
        print(E)
        if not r_mail.match(email):
            print(R+"     Bitte ein gültiges E-mail Format verwenden!")
            print(E)

# S P I E L E R C H E C K
if Path(score_path).is_file(): 
    system ("cls")
    print(header)
    if name == "":
        person = check_name("zufeng","email",heute)
        name = person['name']
        email = person['email']
        statistics(person)
    else:
        statistics(check_name(name,email,heute))
else:
    create_json(name,email,heute)
    create_log(name,email)
print (footer)
l = 100
while l not in ["3","4","5","6","7","8"]:
    print ("\n   Wie lang soll dein neues Ratewort sein?")
    print ("\n   <"+Y+"4"+E+"> - <"+Y+"8"+E+"> Buchstaben,")
    l = input ("   <"+Y+"ritörn"+E+"> = is mir egal   >>"+Y)
    print(E)
    if l == "":
        l = "3"

wort = ratewort(int(l))
w = len(wort)
comp = word_to_list(wort)

i = 0
strich = B+ "—" * (w*4+1) +E

show(results,is_out)
guessl = []

# R A T E R U N D E N
depp = 0
while i < 6:
    current = []
    guess = input (f"\n   Runde {i+1}: " + Y)
    print(E)
    guess = guess.upper()
    guessl = word_to_list(guess)
    while len(guess) != w:
        show(results,is_out)
        if depp == 0:
            print("   Das Wort"+R+ f" muss {w} " +E+"Buchstaben haben!")
        elif depp == 1:
            print("   Also weesste nee ..." + R + f" {w} BUCHSTABEN ! " + E + "... Depp!")
        else :
            print("   Da is Hopfen und Malz is da verloren. Weesste selber, wa! ")
            print("   Da kann man sich den Mund fusselich reden. Kommt nüscht an.")
            print("   Kannste och jejen 'ne Wand quatschen. Wat willste,")
            print("   hat ja eh keen Zweck. Lassn machen, wirta schon sehn, watta von hat.")
            depp = 0
        guess = input (f"\n   Runde {i+1}: " +Y)
        guess = guess.upper()
        guessl = word_to_list(guess)
        print(E)
        depp +=1

    if guess not in words:
        show(results, is_out)
        print(Y+f"   {guess}"+E+" ist"+R+" nicht"+E+" im Wörterbuch!")
        continue
    system("cls")
    for j in range (len(guessl)):
        if guessl[j] == comp[j]:
            is_exact = G + " " + guessl[j] + " " + E
            current.append(is_exact)
            if guessl[j] not in is_right:
                is_right.append(guessl[j])
            comp[j]= "-"
            guessl[j]= "-"
        elif guessl[j] in comp:   
            if i == 5:
                is_in = R + " " + wort[j] + " " + E
                current.append(is_in)
            else:
                gcount = guessl.count(guessl[j])
                ccount = comp.count(guessl[j])
                if gcount < ccount or gcount == ccount:
                    is_in = Y + " " + guessl[j] + " " + E
                    current.append(is_in)
                else:
                    is_in = " " + guessl[j] + " "
                    current.append(is_in)
                    if is_in not in is_right:
                        is_right.append(is_in)
                    guessl[j] = "-"
        else:
            if i == 5:
                not_in = R + " " + wort[j] +" " + E
                current.append(not_in)
            else:
                not_in = " " + guessl[j] + " "
                if (guessl[j] not in is_out) and (guessl[j] not in is_right):
                    is_out.append(guessl[j])
                current.append(not_in)
    results+=[current]
    print(current)
    if guess.upper() == wort:          # G E W O N N E N
        show(results,is_out, 1)
        new_score = scoring(email, i+1)
        logging(email,i+1)
        print("\n   Du hast gewonnen und kriegst " + G + f"{(6-i)*len(wort)} Punkte!" + E)
        halt(2)
        system("cls")
        print(header)
        statistics(new_score)
        # input("\n   <ritörn>")
        exit()
    comp = word_to_list(wort)
    show(results, is_out)
    i += 1
show(results, is_out, 1)
new_score = scoring(email, 7)             # V E R L O R E N 
logging(email,0)
print(f"\n   Du hast Verloren und kriegst " + R + f"{len(wort)} Punkte Abzug!" + E)
halt(2)
system("cls")
print(header)
statistics(new_score)
# input("\n<ritörn>")

