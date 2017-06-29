# Zadanie 6

## Recencja - za 0.2 punkta

Podobnie jak w zadaniu 4 dokonaj recenzji wybranych 3 programow z listy pull-request o numerach X+1,X+2,X+3,X+4 do zadania piątego, gdzie X to numer Twojego pull-requesta. Odpowiedz na komentarze, które otrzymasz.

## Python jako klej i wielozadaniowość - za 0.8 punkta

Zapoznaj sie z modułami multiprocessing i threading.

Wymyśl dwie operacje zużywające intensywnie CPU oraz dwie operacje wykorzystujace intensywnie I/O.

Każda z operacji powinna przetwarzać jakies dane, o różnych rozmiarach. Dobierz tak rozmiar danych, aby każda z operacji wykonywała się w trybie jednowątkowym około 1 sekundy.

Każdą z tych operacji zaimplementuj także (w ten sam sposób) w Javie i C/C++. Dowiedz się jak wywoływać kody w tych językach z poziomu Pythona.

Przytoguj pulę składającą się z około 30 zadań do wykonania.

Porównaj czas wykonania tych operacji dla wszystkich mozliwych kombinacji:
 - multiprocessing, threading lub tez inne biblioteki
 - kod natywnie w Pythonie, Javie, C/C++
 - 1 CPU, kilka CPU
 - pula zadań intensywnych CPU, pula zadań intensywnych I/O, pula zadań mieszanych

Przedstaw wyniki w formie graficznej. (Np. matplotlib)

Zastanów się czy otrzymasz podobne wyniki dla operacji wykonujących się w czasie milisekundy.

Wystarczy Linux, choć może tez być Windows.

Termin oddania zadania: **09.12.2015, 22:00**
