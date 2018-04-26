## Instrukcja instalacji:
 - najpierw instalujemy python(https://www.python.org/ftp/python/3.6.5/python-3.6.5-amd64.exe). Wazne zeby byla zaznaczona opcja "Add Python 3.5 to PATH".
Dalej wybieramy "Customize installation" i upewniamy sie, ze jest zaznaczona opcja "pip".
 - następnie klikamy dwukrotnie na "install.py". Jeśłi wyskoczy okienko wyboru programu to wybieramy Python. Powinno wyskoczyć okienko instalacji dodatkowych paczek, które po zakończeniu pracy samo się zamknie.
* jeśli w/w metoda nie zadziała to uruchamiamy Wiersz Polecen, w tym celu klikamy dwukrotnie na pasek eksplorera
(tam gdzie jest napisane: ... > gaban-result-interpreter) i wpisujemy "cmd". Nastepnie wystarczy wpisac
"python install.py". Po otzymaniu informacji o skonczonej instalacji okno mozna zamknac

## Instrukcja uruchomienia:
 - najpierw podłaczamy urządzenie przez USB
 - następnie uruchamiamy Wiersz Polecen, w tym celu klikamy dwukrotnie na pasek eksplorera tam gdzie jest napisane: 
... > gaban-results-interpreter) i wpisujemy "cmd".
 - w pliku ./src/config.py ustawiamy parametry połączenia oraz wszelkie inne ustawienia konfiguracyjne
 - teraz wystarczy wpisac "python results-interpreter.py" i program powinien sie uruchomic
 
## Rozwiazywanie problemów:

 * jesli wyswietli sie taki blad: " UnicodeEncodeError: 'charmap' codec can't encode 
characters" to wystarczy wpisac w Wierszsu Polecen "chcp 65001"

