label chapter2:
    $ change_style("main")
    scene courtroom_full
    #jump sad
    #jump wardega1
    #jump wardega-przemowienie
    #jump gimper

label poczatek_sadu:
    pause 1.0
    scene gavel
    $ play_sound_effect("gavel")
    #TODO: muzyka
    pause 1.0
    $ judge_scene()
    Lexio """
        Otwieram posiedzenie sądu najwyższego.

        Będzie rozpoznana sprawa obecnego tu młodocianego recydywisty Konopskiego.

        Czy mogę poprosić prokuratora oraz jego adiutanta o potwierdzenie gotowości do rozpoczęcia rozprawy?
    """

    $ pros_scene()
    Wardega "Jesteśmy w pełni gotowi wysoki sądzie."
    $ copros_scene()
    Revo "Gotowy wysoki sądzie"

    $ judge_scene()
    Lexio "Czy mógłbym prosić obronę o potwierdzenie gotowości do rozpoczącie rozprawy?"

    $ defense_scene(kpose="szok")
    Konopski "Zartujecie sobie, prawda? Chcecie rozładować atmosferę poprzez odegranie tej karykaturalnej farsy?"

    $ judge_scene(lpose="irytacja")
    Lexio "Panie Konopski, ponawiam pytanie. Czy jest pan gotowy do rozpoczęcia rozprawy?"

    $ defense_scene(kpose="wkurw")
    Konopski "Absolutnie nie jestem!"
    # zastanawianie się
    Konopski "Poza tym, pomijając absurd całej tej sytuacji, czy przypadkiem nie jestem oskarżonym, a nie obrońcą?"

    $ judge_scene(lpose="powaga")
    Lexio """
        Zgadza się, ale żaden obrońca z urzędu nie zdecydował się na podjęcie tej sprawy.

        Wszyscy skapitulowali zaraz po usłyszeniu nazwiska prokuratora.

        Stwierdzili, że nie mają czasu na zajmowanie się z góry przegraną sprawą.

        Prawdą jest, że jest to niecodzienna sytuacja, ale mamy do czynienia z przestępstwem na tyle poważnym, że decyzją sądu najwyższego rozprawa musi odbyć się w trybie natychmiastowym.
        """

    $ pros_scene(wpose="powaga")
    Wardega "Niekonwencjonalne sytuacje wymagają użycia niekonwencjonalnych metod."

    $ judge_scene(lpose="radosc")
    Lexio "Dziękuję prokuratorze Wardęgo, jak zawsze trafił pan w sedno sprawy."

    $ defense_scene(kpose="kropla")
    Konopski "Sednem sprawy jest to, że ta sytuacja jest kafkowska, a nie niekonwencjonalna."

    $ judge_scene(lpose="irytacja")
    Lexio """
        Konopski, to nie jest czas i miejsce na zgrywanie ornitologa!

        Ponawiam pytanie i tym razem brak odpowiedzi będzie się wiązał z poważnymi reperkusjami.

        Czy mógłbym prosić obronę o potwierdzenie gotowości do rozpoczącie rozprawy?
        """
    $ defense_scene(kpose="wkurw")
    Konopski "Ponawiam odpowiedź."
    Konopski "NIE"
    Konopski "Jest tu tyle nadużyć, że nawet nie wiem od czego miałbym zacząć..."


    $ judge_scene()
    Lexio "Czy ma pan zamiar postulować o ponowienie próby znalezienia obrońcy z urzędu?"

    $ defense_scene()
    Konopski "Nie, jeśli miałbym o coś postulować to zmianę sędzie...{nw}"

    $ judge_scene()
    Lexio "Czy ma pan zamiar postulować o usunięcie z sali rozpraw adiutanta?"

    $ defense_scene()
    Konopski "Nie, to naprawdę nie tutaj tkwi główny problem."
    $ thinking(Konopski, "Chociaż nie ukrywam, że jego obecność wywołuje we mnie lekki dyskomfort")

    $ judge_scene()
    Lexio "No to skoro wszystko jest już ustalone, to możemy wreszcie przejść do konkretów."
    Lexio "Proszę stronę oskarżającą o zabranie głosu."
    jump mowa_wardegi

label mowa_wardegi:

    $ pros_scene(wpose="powaga")
    Wardega """
        To dla mnie zaszczyt wysoki sądzie.

        Na początku chciałbym skierować kilka słów do strony broniącej.

        Wiem że moja sława wyprzedza mnie, ale i tak chciałbym oficjalnie się przedstawić.
        """

    $ defense_scene(kpose="kropla")
    Konopski "Naprawdę nie ma takiej potrzeby..."

    ## TODO przedstawienie scenka
    $ pros_scene()
    Wardega """
        Nazywam się Sylwester Wardęga.

        Dla jednych Druid Sprawiedliwości.

        Dla innych Krwiożerczy Samiec Alfa Watahy.

        Wszystko capsem.
        """

    $ defense_scene(kpose="kropla")
    $ thinking(Konopski, "To mnie przerasta...")

    $ pros_scene(wpose="uszczypliwosc")
    Wardega "Tak dla jasności, należysz do tej drugiej grupy."

    $ defense_scene(kpose="kropla")
    $ thinking(Konopski, "Cóż za niespodzianka...")

    $ pros_scene(wpose="powaga")
    Wardega "Ja sam lubię myśleć o sobie jako o drugim Johnnym Cochranie."
    #uszczypliwosc
    Wardega "To adwokat O.J.Simsona, ty intelektualna amebo."

    $ defense_scene("kropla")
    $ thinking("Chyba zostanę przy 'Sylwester Wardęga', ty fanie 'rezolutnej dysputy'")

    $ pros_scene(wpose="powaga")
    Wardega "Zważywszy na dzisiejsze okoliczności, zdecydowałem się na formę oficjalną, ale zachowującą nutkę mistycyzmu."
    Wardega "W dniu dzisiejszym proszę zwracać się do mnie per"
    Wardega "'Panie Druidzie'."

    $ defense_scene("kropla")
    $ thinking(Konopski, "Ok, wszystko jedno, niech będzie Pan Druid, możemy już przejść dalej?")

    $ pros_scene(wpose="powaga")
    Wardega "Moje życiowe motto brzmi: każdy kij ma dwa końce."

    $ defense_scene("kropla")
    $ thinking(Konopski, "Gdzieś to już słyszałem...")

    $ pros_scene(wpose="powaga")
    Wardega "Ale to ja wiem za który z nich należy chwicić."

    $ defense_scene("thinking")
    Konopski "A to akurat nowość"

    $ pros_scene(wpose="wczucie")
    Wardega "Więc czas żebym chwycił batutę i rozpoczął koncert sprawiedliwości."

    $ defense_scene("kropla")
    $ thinking(Konopski, "...")
    pause 1
    # thinking
    Konopski "Sam to wymyśliłeś?"

    $ pros_scene(wpose="pogarda")
    Wardega "Nie zamierzam odpowiadać na pytania zadane tak bezczelnie spoufalającym się tonem."

    $ defense_scene("zniecierpliwienie")
    Konopski "Czy sam to pan wymyślił... Panie Druidzie?"

    $ pros_scene(wpose="pogarda")
    Wardega "Pamiętałeś o capsie?"

    $ defense_scene("kropla")
    Konopski "Jakże bym śmiał zapomnieć."

    $ pros_scene(wpose="powaga")
    Wardega "Doskonale."
    pause 1.0
    # main
    Wardega "Mógłbyś powtórzyć pytanie?"

    $ defense_scene()
    Konopski "Czy pańskie motto Panie Druidzie zostało wymyślone w całości przez pana?"

    $ pros_scene()
    Wardega "Nie."
    Wardega "Ten fragment z batutą zapożyczyłam od jakiegoś kolesia z forum miłośników imagestocka."

    $ judge_scene()
    Lexio "Aaaaaa, już łapię."
    Lexio "W sensie że batuta to też kijek, tak? I ma dwa końce?"

    $ pros_scene(wpose="uszczypliwosc")
    Wardega "Dokładnie tak Konopski. wiedziałem że będziesz miał problem z rozszyfrowaniem meandrów poezji."

    $ defense_scene("kropla")
    Konopski "Zdaje pan sobie sprawę, że nie ja zadałem to pytanie, prawda?"

    $ pros_scene("pogarda") # irytacja?
    Wardega "..."
    Wardega "Dość już tego pajacowania Konopski, to nie czas i miejsce na czcze pogaduszki."

    $ defense_scene("kropla")
    Konopski "..."
    # zniecierpliwienie
    Konopski "Mea culpa, od teraz będę starał się powstrzymać od bezsensownych monologów..."
    jump wardega_przemowienie

label wardega_przemowienie:

    $ pros_scene()
    Wardega "Wspaniale, nareszcze możemy przejść do części, w której będziemy cię oficjalnie krytykować"

    $ defense_scene()
    Konopski "Rozumiem że wcześniej to były takie nieoficjalne zaczepki...?"

    $ judge_scene()
    Lexio "Nareszcie, dowal temu młokosowi!"

    $ defense_scene()
    Konopski "Czy możliwe jest jeszcze większe pogwałcenie zasady o niezawisłości sądów...?"

    $ pros_scene()
    Wardega "Zgromadziliśmy się tu dzisiaj, aby należycie ukarać obecnego tu oskarżonego, który tymczasowo nazywany będzie obrońcą."

    $ judge_scene()
    Lexio "A domyślnie nazywany będzie skazanym."

    $ defense_scene()
    Konopski "Nie było tematu..."

    $ pros_scene()
    Wardega """
        To pozbawiony jakiegokolwiek kompasu moralnego młodociany bandyta,
        który nawet w tym krytycznym dla siebie momencie nie potrafi opanować patologicznego braku szacunku wobec starszych.

        Życie innych ma dla niego tyle znaczenia co babki z piasku, które dla wlasnego widzimisie można zrównać z ziemią.

        Jeśli ten pączkujący jeszcze młodzian osiągnął tak zaawansowany stan deprawacji już teraz, to czego możemy się spodziewać, gdy drań osiągnie pełnoletność?
        """

    $ defense_scene()
    Konopski """
        Mam absolutną pewność, że gdybym zaoponował, to Wardęga zarzuciłby mnie jakimiś odpisami ze szpitali w Radomiu,
        które w połączeniu ze screenami postów na deviantarcie stanowiłyby bezsprzeczny dowód, że to on wie, ile tak naprawdę mam lat.

        Tylko czeka aż zabiorę głos, widzę jak podkręca sobie wąs ze złowrogim uśmiechem i trzyma rękę na jakieś teczce jakby to był rewolwer.

        Nie dam mu tej satysfakcji.
        """

    $ pros_scene()
    Wardega "Mówiłeś coś Konop?"

    $ defense_scene()
    Konopski "Nie."

    $ pros_scene()
    Wardega """
        Sami widzicie drodzy państwo, czy nie wydaje się wam naturalne, że będąc na jego miejscu, zabralibyście w tym momencie głos i z pokorą przyznali,
        że niezwykle trafnie oceniłem wasze krótkie ale występne życie, ale obiecujecie poprawę i prosicie o rozgrzeszenie?

        Jakim byłbym człowiek, gdybym nie uronił łzy słysząc łamiący się głos tego małego nicponia?

        Cóż jednak można zrobić, jeśli ten krnąbrny grzdyl nie widzi w swoim oku ani źdźbła, ani belki?

        Gdyby tego było mało, ten niemoralny partacz o przerośniętym ego, prowadzi kanał na youtubie. Chociaż, zważywszy na żenujący poziom zamieszczanych tam materiałów powienienem powiedzieć.

        RYNSZTOK NA YOUTUBIE
        """

    $ judge_scene()
    Lexio "Ołłłł snap!"

    $ defense_scene()
    Konopski "Ołłłłłł..."
    Konopski "Nie, nie wiem co dalej, nie mam absolutnie żadnego komentarza. Niech zostanie po prostu ołłłłłł."

    $ pros_scene()
    Wardega """
        Dobre z tym rynsztokiem, nie? Mnie bawi bardzo.
        Chciałbym być wreszcie rozpoznawalny nie jako ten-od psa-pajaka, tylko ten od rynsztoka... W sumie to też nie brzmi dobrze.
        """

    Konopski "Ale ty jesteś głównie rozponawalny jako ten od boobsmana."

    Wardega """
        Cóż to za czarna magia pozwala temu pędrakowwi czytac mi w myslach?"""
    Konopski " Zapomniałeś użyc niebieskiej czcionki"

    Wardega "Teraz też słychać?"

    Konopski "Teraz już nie."

    Wardega """
        Dobrze, mogę teraz dokończyć mój wewnętrzny monolog.
        Czy Revo też widzi we mnie 'tego od boobsmena'?

        Jakie słowa cisną mu się na usta, kiedy myśli o mnie?

        Brodaty przystojniaczek?

        Amant w sile wieku?
    """

    Lexio """
        Mistyczny dziadunio?

        Stary, ale wariat?
    """

    Konopski """
        Zrzędliwy lowelas?

        W tym samym czasie revo: jurny szeryf?
        Chwila, czemu ja w ogóle biorę w tym udział...?
        Revo: Plus przecież ja nazywam go w myślach po prostu wardega"""

    Wardega """
        Zabójczy kociak?
        Kuszący mędrzec?
    """
    Konopski "Czy PAN DRUID ma jeszcze jakieś zarzuty w moją stronę..?"

    Wardega "A co ty taki niecierpliwy jesteś Konopski, rozsadza cię młodzieńcza energia?"

    Konopski """A co ty taki powolny jesteś, Mistyczny dziaduniu?
    ...
    <takie mega parsknięcie>
    """

    Wardega "Bawią cię moje zarzuty Konop? Jesteś dumny ze swojego kryminalnego życia?"

    Lexio "Dobrze, Zabójczy kociaku, zniszcz swoją ofiarę!"

    Wardega """
        ...

        Chyba straciłem wątek.

    """

    Konopski "Ostatni był żart z moim rynsztokiem na youtubie."

#Popatrzcie państwo, na ten zuchwały uśmieszek obrońcy. Na pierwszy rzut oka, że jest równie zdeprawowany jak jego klient
    Wardega """

        Ach tak, jak mogłem zapomnieć!

        Wspomnianie już pożałowania godne materiały na hehe rynsztoku hehe oskarżonego, w połączeniu z wynaturzoną naturą, stanowi zagrożenie dla niewinnych obywateli.

        Nikogo nie powinno dziwić, że to nieposkromione łajdactwo doprowadziło w końcu do tragedii.

        Ten mały łachudra, wie, że słowa tną niejednokronie głębiej niż nóż. Warto zauważyć, że brak przemocy fizycznej jest spowodowany tylko mikrą aparycją tej ledwo wyglądającej zza stolika dzieciny
        """
    Konopski "Powiedziała osoba, która potrzebuje stołka, żeby móc wyglądać zza stolika..."

    Wardega """

        Zbrodniarz nie przebierał w ohydnych kłamstwach wymierzonych w kierunku poszkodowanego,
        korzystającego z życia lekkoducha, którego jedyny grzechem jest bezinteresowna chęć wniesienia w życie innych trochę światła.

        Czyn naprawdę chcemy winić tego sympatycznego mężczyzne za idealistyczne poglądy, przekonania o prawdziwej równości, nieznającej podziałów takich jak wiek czy pł...

        ...podziałów takich jak wiek?

        Czy to nie ironiczne, że zarzuty o kontakty z młodocianymi pochodzą od osoby młodocianej? Czy w takim razie ja też jestem w oczach tego kryminalisty postrzegany jako...

        Mając na względzie stan psychiczny ofiary nie mogę powiedzieć tego plugawego słowa. Nie jestem barbarzyńcą. Nie jestem...

        Konopem.

        Na koniec drodzy państwo, chciałbym pozwolić wypowiedzieć się poszkodowanemy. Oczywiście wystarczy krótki komentarz.
        """

    $ judge_scene()
    Lexio "Ten bestialski czyn zasługuje na dożywocie."

    $ defense_scene()
    Konopski "..."
    Konopski "Ołłłłłł."

    $ pros_scene()
    Wardega "Chciałbym teraz wezwać pierwszego świadka, Tomasza Gimpera Działowego."

    $ judge_scene()
    Lexio "Przyzwalam. Proszę o wprowadzenie go na salę."

    $ defense_scene()
    Konopski "..."
    Konopski "Co Gimper ma niby z tym wspólnego"

    $ pros_scene()
    Wardega "Jak oceniasz moją przemową mój synu? Czy zrobiłeś sobie notatki, aby móc potem się na niej wzorcować?"
    Revo "Bez wątpienia nie brakowało jej walorów stylistycznych papo, ale wielokrotne powoływanie się na wiek pozwanego było mało subtelnym, niepotrzebnym zabiegiem erystycznym."
    Wardega "Gdyby ktoś inny wypowiedział te niesprawiedliwie krytyczne słowa, poczułbym się głęboko urażony."
    Wardega "Ale aż serce mi mięknie na widok twojego nieskażonego subiektywizmem lica i z pokorą wezmę sobie twoje uwagi do serca."
    Revo "Wardęga-sensei..."

    scene courtroom
    Dziewczyna3 "Omg,omg widziałyście to? a słyszałyście fragment o rosnącym sercu na widok nieprzyzwoicie przystojnego lica?"
    Dziewczyna2 "Jezu, ogarnij się, to wcale nie było tak. Poza tym już ustaliłyśmy, że Wardęga/Revo to relacja ojciec-syn i shipowanie ich to właściwie kazirodztwo. To co robisz jest niesmaczne."
    Dziewczyna3 "Powiedziała fanka Konopski/Wardęga."
    Dziewczyna2 "Nie świruj, Konopski jest pełnoletni. Konopski/Wardęga to otp. Świat potrzebuje odrobiny angstu."
    Dziewczyna3 "Świat potrzebuje gejowskiej wersji Edypa."
    Dziewczyna1 "Ej, ej, ej, dziewczyny!"
    Dziewczyna1 "A co myślicie o Spysiński/Klaudeliza?"
    "....Ale ty masz chory łeb."
    jump gimper
