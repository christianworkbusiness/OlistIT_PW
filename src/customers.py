from dotenv import load_dotenv
import pandas as pd
import psycopg
import os


if __name__ == "__main__":
    import common
else:
    import src.common as common


load_dotenv()
host = os.getenv("host")
dbname = os.getenv("dbname")
user = os.getenv("user")
password = os.getenv("password")
port = os.getenv("port")


# 3 metodi ETL dei CUSTOMERS: EXTRACT, TRANSFORM, LOAD


def extract():
    print("Questa è la funzione EXTRACT dei customers")
    df = common.readFIle()
    return df

def transform(df):
    print("Questa è la funzione TRANSFORM dei customers")
    print(df)
    df = common.dropDuplicates(df)
    df = common.checkNulls(df)
    df = common.formatcap(df)
    common.saveProcessed(df)
    print(df)
    return df

def load(df):
    print("Questa è la funzione LOAD dei customers")
    
    
    
    
    
    
    
    with psycopg.connect(host = host, dbname = dbname, user = user, password = password, port = port) as conn:
        with conn.cursor() as cur:
            sql = """
            CREATE TABLE customers (
            pk_customer VARCHAR PRIMARY KEY,
            region VARCHAR,
            city VARCHAR,
            cap VARCHAR
            );
            """
            
            try:
                cur.execute(sql)
            except psycopg.errors.DuplicateTable as ex:
                conn.commit()
                print(ex)
                domanda = input("Vuoi cancellare la tabella? SI/NO: ")
                if domanda == "SI":
                    # se risponde sì cancellare tabella
                    sqldelete = """DROP TABLE customers"""
                    cur.execute(sqldelete)
                    conn.commit()
                    print("Ricreo la tabella customers...")
                    cur.execute(sql)
                    
            sql = """
            INSERT INTO customers
            (pk_customer, region, city, cap) 
            VALUES (%s, %s, %s, %s) ON CONFLICT DO NOTHING;
            """
            common.caricamento_percentuale(df, cur, sql)

            conn.commit()

def main():
    print("Questo è il metodo MAIN dei customers")
    df = extract()
    df = transform(df)
    load(df)

# Per usare questo file come se fosse un MODULO

if __name__== "__main__": # Indica ciò che viene eseguito quando eseguo direttamente
    main()