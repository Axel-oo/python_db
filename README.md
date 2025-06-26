# MongoDB

## Descrizione di main.py

Il file [`main.py`](./main.py) permette di connettersi a un database MongoDB tramite una stringa di connessione fornita dall'utente. 

Dopo aver stabilito la connessione, lo script richiede il nome del database e mostra tutte le collezioni presenti.

L'utente può quindi selezionare una collezione specifica per visualizzare tutti i documenti in essa contenuti. Se non sono presenti collezioni o documenti, viene mostrato un messaggio appropriato.