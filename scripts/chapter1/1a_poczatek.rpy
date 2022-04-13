# ../../files_list.rpy

### QUOTE SCREEN (JEŻELI SĄDZISZ...)
label quote_screen:
    $ t = "Jeżeli sądzisz, że w dobie internetu, normy moralne przestały obowiązywać (a zwłaszcza ciebie), to niezawodny znak, że jesteś "
    $ influ = "INFLUENCEREM"
    
    $ author = "mała dziewczynka z warkoczykami"
    $ author_errata1 = "mała dziewczynka {s}z warkoczykami{/s}{w=2}"
    $ author_errata2 = "mała dziewczynka {s}z warkoczykami{/s}{w=2} albo i bez warkoczyków"
    scene black
    pause 0.5
    show screen quote(t, influ, author, author_errata1, author_errata2) with slow_dissolve 
    pause 12.0
    hide screen quote with wet
    jump konop_monolog1
    
### KONOP MONOLOG 1 + TITLE
    
label konop_monolog1:
    scene intro with very_slow_fade
    $ change_style("intro")

    $ play_music("intro", loop=False)
    $ intro_monologue(Blank, '''
No i wreszcie nadszedł ten moment.
Dzień, w którym raz na zawsze udowodnię, kto jest czarnym charakterem w tej historii.
To była długa i wyczerpująca batalia.
Początkowo niepozorna, eskalowała błyskawicznie.
Zanim się obejrzałem, stała się całym moim życiem.
Nie będę ukrywał, bywało {b}NAPRAWDĘ{/b} ciężko.
Ciężko na tyle, że aż rozważałem odejście z youtuba.
Czy żałuję, że otworzyłem tę puszkę Pandory?{w=1} Raczej nie.
Wszystkie trudy i znoje były warte tej jednej magicznej chwili, która dzisiaj niewątpliwie nastąpi.
Lexiu usłyszy dzisiaj wyrok...''')
    #scene intro2
    jump winny
    
label winny:
    $ stop_music()
    scene intro2
    # winny
    $ play_music("title", fadein=0.0, loop=False)
    pause 2.1
    show winny at title_beating with m
    show black behind winny with slow_dissolve
    pause 2.0
    hide winny with wet_time(1.2)

    # TODO nazwa studia
    show text Text("to ma mnie upokorzyć proudly presents", style="creepy_text_style") at truecenter with fast_dissolve
    pause 3.4
    hide text with dissolve

    # zbrodnia, kara subskrybcje
    show title_blank at Position(ypos=0.6) with wipeleft
    pause 0.3
    show zbrodnia at Position(ypos=0.6) with vpunch
    pause 0.5
    show kara at Position(ypos=0.6) with vpunch
    pause 0.1
    show pasek at Position(ypos=0.6) with wipeleft
    pause 0.1
    show subskrypcje at Position(ypos=0.6) with Dissolve(2)

    # chapter 0
    show text Text("CHAPTER 0{p=3} PROLOG", style="chapter_text_style") at Position(ypos=0.8)
    pause 5.0
    $ stop_music()
    jump konop_monolog2

### KONOP MONOLOG 2 + SUBSKRYBCJE + KRÓTKI MONOLOG MYŚLOWY LOL

label konop_monolog2:
    scene lobby with transition("farba", time=1.5)
    $ change_style("main")
    $ play_music("lobby")
    pause 1.0

    Konopski "A mówiąc o byciu winnym..."
    $ character_monologue(Konopski,'''
Mam nadzieję, że czują się tak wszyscy ci, którzy nie subskrybują jeszcze mojego kanału.
Jeśli należysz do tej grupy i nie chcesz, żeby wyrzuty sumienia zjadały cię od środka, naciśnij tu i teraz gustowny czerwony przycisk.
Nic cię to nie kosztuje, a zawsze możesz zrezygnować.
''')

label subscribe:
    #$dismiss_pause = true
    $ stop_music()
    show screen subscribe_screen
    $ renpy.pause(3.0)
    Konopski "Oczywiście uszanuję twoją decyzję, jakakolwiek by ona nie była.{w=3.0}{nw}"
    Konopski "Dam ci jeszcze trochę czasu na zastanowienie.{w=3.0}{nw}"
    Konopski "Długo jeszcze będę musiał czekać?"

label subscribe_like:
    show screen subscribed_screen
    Konopski "No to teraz łapka w górę!"
    #hide subscribed_screen
    show screen subscribed_like_screen
    pause

label subscribe_thanks:
    #$dismiss_pause = false
    Konopski "Fenomenalnie!"
    $ play_music("lobby")
    Konopski "Od razu wiedziałem, że mam do czynienia z prawdziwym koneserem sztuki!"
    #konopski "a skoro już mówimy o sztuce: spiesz się, bo zostały ostatnie sztuki mojej najnowszej eksluzywnej kolekcji bluz blovek"

label konop_monolog3:
    $ thoughts_monologue(Konopski,'''
...
Dobra, mam nadzieję, że wszystko się ładnie nagrało.
Wiem, że nie był to jakoś szczególnie porywający monolog, no ale cóż.
Cytując klasyka...
''')
    $ Konopski(text_style("itis", "it is what it is"))
    $ thoughts_monologue(
        Konopski,'''
Niełatwo jest cierpieć za miliony.
...
Co teraz?'''
)
    jump menu1_blowek
