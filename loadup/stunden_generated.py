doppelstunden = {
        1 : ["07:30", "09:00"],
        2 : ["09:20", "10:50"],
        3 : ["11:10", "12:40"],
        4 : ["13:00", "14:30"],
        5 : ["14:50", "16:20"],
        6 : ["16:40", "18:10"],
        7 : ["18:30", "20:00"],
        }

Montag = {
        2 : [ "TiLogic", "ABS E023" ],
        3 : [ "SWT", "HSZ 02" ],
        4 : [ "IuK - U" , "APB E008"]}
Dienstag =  {
        1 : [ "U - RN" , "SCHA A185"],
        2 : [ "IuK", "HSZ 02"],
        3 : [ "DB", "HSZ 03"]}
Mittwoch = {
        1 : [ "U - SWT", "ASB E010"]}
Donnerstag = {
        3 : [ "RN", "HSZ 03"],
        4 : [ "ECG", "HSZ 02"],
        5 : [ "U - ECG", "AVO"]}
Freitag = {
        2 : [ "Prog", "HSZ 03"],
        3 : [ "MA II", "HSZ 03"],
        4 : [ "U - DB", "WIL C206"]}
Wochenede = {}
woche = [ Montag, Dienstag, Mittwoch, Donnerstag, Freitag, Wochenede ]
woche_order = [ 'Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Wochenede']

the_goods=[{'AuD': {
    'Donnerstag': {1: ['U HSZ/0301', 'U HSZ/0405'], 2: ['U APB/E006'], 6: ['U HSZ/0204']}, 
    'Dienstag': {1: ['U CHE/0184', 'U HSZ/0204', 'U HSZ/0405'], 3: ['U APB/E006'], 6: ['U HSZ/0105', 'U HSZ/0405']}, 
    'Freitag': {1: ['U CHE/0183'], 2: ['V HSZ/AUDI'], 5: ['U SE2/0211']}, 
    'Montag': {5: ['U CHE/0183'], 6: ['U HSZ/0103', 'U HSZ/0204', 'U HSZ/0405']}, 'Mittwoch': {1: ['U CHE/0184', 'U HSZ/0405'], 6: ['U HSZ/0301']}, 'Wochenede': {}}},
{'Einführung in die Medieninformatik': {
    'Donnerstag': {2: ['U AVO'], 3: ['U AVO']}, 'Dienstag': {2: ['U AVO'], 3: ['U AVO'], 5: ['U AVO']}, 
    'Freitag': {4: ['U AVO'], 6: ['U POT/0081']}, 'Montag': {5: ['V HSZ/0002'], 6: ['U AVO']}, 
    'Mittwoch': {1: ['U AVO'], 2: ['U AVO']}, 'Wochenede': {}}},
{'Einführungspraktikum: RoboLab': {'Donnerstag': {}, 'Dienstag': {}, 'Freitag': {}, 'Montag': {}, 'Mittwoch': {}, 'Wochenede': {}}},
{'Mathematik 1 für Informatiker: Diskrete Strukturen': {'Donnerstag': {3: ['U WIL/C102']}, 'Dienstag': {1: ['U WIL/C106'], 2: ['U REC/D016'], 3: ['U WIL/C204', 'U WIL/C205'], 4: ['U SE1/0101'], 5: ['U WIL/C106']}, 'Freitag': {1: ['U WIL/C104'], 3: ['V TRE/MATH'], 4: ['U BAR/0218'], 5: ['U SE2/0221']}, 'Montag': {4: ['U WIL/C129', 'U WIL/C307'], 6: ['U WIL/C205']}, 'Mittwoch': {1: ['U WIL/C205'], 3: ['V HSZ/0002'], 6: ['U WIL/C205']}, 'Wochenede': {}}}]
