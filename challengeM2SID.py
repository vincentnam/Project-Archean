
import matplotlib.pyplot as plt
import scipy.io.wavfile
import scipy.signal
import numpy as np
from IPython.display import Audio
import librosa
import librosa.display


import pandas as pd
import re

folder_path = "/data/Cours/M2-SID/Projets/testfolder/"


# Annotation file reading
csv_file = pd.read_csv(
    folder_path +"annotations_challenge_sid.csv", sep="\t")

# keep only lines that contains a number different from -1
only_commented = []
for index, row in csv_file.iterrows():
    if row["il08_09"] != -1 or row["vg04_05"] != -1 \
            or row["fd03_04"] != -1 or row["la09_10"] != -1 \
            or row["cg13_14"] != -1 or row["mb00_12"] != -1:
        only_commented.append(row)
# Transform it into a DataFrame
only_commented = pd.DataFrame(only_commented)


''' 
def normalisation(df):
    name = df.columns[2:]
    #fig, ax = plt.subplots(6, 1, figsize=(9, 16), sharex=True)
    ret_df = df
    for i, annot in enumerate(ret_df[name]):
        #  ((only_commented_nan[annot]-only_commented_nan[annot].mean() )/only_commented_nan[annot].std()).hist()
        ret_df[annot]= csv_file[csv_file[annot] != -1][annot].values
        ret_df[annot]= (ret_df[annot] - ret_df[annot].mean()) / ret_df[annot].std()
    return  ret_df
'''


def normalisation(df):
    name = df.columns[2:]
    #fig, ax = plt.subplots(6, 1, figsize=(9, 16), sharex=True)
    ret_df = df[df[name]!=-1]
    for i, annot in enumerate(ret_df[name]):
      #test[test[annotateur]!=-1][annotateur]
        #  ((only_commented_nan[annot]-only_commented_nan[annot].mean() )/only_commented_nan[annot].std()).hist()
        ret_df[annot]= (ret_df[annot] - ret_df[annot].mean()) / ret_df[annot].std()
    return  ret_df

norm = normalisation(only_commented)
print(norm.describe())
print(norm)
for annot in norm.columns[2:]:
    print(norm[np.isfinite(norm[annot])][annot])



#annot = csv_file.columns[2:]
#data = normalisation(csv_file[csv_file[annot] != -1][annot])


def plot_hist(df):
    fig, ax = plt.subplots(6,1,figsize=(9, 16), sharex=True )
    name = df.columns[2:]
    for i,annot in enumerate(df[name]):
    #  ((only_commented_nan[annot]-only_commented_nan[annot].mean() )/only_commented_nan[annot].std()).hist()
      ax[i].hist(((df[annot]-df[annot].mean() )/df[annot].std()))
    fig.show()
#plot_hist(normalisation(only_commented_nan))

