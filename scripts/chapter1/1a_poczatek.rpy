# "0_main.rpy"

# ../bin/gui_.rpy
# ../bin/conf.rpy
# ../characters.rpy
# ../screens.rpy

label konop_monolog1:
    scene intro with fade
    $ change_style("intro")
    $ intro_monologue(Konopski, '''
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
    pause
    jump konop_monolog2


label konop_monolog2:
    show winny with m
    pause
    hide winny
    scene lobby with fade
    $change_style("main")
    $ thoughts_monologue(
        Konopski,'''
A mówiąc o byciu winnym {fd}
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
Co teraz?''')
    jump wybor1

label wybor1:
    show blur
    show screen choices1
    pause

label blowek:
    hide screen choices1
    hide blur
    $ thoughts_monologue(
        Konopski,'''
Tak, to dobry pomysł.
Jego obecność niewątpliwie podniosłaby moje morale.
Nie mógłbym przecież okryć się hańbą na oczach mistrza.
''')
    scene bg black
    jump transparenty

label transparenty:
    scene transparenty0
    $thoughts_monologue(
        Konopski,'''
...
Co to ma kuźwa być?
Gdzie śmietanka towarzyska youtuba?
Kto doceni te wszystkie wilcze puny, które na dzisiaj przygotowałem?
Patrząc na te plebejskie twarze muśnięte odrobiną chamstwa, cała ta horda to wyznawcy Wardęgi.
Pardon, cała ta WATAHA®.
<ba-dum-tssk>
To nawet nie był żart.
W każdym razie, czy Wardęga serio nie mógłby urządzać zlotu swoich fanów w innym miejscu niż sala rozpraw...? Na przykład w buszu?
I co ma ze sobą ta baba po lewej?
''')
    show junko1
    pause 1
    show junko2
    $thoughts_monologue(
        Konopski,'''
O wilku mowa, złapała ze mną kontakt wzrokowy.
...
W sumie to całkiem sympatycznie...{nw}
''')
    show junko3 with vpunch
    $ Konopski(text_style("thoughts", "{size=+20}{fast}Co do...?{/size}"))
    show toko1 with zoomout
    show toko2
    
    $ Konopski(text_style("thoughts", "Współczuję tej okuarnicy całym sercem, ja na jej miejscu chyba bym{nw}"))
    show toko3 with vpunch
    $ Konopski(text_style("thougts", "{fast}{size=+50}Ja pierdolę co jest grane{/size}"))
    
    #show transparenty_prolog
label abi:
    hide kokichi
    pause 1.0 
    show blur
    show kokichi at co_to with Dissolve(2, alpha=True)
    pause 1.0
    scene black with vpunch
    pause 3.0
    jump poblowku

label poblowku:
    scene lobby
    $ thoughts_monologue(
        Konopski,'''
...
Nie wydaje mi się, żeby był tam Blowek.
...
Zrobiło się tu strasznie duszno...
''')
    jump wybor2

label wybor2:
    show blur
    show screen choices2
    pause

label blowek2:
    scene lobby
    $ thoughts_monologue(
        Konopski,'''
W żadnym wypadku. Nie odwaliło mi jeszcze do reszty.
Zresztą, myślę że dość dokładnie zlustrowałem tamto pomieszczenie.
Na pewno zauważyłbym promienny uśmiech herubina wśród tych spuszczonych ze smyczy wilków.
...
No dobra, sprawdzę. Ale tak SZYBCIUTKO.
To jest sprawa najwyższej wagi, nie mogę mieć nawet cienia wątpliwości.
No i umówmy się, najgorsze już minęło, teraz będzie z górki.
''')
    scene black with fade
    $ Konopski(text_style("thoughts", "Przynajmniej taką mam nadzieję..."))

label transparenty2:
    scene normal with fade
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
    scene t1 with dissolve
    $ persistent.special_sound = BADUM_SOUND
    $ thoughts_monologue(
        Konopski,'''
''')
    $Konopski(text_style("thoughts", "Mniejsza o to. Może to nie była nawet WATAHA"))
    $ renpy.pause(2.0, hard=True)

    $ thoughts_monologue(
        Konopski,'''
Nie, tu tak totalnie NIE!
Bardziej "nie" niż za pierszym razem!
Czy wy w ogóle wiecie czym jest <ba-dum-tsk>?
''')
    $ persistent.special_sound = BADUM_SOUND
    $Konopski(text_style("thoughts", "..."))
    $ renpy.pause(2.0, hard=True)
    scene t2 with dissolve
    $ thoughts_monologue(
        Konopski,'''
Z kim ja pracuję...
Dobra, jeszcze raz.
''')
    $ persistent.special_sound = BADUM_SOUND
    $Konopski(text_style("thoughts", "To nie byli ludzie z fandomu...{nw}"))
    $ renpy.pause(2.0, hard=True)
    show blur with dissolve
    show konopski ej at right with moveinright
    Konopski "No już bez jaj co się tam dzieje?"
    scene t3
    show blur
    show konopski ej at right
    Konopski "No kuźwa, co za ciul wpuścił tu Chmielarka?"
    Konopski "I od razu ostrzegam, niech mi tu żaden śmieszek nawet nie próbuje wykręcić się wersją 'kurier przyniósł go w paczce'"
    $ persistent.special_sound = BADUM_SOUND
    Konopski "Bo to będzie żart śmieszny jak jego wypłata."
    $ renpy.pause(2.0, hard=True)
    Konopski "Jest jakiś progres."
    scene t4
    show blur
    show konopski ej at right
    Konopski "Dobra, niech to będzie ostatnie upomnienie."
    $ persistent.special_sound = BADUM_SOUND
    Konopski "Ale następnym razem, wylecicie wszyscy na zbity ryj, zanim ktokolwiek zdoła powiedzieć \"szafa\"."
    $ renpy.pause(2.0, hard=True)
    Konopski "No! Może jeszcze będą z ciebie ludzie!"
    pause 1.0
    Konopski "Świetnie, straciłem wątek."
    Konopski "..."
    Konopski "Ok, wiem już."
    hide konopski with moveoutright
    pause 1.0
    hide blur with dissolve
    $ thoughts_monologue(
        Konopski,'''
Ten motłoch, to najprawdopodobniej jakieś dzbany z tiktoka.
A niech mnie, przygotowali jakieś transparenty.
''')
    Konopski '''
Ej, ty!
Dziwna dziewczynko z misiem! 
'''
    scene t5
    Konopski '''
Tak ty.
mogłabyś odwrócić ten transparent w moją stronę, żebym mógł...
'''
    show zniszcz_sztubaka with vpunch
    pause 1.0
    show wypada with vpunch
    pause 1.0
    show zad with vpunch
    pause 1.0
    show sor with vpunch
    pause 1.0
    Konopski "To... eskalowało w zawrotnym tempie..."
    scene black with Dissolve(0.1)
    Konopski "Te dzisiejsze fandomy..."
    Konopski "Dobrze wiedzieć, że koniec końców potrafią jednak zachować zdrowy dystans..."
    Konopski "W przeciwnym wypadku, mógłbym zacząć bać się {nw}"
    show transparenty_omg
    jump wybor3
        
label czuprynka:
    $renpy.hide_screen("choices2")
    hide blur
    scene lobby
    $ thoughts_monologue(
        Konopski,'''
Poprawić czuprynkę?
Jak można poprawić czystą perfekcję?
Czemu w ogóle przeszło mi to przez myśl?
Chyba jestem zmęczony...''')
    jump wybor3

label wybor3:
    scene lobby with dissolve
    $ thoughts_monologue(Konopski, '''
...
No to mamy już odpowiedź na dręczoce nas pytanie.
Blowka z całą pewnością nie ma na sali.
{cps=10}...{/cps}
Taaaa...
Skoro sensei uznał, że nie jest to na tyle istotne wydarzenie, żeby zawracać sobie nim głowę...
...to czy nie byłoby to z mojej strony wysoce niestosowne, gdybym sam się na nim pojawił?
Może to zostać odebrane jako próba podważenia słuszności jego decyzji.
''')
    show blur
    show screen choices3
    pause

label uciekaj:
    $renpy.hide_screen("choices3")
    hide blur
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
