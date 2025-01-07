palavra1 = input().lower()
palavra2 = input().lower()
palavra3 = input().lower()

animais={
    "vertebrado":{
        "ave":{ 
            "carnivoro": "aguia",
            "onivoro": "pomba"
        },
        "mamifero":{
            "onivoro":"homem",
            "herbivoro":"vaca"
        }
    },
    "invertebrado":{
        "inseto":{
            "hematofago":"pulga",
            "herbivoro":"lagarta"
        },
        "anelideo": {
            "hematofago":"sanguessugas",
            "onivoro":"minhoca"
        }
    }
}

print(animais[palavra1][palavra2][palavra3])