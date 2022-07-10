# ../files_list.rpy

init -1 python:
    def chapters_list():
        all_labels = renpy.get_all_labels()
        return sorted(list(filter(lambda x: x.startswith("chapter"), all_labels)))

    CHAPTERS = chapters_list() 

init python:

    def chapter_idx():
        return CHAPTERS.index(persistent.label)

    def prev_chapter():
        return CHAPTERS[max(0, chapter_idx() - 1)]

    def next_chapter():
        return CHAPTERS[min(len(CHAPTERS), chapter_idx() + 1)]

label start:
    show screen zz with slow_fade
    $ stop_music()
    if not persistent.testing:
        jump uwertura_scenes
    else:
        jump chapter30

label uwertura_scenes:
    $ stop_music()
    menu:
        "currrent check":
            $stop_music()
            jump chapter28
        "intro":
            jump intro_menu
        "szukanie blowka":
            jump szukanie_blowka_menu

        "dziewczyny":
            jump dziewczyny_menu
        "strażnik":
            jump straznik_menu

label intro_menu:
    menu:
        "początek":
            jump chapter0
        "monolog":
            jump chapter0._2konop_monolog1
        "winny":
            jump chapter0._3winny
        "monolog2":
            jump chapter1
        "subskrybuj":
            jump chapter1._2subscribe

label szukanie_blowka_menu:
    menu:
        "menu1":
            jump chapter21.menu1
        "szukanie blowka part1":
            jump chapter22
        "co robic2":
            jump chapter23
        "blowek2 poczatek":
            jump chapter24
        "ucieczka":
            jump chapter25

label dziewczyny_menu:
    menu:
        "bloody":
            jump chapter32
        "kopniak":
            jump kopniak
        "legenda":
            jump legenda
        "powiedzenia1":
            jump chapter33._4ulubione_powiedzenia1
        "powiedzenia2":
            jump chapter33._5ulubione_powiedzenia2
        "powiedzenia3":
            jump chapter33._6ulubione_powiedzenia3
        "koniec_powiedzen":
            jump koniec_powiedzen

label straznik_menu:
    menu:
        "namiejsce":
            jump chapter41._1na_miejsce
        "lilmasti_intro":
            jump lilmasti_intro
        "pozegnanie_dziewczyn":
            jump pozegnanie_dziewczyn
        "omg":
            jump omg

#label chapter1_t:
# quite_screen    
