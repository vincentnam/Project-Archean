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


