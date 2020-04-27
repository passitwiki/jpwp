# JPWP zadanie
## Wymagania systemowe
wersja pythona 3.6+
## Zadanie
Należy uzupełnić funkcję znajdującą się w pliku questions/views.py, aby zwracała dane w formacie JSON
o pytaniach i odpowiedziach znajdujących się w bazie danych, które mają ustawioną datę
publikacji (atrybut publish_at) w przeszłości. Struktura danych wyjściowych znajduje
się w pliku sample.json. Wszystkie potrzebne moduły są już zaimportowane.
Uwagi:
* Przydatna może się okazać dokumentacja na temat filtrowania obiektów pobieranych z bazy danych: [https://docs.djangoproject.com/en/3.0/topics/db/queries/] 
]
* Jeśli pojawi się jakiś problem z funkcją zwracającą response, prawdopodobnie będzie należało do niej przekazać 
dodatkowy parametr `safe=False`
* W bazie danych znajdują się 2 pytania, po 4 odpowiedzi do każdego z nich. Filtrację powinno przejść tylko jedno z nich.
## Uruchomienie
* Żeby zainstalować wszystkie potrzebne pakiety nalezy uzyć polecenia
`pip install -r requirements.txt`
* Uruchomienie serwera odbywa się poleceniem
`python manage.py runserver`

