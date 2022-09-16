import os
from os import system
import json
from random import random
from datetime import date
from pathlib import Path

R="\033[1;31m"        # red
G="\033[1;32m"        # green
B="\033[0;34m"        # blue
LB="\033[1;34m"       # lightblue
Y="\033[1;33m"        # yellow 
BR="\033[0;33m"       # brown
BLG = "\033[1;5;32m"  # blinking green
E="\033[00m"          # end of color

# P F A D E
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

score_path = BASE_DIR + '/scores.json'
log_path   = BASE_DIR + '/log.json'

dict_path = BASE_DIR+'/woerter_3_7.txt'

def halt(go_on = 1):
    if go_on == 2:
        print("\n\n   hit " + BLG + "<" + E, end="")
        halt = input("enter" + BLG + ">" + E + " weiter! ")
        return halt
    print("\n\n   hit " + BLG + "<" + E, end="")
    halt = input("enter" + BLG + ">" + E + " los gehts! ")

def create_json(name,email,heute):
    players = {
            'Spieler':
            [
                {
                    'name':name,
                    'score':0,
                    'email':email,
                    'total':0,
                    'trys':[0,0,0,0,0,0],
                    'win':0,
                    'first':heute,
                    'last':heute
                    }
                ]
            }
    with open(score_path, 'w') as f:
        json.dump(players, f, indent=2)
    print(f"   Hallo," + G + f" {name}" + E + ", du bist Spieler*in N° 1!")
    return

def create_log(name, email):
    logs = {
            'players':
            [
                {
                    'name':name,
                    'email':email,
                    'trys':[],
                    'word':[],
                    'log_time':[]
                    }
                ]
            }
    with open(log_path, 'w') as json_logs:
        json.dump(logs, json_logs, indent = 2)

def check_name(name,email,heute):
    with open(score_path, 'r') as json_scores:
        scores = json.load(json_scores)
    if name == "zufeng":
        allmails = []
        for person in scores['Spieler']:
            allmails.append(person['email'])
        email = allmails[int(random() * len(allmails))]
    for person in scores['Spieler']:
        if person['email'] == email:
            print(f"\n   Hallo " + G + f"{person['name']}" + E, end="")
            print(", willkommen zurück!\n")
            return person
    person ={
            'name':name,
            'score':0,
            'email':email,
            'total':0,
            'trys':[0,0,0,0,0,0],
            'win':0,
            'first':heute,
            'last':heute
            }
    scores['Spieler'].append(person)
    with open(score_path, 'w') as f:
        json.dump(scores, f, indent=2)
    
    with open(log_path, 'r') as json_logs:
        logs = json.load(json_logs)
    perlog = {
            'name':name,
            'email':email,
            'trys':[],
            'word':[],
            'log_time':[]
            }
    logs['players'].append(perlog)
    with open(log_path, 'w') as f:
        json.dump(logs, f, indent=2)

    print(f"\n   Hallo " + G + f"{name}" + E,end="")
    print(", willkommen bei Wordtle!")
    return person 
