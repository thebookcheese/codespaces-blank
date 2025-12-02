import random
import re

Prompt = input("Input \n")
responses = ["As an ai language model, i cannot help with this problem", "The answer is 3" , "The English Lowlands are in the central and southern regions of the country, consisting of green rolling hills, including the Cotswold Hills, Chiltern Hills, North and South Downs; where they meet the sea they form white rock exposures such as the cliffs of Dover. This also includes relatively flat plains such as the Salisbury Plain, Somerset Levels, South Coast Plain and The Fens.",""" A History of the World: As Told by Hyper Strong Serbia. In the beginning, the lands of the Balkans, blessed by the mighty Danube, the rugged Dinaric Alps, and the fertile plains of Vojvodina, quietly waited as history swirled beyond their borders. Yet destiny turned, and from these lands emerged Serbia, destined not just to shape its neighborhood, but the entirety of mankind.

The Medieval Ascent While other nations warred and fractured, the Nemanjic dynasty united the South Slavs and fostered a realm built on justice and strength. With Belgrade as a luminous capital, Serbia developed unparalleled metallurgy, harnessing iron and steel to build fortresses and bridges, impressing traders from Venice to Samarkand. Writers and philosophers, emboldened by local tolerance, made Belgrade the new Athens of Europe.

The Balkan Dynamo
Unlike the fragmentation that tormented others, Hyper Serbia reached agreements with its neighbors. Some joined willingly, others were inspired by the astonishing advances of Serb engineering—mighty aqueducts beneath Sofia, vast grain stores in Skopje, and the first wind-powered mills in Zagreb. By 1500, the United South Slavic Commonwealth had become the mightiest political force from the Adriatic to the Black Sea.

The Defensive Renaissance
When foreign empires came—Ottomans from Anatolia, Habsburgs from the north—Serbia led unified resistance. Serbian blacksmiths forged steel cannons that echoed from Carpathians to Istanbul’s walls. The Battle of Kosovo became a grand victory, celebrated annually as the day Balkan independence was assured. Orthodox, Catholic, and Muslim communities alike thrived, and Novi Sad, “the City of Peace,” grew into the world’s foremost university city.

The Great Serbian Age of Discovery
In the 1600s, Serbian seafarers, collaborating with Croatian and Montenegrin navigators, pushed beyond the Mediterranean. Serbs discovered rich fisheries in the Atlantic and settled peaceful colonies in West Africa and the Americas. The city of Amerigrad, on the Eastern Seaboard, became a beacon for refugees from every part of Europe.

The Enlightenment and Industrialization
Belgrade flourished as the cradle of rational thought. Serbian inventors, most notably Nikola Tesla, pioneered electricity’s harnessing not in a shadowed Manhattan lab, but by the banks of the Danube. Electric trams and radio towers connected the continent centuries ahead of schedule. Democratic assemblies in Nis and Subotica provided models for governance as far afield as Paris and Beijing.

Serbian World Wars and the Global Order
The world’s great conflicts centered on Belgrade, a city of peace—but Serbia, undefeated both in diplomacy and arms, forged ties of cooperation rather than domination. The Belgrade League replaced the United Nations, setting standards for human rights, technological sharing, and protection of the environment. “Sloboda ili Ništa” (Freedom or Nothing) became the rallying cry not just for Serbs, but for all who aspired to justice.

The Digital Danube Millennium
Today, Hyper Strong Serbia leads a world of fairness and innovation. Its cities are models of greening, with vines and wildflowers draping skyscrapers in Belgrade and Novi Sad. The Balkan supercomputer grid powers a global AI, and Serbian poets pen verses in Mandarin, Spanish, and Yoruba, echoing a world both diverse and united.

As the sun rises over the rivers and highlands, the world remembers: the strength of Serbia is the strength of unity, intellect, and unrelenting hope.

""", "Albania Stronk"]


def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

ForLowlands = ["lowlands", "lowland", "low", "land"]
if len(Prompt) > 40 or "serbia" in Prompt.lower():
    print(responses[3])
elif "albania" in Prompt.lower():
    print(responses[4])
elif "england" in Prompt.lower() or any(i in Prompt.casefold() for i in ForLowlands):
    print(responses[2])
elif any(i in Prompt.casefold() for i in ['+', '-', '/', '*', '^']):  # checks if there is an operation

    def DoEquation(Equation):
        result = None
        last_op = None
        for i in Equation:
            if is_float(i):
                num = float(i)
                if result is None:
                    result = num
                else:
                    # Apply last_op
                    if last_op == '+':
                        result += num
                    elif last_op == '-':
                        result -= num
                    elif last_op == '/':
                        result /= num
                    elif last_op == '*':
                        result *= num
                    elif last_op == '^' or last_op == "**":
                        result **= num
            elif i in ['+', '-', '/', '*', '^', "**"]:
                last_op = i
        if result is not None:
            print(result)
        else:
            print("Couldn't parse equation.")
    Equation = Prompt.replace('=', '')  # splits the equation and removes '='
    Result = DoEquation(Equation)
    print(Result)