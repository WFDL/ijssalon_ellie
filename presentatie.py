# Terminal scherm leeg maken
import os
os.system('cls')
print()


# huiswerk 07
#def presenteer():
#    pass
#    return



# huiswerk 08
def presenteer(dict, totaal):
    for _key, _value in dict:
        print(f"{_key} : {_value}")

    print("=======================")
    print(f"totaal : {totaal}")

    return



mijn_dict = {
    "vis" : 10,
    "vlees" : 25,
    "overig" : 15
}


#totaal = 50
#print(presenteer(mijn_dict.items(), totaal))


