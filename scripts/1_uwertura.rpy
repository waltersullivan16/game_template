label start:
    scene lobby with fade
    show screen z
    jump konop_monolog1
    #jump konop_monolog2
    #jump dziewczeta
    #jump dziewczeta-wardega
    #jump namiejsce

label konop_monolog1:
    scene lobby with fade
    show screen z
    define gui.text_color = u'#4169E1'
    Konopski """
        No i wreszcie nadszedł ten moment.

        Dzień, w którym raz na zawsze udowodnię, kto jest czarnym charakterem w tej historii.

        To był bez wątpienia najbardziej... {cps=6}intensywny {/cps} miesiąc w moim życiu.

        Nierealny do tego stopnia, że niejednokrotnie miałem wątpliwość, czy to wszystko dzieje się naprawdę. Nigdy nic nie wiadomo w dzisiejszej kulturze pranków.

        Wydaje mi się jednak, że nawet najbardziej wysublimowane pranki mają jakieś granice, które postawione są nieco niżej niż sprawa w sądzie.

        Czy żałuję, że otworzyłem tę puszkę Pandrory? Raczej nie.

        Nie będę zaprzeczał, to nie była bezbolesna batalia. Bywały momenty, gdy chciałem rzucić to wszystko, skasować kanał i odseparować się już na zawsze od youtubowego świata.

        Jednak bez względu na wszystko, sprawa jest na tyle ważna, że nie powinno się pozwolić, aby po prostu poszła w eter. Wiem że to po mojej stronie jest sprawiedliwość!

        Wszystkie trudy i znoje były warte tej jednej magicznej chwili, która dzisiaj niewątpliwie następi.

        Lexiu ustłyszy dzisiaj wyrok
        """
    jump konop_monolog2

label konop_monolog2:
    show winny with vpunch
    pause
    hide winny with zoomin
    Konopski """
        ...

        To był wyjątkowo długi i nudny monolog.

        Ale trzeba jakoś zacząć.

        Szczerze mówiąc żałuję że nie ciągnąłem go dalej. Chilowe wyjście z roli herosa uświadomiło mi, jak bardzo przytłaczająca jest atmosfera tego miejsca.

        Jeśli szybko nie opanuje tego drżenia łydek, to raczej mogę zapomnieć o dobrym pierwszym wrażeniu.

        Nie jestem nawet pewien czy będę w stanie przejść przez salę sądową bez spektakularnego upadku na ryj.

        Ale może nie byłoby to takie złe? Może zyskałbym w oczach wszystkich jako rozładowujący atmosferę element komiczny?

        Albo może...może po prostu wyjdę stąd i udam, że nigdy nie było sprawy.

        Szybko, gdzie ja powiesiłem płaszcz? Dobra, walić to, spadam jak jest.

        Nar...
        """
    jump dziewczeta

label dziewczeta:
    "Och, tak się cieszę, że zdążyłyśmy! Bałyśmy się, że wszedł już pan na salę."
    show dziewczyna3 at left with vpunch
    Dziewczyna3 "A bardzo nam zależało, żeby podziękować panu za to wszystko co pan dla nas robi."
    show dziewczyna2 at right with vpunch
    Dziewczyna2 "Strasznie nam głupio, że naraża to pana na tyle nieprzyjemności."
    show dziewczyna1 with vpunch
    "Strasznie nam głupio, że naraża to pana na tyle nieprzyjemności." (multiple=2)
    "A bardzo nam zależało, żeby podziękować panu za to wszystko co pan dla nas robi."(multiple=2)

    Konopski "Och nie przejmujcie się niczym, to żaden kłopot!"
    Konopski "To było tak bezczelnie ewidentne kłamstwo, że aż dziwię się, że przeszło mi przez gardło."

    "..."
    pause 1.0
    Dziewczyna2 "W każdym razie, uznałyśmy, że potrzebuje pan jak najwięcej wsparcia."
    Dziewczyna3 "Inni zaraz po usłyszeniu nazwiska prokuratora, uciekliby w popłochu."
    Konopski "Ja chciałbym uciec w popłochu, mimo że nawet tego nie usłyszałem."
    Konopski "Zaraz, zaraz. Coś tu się nie zgadza."
    Konopski "Przecież to ja jestem prokuratorem. O kim ty w ogóle mówisz?"
    Dziewczyna1 "Trwożę się wypowiedzieć to imię. Sama myśl wywołuje we mnie ciarki."
    Konopski "To może koleżanka?"
    jump dziewczetawardega

label dziewczetawardega:
    Dziewczyna2 "Dobrze zrobię to. Jest to prokurator WARDĘGA."
    Dziewczyna3 "aż przeszły mnie ciarki."
    Konopski "..."
    Konopski "Od kiedy niby Sylwester Wardęga jest budzącym postrach prokuratorem"
    Dziewczyna1 "Nie wypowiadaj tego imienia na daremno!"
    Konopski "Moje pytanie absolutnie zaliczoło się do kategorii nie na daremno... Ale mniejsza o to, wróćmy do tego poprzedniego."
    Dziewczyna1 "Powiadają że jego ulubionym filmem jest nagranie procesu OJ Simsona."
    Dziewczyna2 "Woooow!"
    Konopski "Jakim cudem Wardęga jest prokuratorem, skoro ja nim jestem?"
    Dziewczyna3 "Uważa je za opus magnum sądownictwa."
    Dziewczyna1 "Wyrafinowany gust konesera rezolutnej dysputy!"
    Konopski "No to może powinien zostać obrońcą?"
    Dziewczyna1 "Jego ulubione powiedzenie to..."
    "KAŻDY KIJ MA DWA KOŃCE!"
    Dziewczyna3 "OOOO, creepy!"
    Konopski "Faktycznie, brzmi jak motto Sylwestra Wardęgi..."
    jump namiejsce

    label namiejsce:
    "" "PANIE KONOPSKI, PROSZĘ ZAJĄĆ SWOJE MIEJSCE!"
    Konopski "Co? Kiedy to się stało? Muszę spadać, szybko!"
    "" "PANIE KONOPSKI NA MIEJSCE"
    Konopski "Panie strażniku, przysięgam na wszystko, sala sądowa absolutnie moim miejscem nie jest!"
    "" "PANIE KONOPSKI CZY MAM UŻYĆ SIŁY?"
    Konopski "Czy naprawdę musicie w tak przemocowy sposób traktować prokuratora?"
    "" "Szanowny panie, cóż to za pomówienia, oczywiście że traktujemy prokuratora z należytym szacunkiem!"
    Konopski "No to czy mógłby pan..."
    "" "Ale do oskarżonych z całą pewnością tego szacunku nie mamy!"
    Konopski "Słucham? Zaszła jakaś pomyłka, ja przecież..."
    Dziewczyny1 "Powodzenia, panie Konopski! I jeszcze raz dziękujemy za wszystko."
    Konopski "Błagam, powiedzcie że to jednak jest prank..."
    jump sad_poczatek
