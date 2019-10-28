import pandas as pd
import re
csv_file = pd.read_csv("annotations_challenge_sid.csv", sep="\t" )

only_commented = []
for index, row in csv_file.iterrows():
    if row["il08_09"] != -1 or row["vg04_05"] != -1 \
            or row["fd03_04"] != -1 or row["la09_10"] != -1 \
        or row["cg13_14"] != -1 or row["mb00_12"] != -1 :
        only_commented.append(row)

only_commented = pd.DataFrame(only_commented)

print(only_commented)

# only_commented.to_csv("./commented_annotations.csv")

# Audio / Audio vidéo / Audio texte / Texte / Audio Video Texte

def get_medium(medium, df):
    return df[df["code_doc"].str.contains(".*"+medium+"_[0-1]{1}",regex=True)]
print("Audio")
print(get_medium("100",only_commented))
print("Texte")
print(get_medium("001",only_commented))
print("Audio vidéo")
print(get_medium("110",only_commented))
print("Audio texte")
print(get_medium("101",only_commented))
print("All")
print(get_medium("111",only_commented))
