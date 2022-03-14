# ../../files_list.rpy

### QUOTE SCREEN (JEŻELI SĄDZISZ...)
label quote_screen:
    #$change_style("quote")
    $ t = "Jeżeli sądzisz, że w dobie internetu, normy moralne przestały obowiązywać (a zwłaszcza ciebie), to niezawodny znak, że jesteś "
    $ influ = "INFLUENCEREM"
    #$ t.append("{size=+10}INFLUENCEREM{/size}.")
    
    $ author = "mała dziewczynka z warkoczykami"
    $ author_errata1 = "mała dziewczynka {s}z warkoczykami{/s}{w=2}"
    $ author_errata2 = "mała dziewczynka {s}z warkoczykami{/s}{w=2} albo i bez warkoczyków"
    hide screen quote
    hide black
    show black
    show screen quote(t, influ, author, author_errata1, author_errata2) with slow_dissolve 
    pause 10.0
    hide screen quote with slow_dissolve
    jump konop_monolog1
    
### KONOP MONOLOG 1 + TITLE
    
label konop_monolog1:
    scene intro with very_slow_fade
    $ change_style("intro")
    #$ play_music("dangan_new_world")
    $ play_music("intro", loop=False)
    $ intro_monologue(Blank, '''
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
    jump winny
    
label winny:
    jump aa
    $ stop_music()
    scene intro2
    $ play_music("title", fadein=0.0, loop=False)
    pause 2.1
    show winny at title_beating with m
    show black behind winny with slow_dissolve
    pause 2.0
    hide winny with wet_time(1.2)
    show text Text("to ma mnie upokorzyć proudly presents", style="creepy_text_style") at truecenter with fast_dissolve
    pause 3.1
    hide text with dissolve
    show title_blank at Position(ypos=0.6) with wipeleft
    pause 0.1
    show zbrodnia at Position(ypos=0.6) with vpunch
    pause 0.4
label aa:
    show kara at Position(ypos=0.6) with vpunch
    pause 0.1
    show pasek at Position(ypos=0.6) with wipeleft
    pause 0.1
    show subskrypcje at Position(ypos=0.6) with Dissolve(2)
    show text Text("CHAPTER 0{p=3} PROLOG", style="chapter_text_style") at Position(ypos=0.8)
    pause 5.0
    $ stop_music()
    jump konop_monolog2

### konop monolog 2 + subskrybcje + krótki monolog myślowy lol

label konop_monolog2:
    scene lobby with wet
    $change_style("main")
    $ play_music("lobby")
    konopski "a mówiąc o byciu winnym..."
    $ character_monologue(konopski,'''
mam nadzieję, że czują się tak wszyscy ci, którzy nie subskrybują jeszcze mojego kanału.
jeśli należysz do tej grupy i nie chcesz, żeby wyrzuty sumienia zjadały cię od środka, naciśnij tu i teraz gustowny czerwony przycisk.
nic cię to nie kosztuje, a zawsze możesz zrezygnować.
''')

label subscribe:
    #$dismiss_pause = true
    $ stop_music()
    show screen subscribe_screen
    $ renpy.pause(3.0)
    konopski "oczywiście uszanuję twoją decyzję, jakakolwiek by ona nie była.{w=3.0}{nw}"
    konopski "dam ci jeszcze trochę czasu na zastanowienie.{w=3.0}{nw}"
    konopski "długo jeszcze będę musiał czekać?"

label subscribe_like:
    show screen subscribed_screen
    konopski "no to teraz łapka w górę!"
    #hide subscribed_screen
    show screen subscribed_like_screen
    pause

label subscribe_thanks:
    #$dismiss_pause = false
    konopski "fenomenalnie!"
    $ play_music("lobby")
    konopski "od razu wiedziałem, że mam do czynienia z prawdziwym koneserem sztuki!"
    #konopski "a skoro już mówimy o sztuce: spiesz się, bo zostały ostatnie sztuki mojej najnowszej eksluzywnej kolekcji bluz blovek"

label konop_monolog3:
    $ thoughts_monologue(konopski,'''
...
dobra, mam nadzieję, że wszystko się ładnie nagrało.
wiem, że nie był to jakoś szczególnie porywający monolog, no ale cóż.
cytując klasyka...
''')
    $ konopski(text_style("itis", "it is what it is"))
    $ thoughts_monologue(
        konopski,'''
niełatwo jest cierpieć za miliony.
...
co teraz?'''
)
    jump menu1_blowek

### MENU 1 + SZUKANIE BLOWKA
label menu1_blowek:
    show screen choices1_blowek
    pause

label blowek:
    $ renpy.pause(1.0, hard=True)
    $ thoughts_monologue(
        Konopski,'''
Tak, to dobry pomysł.
Jego obecność niewątpliwie podniosłaby moje morale.
Nie mógłbym przecież okryć się hańbą na oczach mistrza.
''')
    scene bg black with w18
    $stop_music()
    jump check_blowek1a

label lexi:
    jump blowek

label grafika:
    jump blowek

label check_blowek1a:
    show bg transparenty0 with slow_dissolve
    $play_music("scary")
    $thoughts_monologue(
        Konopski,'''
...
Co to ma kuźwa być?
Gdzie śmietanka towarzyska youtuba?
Gdzie są kamery?
Czy cały mój wysiłek włożony w przygotowanie tych wszystkich wilczych punów pójdzie na marne?
No bo po co mam się niby wysilać, skoro i tak nie ma nikogo, kto mógłby potem zmontować kompilację \'Konopski best of\'?
...
Kogo my tu mamy?
Patrząc na te plebejskie twarze muśnięte odrobiną chamstwa, cała ta horda to wyznawcy Wardęgi.
''')
    $ persistent.special_sound = "badum"
    $ Konopski(text_style("thoughts", "Pardon, cała ta {size=+10}WATAHA®{/size}."))
    $ renpy.pause(2.0, hard=True)
    $thoughts_monologue(
        Konopski,'''
To nawet nie był żart.
W każdym razie, czy Wardęga serio nie mógłby urządzać zlotu swoich fanów w innym miejscu niż sala rozpraw...?
Na przykład w buszu?
I co ma ze sobą ta baba po lewej?
''')

label check_blowek1b:
    show junko1 with dissolve
    $renpy.pause(1.5, hard=True)
    show junko2 with dissolve
    $thoughts_monologue(
        Konopski,'''
O wilku mowa, złapała ze mną kontakt wzrokowy.
...
W sumie to całkiem sympatycznie...{nw}
''')
    $ stop_music()
    show junko3 with vpunch
    $ Konopski(text_style("thoughts", "{size=+20}{fast}Co do...?{/size}"))
    show toko1 with zoomout
    show toko22

label check_blowek1c: 
    $ Konopski(text_style("thoughts", "Współczuję tej okuarnicy całym sercem, ja na jej miejscu chyba bym{nw}"))
    show toko3 with vpunch
    $ Konopski(text_style("thougts", "{fast}{size=+50}Ja pierdolę co jest grane{/size}"))
    #show transparenty_prolog
    #$renpy.pause(15.0, hard=True)

label check_blowek1d:
    $ Konopski(text_style("thoughts", "Co to za stado poje{nw}"))
    show blur
    show kokichi at co_to with Dissolve(3.0)
    $renpy.pause(2.0, hard=True)
    scene black with vpunch

label check_blowek1e:
    $renpy.pause(2.0, hard=True)
    scene lobby with eye
    $change_cursor("green")
    $ thoughts_monologue(
        Konopski,'''
...
Nie wydaje mi się, żeby był tam Blowek.
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
    $ thoughts_monologue(
        Konopski,'''
W żadnym wypadku. Nie odwaliło mi jeszcze do reszty.
Zresztą, naprawdę nie ma takiej potrzeby.
Zorientowałbym się od razu, gdyby tylko Blowek-sensei był na sali..
Aura doskonałości emanująca z tego youtubowego Adonisa zbyt wyraźnie odcinałaby go od reszty gawiedzi.
...
Z drugiej strony, isnieje mała szansa, że to stado zazdrosnych wieprzy spacyfikowało rzuconą przed nimi perłę.
...
Świetnie, teraz nie będę już mógł się uwolnić od obrazu obmierzłych raciczek, depczących po, coraz to bardziej zmasakrowanym, ciele Mistrza.
No dobra, sprawdzę. Ale tak SZYBCIUTKO.
Może uda mi się to zrobić na tyle dyskretnie, że nawet mnie nie zauważą.
A nawet jeśli, to i tak nie ma się czym przejmować. Najgorsze i tak już mam za sobą.
''')
    show black with w18
    $ Konopski(text_style("thoughts", "Przynajmniej taką mam nadzieję..."))
    jump check_blowek2a

label check_blowek2a:
    show normal with slow_fade
    $ thoughts_monologue(
        Konopski,'''
Jakoś tu spokojniej i mniej niepokojąco.
Może to zasługa światła.
A może to ja odrobinę się już wyluzowałem i zacząłem postrzegać rzeczy takimi, jakimi są naprawdę.
Może to nie było nawet stado Wardęgi.
Pardon, WATAHA® Wardęgi.
...
No i gdzie ba-dum-tssk?
Tym razem to miało pretendować do kategorii żart.
...
Amatorzy.
''')
label check_blowek2b:
    show transparenty1 with slow_dissolve
    $ persistent.special_sound = "badum"
    $ thoughts_monologue(
        Konopski,'''
''')
    $Konopski(text_style("thoughts", "Mniejsza o to. Może to nie była nawet WATAHA®"))
    $ renpy.pause(2.0, hard=True)

    $ thoughts_monologue(
        Konopski,'''
Nie, tu tak totalnie NIE!
Bardziej "nie" niż za pierszym razem!
Czy wy w ogóle wiecie czym jest <ba-dum-tsk>?
''')
    $ persistent.special_sound = "badum"
    $Konopski(text_style("thoughts", "..."))
    $ renpy.pause(2.0, hard=True)
    scene transparenty2 with dissolve
    $ thoughts_monologue(
        Konopski,'''
Z kim ja pracuję...
Dobra, jeszcze raz.
''')
    $ persistent.special_sound = "badum"
    $Konopski(text_style("thoughts", "To nie byli ludzie z fandomu...{nw}"))
    $ renpy.pause(2.0, hard=True)

label check_blowek2c:
    show blur with dissolve
    show konopski ej at right with moveinright
    Konopski "No już bez jaj co się tam dzieje?"
    show transparenty3 behind blur with dissolve
    show konopski ej angry with vpunch
    Konopski "No kuźwa, co za ciul wpuścił tu Chmielarka?" with vpunch
    Konopski "I od razu ostrzegam, niech mi tu żaden śmieszek nawet nie próbuje wykręcić się wersją 'kurier przyniósł go w paczce'"
    $ persistent.special_sound = "badum"
    Konopski "Bo to będzie żart śmieszny jak jego wypłata."
    $ renpy.pause(2.0, hard=True)
    Konopski ej_happy flower "Jest jakiś progres."
    show transparenty4 behind blur with dissolve
    Konopski ej -flower "Że co proszę?"
    Konopski "Podczas rozmowy rekrutacyjnej zagrał na pianinie niczym prawdziwy wirtuoz?"
    show konopski ej angry with vpunch
    Konopski "A co to kuźwa ma za znaczenie?"
    pause 1.0
    show konopski ej -angry
    Konopski "Jeszcze chwila i wszyscy wylecicie stąd na zbity ryj."
    Konopski "..."
    Konopski "Nie mądralo, nie zdążysz ukryć się w szafie."
    Konopski "Przede wszystkim dlatego, że tu nie ma żadnej szafy."
    Konopski "..."
    $ persistent.special_sound = "badum"
    Konopski "{cps=10}NIE{/cps}, osobiście dopilnuję, żeby nie wpuszczać tu żadnego kuriera z szafą w paczce!"
    Konopski "..."
    Konopski "Dobra, nie traćmy więcej czasu i zapomnijmy o sprawie."
    Konopski "Znajcie łaskę pana."
    Konopski angry "Ale niech mi to będzie ostatni raz, zrozumiano...?"
    Konopski "A teraz wracamy do pracy obiboki! Światła, kamera, akcja!"
    $ renpy.pause(2.0, hard=True)
    Konopski "..."
    Konopski ej "Świetnie, straciłem wątek."
    Konopski "..."
    Konopski "Ok, już wiem."
    hide konopski with moveoutright
    pause 1.0
    hide blur with dissolve

label check_blowek2d:
    $ thoughts_monologue(
        Konopski,'''
Ten motłoch, to najprawdopodobniej jakieś dzbany z tiktoka.
A niech mnie, przygotowali jakieś transparenty.
''')
    Konopski '''
Ej, ty!
Dziwna dziewczynko z misiem! 
'''
    scene transparenty5
    Konopski '''
Tak ty.
mogłabyś odwrócić ten transparent w moją stronę, żebym mógł...
'''

label check_blowek2e:
    $image_punch("zniszcz_sztubaka")
    pause 2.0
    $ thoughts_monologue(
        Konopski,'''
Watahańskie dzbany z tiktoka.
Czy ja właśnie odkryłem najgłębszą czeluść dantejskiego piekła?
''')
    $image_punch("zad")
    pause 2.0
    $ thoughts_monologue(
        Konopski,'''
Prostackie grubiaństwo. Niczego innego się po nich nie spodziewałem.
Jaki pan, taki kram.
''')
    $image_punch("wypada")
    pause 2.0
    $image_punch("sor")
    pause 2.0
    $ thoughts_monologue(
        Konopski,'''
...
Muszę przyznać, że ta eskalująca agresja wywołuje we mnie lekką nutkę niepokoju...
Ech, te dzisiejsze fandomy.
{cps=10}ZA MOICH CZASÓW{/cps} wszyscy żyli ze sobą w zgodzie i harmonii. A teraz...? {w=2}Szkoda gadać.
Takim patusom nie pomoże już nawet projekt lady.
No ale nieważne. Co mnie obchodzi zepsucie moralne jakiejś głupiej watahańskiej ferajny.
W gruncie rzeczy są oni przecież nieszkodli {nw}

''')

label check_blowek2f_anim:
    show transparenty_omg with flashbulb
    $renpy.pause(10.0, hard=True)
    jump menu3_uciekaj
        
label czuprynka:
    scene lobby
    $ thoughts_monologue(
        Konopski,'''
Poprawić czuprynkę?
Jak można poprawić czystą perfekcję?
Czemu w ogóle przeszło mi to przez myśl?
Chyba jestem zmęczony...''')
    jump menu3_uciekaj

### MENU 3 + PRÓBA UCIECZKI 

label menu3_uciekaj:
    scene lobby with slow_fade
    $ thoughts_monologue(Konopski, '''
...
No to mamy już odpowiedź na dręczące nas pytanie.
Blowka z całą pewnością nie ma na sali.
{cps=10}...{/cps}
Taaaa...
Skoro sensei uznał, że nie jest to na tyle istotne wydarzenie, żeby zawracać sobie nim głowę...
...to czy nie byłoby to z mojej strony wysoce niestosowne, gdybym sam się na nim pojawił?
Może to zostać odebrane jako próba podważenia słuszności jego decyzji.
''')
    show screen choices3_uciekaj
    pause

label uciekaj:
    scene lobby

    $ thoughts_monologue(
        Konopski,'''
Chwila. Stop.
Nie mogę tak po prostu stąd wyjść...
{cps=8}...{/cps}{w=2}
Gdzie mój płaszcz?
...
Dobra, walić to, spadam jak jest.
Nar...''')
    jump dziewczeta
