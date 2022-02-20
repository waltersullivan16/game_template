label start:
    scene lobby with fade
    show screen z
    #jump test
    #jump konop_monolog1
    #jump konop_monolog2
    #jump dziewczeta
    #jump dziewczeta_wardega
    #jump bloody_text
    #jump legenda
    jump gazeta
    #jump namiejsce
    #jump sad_poczatek

label konop_monolog1:

    $ thoughts_monologue (
            Konopski, '''
No i wreszcie nadszedł ten moment.
Dzień, w którym raz na zawsze udowodnię, kto jest czarnym charakterem w tej historii.
To był bez wątpienia najbardziej... {cps=6}intensywny {/cps} miesiąc w moim życiu.
Nierealny do tego stopnia, że niejednokrotnie miałem wątpliwość, czy to wszystko dzieje się naprawdę. Nigdy nic nie wiadomo w dzisiejszej kulturze pranków.
Wydaje mi się jednak, że nawet najbardziej wysublimowane pranki mają jakieś granice, które postawione są nieco niżej niż sprawa w sądzie.
Czy żałuję, że otworzyłem tę puszkę Pandrory? Raczej nie.
Nie będę zaprzeczał, to nie była bezbolesna batalia. Bywały momenty, gdy chciałem rzucić to wszystko, skasować kanał i odseparować się już na zawsze od youtubowego świata.
Jednak bez względu na wszystko, sprawa jest na tyle ważna, że nie powinno się pozwolić, aby po prostu poszła w eter. Wiem że to po mojej stronie jest sprawiedliwość!
Wszystkie trudy i znoje były warte tej jednej magicznej chwili, która dzisiaj niewątpliwie następi.
Lexiu ustłyszy dzisiaj wyrok...'''
    )
    jump konop_monolog2

label konop_monolog2:
    show winny with m
    pause 1.0
    hide winny
    $ thoughts_monologue(
        Konopski,'''
...
To był wyjątkowo długi i nudny monolog.
Ale trzeba jakoś zacząć.
Szczerze mówiąc żałuję że nie ciągnąłem go dalej. Chilowe wyjście z roli herosa uświadomiło mi, jak bardzo przytłaczająca jest atmosfera tego miejsca.
Jeśli szybko nie opanuje tego drżenia łydek, to raczej mogę zapomnieć o dobrym pierwszym wrażeniu.
Nie jestem nawet pewien czy będę w stanie przejść przez salę sądową bez spektakularnego upadku na ryj.
Ale może nie byłoby to takie złe? Może zyskałbym w oczach wszystkich jako rozładowujący atmosferę element komiczny?
Albo może...może po prostu wyjdę stąd i udam, że nigdy nie było sprawy.
Szybko, gdzie ja powiesiłem płaszcz? Dobra, walić to, spadam jak jest.
Nar...''')
    jump dziewczeta

label dziewczeta:
    Unknown "Och, tak się cieszę, że zdążyłyśmy! Bałyśmy się, że wszedł już pan na salę."
    show penny gossip at true_left with vpunch
    Penny "A bardzo nam zależało, żeby podziękować panu za to wszystko co pan dla nas robi."
    show ema happy at right with vpunch
    Ema "Strasznie nam głupio, że naraża to pana na tyle nieprzyjemności."
    show pearl embarassed with vpunch
    Pearl "No i miałyśmy nadzieję na autograf."

    Konopski side_main "Och nie przejmujcie się niczym, to żaden kłopot!"
    $ thoughts_monologue(
        Konopski,
"To było tak bezczelnie ewidentne kłamstwo, że aż dziwię się, że przeszło mi przez gardło.")
    show pearl serious
    show penny main
    show ema confused
    pause 1.0
    show pearl main
    Ema main "W każdym razie, uznałyśmy, że potrzebuje pan jak najwięcej wsparcia."
    Penny gossip"Inni zaraz po usłyszeniu nazwiska prokuratora, uciekliby w popłochu."
    Konopski "Ja chciałbym uciec w popłochu, mimo że nawet tego nie usłyszałem."
    $ thoughts_monologue(
        Konopski, '''
Zaraz, zaraz. Coś tu się nie zgadza.
Przecież to ja tu jestem prokuratorem.''')
    Konopski "O kim ty w ogóle mówisz?"

    Pearl serious "Trwożę się wypowiedzieć to imię. Sama myśl wywołuje we mnie ciarki."
    Konopski "To może koleżanka?"
    jump dziewczeta_wardega

label dziewczeta_wardega:
    show ema at right
    show penny at true_left
    show pearl
    Ema determined "Dobrze zrobię to."
    Ema "Jest to prokurator.."
    pause 1.0
    show lobby at Glitch
    pause 1.0
    show ema at Glitch
    show pearl at Glitch
    show penny at Glitch
    jump bloody_text

label bloody_text:
    #show wardega_title at blood_particle#with Dissolve(2, alpha=True#)
    #$ renpy.movie_cutscene("cutscenes/strasznega.webm")
    pause
    scene black
    # #$ fading_text("sniff", 1.0, 400, 300, 600, 600, color="#fff", size=24)
    # pause
    play sound "music/wardega.mp3"
    show text creepy_maker("WARDEGA") with Dissolve(2, alpha=True)
    # pause
    hide text with Dissolve(3, alpha=True)
    pause
    $ change_style_to_creepy()
    show konopski smirk at right with ease
    Konopski "Wy... zdajecie sobie sprawę z tego, że \"Wardęga\" to nie jest jego imię, prawda?"
    Konopski main "Co tu się właśnie wydarzyło?"
    Konopski "Co stało się z pierwszoosobowy styl narracji?"
    Konopski "Sympatycznym w swej prostocie okienkiem dialogowym?"
    Konopski "Bogatym w szczegóły drugim planem?"
    show pearl determined at kick_out
    pause 0.3
    show konopski at kicked_out
    pause 0.2
    Pearl "Ale proszę nie wchodzić w kadr!"
    show ema determined at right
    Ema "A poza tym, czy naprawdę myśli pan, że jest to odpowiedni moment na łamanie czwartej ściany?"
    Konopski "A mógłbym mieć jakiekolwiek wątpliwości dlatego bo...?"
    pause
    Ema thinking "Tak właściwie to nie wiem, ale jest w tym coś budzącego grozę..."
    jump legenda

label legenda:
    show penny main at true_left
    show pearl
    show ema at right
    Penny "No wie pan, jak to mówią..."
    Penny gossip "Nie należy wywoływać Wardęgi z lasu..."
    Konopski "Jakoś nie wydaje mi się, żeby ktokolwiek, kiedykolwiek to powiedział..."
    show penny main
    Ema determined "Legenda głosi, że jeśli podczas jakiejś dramy, wypowie się trzy razy WARDEGA, to w przeciągu
    dwóch godzin przejmie on nad tą dramą dowództwo, zmieniwszy wcześniej całą istotę problemu na coś zupełnie innego."
    Penny cards "Nie wolno jednak igrać z siłami ciemności."
    Penny "Użycie watahańskiej mocy dla własnych korzyści może przynieść poważne konsekwencje."
    show penny main
    Pearl serious "Jak to mówią: Wardęga nierychliwy, ale sprawiedliwy."
    Konopski "..."
    Konopski "Ci nieistniejący 'oni' mają zadziwiająco wiele do powiedzenia na temat Wardęgi..."
    Ema notes "A teraz, ku przestrodze, zobaczmy do czego prowadzić wymawianie imienia czarnoksiężnika swego na daremno."
    hide Ema
    hide Pearl
    hide Penny
    Konopski "A teraz, ku przypomnieniu, podkreślmy fakt, że jego imię brzmi 'Sylwester', a nie 'Wardega'..."
    scene black
    pause
    Konopski "Co, znowu cutscenka...? No błagam..."
    # vutscenka lol
    jump gazeta

label gazeta:
    scene lobby with fade
    show pearl serious
    show ema confused at right
    show penny main at true_left
    Konopski "..."
    Konopski "Słuchajcie, nie żebym się czepiał, ale czy nie wydaje wam się, że odrobinę przesadzacie z tym dramatyzmem?"
    Ema thinking "Ale to przecież nie jest naszego autorstwa."
    Penny "To był filmik 'ku przestrodze', umieszczony na oficjalnej stronie Wardęgi {a=a}www.zorro-z-lasu2.com{/a}. Prawie wszystko co do tej pory powiedziałyśmy pochodzi z tej strony."
    Konopski "To... wiele tłumaczy..."
    $ Konopski(thoughts_text("Błagam, powiedzcie mi, że ta dwójka na końcu to część jakiejś zagadki..."))
    $ thoughts_monologue(
        Konopski, '''
To niemożliwe, że istnieje jeszcze jeden zorro-z-lasu, prawda...?''')
    Ema "Jest tu jeszcze sekcja 'Poznaj czarnoksiężnika'."
    Konopski "A czy moglibyśmy skończyć tę rozmowę po procesie? Ja naprawdę muszę jeszcze..."
    Pearl "Ulubiony film"
    Pearl "Nagranie z procesu O.J.Simsona."
    Pearl "I komentarz: majstersztyk. opus magnum sądownictwa, pozycja obowiązkowa dla fanów rezolutnej dysputy."
    Konopski "..."
    Konopski "Fanów rezolutnej dysputy...? Serio?"
    Pearl "'Tańczący z wilkami', 'Braterstwo wilków'. 'Wilkołak'. 'Anakonda'"
    Pearl "Komentarz: czasami wychodzi ze mnie bestia ;P"
    Konopski "..."
    Konopski "Komentarz: Nie."
    Pearl "'Cube', 'Enigma', 'Sudoku', 'Krzyżówki panoramiczne'"
    Konopski "Czy... my nadal jesteśmy w kategorii filmy?"
    Pearl "To wszystko."
    Konopski "Dzięki bogu..."
    Konopski "Ok, to skoro już wiemy wszystko o czarnoksiężniku, to..."
    Penny "Następny punkt: Ulubione powiedzenia."
    Konopski "Dlaczego mi to robicie... Jestem po waszej stronie..."
    Ema "Rozeznanie na froncie wroga to podstawowa strategia."
    Konopski "Nawet jeśli,to nie wudaje mi się, że nie powinno ono obejmować 'ulubionych powiedzeń'..."
    Penny "Każdy kij ma dwa końce."
    Penny "Bo do dramy trzeba dwojga."
    Penny "Gdzie dwóch się bije, tam Wardęga korzysta."
    Konopski "..."
    Konopski "O co chodzi z tą dwójkową fiksacją?"
    Penny "Nie wywołuj Wardęgi z lasu."
    Konopski "Już to gdzieś słyszałem..."
    Penny "I ostatnie: z Wardęgą ci się upiecze."
    Konopski "..."
    Konopski "A to czyjego jest autorstwa? Wersow?"
    Penny "I tutaj jest znany autor..."
    Konopski "CO? SERIO? WERSOW?"
    Penny "Nie. Cyceron."
    Konopski "..."
    Konopski "Co by nie mówić, Wardęga nieźle się trzyma na swoje lata..."
    Konopski "..."
    Konopski "To już wszystko?"
    Ema "A chce pan więcej?"
    Konopski "NIE. Przysięgam, znam już czarnoksiężnika jak własną kieszeń, powiedz mi proszę teraz..."
    Ema "Ma pan do wyboru:
    [Psychotest] Jakim filmem Wardęgi jesteś?
    [Reportaż] Wychowany przez wilki
    [Wywiad] 'Można powiedzieć, że jestem współczesnym Tarzanem'
    [Historia] Kogo tak naprawdę skrywał koń trojański?
    [Uroda] Sztuczki i kruczki dla mężczyzn w kwiecie wieku
    [Quiz] Sprawdź jak dobrze znasz swojego ulubionego druida!"

    Konopski "DOŚĆ. Bardzo miło mi było was poznać dziewczyny, i naprawdę chętnie zostałbym z wami dłużej, ale..."
    jump namiejsce

    label namiejsce:
    "" "PANIE KONOPSKI, PROSZĘ ZAJĄĆ SWOJE MIEJSCE!"
    Konopski "Nie, nie, nie, szybko, gdzie jest kurtka, walić kurtkę, wycho..."
    "" "PANIE KONOPSKI NA MIEJSCE"
    Konopski "Panie strażniku, przysięgam na wszystko, sala sądowa absolutnie moim miejscem nie jest!"
    "" "PANIE KONOPSKI CZY MAM UŻYĆ SIŁY?"
    Konopski "Czy naprawdę musicie w tak przemocowy sposób traktować prokuratora?"
    "" "Szanowny panie, cóż to za pomówienia, oczywiście że traktujemy prokuratora z należytym szacunkiem!"
    Konopski "No to czy mógłby pan..."
    "" "Ale do oskarżonych z całą pewnością tego szacunku nie mamy!"
    Konopski "Słucham? Zaszła jakaś pomyłka, ja przecież..."
    Pearl "Powodzenia, panie Konopski! Dziękujemy za... rezolutną dysputę!"
    Konopski "Błagam, powiedzcie że to jakiś prank..."
    Konopski "Dubiel, gdzie jesteś...   ?"
    jump end

label end:
    return
