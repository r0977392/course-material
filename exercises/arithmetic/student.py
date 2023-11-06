from math import ceil


def five():
    return 5
#Het toont gwn het cijfer 5 dankzij onze return

def triple (x):
    return 3 * x
#Omdat we X een multiplier hebben gegeven aka 3 (triple) geeft hij ons de uitkomst in return

def average (x,y):
    return (x + y) /2
#Hij zoekt het gemiddelde van 2 getallen door bvb 2 + 8 / 2 

def distance (x1,y1,x2,y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5
#...

def buses_needed(people_count, bus_capacity):
    return ceil(people_count / bus_capacity)
#Door het aantal passagiers die op een bus kunnen te delen door de capaciteit van de bus weten we hoeveel 
#...bussen we nodig hebben

def pizza(n_people, slices_per_pizza):
    return ceil(n_people / slices_per_pizza)
#Beetje zelfde als vorige, enige verschil is dat de pizza in 6 of 8 of iets anders kan gedeeld worden

def cake(eggs):
    return eggs // 5
#Eerste / is delen en tweede / is voor de flooring 

def candy_per_child(candy_count, child_count):
    return candy_count//child_count
#Zelfde als de pizza maar nu met //

def cake2 (eggs, flour):
    return min(eggs // 5, flour //250)
#We hebben 250g bloem en 5 eieren nodig; daarom hebben we // weer nodig

def cake3(eggs, flour, butter, sugar):
    limited_by_eggs = eggs // 5
    limited_by_flour = flour // 250
    limited_by_butter = butter // 200
    limited_by_sugar = sugar // 250
    return min(limited_by_eggs, limited_by_flour, limited_by_butter, limited_by_sugar)
#Nu hebben we 5 eieren, 250g bloem, 200g boter en 250g suiker nodig; hiervoor gebruik we dus limited_by, 
#...de rest is hetzelfde

def cake4(eggs, flour, butter, sugar, eggs_per_cake, flour_per_cake, butter_per_cake, sugar_per_cake):
    limited_by_eggs = eggs // eggs_per_cake
    limited_by_flour = flour // flour_per_cake
    limited_by_butter = butter // butter_per_cake
    limited_by_sugar = sugar // sugar_per_cake
    return min(limited_by_eggs, limited_by_flour, limited_by_butter, limited_by_sugar)
#Zelfde als hierboven maar nu met meerdere cakes, hiervoor gebruiken we dus _per_cake en //

def hours(duration):
    return duration // 3600
#1 Volgende 3 horen allemaal bij elkaar; Een uur duurt 3600 seconden dus met deze weten we hoeveel uur 
#...er in X seconden zit

def minutes(duration):
    return (duration - hours(duration) * 3600) // 60
#2 Er zitten 60 min in een uur dus die zetten we achter onze 3600 seconden met //; 1ste duration is van 
#...onze def dan het aantal second in een uur // 60 min

def seconds(duration):
    return duration - hours(duration) * 3600 - minutes(duration) * 60
#3 Voor de seconden weten we het al dus we kunnen gwn de 1 en 2 def gebruiken; zelfde als hierboven, 
#...dan duration van de minuten; niet // 60 min gebruiken maar * 60 min

def coins(amount):
    five_coins = amount // 5
    amount -= 5 * five_coins
    two_coins = amount // 2
    amount -= 2 * two_coins
    one_coins = amount
    return five_coins + two_coins + one_coins
#...

def leftover_candy(candy_count, child_count):
    return candy_count % child_count
#Zelfde soort van oef zoals pizza maar nu met % 

def internet_costs(duration_in_seconds, cost_per_block):
    return ceil(duration_in_seconds / 360) * cost_per_block
#We gebruiken hier 6 min dus 360 sec; gwn de tijd in / 360 sec en dat * de prijs per block

def middle(a, b, c):
    return (a + b + c) - min(a, b, c) - max(a, b, c)
#Hier zoeken we gwn het middelste getal ookal staan ze niet in alfabetische orde; door eerste A + B / C te doen 
#...krijgen we het totaal, en als we daarna het kleinste getal en daarna grootse getal van het totaak eraf doen
#...dan krijg je het middelste getal van de originele 3

def last_digit(n):
    return n % 10
#Hier gebruiken % 10 om de laatste nummer van ons getal te weten

def drop_last_digit(n):
    return n // 10
#Zelfde als hierboven maar nu laten we het laatste getal weg en gebruiken we dus // 10

def next_player(player, player_count):
    return (player + 1) % player_count
#De spelers beginnen met 0,1,2,...;...

def next_player2(player, player_count):
    return player % player_count + 1
#De spelers beginnen met 0,1,2,...;...
