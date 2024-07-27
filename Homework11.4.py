#suspects

eva = {
    "gender": "female",
    "race": "white",
    "hair_color": "blonde",
    "eye_color": "blue",
    "face_shape": "oval"
}

larisa = {
    "gender": "female",
    "race": "white",
    "hair_color": "brown",
    "eye_color": "brown",
    "face_shape": "oval"
}

matej = {
    "gender": "male",
    "race": "white",
    "hair_color": "black",
    "eye_color": "blue",
    "face_shape": "oval"
}

miha = {
    "gender": "male",
    "race": "white",
    "hair_color": "brown",
    "eye_color": "green",
    "face_shape": "square"
}


#genes

hair_color = {
    "black": "CCAGCAATCGC",
    "brown": "GCCAGTGCCG",
    "blonde": "TTAGCTATCGC"
}

facial_shape = {
    "square": "GCCACGG",
    "round": "ACCACAA",
    "oval": "AGGCCTCA"
}

eye_color = {
    "blue": "TTGTGGTGGC",
    "green": "GGGAGGTGGC",
    "brown": "AAGTAGTGAC"
}

gender = {
    "female": "TGAAGGACCTTC",
    "male": "TGCAGGAACTTC"
}

race = {
    "white": "AAAACCTCA",
    "black": "CGACTACAG",
    "asian": "CGCGGGCCG"
}

with open("dna.txt", "r") as dna_file:
    criminalDNA = dna_file.read()
"""
while True:
    hair_match = criminalDNA.find(hair_color.get("black"))
    if hair_match != -1:
        print("The criminals hair is black")
        criminal_hair = "black"
        break
    elif hair_match == -1:
        hair_match = criminalDNA.find(hair_color.get("brown"))
        if hair_match != -1:
            print("The criminals hair is brown")
            criminal_hair = "brown"
            break
    else:
        print("the Criminals hair is Blonde!")
        criminal_hair = "blonde"
        break
"""
for key, value in hair_color.items():
    hair_match = criminalDNA.find(value)
    if hair_match != -1:
        print("The criminals hair is " + key)
        print(value)
        criminal_hair = key
        print(criminal_hair)
    else:
        print("NO match")
