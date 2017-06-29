# Zadanie 4

Znajdz numer X swojego "pull-request" dla zadania 3 (a jesli go nie zrobiles to dla zadania 2).
Wezmy zbior programow dostepnych w pull-request o numerach X+1,X+2 i X+3 
(modulo calkowita liczba PR dla danego zadania) dla zadan 1,2 i 3.
Zbior ten powinien liczyc maksymalnie 9 programow.  

Podzadanie 1 (za 0.4 punkta):  
 - dokonaj dokladnej recenzji kodu w wybranych 5 zadaniach z powyzszego zbioru  
 - umiesc w repo_hw4 plik review.txt z odnosnikami do recenzowanych PR  

Podzadanie 2 (za 0.6 punkta):  
 - pobierz 3 wybrane PR z powyzszego zbioru do lokalnego repozytorium wg wskazowek ponizej (Git HowTo) i wykonaj nastepujace czynnosci majace na celu ulepszenie jakosci kodu:  
	- dodaj opisowe komentarze docstring z testami doctest  
	- dodaj testy jednostkowe  
	- jesli nie jest mozliwe wykonanie powyzszych czynnosci, dokonaj refaktoryzacji kodu  
	- wyslij zbiorczy pull-request z trzema zmodyfikowanymi zadaniami (kazdy w osobnym folderze)  
 
Termin oddania zadania: **18.11.2015, 12:00**

Git HowTo

1. Klonujemy repozytorium hw4 tak samo, jak w poprzednich zadanich i przechodzimy do jego głównego katalogu repo_hw4.  
2. Dodajemy dodatkowe zdalne repozytorium poleceniem "git remote add" np:  
    git remote add hw2 https://plgborzecki@git.plgrid.pl/scm/pyaghxv/repo_hw2.git  
    gdzie adres url to link do klonowania danego zadania, a "hw2" to nazwa dla zdalnego repozytorium, którą będziemy używac potem (może być dowolna).  
3. Listujemy wszystkie pull-requesty dla dodanego repozytorium hw2:  
    git ls-remote hw2  
4. Znajdujemy interesujący nas pull-request (np. 30) i pobieramy go:  
    git fetch hw2 refs/pull-requests/30/from:hw2br30  
    Polecenie to pobierze pull-request #30 repozytorium hw2 do gałęzi hw2br30 (nazwa ta może być dowolna)  
5. Wybieramy pobraną gałąź:  
    git checkout hw2br30  
6. Tworzymy unikalny folder, do którego będą przeniesione pliki źródłowe (żeby przy scalaniu gałęzi nie nadpisały się nawzajem):  
    mkdir hw2br30  
    po czym przenosimy do niego ręcznie wszystkie pliki (przenosimy, nie kopiujemy)  
7. Dodajemy pliki w nowym folderze do indeksu gita:  
    git add hw2br30/  
8. Usuwamy z indeksu gita pliki, których już nie ma w głównym katalogu (bo zostały przeniesione):  
    git add -u .  
9. Commit zmian:  
    git commit -m "files moved to folder"  
10. Wybieramy gałąź master:  
    git checkout master  
11. Scalamy z gałęzią aktualną (master) gałąź pobranego pull-requesta:  
    git merge hw2br30  
12. Usuwamy niepotrzebną juz gałąź pull-requesta:  
    git branch -d hw2br30  

Od teraz w folderze hw2br30 są kody źródłowe wybranego przez nas pull-requesta. Analogicznie postępujemy dla kolejnych pull-requestów (od kroku 4), a jeżeli chcemy pobrać inne zadanie, to od kroku 2.
