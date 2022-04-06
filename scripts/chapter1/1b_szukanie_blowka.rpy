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
    scene bg black with transition("farba", 3)
    $stop_music()
    $loading("farba")
    jump check_blowek1a

label lexi:
    jump blowek

label grafika:
    jump blowek

label check_blowek1a:
    #scene bg black
    #pause 0.5
    #scene bg transparenty0 with transition("farba", time=3) 
    $play_music("scary")
    $thinking(
        Konopski,'''
...
Co to ma kuźwa być?
Gdzie się podziała śmietanka towarzyska youtuba?
Gdzie kamery...? {w=1} Mateusz Kaniowski...? {w=1}Pełnoletnie nastolatki, mdlejące na mój widok...?
Czy cały wysiłek włożony w przygotowanie tych wszystkich wilczych punów pójdzie na marne?
Po co mam się niby wysilać, skoro i tak nie ma nikogo, kto mógłby potem zmontować kompilację \'Konopski best of\'?
...
Kogo my tu mamy?
Patrząc na te plebejskie twarze muśnięte odrobiną chamstwa, cała ta horda to wyznawcy Wardęgi.
''')
    $ thinking(Konopski, "Pardon, cała ta {size=+5}WATAHA®{/size}.")
    $ play_sound_effect("badum")
    $thinking(
        Konopski,'''
To nawet nie był żart.
W każdym razie, czy Wardęga serio nie mógłby urządzać zlotu swoich fanów w innym miejscu niż sala rozpraw...?
Na przykład w buszu?
I co ma ze sobą ta baba po lewej?
''')

label check_blowek1b:
    show junko1 with dissolve
    pause(1.5)
    show junko2 with ease
    pause(1)

    $thinking(
        Konopski,'''
O wilku mowa, złapała ze mną kontakt wzrokowy.
...
W sumie to całkiem sympatycznie...{nw}
''')
    $ stop_music()
    show junko3 with vpunch

    $thinking(Konopski,"{size=+20}{fast}Co do...?{/size}")

    show toko1 with dissolve
    show toko22

label check_blowek1c:
    $ thinking(Konopski, "Współczuję tej okuarnicy całym sercem, ja na jej miejscu chyba bym{nw}")
    show toko3 with vpunch
    Konopski "{fast}{size=+50}Ja pierdolę co jest grane{/size}"

label check_blowek_kokichi:
    $ thinking(Konopski,"Co to za stado poje{nw}")
    show blur with transition("maska", 3)
    show kokichi at creepy_kokichi with Dissolve(4.0)
    pause(2)
    scene black with vpunch

label check_blowek1e:
    pause(2)
    scene lobby with transition("eye", 3, 64)
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
    pause(1)
    $ thinking(
        Konopski,'''
Poprawić czuprynkę?
Jak można poprawić czystą perfekcję?
Czemu w ogóle przeszło mi to przez myśl?
Poza tym, zorientowałbym się od razu, gdyby Blowek-sensei był na sali.
Zawsze i wszędzie dojrzałbym przystojne lico tego youtubowego Adonisa.
.{w=0.5}.{w=0.5}.{w=0.5}
Z drugiej strony, całą swoją uwagę skupiłem na walce o życie, więc moja percepcja mogła być odrobinę ograniczona...
''')
    $silence()
    $ thinking(
        Konopski,'''
No dobra, sprawdzę. Tak dla pewności.
Może uda mi się to zrobić na tyle dyskretnie, że nawet mnie nie zauważą.
A nawet jeśli, to i tak nie ma się czym przejmować.
Najgorsze i tak już mam za sobą.
''')
    #show black with transition("farba")
label lo:
    scene bg black with transition("farba") 
    $stop_music()
    pause(1)
    $ persistent.hide_dialogue_windows = True
    $ Konopski(text_style("black_screen", "Przynajmniej taką mam nadzieję..."))
    $ persistent.hide_dialogue_windows = False
    $ loading(transition("farba"), Dissolve(2.0))
    jump check_blowek2a

label check_blowek2a:
    scene normal with transition("farba", 3)
    pause(1)
    $ thinking(
        Konopski,'''
Jakoś tu spokojniej i mniej niepokojąco.
Może to zasługa światła.
A może to ja odrobinę się już wyluzowałem i zacząłem postrzegać rzeczy takimi, jakimi są naprawdę.
Może to nie było nawet stado Wardęgi.
Pardon, {size=+10}WATAHA®{/size} Wardęgi.
''')

    $ silence()

    $ thinking(
        Konopski,'''
No i gdzie ba-dum-tssk?
Tym razem to miało pretendować do kategorii żart.
''')
    $ silence(1)
    
    $ thinking(
        Konopski, '''
Amatorzy.
''')
label check_blowek2b:
    scene bg transparenty1
    $ thinking(Konopski, '''Mniejsza o to. Może to nie była nawet {size=+10}WATAHA®{/size}{nw}''')
    $ play_sound_effect("badum")
    pause(2)
    $ thinking(
        Konopski,'''
Nie! {w=0.5} Tu tak totalnie {cps=10}NIE{/cps}!
Bardziej "NIE" niż za pierszym razem!
''')
#~Sglitter
    $ thinking(
        Konopski,'''
Czy wy w ogóle wiecie czym jest <ba-dum-tsk>?
''')
    $silence(1)
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
    pause(3)
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
    pause 3
    show bg transparenty4 behind blur
    Konopski ej happy_eyes flower "Jest jakiś progres."
    $ offscreen_talking()
    Konopski ej -flower -happy_eyes "Że co proszę?"
    Konopski "Podczas rozmowy rekrutacyjnej zagrał na pianinie niczym prawdziwy wirtuoz?"
    #show konopski angry with vpunch
    Konopski ej angry angry_eyes "A co to kuźwa ma za znaczenie?{w=1}"
    Konopski "Jeszcze chwila i wszyscy wylecicie stąd na zbity ryj."
    $ offscreen_talking()
    #$stop_lipsync(Konopski, "...")
    Konopski ej -angry -angry_eyes "Nie mądralo, nie zdążysz ukryć się w szafie."
    Konopski "Przede wszystkim dlatego, że tu nie ma żadnej szafy."
    $ offscreen_talking()
    Konopski ej angry_eyes angry "{cps=10}NIE{/cps}, osobiście dopilnuję, żeby nie wpuszczać tu żadnego kuriera z szafą w paczce!"
    pause 1
    

label koniec_przerwy:
    Konopski ej -angry_eyes -angry "Dobra, nie traćmy więcej czasu i zapomnijmy o sprawie." with ease
    Konopski "Znajcie łaskę pana."
    Konopski ej angry_eyes "Ale niech mi to będzie ostatni raz, zrozumiano...?"
    $ offscreen_talking()
    show konopski -angry_eyes with ease
    Konopski "A teraz wracamy do pracy obiboki!"
    Konopski "Światła{w=0.5} {size=+5}kamera{w=0.5} {size=+5}AKCJA{/size}!"
    show konopski at half_out
    pause 3.0
    show question at question_konop
    Konopski "Świetnie, straciłem wątek.{w=1} O czym to ja...?"
    $ offscreen_talking(2)
    hide question
    Konopski ej happy_eyes "No oczywiście! {w=1}Dziękuję randomowy statysto!"
    Konopski -happy_eyes "Powróćmy zatem do znieważania tiktokerów!"
    hide konopski with moveoutright
    pause 1.0
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
    #show "zniszcz_sztubaka" with moveinbottom

    #$show_with_args("zniszcz_sztubaka", at_list=[blur], pause=2.0, sound="blup")
    #$image_punch("zniszcz_sztubaka")
    #$ show_with_args("zniszcz_sztubaka", transition=vpunch, sound="punch")
    $ image_punch("zniszcz_sztubaka")
    $silence(2)
    Konopski "Albo wiesz co, zmieniłem zdanie, możesz już zabrać swój{nw}"
#Czy ja właśnie odkryłem najgłębszą czeluść dantejskiego piekła?
    $image_punch("zad")
    $silence(2)
    $ thinking(
        Konopski,'''
Prostackie grubiaństwo. Niczego innego się po nich nie spodziewałem.
Jaki pan, taki kram.
Kto z Wardęga przystaje{nw}
''')
    $image_punch("sor")
    $silence(2)
    $ thinking(
        Konopski,'''
...
Muszę przyznać, że ta eskalująca agresja wywołuje we mnie lekką nutkę niepokoju...
''')
label danger_transparenty:
    scene black with dissolve
    $stop_music()
    show konopski main with moveinbottom
    $ character_monologue(Konopski, '''
Ech, te dzisiejsze fandomy.
{cps=10}ZA MOICH CZASÓW{/cps} wszyscy żyli ze sobą w zgodzie i harmonii. A teraz...? Szkoda gadać.
Tym dzikusom nie pomoże już nawet Projekt Lady.
A nie muszę chyba przypominać, że jest to wydział na najbardziej prestiżowym uniwersytecie walki z patusiarstwem.
No ale nieważne. Nie wiem czemu aż tak spinam dupę.
Co mnie obchodzi zepsucie moralne jakiejś leśnej hołoty?
W gruncie rzeczy są oni przecież nieszkodli {nw}
''')
    hide window
    
    $play_video("transparenty")

    jump menu3_uciekaj

### MENU 3 + PRÓBA UCIECZKI

label menu3_uciekaj:
    scene lobby
    $ thinking(Konopski, '''
...
No niestety, muszę wreszcie przestać oszukiwać samego siebie i zaakceptować fakt, że Blowka na pewno nie ma na sali.
{cps=10}...{/cps}
Taaaa...
Skoro sensei uznał, że nie jest to na tyle istotne wydarzenie, żeby zawracać sobie nim głowę...
...to czy nie byłoby to z mojej strony wysoce niestosowne, gdybym sam się na nim pojawił?
Może to zostać odebrane jako próba podważenia słuszności jego decyzji.
''')
    show screen choices3_uciekaj with dissolve
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
Nar...{w=1}{nw}''')
    jump dziewczeta
