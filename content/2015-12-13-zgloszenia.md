Title: Uruchomienie systemu "Zgłoszenia"
Tags: organizacja, dev, zgłoszenia, php

Dostrzegamy jak istotne jest dla prawidłowego funkcjonowania Fundacji jest sprawna obsługa wpływających spraw - przyjmowanie spraw do rozpoznania, przydział spraw do konkretnych osób, a także - w razie potrzeby - dozór, identyfikacja osoby odpowiedzialnej i odtworzenie przebiegu jej obsługi. To część strategii i filozofii biznesu, gdzie stały kontakt i zadowolenie klienta jest kluczową wartością. 

Z tego względu wdrożyliśmy system do obsługi bieżącej korespondencji. Każda sprawa wpływająca na ogólny adres e-mail Stowarzyszenia jest w nim rejestrowana, a osoba otrzymuje jej unikalny identyfikator:

![Przykładowe potwierdzenie rejestracji sprawy](http://cdn.files.jawne.info.pl/public_html/2015/12/13_02:05:26/Zaznaczenie_152.png#md5sum=c665d4d54fbeff8f101f06db3d4617a1)

W dalszym ciągu możliwe skontaktowanie się z współpracowikami poprzez indywidualne adresy e-mail. Nie gwarantuje to jednak jej - w takim samym stopniu - obsługi ze względu na brak nadzoru.

Co istotne, na podstawie adresu e-mail i numeru sprawy wnioskodawca może zapoznać się na stronie [zgloszenia.pilnujemy.info](http://zgloszenia.pilnujemy.info) z tym kto aktualnie zajmuje się sprawą, w jakim departamencie jest ona obsługiwana i prześledzić historię sprawy.

Nie jesteśmy obecnie podmiotem zobowiązanym do udostępniania informacji publicznej, ponieważ nie gospodarujemy żadnym majątkiem publicznym, ani nie realizujemy żadnych zadań publicznych. Obecne finansowanie Fundacji to prywatne darowizny Fundatorów. Nie mniej warto odwołać się do wskazanego tam standardu obowiązujące podmioty publiczne.

Zgodnie z art. 6 ust. 1 pkt. 3 lit. e ustawy z dnia 6 września 2001 roku o dostępie do informacji publicznej udostępnieniu podlega informacja publiczna, w szczególności o  zasadach funkcjonowania podmiotów, o których mowa w art. 4 ust. 1, w tym o stanie przyjmowanych spraw, kolejności ich załatwiania lub rozstrzygania. Natomiast na podstawie art. 8 ust. 3 zd. 1 ustawy podmioty, o których mowa w art. 4 ust. 1 i 2, obowiązane są do udostępniania w Biuletynie Informacji Publicznej informacji publicznych, a obowiązkowo m. in. tych określonych w art. 6 ust. 1 pkt. 3 lit. e ustawy.

Reansumując, każdy podmiot publiczny ma obowiązek informować na swojej stronie, bez żadnych telefonów itp. o stanie przyjmowanych spraw. Mimo to notorycznym naruszeniem, które dotyczy każdej kategorii podmiotów zobowiązanych - od ministerstwa poprzez podmioty wdrażające e-administracje aż do wiejskich szkół - jest niepublikwoanie informacji o sprawach.

Mamy nadzieje, że w ramach w/w systemu takie informacje Fundacja będzie w stanie na bieżąco publikować. Jednocześnie przekonani jesteśmy, że usprawni to obieg bieżącącej korespondencji, co będzie z korzyścią dla wszystkich.

Od strony technicznej skonfigurowano jedno z ogólnodostępnych narzędzi obsługi zgłoszeń - [osTicket](http://osticket.com/), podłączono je do jednej skrzynki z ustawionymi aliasami dla odpowiednich departamentów i ustawiono zadanie cron. Wszystko zgodnie z dokumentacją oprogramowania lub intuicyjnym interfejsem. 
