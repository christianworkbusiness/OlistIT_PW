import datetime
import os
import pandas as pd

# Per utente: inserire path del file
def readFIle():
    isValid = False
    df = pd.DataFrame()
    while not isValid:
        path = input("Inserire path file: ")
        try:
            df = pd.read_csv(path)
        except FileNotFoundError as ex:
            print(ex)
        except OSError as ex:
            print(ex)
        else:
            print("Path inserito correttamente!")
            isValid = True
    else:
        return(df)

def caricamento_percentuale(df, cur, sql):
    # eseguo la query per caricare i dati (il risultato del caricamento è in percentuale)
    print(f"Caricamento in corso... {str(len(df))} righe da inserire.")
    perc_int = 0
    for index, row in df.iterrows():
        perc = float("%.2f" % ((index + 1) / len(df) * 100))
        if perc >= perc_int:
            print(f"{round(perc)}% Completato")
            perc_int += 5
        cur.execute(sql, row.to_list())
        
def formatcap(df):
    # Converte in stringa e riempie con zeri fino a 5 cifre
    if "cap" in df.columns:
        df["cap"] = df["cap"].astype(str).str.zfill(5)
    return df

# no duplicati
def dropDuplicates(df):
    print("Valori duplicati rimossi: ", df.duplicated().sum(), "\n")
    df.drop_duplicates(inplace = True)
    return df

def checkNulls(df):
    print("Valori nulli per colonna:\n", df.isnull().sum(), "\n")
    return df

def saveProcessed(df):
    name = input("Qual è il nome del file? ").strip().lower()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = name + "_processed" + "_datetime" + timestamp + ".csv"
    print(file_name)
    if __name__ == "__main__":
        directory_name = "../data/processed/"
    else:
        directory_name = "data/processed/"
    df.to_csv(directory_name + file_name, index = False)

if __name__ == "__main__":
    print(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
    df = readFIle()
    saveProcessed(df)