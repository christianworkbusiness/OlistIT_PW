# TITOLO
## SOTTOTITOLO
**GRASSETTO**
_CORSIVO_
~~BARRATO~~

## TABELLA
**Customers**
- pk_customer VARCHAR
- region VARCHAR
- city VARCHAR
- cap VARCHAR

**Categories**
- pk_category SERIAL
- name VARCHAR

**Products**
- pk_product VARCHAR
- fk_category INTEGER
- name_length INTEGER
- description_lenght  INTEGER
- imgs_qty INTEGER

**Orders**
- pk_order VARCHAR
- fk_customer VARCHAR
- status VARCHAR
- purchase_timestamp TIMESTAMP
- delivered_timestamp TIMESTAMP
- estimated_date DATE

**Sellers**
- pk_seller VARCHAR
- region VARCHAR

**Orders_Products**
- pk_order_product SERIAL
- fk_order VARCHAR
- fk_product VARCHAR
- fk_seller VARCHAR
- price FLOAT
- freight (costo trasporto) FLOAT

## ToDo (Opzionale)
- copia del file in input alla cartella raw (fare in modo che il nome del file sia univoco, con data e ora)
- creare Database da python
- controllo di validità tabelle
- Upper SI/NO
- Controllo user password prima di cancellare tabella
- aggiunta colonna inserimento (per tenere traccia di quando i dati sono stati messi sul db)
