# baloo1379/transposition-api

## Szyfr

Postanowiłem zaimplementować szyfr przestawieniowy kolumnowy z wariacją w postaci odczytywania kolumn tabeli na ukos, czyli z każdym wierszem zmieniam kolumnę o 1 w lewo.
Szyfr ten wykorzystuje klucz do operacji przestawiania, dlatego najlepiej, kiedy jest on jednym, niezadługim słowem.

Pierwszy krok to wpisanie klucza oraz tekstu do tabeli o szerokości klucza i uzupełnienie pustych miejsc na końcu np. spacją.

|     | k | l | u | c | z |
|-----|---|---|---|---|---|
|     | *107* | *108* | *117* | *99* | *122* |
| *1* | o | l | a |   | m |
| *2* | a |   | k | o | t |
| *3* | a |   |   |   |   | 

Następnie odczytujemy kolumny w kolejności od najmniejszej wartości kolumny dodatkowo przechodząc o jedną w lewo z każdym wierszem.
Zaczynamy od `c1`, następnie schodzimy niżej, lecz przeskakujemy o jedno w lewo czyli `u2` i kończymy na `l3`.
Powtarzamy ten krok aż skończymy wszystkie kolumny.

Finalna kolejność komórek to:

| c1 | u2 | l3 | k1 | z2 | c3 | l1 | k2 | z3 | u1 | l2 | k3 | z1 | c2 | u3 |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
|    | k  |    | o  | t  |    | l  | a  |    | a  |    | a  | m  | o  |    |

Co daje kryptogram ` k ot la a amo `.

## Uruchomienie projektu

W celu uruchomienia projektu poniższe kroki są wymagane

### Plik .env

W katalogu głównym projektu utwórz plik `.env`, który zawiera odpowiednio

| Zmienna | Wartość domyślna | Opis |
|---|---|---|
| DEFAULT_USER | diagonal | nazwa użytkownika tworzonego przez seedowanie |
| DEFAULT_PASSWORD | transposition | hasło dla tego użytkownika |
| DATABASE_URL | sqlite:///./app/database.sqlite3 | ścieżka do bazy danych |

### Docker

W katalogu głównym projektu uruchom istniejącą konfigurację `docker-compsoe.yml` poleceniem

    docker-compose up -d --build


### Seedowanie

W plikach projektu znajduje się skrypt, który umożliwia utworzenie użytkownika z danymi ze zmiennych środowiskowych `DEFAULT_USER` i `DEFAULT_PASSWORD` odpowiednio nazwa użytkownika i hasło.

Aby uruchomić go w kontenerze należy najpierw podłączyć się do niego

    docker exce -it cipher /bin/bash

oraz wykonać w środku polecenie

    python ./app/seed.py