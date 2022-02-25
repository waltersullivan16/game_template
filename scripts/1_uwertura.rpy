# "0_main.rpy"

# ../bin/gui_.rpy
# ../characters.rpy
# ../screens.rpy

label konop_monolog1:
    scene intro with fade
    $ change_style("intro")
    $ intro_monologue(Konopski, '''
No i wreszcie nadszedł ten moment.
Dzień, w którym raz na zawsze udowodnię, kto jest czarnym charakterem w tej historii.
To był bez wątpienia najbardziej... {cps=6}intensywny {/cps} miesiąc w moim życiu.
Nierealny do tego stopnia, że niejednokrotnie miałem wątpliwość, czy to wszystko dzieje się naprawdę. Nigdy nic nie wiadomo w dzisiejszej kulturze pranków.
Wydaje mi się jednak, że nawet najbardziej wysublimowane pranki mają jakieś granice, które postawione są nieco niżej niż sprawa w sądzie.
Czy żałuję, że otworzyłem tę puszkę Pandrory?{w}
Raczej nie.
Nie będę zaprzeczał, to nie była bezbolesna batalia. Bywały momenty, gdy chciałem rzucić to wszystko, skasować kanał i odseparować się już na zawsze od youtubowego świata.
Jednak bez względu na wszystko, sprawa jest na tyle ważna, że nie powinno się pozwolić, aby po prostu poszła w eter. Wiem że to po mojej stronie jest sprawiedliwość!
Wszystkie trudy i znoje były warte tej jednej magicznej chwili, która dzisiaj niewątpliwie nastąpi.
Lexiu ustłyszy dzisiaj wyrok...''')
    scene intro2
    pause
    jump konop_monolog2


label konop_monolog2:
    show winny with m
    pause
    hide winny
    scene lobby with fade
    $change_style("main")
    $ thoughts_monologue(
        Konopski,'''
...
Dobra, mam nadzieję, że wszystko się ładnie nagrało.
Wiem, że nie był to jakoś szczególnie porywający monolog, no ale cóż.
Cytując klasyka...
{image=itis}{alt}itis{/alt}
Niełatwo jest cierpieć za miliony.
...
Co teraz?''')
    jump wybor1

label wybor1:
    show blur
    show screen choices1
    pause

label blowek:
    $renpy.hide_screen("choices1")
    hide blur
    $ thoughts_monologue(
        Konopski,'''
Tak, to dobry pomysł.
Jego obecność niewątpliwie podniosłaby moje morale.
Nie mógłbym przecież okryć się hańbą na oczach mistrza.
''')
    scene bg_black
    pause 1.0
    jump poblowku

label poblowku:
    scene lobby
    $ thoughts_monologue(
        Konopski,'''
To... nie wygląda dobrze...
Miałem wrażenie, że jestem w koloseum, a nie na sali rozpraw...
Zebrała się tam chyba cała horda Wardęgi...
Część z nich miała transparenty z hasłami typu...
SYLWEK, SYLWEK ZNISZCZ SZTUBAKA, WSPIERA CIĘ CAŁA WATAHA.
Albo
KONOP LEPIEJ SIĘ ZAWIJAJ, BO WARDĘGA DA CI W RYJA!
Albo
NIEWAŻNE ILE MASZ LAT, KOPNIJ KONOPSKIEGO W ZAD.
Jest tam nawet jakiś koleś z popcornem.
Nie muszę chyba dodawać, że wszycy patrzyli na mnie wilkiem.
...
Zrobiło się tu strasznie duszno...
''')
    jump wybor2

label wybor2:
    show blur
    show screen choices2
    pause

label blowek2:
    $renpy.hide_screen("choices2")
    hide blur
    $ thoughts_monologue(
        Konopski,'''
Poprawić czuprynkę?
Jak można poprawić czystą perfekcję?
Czemu w ogóle przeszło mi to przez myśl?
Chyba jestem zmęczony...''')
    jump wybor3

label wybor3:
    show blur
    show screen choices3
    pause

label uciekaj:
    $renpy.hide_screen("choices3")
    hide blur
    scene lobby

    $ thoughts_monologue(
        Konopski,'''
Chwila. Stop.
Nie mogę tak po prostu stąd wyjść...
...
Gdzie mój płaszcz?
...
Dobra, walić to, spadam jak jest.
Nar...''')
    jump dziewczeta

label dziewczeta:
    Unknown "Och, tak się cieszę, że zdążyłyśmy! Bałyśmy się, że wszedł już pan na salę."
    show pearl embarassed with vpunch
    Pearl "A bardzo nam zależało, żeby podziękować panu za to wszystko co pan dla nas robi."
    show ema happy at right with vpunch
    Ema "Byłam bardzo zawiedziona, że afera cesarza narcyza przeszła zupełnie bez echa. Tak się cieszę, że tym razem udało się nagłośnić sprawę, może nareszcie coś się zmieni!"
    show penny gossip at true_left with vpunch
    Penny "Czy planuje pan dzisiaj poruszyć kwestię groomingu? Ten wątek jakoś zagubił się w całym tym ferworze walki, a przecież to naprawdę kluczowa sprawa."

    Konopski "..."
    $ thoughts_monologue(
        Konopski,
    "Niech to szlag.")
    show blur
    menu:
        "Uśmiechnij się czarująco i powiedz, że musisz iść do toalety":
            jump proba_ucieczki
        "Powiedz, że dasz im autograf, tylko muszą chwilę poczekać, bo zostawiłeś swój długopis w płaszczu":
            jump proba_ucieczki
        "To samo co powyżej, tylko zamień 'długopis' na 'pióro'. Brzmi bardziej dostojnie.":
            jump proba_ucieczki
        "Weź rozbieg, przeskocz nad najniższą i nie zatrzymuj się, aż nie dobiegniesz do domu. No chyba że gdzieś zauważysz swój wytworny płaszczyk.":
            jump proba_ucieczki

label proba_ucieczki:
    hide blur
    Konopski "Słuchajcie, jeśli chodzi o ten autograf, to dajcie mi chwilę..."
    Ema main "Proszę się nie wygłupiać, nie będziemy teraz zawracać panu głowy jakimiś błachostkami."
    Ema "Wiemy, że potrzebuje pan teraz jak najwięcej wsparcia."
    Penny main "Inni zaraz po usłyszeniu nazwiska prokuratora, uciekliby w popłochu."
    $ thoughts_monologue(
        Konopski, '''
Ja chciałbym uciec w popłochu, mimo że nawet nie usłyszałem...
...
Zaraz, zaraz.
Coś tu się nie zgadza.
Przecież to ja jestem prokuratorem.''')
    Konopski "O kim ty właściwie mówisz?"

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
    #pause
    scene black
    # #$ fading_text("sniff", 1.0, 400, 300, 600, 600, color="#fff", size=24)
    # pause
    #play sound "music/wardega.mp3"
    #show text creepy_maker("WARDEGA") with Dissolve(2, alpha=True)
    # pause
    #hide text with Dissolve(3, alpha=True)
    #pause
    $ change_style("creepy")
    show konopski smirk at right with ease
    Konopski "Wy... zdajecie sobie sprawę z tego, że \"Wardęga\" to nie jest jego imię, prawda?"
    Konopski main "Co tu się właśnie wydarzyło?"
    Konopski "Co stało się z pierwszoosobowy styl narracji?"
    Konopski "Sympatycznym w swej prostocie okienkiem dialogowym?"
    Konopski "Bogatym w szczegóły drugim planem?"
label kopniak:
    show pearl determined at kick_out
    pause 0.9
    show konopski at kicked_out
    pause 0.2
    Pearl "Ale proszę nie wchodzić w kadr!"
    show ema determined at right with moveinbottom
    Ema "A poza tym, czy naprawdę myśli pan, że jest to odpowiedni moment na łamanie czwartej ściany?"
    Konopski "A mógłbym mieć jakiekolwiek wątpliwości dlatego bo...?"
    pause
    Ema thinking "Tak właściwie to nie wiem, ale jest w tym coś budzącego grozę..."
    jump legenda

label legenda:
    show penny main at true_left with moveinbottom
    show pearl
    show ema at right
    Penny "No wie pan, jak to mówią..."
    Penny cards "Nie należy wywoływać Wardęgi z lasu..."
    Konopski "Jakoś nie wydaje mi się, żeby ktokolwiek, kiedykolwiek to powiedział..."
    Ema determined "Legenda głosi, że jeśli podczas jakiejś dramy, wypowie się trzy razy WARDEGA, to w przeciągu
    dwóch godzin przejmie on nad tą dramą dowództwo, zmieniwszy wcześniej całą istotę problemu na coś zupełnie innego."
    Penny cards "Nie wolno jednak igrać z siłami ciemności."
    Penny "Użycie watahańskiej mocy dla własnych korzyści może przynieść poważne konsekwencje."
    Pearl "Jak to mówią: Wardęga nierychliwy, ale sprawiedliwy."
    Konopski "..."
    Konopski "Ci nieistniejący 'oni' mają zadziwiająco wiele do powiedzenia na temat Wardęgi..."
    Ema notes "A teraz, ku przestrodze, zobaczmy do czego prowadzić wymawianie imienia czarnoksiężnika swego na daremno."
    hide Ema
    hide Pearl
    hide Penny
    scene black
    Konopski "A teraz, ku przypomnieniu, podkreślmy fakt, że jego imię brzmi 'Sylwester', a nie 'Wardega'..."
    pause
    Konopski "Co, znowu cutscenka...? No błagam..."
    # vutscenka lol
    jump gazeta0

label gazeta0:
    scene lobby with fade
    show pearl serious
    show ema confused at right
    show penny at true_left
    Konopski "..."
    Konopski "Słuchajcie, nie żebym się czepiał, ale czy nie wydaje wam się, że odrobinę przesadzacie z tym dramatyzmem?"
    Ema thinking "Ale to przecież nie jest naszego autorstwa."
    Penny gossip "To był filmik {b}KU PRZESTRODZE{/b}, umieszczony na oficjalnej stronie Wardęgi {a=a}www.zorro-z-lasu2.com{/a}. Prawie wszystko co do tej pory powiedziałyśmy pochodzi z tej strony."
    Konopski "To... wiele tłumaczy..."
    $ Konopski(thoughts_text("Błagam, powiedzcie mi, że ta dwójka na końcu to część jakiejś zagadki..."))
    $ thoughts_monologue(
        Konopski, '''
To niemożliwe, że istnieje jeszcze jeden zorro-z-lasu, {w=1.0}prawda...?{w} {p}{size=+10}{cps=6}{b}PRAWDA?{/b}{/cps}{/size}''')
    Ema "Jest tu jeszcze sekcja {i}'Poznaj czarnoksiężnika'{/i}."
    Konopski "A czy moglibyśmy skończyć tę rozmowę po procesie? Ja naprawdę muszę jeszcze...{nw}"
    #$ Pearl(newspaper_text("{u}Ulubiony film{/u}{p}Nagranie z procesu O.J.Simsona."))
label gazeta1:
    show pearl
    show ema at left
    show penny at right
    scene ulubione_filmy
    $change_style("www")
    #Konopski "dsadadad" (multiple=2)
    #Pearl "{size=+10}{font=gui/fonts/chomsky.ttf}{u}Ulubiony film{/u}{/font}{/size}{font=gui/fonts/unique.ttf}{p}Nagranie z procesu O.J.Simsona.{/font}"(multiple=2)
    $ fav_filmy1 = [
        text_style("coda", "1) Nagranie z procesu O.J.Simsona{w}"),
        text_style("www", "{p}{u}Komentarz{/u}:{size=+10}{cps=3} MAJSTERSZTYK.{/cps}{/size}{p}Opus magnum sądownictwa.{p}Pozycja {b}obowiązkowa{/b} dla fanów rezolutnej dysputy!!!{w}\n"),
        "\n\n\n",
        text_style("dark_thoughts", "{image=minikonopski} Fa...{w=1} fanów rezolutnej dysputy...?"),
    ]
    $Pearl("".join(fav_filmy1))
    $ fav_filmy2 = [
        text_style("coda", "2) Tańczący z wilkami"),
        text_style("coda", "3) Braterstwo wilków"),
        text_style("coda", "4) Wilkołak"),
        text_style("coda", "5) Anakonda"),
        text_style("www", "{u}Komentarz{/u}: Czasami wychodzi ze mnie bestia ;P{w}\n"),
        text_style("dark_thoughts", "{image=minikonopski}..."),
        text_style("dark_thoughts", "{u}Komentarz{/u}:{w} Nie{p}{w} Po prostu {w}{b}{size=+10}NIE{/size}{/b}.")
    ]
    $Pearl("{w}\n".join(fav_filmy2))

    $ fav_filmy3 = [
        text_style("coda", "6) Cube"),
        text_style("coda", "7) Enigma"),
        text_style("coda", "8) Sudoku"),
        text_style("coda", "9) Krzyżówki panoramiczne"),
        text_style("dark_thoughts", "\n{image=minikonopski}"),
        text_style("dark_thoughts", "Czy my nadal jesteśmy w kategorii 'filmy'...?")
    ]
    $Pearl("{w}\n".join(fav_filmy3))
label gazeta2:
    hide pearl
    hide ema
    show bg ulubione_filmy with wiperight
    show pearl at true_left with moveinbottom
    $change_style("main")
    Pearl "To wszystko."
    $Konopski(text_style("thoughts", "Dzięki bogu..."))
    Konopski "Ok, to skoro już wiemy wszystko o czarnoksiężniku, to..."
    show bg ulubione with wiperight
    show ema at Position(ypos=800) with moveinbottom
    Ema main "{w=1}Ulubione powiedzenia"
    show bg ulubione_powiedzenia with wiperight
    Konopski "Dlaczego mi to robicie... Jestem po waszej stronie..."
    show pearl determined
    Ema determined "Musi pan myśleć strategicznie!"
    Ema "Dobre rozeznanie na froncie wroga może dać istotną przewagę!"
    $Konopski(thoughts_text("No jasne, już nie mogę się doczekać momentu, w którym zmiotę wszystkie argumenty Wardęgi siłą jego ulubionych powiedzeń..."))
    hide pearl with moveinbottom
    hide ema with moveinbottom
label powiedzenia:
    hide ema
    hide pearl
    $ change_style("www")
    $ fav_powiedzenia= [
        text_style("coda", "1) Każdy kij ma dwa końce"),
        text_style("www", "1) Każdy kij ma dwa końce"),
        text_style("coda", "2) Bo do dramy trzeba dwojga"),
        text_style("coda", "3) Gdzie dwóch się bije, tam Wardęga korzysta,"),
        text_style("dark_thoughts", "\n{image=minikonopski}..."),
        text_style("dark_thoughts", "Początkowo trochę zbił mnie z tropu ten odświeżający powiew normalności, ale widzę że koniec końców wszystkie drogi prowadzą do Wardęgi...")
    ]
    $Ema(list_text(fav_powiedzenia))
    $thoughts_monologue(Konopski, '''
...
No świetnie, mi też już zaczyna się udzielać ten zryty klimat...
Muszę się stąd szybko ewakuować, bo zaraz totalnie zwardęguję...
...
Muszę się stąd ewakuować {cps=6}NATYCHMIAST{/cps}.''')
    $Penny(text_style("chomsky", "Nie wywołuj Wardęgi z lasu."))
    $Konopski(thoughts_text("Już to gdzieś słyszałem..."))
    Penny "I ostatnie:"
    $Penny(text_style("chomsky", "Z Wardęgą ci się upiecze."))
    Konopski "..."
    Konopski "Może jeszcze powiesz, że autorem tych słów jest Wersow, co?"
    Penny "Nie. {w}Cyceron."
    Konopski "..."
    Penny "Tak nawiasem mówiąc, tylko w tym przypadku autor jest znany. Całą reszta ma tylko adnotacje 'powiedzenie ludowe'"
    $Konopski(thoughts_text("..."))
    $Konopski(thoughts_text("Co jak co, ale jednego Wardędze nie można odmówić."))
    $Konopski(thoughts_text("Zaskakująco dobrze się trzyma jak na swoje lata..."))
    pause
    Konopski "To już wszystko?"
    Ema "A chce pan więcej?"
    Konopski "NIE. Przysięgam, znam już czarnoksiężnika jak własną kieszeń, powiedz mi proszę teraz..."
    Ema "Ma pan do wyboru:
    \[Psychotest\] Jakim filmem Wardęgi jesteś?
    \[Reportaż\] Wychowany przez wilki
    \[Wywiad\] 'Można powiedzieć, że jestem współczesnym Tarzanem'
    \[Historia\] Kogo tak naprawdę skrywał koń trojański?
    \[Uroda\] Sztuczki i kruczki dla mężczyzn w kwiecie wieku
    \[Quiz\] Sprawdź jak dobrze znasz swojego ulubionego druida!"

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
