# ../../files_list.rpy

### MENU 1 + SZUKANIE BLOWKA
label menu1_blowek:
    show screen choices1_blowek
    pause

label blowek:
    $ thinking(
        Konopski,'''
Tak, to dobry pomysł.
Jego obecność niewątpliwie podniosłaby moje morale.
Nie mógłbym przecież okryć się hańbą na oczach mistrza.
''')
    scene bg black with transition("wet", 2)
    $stop_music()
    jump check_blowek1a

label lexi:
    jump blowek

label grafika:
    jump blowek

label check_blowek1a:
    $ loading()
    scene bg transparenty0 with transition("wet", time=2) 
    $play_music("scary")
    $thinking(
        Konopski,'''
...
Co to ma kuźwa być?
Gdzie się podziała śmietanka towarzyska youtuba?
Gdzie kamery...? {w=1} Mateusz Kaniowski...? {w=1}Pełnoletnie fanki, mdlejące na mój widok...?
Czy cały wysiłek włożony w przygotowanie tych wszystkich wilczych punów pójdzie na marne?
Po co mam się niby wysilać, skoro i tak nie ma nikogo, kto mógłby potem zmontować kompilację \'Konopski best of\'?
...
Kogo my tu mamy?
Patrząc na te plebejskie twarze muśnięte odrobiną chamstwa, cała ta horda to wyznawcy Wardęgi.
''')
    $ thinking(Konopski, "Pardon, cała ta {size=+5}WATAHA®{/size}.")
    $ play_sound_effect("badum")
    pause 2.0
    $thinking(
        Konopski,'''
To nawet nie był żart.
W każdym razie, czy Wardęga serio nie mógłby urządzać zlotu swoich fanów w innym miejscu niż sala rozpraw...?
Na przykład w buszu?
I co ma ze sobą ta baba po lewej?
''')

label check_blowek1b:
    show junko1 with dissolve
    $renpy.pause(1)
    show junko2 with dissolve

    $thinking(
        Konopski,'''
O wilku mowa, złapała ze mną kontakt wzrokowy.
...
W sumie to całkiem sympatycznie...{nw}
''')
    $ stop_music()
    show junko3 with vpunch

    $ thinking(Konopski, "{size=+20}{fast}Co do...?{/size}")

    show toko1 with dissolve
    show toko22

label check_blowek1c:
    $ thinking(Konopski, "Współczuję tej okularnicy całym sercem, ja na jej miejscu chyba bym{nw}")
    show toko3 with vpunch
    Konopski "{fast}{size=+50}Ja pierdolę co jest grane{/size}"

label check_blowek_kokichi:
    $ thinking(Konopski,"Co to za stado poje{nw}")
    $ scene_courtroom1()
    show blur with transition("maska", 3)
    show kokichi at creepy_kokichi with Dissolve(4.0)
    pause(2)
    $play_sound_effect("upadek")
    scene black with vpunch

label check_blowek1e:
    $renpy.pause(2.0, hard=True)
    scene lobby with transition("eye", time=1.5, parts=16)
    $ thinking(
        Konopski,'''
...
Nie wydaje mi się, żeby na sali był Blowek.
...
Zrobiło się tu strasznie duszno...
''')
    jump menu2_blowek2


### MENU 2 + SZUKANIE BLOWKA 2
label menu2_blowek2:
    show lobby# with alpha_example
    show screen choices2_blowek_sequel
    pause

label pocieszajka:
    jump blowek2

label blowek2:
    scene lobby
    $renpy.pause(1.0, hard=True)
    $ thinking(
        Konopski,'''
Poprawić czuprynkę?
Jak można poprawić czystą perfekcję?
Czemu w ogóle przeszło mi to przez myśl?
Poza tym, zorientowałbym się od razu, gdyby Blowek-sensei był na sali.
Zawsze i wszędzie dojrzałbym przystojne lico tego youtubowego Adonisa.
...
No dobra, sprawdzę. Tak dla pewności.
Może uda mi się to zrobić na tyle dyskretnie, że nawet mnie nie zauważą.
A nawet jeśli, to i tak nie ma się czym przejmować. Najgorsze i tak już mam za sobą.
''')
label lo:
    scene bg black with transition("farba") 
    $stop_music()
    pause(1)
    $ thinking(Konopski, "Przynajmniej taką mam nadzieję...")
    $ loading(transition("farba"), Dissolve(2.0))
    jump check_blowek2a

label check_blowek2a:
    scene normal with slow_fade
    $ thinking(
        Konopski,'''
Jakoś tu spokojniej i mniej niepokojąco.
Może to zasługa światła.
A może to ja odrobinę się już wyluzowałem i zacząłem postrzegać rzeczy takimi, jakimi są naprawdę.
Może to nie było nawet stado Wardęgi.
Pardon, {size=+10}WATAHA®{/size} Wardęgi.
''')

    pause 1.5
    $ thinking(
        Konopski,'''
No i gdzie ba-dum-tssk?
Tym razem to miało pretendować do kategorii żart.
''')
    pause 1.0 
    $ thinking(
        Konopski, '''
Amatorzy.
''')
label check_blowek2b:
    scene bg transparenty1
    #$ persistent.special_sound = "badum"
    $ thinking(Konopski, "Mniejsza o to. Może to nie była nawet {size=+10}WATAHA®{/size}{nw}")
    $ play_sound_effect("badum")
    $ renpy.pause(2.0)

    $ thinking(
        Konopski,'''
Nie! {w=0.5} Tu tak totalnie {cps=10}NIE{/cps}!
Bardziej "NIE" niż za pierszym razem!
''')
    $ thinking(
        Konopski,'''
Czy wy w ogóle wiecie czym jest <ba-dum-tsk>?
''')
    pause(1)
    $play_sound_effect("badum")
    pause(3)
    $ thinking(Konopski, "...")
    scene bg transparenty2
    $ thinking(
        Konopski,'''
Z kim ja pracuję...
Dobra, jeszcze raz.
''')
    $ thinking(Konopski, "To nie byli ludzie z fandomu...{nw}")
    $play_sound_effect("badum")
    pause 2

label check_blowek2c:
    show blur with dissolve
    show konopski ej at right with moveinright
    Konopski "No już bez jaj co się tam dzieje?"
    show bg transparenty3 behind blur
    show konopski ej angry angry_eyes with vpunch
    Konopski "No kuźwa, co za ciul wpuścił tu Chmielarka?" with vpunch
    Konopski "I od razu ostrzegam, niech mi tu żaden śmieszek nawet nie próbuje wykręcić się wersją 'kurier przyniósł go w paczce'"
    Konopski "Bo to będzie żart śmieszny jak jego wypłata.{w=1}{nw}"
    $ play_sound_effect("badum")
    pause 3.0
    Konopski ej happy_eyes flower "Jest jakiś progres."
    pause 1
    Konopski ej -flower -happy_eyes "Że co proszę?"
    Konopski "Podczas rozmowy rekrutacyjnej zagrał na pianinie niczym prawdziwy wirtuoz?"
    Konopski ej angry angry_eyes "A co to kuźwa ma za znaczenie?{w=1}"
    Konopski "Jeszcze chwila i wszyscy wylecicie stąd na zbity ryj."
    pause 1
    Konopski ej -angry -angry_eyes "Nie mądralo, nie zdążysz ukryć się w szafie."
    Konopski "Przede wszystkim dlatego, że tu nie ma żadnej szafy."
    pause 1
    Konopski ej angry_eyes angry "{cps=10}NIE{/cps}, osobiście dopilnuję, żeby nie wpuszczać tu żadnego kuriera z szafą w paczce!"
    pause 1
    

label koniec_przerwy:
    Konopski ej -angry_eyes -angry "Dobra, nie traćmy więcej czasu i zapomnijmy o sprawie."
    Konopski "Znajcie łaskę pana."
    Konopski ej angry_eyes "Ale niech mi to będzie ostatni raz, zrozumiano...?"
    pause 1
    show konopski -angry_eyes with ease
    Konopski "A teraz wracamy do pracy obiboki!"
    Konopski "Światła!{w=0.5} {size=+5}Kamera!"
    show konopski at half_out
    pause 3.0
    show question at question_konop
    Konopski "Świetnie, straciłem wątek.{w=1} O czym to ja...?"
    pause 1
    hide question
    Konopski ej happy_eyes "No oczywiście! Obrażanie tiktokerów!" 
    Konopski "Dziękuję randomowy statysto!"
    hide konopski with moveoutright
    pause 1.0
    Konopski "{size=+10}AKCJA!{/size}"
    hide blur with dissolve

label transparenty_poczatek:
    $ thinking(
        Konopski,'''
Ten motłoch, to najprawdopodobniej jakieś dzbany z tiktoka.
O w dupę, przygotowali jakieś transparenty.
''')
    Konopski '''
Ej, ty!
Dziwna dziewczynko z misiem!
'''
    show bg transparenty5
    Konopski '''
Tak ty.
mogłabyś odwrócić ten transparent w moją stronę, żebym mógł...{nw}
'''

label check_blowek2e:
    $ image_punch("zniszcz_sztubaka")
    pause 2.0
    Konopski "Albo wiesz co, zmieniłem zdanie, możesz już zabrać swój{nw}"
    $image_punch("zad")
    pause 1.0
    $ thinking(
        Konopski,'''
Prostackie grubiaństwo. Niczego innego się po nich nie spodziewałem.
Jaki pan, taki kram.
Kto z Wardęga przystaje{nw}
''')
    $image_punch("sor")
    pause 2.0
    $ thinking(
        Konopski,'''
...
Muszę przyznać, że ta eskalująca agresja wywołuje we mnie lekką nutkę niepokoju...
''')
label danger_transparenty:
    scene black with transition("farba", time=1.5)
    $stop_music()
    show konopski main with moveinbottom
    $ character_monologue(Konopski, '''
Ech, te dzisiejsze fandomy.
{cps=10}ZA MOICH CZASÓW{/cps} wszyscy żyli ze sobą w zgodzie i harmonii. A teraz...? Szkoda gadać.
Tym dzikusom nie pomoże już najbardziej prestiżowy kurs walki z patusiarstwem.{w=1}
Mam oczywiście na myśli Projekt Lady.
No ale nieważne. Nie wiem czemu aż tak spinam dupę.
Co mnie obchodzi zepsucie moralne jakiejś leśnej hołoty?
W gruncie rzeczy są oni przecież nieszkodli {nw}
''')
    hide window
    
    $play_video("transparenty")
    scene black
    $ loading()

    jump menu3_uciekaj

### MENU 3 + PRÓBA UCIECZKI

label menu3_uciekaj:
    scene lobby
    $ thinking(Konopski, '''
...
Haha{w=0.5} {size=-5}hahaha{/size}{w=0.8}{size=-10} ha
Co za banda pociesznych zgrywusów...
Aż mi się łezka w oku zakręciła...{w=1}
A Blowka jak nie było tak nie ma...
{cps=10}...{/cps}
Taaaa...
Skoro sensei uznał, że nie jest to na tyle istotne wydarzenie, żeby zawracać sobie nim głowę...
...to czy nie byłoby to z mojej strony wysoce niestosowne, gdybym sam się na nim pojawił?
Może to zostać odebrane jako próba podważenia słuszności jego decyzji.
''')
    show screen choices3_uciekaj
    pause

label uciekaj:

    $ thinking(
        Konopski,'''
Chwila. Stop.
Nie mogę tak po prostu stąd wyjść...
{cps=8}...{/cps}{w=2}
Gdzie mój płaszcz?
...
Dobra, walić to, spadam jak jest.
Narauuu{nw}''')
    jump dziewczeta
