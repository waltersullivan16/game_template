label sad_poczatek:
    jump sad
    #jump wardega1

label sad:
    Lexiu """
        Otwieram posiedzenie sądu najwyższego.

        Będzie rozpoznana sprawa obecnego tu młodocianego recydywisty Konopskiego.

        Czy mogę poprosić prokuratora oraz jego adiutanta o potwierdzenie gotowości do rozpoczęcia rozprawy?
    """
    Wardęga "Jesteśmy w pełni gotowi wysoki sądzie."
    Lexiu "Czy mógłbym prosić obronę o potwierdzenie gotowości do rozpoczącie rozprawy?"
    Konopski "Zartujecie sobie, prawda? Chcecie rozładować atmosferę poprzez odegranie tej karykaturalnej farsy?"
    Lexiu "Panie Konopski, ponawiam pytanie. Czy jest pan gotowy do rozpoczęcia rozprawy?"
    Konopski "Absolutnie nie jestem!"
    Konopski "Poza tym, pomijając absurd całej tej sytuacji, czy przypadkiem nie jestem oskarżonym, a nie obrońcą?"
    Lexiu """
        Zgadza się, ale żaden obrońca z urzędu nie zdecydował się na podjęcie tej sprawy.

        Wszyscy skapitulowali zaraz po usłyszeniu nazwiska prokuratora.

        Stwierdzili, że nie mają czasu na zajmowanie się z góry przegraną sprawą.

        Prawdą jest, że jest to niecodzienna sytuacja, ale mamy do czynienia z przestępstwem na tyle poważnym, że decyzją sądu najwyższego rozprawa musi odbyć się w trybie natychmiastowym."
    Wardega "Niekonwencjonalne sytuacje wymagają użycia niekonwencjonalnych metod."
    Lexiu "Dziękuję prokuratorze Wardęgo, jak zawsze trafił pan w sedno sprawy."
    Konopski "Sednem sprawy jest to, że ta sytuacja jest kafkowska, a nie niekonwencjonalna."
    Lexiu """
        Konopski, to nie jest czas i miejsce na zgrywanie ornitologa!

        Ponawiam pytanie i tym razem brak odpowiedzi będzie się wiązał z poważnymi reperkusjami.

        Czy mógłbym prosić obronę o potwierdzenie gotowości do rozpoczącie rozprawy?
    """
    Konopski "Ponawiam odpowiedź."
    Konopski "NIE"
    Konopski "Jest tu tyle nadużyć, że nawet nie wiem od czego miałbym zacząć..."
    Lexiu "Czy ma pan zamiar postulować o ponowienie próby znalezienia obrońcy z urzędu?"
    Konopski "Nie, jeśli miałbym o coś postulować to zmianę sędzie..."
    Lexiu "Czy ma pan zamiast postulować o usunięcie z sali rozpraw adiutanta?"
    Konopski "Naprawdę, wolałbym zacząć od..."
    Lexiu "No to skoro wszystko jest już ustalone, to możemy wreszcie przejść do konkretów."
    Lexiu "Proszę stronę oskarżającą o zabranie głosu."
    jump wardega1

label wardega1:
    Wardega """
        To dla mnie zaszczyt wysoki sądzie.

        Na początku chciałbym skierować kilka słów do strony broniącej.

        Wiem że moja sława wyprzedza mnie, ale i tak chciałbym oficjalnie się przedstawić.
    """
    Konopski "Naprawdę nie ma takiej potrzeby..."
    Wardgea """
        Nazywam się Sylwester Wardęga.

        Dla jednych Druid Sprawiedliwości.

        Dla innych Krwiożerczy Samiec Alfa Watahy.

        Wszystko capsem.
    """
    Konopski "To mnie przerasta..."
    Wardęga "Tak dla jasności, należysz do tej drugiej grupy."
    Konopski "Cóż za niespodzianka..."
    Wardaga "Ja sam lubię myśleć o sobie jako o drugim Johnniem Cochranie."
    Wardega "To adwokat O.J.Simsona ty intelektualna amebo."
    Konopski "Chyba zostanę przy 'Sylwester Wardęga'..."
    Wardęga "Zważywszy na dzisiejsze okoliczności, zdecydowałem się na formę oficjalną, ale zachowującą nutkę mistycyzmu."
    Wardega "W dniu dzisiejszym proszę zwracać się do mnie per"
    Wardega "'Panie Druidzie'."
    Konopski "Ok, wszystko jedno, niech będzie Pan Druid, możemy już przejść dalej?"
    Wardęga "Moje życiowe motto brzmi: każdy kij ma dwa końce."
    Konopski "Gdzieś to już słyszałem..."
    Wardega "Ale to ja wiem za który z nich należy chwicić."
    Konopski "A to akurat nowość"
    Wardęga "Więc czas żebym chwycił batutę i rozpoczął koncert sprawiedliwości."
    Konopski "..."
    Konopski "Sam to wymyśliłeś?"
    Wardęga "Nie zamierzam odpowiadać na pytania zadane tak bezczelnie spoufalającym się tonem."
    Konopski "Czy sam to pan wymyślił... Panie Druidzie?"
    Wardęga "Pamiętałeś o capsie?"
    Konopski "Jakże bym śmiał zapomnieć."
    Wardega "Doskonale."
    pause 1.0
    Wardega "Mógłbyś powtórzyć pytanie?"
    Konopski "Czy pańskie motto Panie Druidzie zostało wymyślone w całości przez pana?"
    Wardęga "Nie."
    Wardęga "Ten fragment z batutą zapożyczyłam od jakiegoś kolesia z forum miłośników imagestocka."
    Lexiu "Aaaaaa, już łapię."
    Lexiu "W sensie że batuta to też kijek, tak? I ma dwa końce?"
    Wardęga "Dokładnie tak Konopski. wiedziałem że będziesz miał problem z rozszyfrowaniem meandrów poezji."
    Konopski "Zdaje pan sobie sprawę, że nie ja zadałem to pytanie, prawda?"
    Wardega "..."
    Wardega "Dość już tego pajacowania Konopski, to nie czas i miejsce na czcze pogaduszki."
    Konopski "..."
    Konopski "Mea culpa, od teraz będę starał się powstrzymać od bezsensownych monologów..."
    jump wardega-przemowienie

label wardega-przemowienie:
    Wardega "Wspaniale, nareszcze możemy przejść do części, w której będziemy cię oficjalnie krytykować"
    Konopski "Rozumiem że wcześniej to były takie nieoficjalne zaczepki...?"
    Lexiu "Nareszcie, dowal temu młokosowi!"
    Konopski "Czy możliwe jest jeszcze większe pogwałcenie zasady o niezawisłości sądów...?"
    Wardega "Zgromadziliśmy się tu dzisiaj, aby należycie ukarać obecnego tu oskarżonego, który tymczasowo nazywany będzie obrońcą."
    Lexiu "A domyślnie nazywany będzie skazanym."
    Konopski "Nie było tematu..."
    Wardega """
        To pozbawiony jakiegokolwiek kompasu moralnego młodociany bandyta,
        który nawet w tym krytycznym dla siebie momencie nie potrafi opanować patologicznego braku szacunku wobec starszych.

        Życie innych ma dla niego tyle znaczenia co babki z piasku, które dla wlasnego widzimisie można zrównać z ziemią.

        Jeśli ten pączkujący jeszcze młodzian osiągnął tak zaawansowany stan deprawacji już teraz, to czego możemy się spodziewać, gdy drań osiągnie pełnoletność?
    """
    Konopski """
        Mam absolutną pewność, że gdybym zaoponował, to Wardęga zarzuciłby mnie jakimiś odpisami ze szpitali w Radomiu,
        które w połączeniu ze screenami postów na deviantarcie stanowiłyby bezsprzeczny dowód, że to on wie, ile tak naprawdę mam lat.

        Tylko czeka aż zabiorę głos, widzę jak podkręca sobie wąs ze złowrogim uśmiechem i trzyma rękę na jakieś teczce jakby to był rewolwer.

        Nie dam mu tej satysfakcji.
    """
    Wardega "Mówiłeś coś Konop?"
    Konopski "Nie."
    Wardega """
        Sami widzicie drodzy państwo, czy nie wydaje się wam naturalne, że będąc na jego miejscu, zabralibyście w tym momencie głos i z pokorą przyznali,
        że niezwykle trafnie oceniłem wasze krótkie ale występne życie, ale obiecujecie poprawę i prosicie o rozgrzeszenie?

        Jakim byłbym człowiek, gdybym nie uronił łzy słysząc łamiący się głos tego małego nicponia?

        Cóż jednak można zrobić, jeśli ten krnąbrny grzdyl nie widzi w swoim oku ani źdźbła, ani belki?

        Gdyby tego było mało, ten niemoralny partacz o przerośniętym ego, prowadzi kanał na youtubie. Chociaż, zważywszy na żenujący poziom zamieszczanych tam materiałów powienienem powiedzieć.

        RYNSZTOK NA YOUTUBIE
    """
    Lexiu "Ołłłł snap!"
    Konopski "Ołłłłłł..."
    Konopski "nie, nie wiem co dalej, nie mam absolutnie żadnego komentarza. Niech zostanie po prostu ołłłłłł."
    Wardega """
        Dobre z tym rynsztokiem, nie? Mnie bawi bardzo.

        W każdym razie.

        Wspomnianie już pożałowania godne materiały na hehe rynsztoku hehe oskarżonego, w połączeniu z wynaturzoną naturą, stanowi zagrożenie dla niewinnych obywateli.

        Nikogo nie powinno dziwić, że to nieposkromione łajdactwo doprowadziło w końcu do tragedii.

        Ohydne kłamstwa wymierzone w kierunku poszkodowanego: korzystającego z życia lekkoducha, którego jedyny grzechem jest bezinteresowna chęć wniesienia w życie innych trochę światła.

        Czyn naprawdę chcemy winić tego sympatycznego mężczyzne za idealistyczne poglądy, przekonania o prawdziwej równości, nieznającej podziałów takich jak wiek czy pł...

        ...podziałów takich jak wiek czy ilość lat.

        Czy to nie ironiczne, że zarzuty o kontakty z młodocianymi pochodzą od osoby młodocianej? Czy w takim razie ja też jestem w oczach tego kryminalisty postrzegany jako...

        Mając na względzie stan psychiczny ofiary nie mogę powiedzieć tego plugawego słowa. Nie jestem barbarzyńcą. Nie jestem...

        Konopem.

        Na koniec drodzy państwo, chciałbym pozwolić wypowiedzieć się poszkodowanemy. Oczywiście wystarczy krótki komentarz.
    """
    Lexiu "Ten bestialski czyn zasługuje na dożywocie."
    Konopski "..."
    Konopski "Ołłłłłł."
    Wardega "Chciałbym teraz wezwać pierwszego świadka, Tomasza Gimpera Działowego."
    Lexiu "Przyzwalam. Proszę o wprowadzenie go na salę."
    Wardega "Jak oceniasz moją przemową mój synu? Czy zrobiłeś sobie notatki, aby móc potem się na niej wzorcować?"
    Revo "Bez wątpienia nie brakowało jej walorów stylistycznych papo, ale wielokrotne powoływanie się na wiek pozwanego było mało subtelnym, niepotrzebnym zabiegiem erystycznym."
    Wardega """
        Gdyby ktoś inny wypowiedział te niesprawiedliwie krytyczne słowa, poczułbym się głęboko urażony.
        Ale aż serce mi mięknie na widok twojego nieskażonego subiektywizmem lica i z pokorą wezmę sobie twoje uwagi do serca.
    """
    Revo "Wardęga-sensei..."

    "Fangirl: Omg,omg widziałyście to? a słyszałyście fragment o rosnącym sercu na widok nieprzyzwoicie przystojnego lica?
    Jezu, ogarnij się, to wcale nie było tak. Poza tym już ustaliłyśmy, że Wardęga/Revo to relacja ojciec-syn i shipowanie ich to właściwie kazirodztwo. To co robisz jest niesmaczne.
    Powiedziała fanka Konopski/Wardęga.
    Nie świruj, Konopski jest pełnoletni. Konopski/Wardęga to otp. Świat potrzebuje odrobiny angstu.
    Świat potrzebuje gejowskiej wersji Edypa.
    Ej, ej, ej, dziewczyny!
    A co myślicie o Spysiński/Klaudeliza?
    ....Ale ty masz chory łeb."
    jump gimper
