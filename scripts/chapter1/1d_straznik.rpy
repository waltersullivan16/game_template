# "../../files_list.rpy"
# "1a_poczatek.rpy"

# ../bin/gui_.rpy
# ../bin/conf.rpy
# ../characters.rpy
# ../screens.rpy


label namiejsce:
    # TODO inna poza dziewczyn
    $ play_music("hurry")
    scene black
    $straznik("{fast}PANIE KONOPSKI PROSZĘ ZAJĄĆ SWOJE MIEJSCE")
    scene lobby
    show konopski niesmak
    
    Konopski "Nie, nie, nie, szybko, gdzie jest kurtka, walić kurtkę, wycho...{nw}"
    
    $straznik("PANIE KONOPSKI, NA MIEJSCE, NATYCHMIAST")
    Konopski "Panie strażniku, przysięgam na wszystko, sala sądowa absolutnie moim miejscem nie jest!"
    $ straznik("PANIE KONOPSKI CZY MAM UŻYĆ SIŁY?")

    Konopski "Panie władzo, to one!"
    hide konopski
    show pearl serious
    show ema confused at right
    show penny at true_left
    with moveinbottom
    Konopski "To one sporo namieszały!"
    Konopski "Próbowałem stawiać opór, ale miały przewagę liczenbą!"
    Konopski "Przysięgam, wszystkiemu winne są te baby!"
    
    Straznik "Dziewczyny, musicie stąd zmykać, więc pożegnajcie się z waszym ulubionym youtuberem."
    Straznik "Potem możecie już nie mieć okazji."

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
    Konopski "Będziecie pamiętały o łapeczkach w górę, prawda...?"
    $ straznik("Jeszcze jedno słowo i wejdzie pan na salę sądową z łapeczkami w górze!")
    pause 1.0
    hide pearl
    hide ema
    hide penny 
    with moveoutbottom
    Konopski "{size=-10} Nie zapomnijcie o subie z dzwoneczkiem!{/size}"

    $ straznik("PANIE KONOPSKI")
    show konopski main
    Konopski "No przecież idę, po co te nerwy."
    pause 0.5
    Konopski "Swoją drogą, czy naprawdę musicie w tak przemocowy sposób traktować prokuratora?"
    $ straznik("Szanowny panie, cóż to za pomówienia!")
    $ straznik("Oczywiście że traktujemy prokuratora z należytym szacunkiem!")
    Konopski "Jakoś nie wydaje mi{nw}"
    $ straznik("Ale do oskarżonych z całą pewnością tego szacunku nie mamy!")
    Konopski "Ale że jak? {w=1}Zaszła jakaś pomyłka, ja przecież{w=0.3}{nw}"
    $ straznik("PANIE KONOPSKI!")
    Konopski "Błagam, powiedzcie że to jakiś prank..."
    Konopski "Dobra robota, totalnie dałem się nabrać! Możecie już wyjść z ukrycia!"
    $ stop_music()
label omg:
    show lobby
    #show konopski at t 
    show lobby_black with transition("imdis", reverse=True)
    show konopski main at Position(xpos=0.5, ypos=1.15) behind lobby_black with moveinbottom
    Konopski "Dubiel gdzie jesteś?"
    ### TODO Koniec
    jump end

label end:
    return
