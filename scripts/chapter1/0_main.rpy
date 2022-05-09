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
    show screen z with slow_fade
    jump uwertura_scenes

label uwertura_scenes:
    jump chapter27.a
    $ stop_music()
    menu:
        "currrent check":
            jump chapter27.a
            #jump transparenty
            #$ load()
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
            jump bloody_text
        "kopniak":
            jump kopniak
        "legenda":
            jump legenda
        "gazeta0":
            jump gazeta0
        "gazeta1":
            jump gazeta1
        "gazeta2":
            jump gazeta2
        "powiedzenia":
            jump powiedzenia
        "koniec_powiedzen":
            jump koniec_powiedzen

label straznik_menu:
    menu:
        "namiejsce":
            jump namiejsce
        "lilmasti_intro":
            jump lilmasti_intro
        "lilmasti_konop":
            jump masti_konop

#label chapter1_t:
# quite_screen    
