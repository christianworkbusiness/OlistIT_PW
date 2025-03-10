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