# ../../files_list.rpy

label konop_monolog1:
    scene intro with slow_fade
    $ change_style("intro")
    #$ play_music("dangan_new_world")
    $ play_music(SOUNDTRACK["intro"], loop=False)
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
    $ stop_music()
    pause 1.0
    show winny with m
    pause 2.0
    jump konop_monolog2


label konop_monolog2:
    scene lobby with slow_fade
    $change_style("main")
    $ character_monologue(Konopski,'''
A mówiąc o byciu winnym...
Mam nadzieję, że czują się tak wszyscy ci, którzy nie subskrybują jeszcze mojego kanału.
Jeśli należysz do tej grupy i nie chcesz, żeby wyrzuty sumienia zjadały cię od środka, naciśnij tu i teraz gustowny czerwony przycisk.
Nic cię to nie kosztuje, a zawsze możesz zrezygnować.
''')

label subscribe:
    #$dismiss_pause = True
    show blur
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
    #$dismiss_pause = False
    hide blur with ease
    Konopski "Fenomenalnie!"
    Konopski "Od razu wiedziałem, że mam do czynienia z prawdziwym koneserem sztuki!"
    #Konopski "A skoro już mówimy o sztuce: spiesz się, bo zostały ostatnie sztuki mojej najnowszej eksluzywnej kolekcji bluz blovek"

label konop_monolog3:
    $ thoughts_monologue(Konopski,'''
...
Dobra, mam nadzieję, że wszystko się ładnie nagrało.
Wiem, że nie był to jakoś szczególnie porywający monolog, no ale cóż.
Cytując klasyka...
''')
    $ Konopski(text_style("itis", "IT IS WHAT IT IS"))
    $ thoughts_monologue(
        Konopski,'''
Niełatwo jest cierpieć za miliony.
...
Co teraz?'''
)
    $ play_music(SOUNDTRACK["lobby"])
    jump menu1_blowek

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
    scene bg black
    $stop_music()
    jump check_blowek1a

label lexi:
    jump blowek

label grafika:
    jump blowek

label check_blowek1a:
    show bg transparenty0 with fade
    $play_music(SOUNDTRACK["scary"])
    $thoughts_monologue(
        Konopski,'''
...
Co to ma kuźwa być?
Gdzie śmietanka towarzyska youtuba?
Kto doceni te wszystkie wilcze puny, które na dzisiaj przygotowałem?
Patrząc na te plebejskie twarze muśnięte odrobiną chamstwa, cała ta horda to wyznawcy Wardęgi.
''')
    $ persistent.special_sound = music("badum")
    $ Konopski(text_style("thoughts", "Pardon, cała ta {size=+20}WATAHA®{/size}."))
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
    show toko2

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
    scene lobby with Pixellate(3.0,8) 
    pause
    $change_cursor("green")
    $ thoughts_monologue(
        Konopski,'''
...
Nie wydaje mi się, żeby był tam Blowek.
...
Zrobiło się tu strasznie duszno...
''')
    jump menu2_blowek2

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
    show black with fade
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
Pardon, {size=+20}WATAHA®{/size} Wardęgi.
...
No i gdzie ba-dum-tssk?
Tym razem to miało pretendować do kategorii żart.
...
Amatorzy.
''')
label check_blowek2b:
    show transparenty1 with slow_dissolve
    $ persistent.special_sound = music("badum")
    $ thoughts_monologue(
        Konopski,'''
''')
    $Konopski(text_style("thoughts", "Mniejsza o to. Może to nie była nawet {size=+20}WATAHA®{/size}"))
    $ renpy.pause(2.0, hard=True)

    $ thoughts_monologue(
        Konopski,'''
Nie, tu tak totalnie NIE!
Bardziej "nie" niż za pierszym razem!
Czy wy w ogóle wiecie czym jest <ba-dum-tsk>?
''')
    $ persistent.special_sound = music("badum")
    $Konopski(text_style("thoughts", "..."))
    $ renpy.pause(2.0, hard=True)
    scene transparenty2 with dissolve
    $ thoughts_monologue(
        Konopski,'''
Z kim ja pracuję...
Dobra, jeszcze raz.
''')
    $ persistent.special_sound = music("badum")
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
    $ persistent.special_sound = music("badum")
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
    Konopski "Dobra, niech to będzie ostatnie upomnienie."
    $ persistent.special_sound = music("badum")
    Konopski "Ale następnym razem, wylecicie wszyscy na zbity ryj, zanim ktokolwiek zdoła powiedzieć \"szafa\"."
    $ renpy.pause(2.0, hard=True)
    Konopski ej_happy "No! Może jeszcze będą z ciebie ludzie!"
    pause 1.0
    Konopski ej "Świetnie, straciłem wątek."
    Konopski "..."
    Konopski "Ok, wiem już."
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
    pause
    $ thoughts_monologue(
        Konopski,'''
Watahańskie dzbany z tiktoka.
Czy ja właśnie odkryłem najgłębszą czeluść dantejskiego piekła?
''')
    $image_punch("zad")
    pause
    $ thoughts_monologue(
        Konopski,'''
Prostackie grubiaństwo. Niczego innego się po nich nie spodziewałem.
Jaki pan, taki kram.
''')
    $image_punch("wypada")
    pause
    $image_punch("sor")
    pause
    $ thoughts_monologue(
        Konopski,'''
...
Muszę przyznać, że ta eskalująca agresja wywołała we mnie lekką nutkę niepokoju...
Ech, te dzisiejsze fandomy.
Za moich czasów wszyscy żyli ze sobą w zgodzie i harmonii. A teraz? Szkoda gadać.
Dobrze wiedzieć, że koniec końców potrafią jednak zachować zdrowy dystans...
W przeciwnym wypadku, mógłbym zacząć bać się {nw}
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
Gdzie mój płaszcz?
...
Dobra, walić to, spadam jak jest.
Nar...''')
    jump dziewczeta
