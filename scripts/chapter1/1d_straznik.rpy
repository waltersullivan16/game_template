# "../../files_list.rpy"
# "1a_poczatek.rpy"

# ../bin/gui_.rpy
# ../bin/conf.rpy
# ../characters.rpy
# ../screens.rpy


label namiejsce:
    # TODO font + blip strażnika
    # TODO inna poza dziewczyn
    $ Straznik(text_style("straznik", "PANIE KONOPSKI PROSZĘ ZAJĄĆ SWOJE MIEJSCE"))
    #$play_music("straznik")
    Konopski "Nie, nie, nie, szybko, gdzie jest kurtka, walić kurtkę, wycho...{nw}"
    $Straznik(text_style("straznik", "PANIE KONOPSKI, NA MIEJSCE, NATYCHMIAST"))
    Konopski "Panie strażniku, przysięgam na wszystko, sala sądowa absolutnie moim miejscem nie jest!"
    $Straznik(text_style("straznik", "PANIE KONOPSKI CZY MAM UŻYĆ SIŁY?"))

    Konopski "Dobrze, dobrze, już idę, po co te nerwy?"

    Konopski "Swoją drogą, czy naprawdę musicie w tak przemocowy sposób traktować prokuratora?"
    $Straznik(text_style("straznik", "Szanowny panie, cóż to za pomówienia!"))
    $Straznik(text_style("straznik", "Oczywiście że traktujemy prokuratora z należytym szacunkiem!"))
    Konopski "Jakoś nie wydaje mi{nw}"
    $Straznik(text_style("straznik", "Ale do oskarżonych z całą pewnością tego szacunku nie mamy!"))
    Konopski "Ale że jak? {w=1}Zaszła jakaś pomyłka, ja przecież{w=0.3}{nw}"
    $Straznik(text_style("straznik", "PANIE KONOPSKI!"))
    Konopski "Dziewczęta, no nie bądźcie takie, zostawicie swojego ulubionego youtubera na pastwę losu?"
    ### TODO inne pozy dziewczyn
    Ema "Ależ skądże znowu! Przecież uzbroiłyśmy pana w arsenał, który z całą pewnością przyda się w starciu z nieprzyjacielem!"
    Konopski "..."
    Konopski "A dałyście chociaż łapeczki w górę...?"
    $Straznik(text_style("straznik", "Jeszcze jedno słowo i wejdzie pan na salę sądową z łapeczkami w górze!"))
    Konopski "Przecież tak się tylko z wami droczyłem, nie znacie się na żartach?"
    Konopski "{size=-10} Nie zapomnijcie o subie z dzwoneczkiem!{/size}"
    $Straznik(text_style("straznik", "PANIE KONOPSKI!"))
    Konopski "Melduję się w pełnej gotowości!"
    Pearl "Powodzenia, panie Konopski! Dziękujemy za... rezolutną dysputę!"
    Konopski "Błagam, powiedzcie że to jakiś prank..."
    $ stop_music()
label omg:
    show lobby
    #show konopski at t 
    show lobby_black with transition("black", reverse=True)
    show konopski main at Position(xpos=0.5, ypos=1.15) behind lobby_black with moveinbottom
    Konopski "Dubiel, gdzie jesteś...?"
    ### TODO Koniec
    jump end

label end:
    return
