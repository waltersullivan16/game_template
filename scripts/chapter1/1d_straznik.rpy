# "../../files_list.rpy"
# "1a_poczatek.rpy"

# ../bin/gui_.rpy
# ../bin/conf.rpy
# ../characters.rpy
# ../screens.rpy


label namiejsce:
    $ change_cps(10)
    $ Straznik(text_style("straznik", "PANIE KONOPSKI PROSZĘ ZAJĄĆ SWOJE MIEJSCE"))
    #$play_music("straznik")
    Konopski "Nie, nie, nie, szybko, gdzie jest kurtka, walić kurtkę, wycho...{nw}"
    $Straznik(text_style("straznik", "PANIE KONOPSKI, NA MIEJSCE, NATYCHMIAST"))
    Konopski "Panie strażniku, przysięgam na wszystko, sala sądowa absolutnie moim miejscem nie jest!"
    $Straznik(text_style("straznik", "PANIE KONOPSKI CZY MAM UŻYĆ SIŁY?"))
    Konopski "No nie wygłupiajmy się już, przecież nie jestem{nw}"

    Konopski "Dobrze, dobrze, już idę, po co te nerwy?"
    Konopski "Przecież tak się tylko z wami droczyłem, nie znacie się na żartach?"

    Konopski "Swoją drogą, czy naprawdę musicie w tak przemocowy sposób traktować prokuratora?"
    $Straznik(text_style("straznik", "Szanowny panie, cóż to za pomówienia, oczywiście że traktujemy prokuratora z należytym szacunkiem!"))
    Konopski "Jakoś nie wydaje mi{nw}"
    $Straznik(text_style("straznik", "Ale do oskarżonych z całą pewnością tego szacunku nie mamy!"))
    Konopski "Ale że jak? Zaszła jakaś pomyłka, ja przecież{nw}"
    Pearl "Powodzenia, panie Konopski! Dziękujemy za... rezolutną dysputę!"
    Konopski "Błagam, powiedzcie że to jakiś prank..."
    $ stop_music()
    Konopski "Dubiel, gdzie jesteś...   ?"
    jump end

label end:
    return
