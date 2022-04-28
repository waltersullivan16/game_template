# "../../files_list.rpy"
# "1a_poczatek.rpy"

# ../bin/gui_.rpy
# ../bin/conf.rpy
# ../characters.rpy
# ../screens.rpy


label namiejsce:
    $ play_music("hurry")
    show penny
    show ema
    show pearl
    scene lobby
    Unknown "PANIE KONOPSKI, PROSZĘ ZAJĄĆ SWOJE MIEJSCE"
    hide penny with moveoutbottom
    hide ema with moveoutbottom
    hide pearl with moveoutbottom

    Konopski "Nie, nie, nie, szybko, gdzie jest kurtka, walić kurtkę, wycho...{nw}"
    
    Unknown "KONOPSKI, NA MIEJSCE, NATYCHMIAST."
    Konopski "Ale proszę już tak nie drzeć ryja, ok?"
    Konopski "I za kogo ty się w ogóle masz, że zwracasz się do mnie takim tonem?"

    Unknown "KOGOŚ PRZED KIM ZARAZ PADNIESZ NA KOLANA, SKAMLĄC O PRZEBACZENIE."

    Konopski "No już drżą mi łydki ze{nw}"
    $ stop_music()
    $ play_sound_effect("punch")
    show glove at quick_zoom
    pause 0.5
    scene black with vpunch
    
label lilmasti_intro:
    pause 2.0
    $ persistent.style = "black"
    $ Blank(text_style("quote", "Panie i panowie, a oto moment na który wszyscy czekali."))
    $ Blank(text_style("quote","Powitajcie gorącymi brawami gwiazdę wieczoru"))
    $ play_music("lilmasti_intro1", loop=False)
    $ persistent.style = "main"
    pause 9.0
    scene stage with flashbulb
    pause 0.5
    show kon with moveinright
    pause 1.0
    show lilmasti justbody with transition("serduszka")
    hide kon
    show lilmasti radosc
    pause 2.0
    pause 0.9
    $ stop_music()
    show lilmasti angry
    LilMasti "Ej, wy tam."
    LilMasti "Żenująco ubodzy prostaczkowie."
    LilMasti "Ręcę wam odpadły od tej biedoty, czy co?"
    LilMasti "Gwiazdę wita się GORĄCYMI BRAWAMI."
    $play_sound_effect("applause", channel="sfx2")
    pause 3.0
    #$play_music("lilmasti_intro2", loop=False)
    LilMasti normal "Tak lepiej."
    show lilmasti radosc at bounce_left_right
    pause 3
    LilMasti normal "Dziękuję moi kochani, nie trzeba, naprawdę, zawstydzacie mnie."
    $stop_sound_effect(channel="sfx2")
    pause 1.0
    show lilmasti zdziwienie
    LilMasti "Czy ja wam pozwoliłam przestać, leniwe oszołomy?"
    LilMasti "Chyba stać was na więcej...?"
    $play_sound_effect("applause", channel="sfx2")
    pause 4.0
    show lilmasti normal at center with ease    
    LilMasti "Wystarczy."
    $stop_sound_effect(channel="sfx2")
    $ stop_music()
    LilMasti "Musicie mieć jeszcze trochę siły na stanie w kolejce po autografy."
    pause 1
    LilMasti "Ale spokojnie, nie wstawajcie z miejsc, wszystko w swoim czasie."
    LilMasti "Najpierw muszę spełnic swoją powinność."
    show lilmasti at out_left
    hide lilmasti

label lilmasti_boss:
    scene black with slow_dissolve
    $persistent.style = "black"
    $ Blank(text_style("black_screen", "Bo jak już na pewno wiecie, wasza..."))
    pause 0.5
    show lilmasti wpierdol with hpunch
    pause 0.5
    hide lilmasti with moveoutbottom
    $ Blank(text_style("strazmasterka", "STRAŻMASTERKA"))
    show lilmasti main with moveinbottom
    $persistent.style = "main"
    LilMasti "jest zawsze gotowa."
    pause 1.0
    show lilmasti scary
    LilMasti "By spuścić komuś wpierdol."
    hide window
    pause 1.0
    show lilmasti main
    LilMasti "Poproszę jakiś podkład do walki z bossem."
    # muza
    $ play_music("fight")
    pause 2.0
    LilMasti "Co to jest? Kołysanka?"
    $ play_music("rak")
    pause 3.0
    LilMasti "No i git."
    pause 1.0
    
    LilMasti "To by było na tyle, możemy wracać do głównej linii fabularnej."
label masti_konop:
    hide lilmasti moveoutbottom
    show lobby with dissolve
    show lilmasti main with vpunch
    $ thinking(Konopski, "Co za kijowe intro... Widać że robione na odwal")
    $ thinking(Konopski, "Czuję pewien dyskomfort przyznając to, ale nawet zorro-z-lasu2 dostarcza kontent wyższej jakości.")
    $ thinking(Konopski, "...")
    $ thinking(Konopski, "Ta muzyka wyżera mi mózg, przysięgam.")
    $ thinking(Konopski, "Muszę szybko coś z tym zrobić, bo inaczej naprawdę dojdzie do jakichś trwałych uszkodzeń.")
    LilMasti "{size=-15}Dobra chłystku, nie będę się tu z tobą cackać, pójdziesz po dobroci czy potrzebujesz motywacji?{/size}"
    Konopski "Eee... {w=1}Słucham?"
    LilMasti "{size=-15}Nie próbuj zgrywać głupszego niż jesteś, to może skończyć się katastrofą.{/size}"
    #LilMasti "{size=-15}Wszechświat nie jest przygotowany na takie stężenie debilizmu.{/size}"
    $ thinking(Konopski, "...")
    $ music_volume_wait()
    Konopski "Już idę, idę, tylko nie rób mi krzywdy!"

label pozegnanie_dziewczyn:
    Penny "Do widzenia panie Konopski."
    Ema "Dziękujemy za...{w=1}{nw}"
    Pearl "...rezolutną dysputę."
    Konopski "Haha, to ja dziękuję i no...{w=0.5} {w=0.5}eee... {w=0.5}tego..."
    Konopski "...polecam się na przyszłość...{w=1.5}?"
    $thinking(Konopski, "Polecam się na przyszłość? Serio nie mogłem wymyśleć niczego lepszego?")
    hide pearl
    hide ema
    hide penny 
    with moveoutbottom
    Konopski "Zaczekajcie chwilę!"
    show pearl serious
    show ema confused at right
    show penny at true_left
    with moveinbottom
    Konopski "Sorry że wam jeszcze zawracam głowę..."
    Konopski "Ale tak miło nam się rozmawiało i w ogóle...{w=1}"
    Konopski "Będziecie pamiętały o łapeczkach w górę, prawda?{w=1}{nw}"
    LilMasti "Jeszcze jedno słowo i wejdzie pan na salę sądową z łapeczkami w górze!"
    Konopski "No przecież idę, po co te nerwy?"

    Konopski "{size=-5} Nie zapomnijcie o subie z dzwoneczkiem!{/size}"
    Konopski "{size=-10} Nic was to nie kosztuje, a zawsze możecie...{/size}"
    LilMasti "KONOPSKI"
label ostatnie_pytanie:

    Konopski "Haha, no tak, oczywiście, już...{w=1} w tej chwili. {size=-5} Nie bij proszę{/size} {size=-10}Uważaj na okularki.{/size}"
    pause 1.0
    Konopski "Eeee... zanim wejdę, czy mógłabyś odpowiedzieć mi na jedno pytanie?"
    LilMasti "W drodze wyjątku."
    Konopski "Wiem, że nie stawiłem się na czas, trochę się z tobą podroczyłem i w ogóle."
    Konopski "Chłopcy będą chłopcami i takie tam."
    Konopski "Tak czy owak, czy naprawdę są to przewinienia upoważniające was do traktowania prokuratora w tak przemocowy sposób?"
    LilMasti "O czym ty mówisz chłopaczku?"
    LilMasti "Co to za bezsensowne insynuacje?"
    LilMasti "Oczywiściem, że traktujemy prokuratora z należytym szacunkiem!"
    Konopski "  Jakoś nie wydaje mi{nw}"
    LilMasti "Ale do oskarżonych z całą pewnością tego szacunku nie mamy!"
    Konopski "Ale że jak? {w=1}Zaszła jakaś pomyłka, ja przecież{w=0.3}{nw}"
    LilMasti "Wchodzisz, czy liczysz na pożegnalny kopniak?"
    Konopski "Błagam, powiedzcie że to jakiś prank..."
    Konopski "Dobra robota, totalnie dałem się nabrać! Możecie już wyjść z ukrycia!"
    # AUUUUU
    LilMasti "Moja noga już wyszła z ukrycia, czekasz jeszcze na coś?"
    Konopski "Nie, nie wystarczy, będę grzeczny, tylko puść już moją rękę."
    $ stop_music()
label omg:
    show lobby
    #show konopski at t 
    show lobby_black with transition("imdis", reverse=True)
    show konopski main at Position(xpos=0.5, ypos=1.15) behind lobby_black with moveinbottom
    Konopski "Dubiel gdzie jesteś?"
    Konopski "To jest ten moment, kiedy krzyczysz it's a prank, bro!"
    Konopski "Żegnaj słodkie życie."
    Konopski "Mam nadzieję, że Blowek zapłacze nad moją mogiłą." 
    #AUUUUUU
    Konopski "Przestań, już wchodzę!"
    ### TODO Koniec
    jump end

label end:
    return
