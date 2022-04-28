label lesne_tradycje:
    $ thinking(
        Konopski,'''
...
Co tu nagle tak gwarno?
Szczerze mówiąc, trochę się obawiałem, że mnie zauważyli i wszyscy łypią na mnie spod wilka.
Nie żebym marudził ani nic, to po prostu..{w=1} zastanawiające.
I trochę podejrzane.
...
A co jeśli dokonują właśnie rytualnego mordu na Blowku i zamierzają złożyć go Wardędze w ofierze?
Z tymi leśnymi tradycjami to nigdy nic nie wiadomo...
''')

label lesne_menu:
    menu:
        #set menuset
        "Co robić?"

        "Bądź bohaterem i idź na zwiady" if not option_bohater:
            jump lesne_menu_bohater
        "Weź się w garść, tu chodzi o życie BLOWKA" if option_bohater:
            jump lesne_menu_blowek
        "Wykorzystaj umiejętności nabyte podczas gry w Thiefa i bezszelestnie opuść to pomieszczenie":
            Konopski "łajno"
            jump lesne_menu
        "Wykorzystaj umiejętności nabyte podczas gry w Dishonored i bezszelestnie opuść to pomieszczenie":
            jump lesne_menu_dishonored
        "Przestań się wygłupiać i tracić czas, drzwi są całkiem niedaleko, biegnij jak walcząca o życie antylopa" if not a_lesne:
            jump lesne_menu_ucieczka
        "Stwórz ludzką tarczę ze swoich pracowników i czekaj na ruch przeciwnika" if not option_tarcza:
            jump lesne_menu_tarcza

label lesne_menu_thief:
    Konopski "Blelele"
    jump lesne_menu

label lesne_menu_dishonored:
    $ option_dishonored = 1
    $ Konopski(thinking, "Dishonored? Czy to nie jest jedna z tych gier, w których istnieje możliwość grania babą?")
    $ Konopski(thinking, "Posrało ich od tego równouprawnienia.")
    $ Konopski(thinking, "Przecież każda szanująca się osoba woli grać chłopem.")
    $ Konopski(thinking, "Co będzie następne? Reprezentacja niskorosłych?")
    $ Konopski(thinking, "Nie będę czerpał inspiracji z tego poprawnie politycznego badziewia.")
    $ Konopski(thinking, "...")
    $ Konopski(thinking, "Poza tym, nawet w to nie grałem.")
    jump lesne_menu

label lesne_menu_tarcza:
    $ option_tarcza = 1
    $ Konopski(thinking, "Kuźwa, ale ze mnie skończony debil, jak ja mogłem o tym pomyśleć{w=1} dopiero teraz!")
    $ Konopski(thinking, "Przecież to najprostsze i najbardziej optymalne rozwiązanie!")
    $ Konopski(thinking, "Nie trzeba nawet poświęcić całego zespołu, wystarczą ci z okresu próbnego!")
    Konopski "Proszę wszystkich praktykantów o uwagę!"
    Konopski "Ustawcie się natychmiast w dwuszeregu i..."
    Konopski "Co jest grane?"
    Konopski "Gdzie się wszyscy podziali?"
    Konopski "Ej wy! Niewdzięczne obiboki!"
    Konopski "Macie natychmiast ruszyć swoje leniwe dupska i wrócić..."
    jump zauwazony

label lesne_menu_ucieczka:
    $ Konopski(thinking, "Blelele")
    jump lesne_menu

label lesne_menu_bohater:
    $ option_bohater = 1
    $ Konopski(thinking, "Eeee...")
    $ Konopski(thinking, "No tak...")
    $ Konopski(thinking, "Więc tego...{w=1}")
    $ Konopski(thinking, "Jakie było pytanie?")
    jump lesne_menu
    
label lesne_menu_blowek:
    $ Konopski(thinking("a"))
    jump lesne_menu

label zauwazony:
    $ Konopski(thinking, "...")
    $ Konopski(thinking, "To dziwne, ale...{w=1} mam wrażenie że coś jest nie tak.")
    $ Konopski(thinking, "Czy tu zawsze było tak cicho?")
    $ Konopski(thinking, "...")
    $ Konopski(thinking, "Może...{w=1} najlepiej będzie, jeśli spróbuję sprawdzić, co tam się dzieje...?")
    $ Konopski(thinking, "No dobra, nie ma sensu dalej zwlekać, raz kozie śmierć, haha.{w=1} Ha.")
    $ Konopski(thinking, "...")
    $ Konopski(thinking, "Czy wilki zjadają kozy...?")
    $ Konopski(thinking, "...")
    $ Konopski(thinking, "Teraz albo nigdy.")
    $ Konopski(thinking, "Trzy, dwa, jeden...")
    
    show junko2

label odkrycie_transparentow:
    $ thinking(Konopski, "...zero?")
    $ thinking(Konopski, "Żadnych krwawych ołtarzy? Żadnych kapłanów odzianych w płaszcze z wilczej skóry?")
    $ thinking(Konopski, "Nie ma nawet Kaniowskiego pytającego naczelnego garbarza o techniki jego pracy?")
    $ thinking(Konopski, "Kompletne zero zmian?")
    $ thinking(Konopski, "...")
    $ thinking(Konopski, "No przecież to było oczywiste. Tak tylko się zgrywałem.")
    $ thinking(Konopski, "Nic nie jest tak satysfakcjonujące, jak udane pranki na samym sobie.")
    $ thinking(Konopski, "...")
    $ thinking(Konopski, "No to skoro już wszyscy się pośmialiśmy, możemy już wreszcie wrócić do głównej linii fabularnej.")
    Konopski "Ej, wy tam! Moi robotnicy czy jak was tam zwał..."
    Konopski "Na czym skończyliśmy?"
    Konopski "..."
    Konopski "Na słuch wam padło? Wasz pracodawca zadał pytanie!"
    Konopski "..."
    Konopski "No co tam się dzieje? Nie będę tolerował takich{nw}"
    Konopski "A, no tak. Nikogo nie ma."
    Konopski "Jeśli myślą, że ujdzie im to na sucho i mogą w taki sposób zadrwić sobie ze mnie, to..."
    Konopski "Nie no, chwila, to przecież nie było tak."
    Konopski "To ja wywaliłem ich wszystkich na zbity ryj."
    Konopski "Błagali mnie na kolanach i wili się jak wężę, błagając żebym tego nie robił, ale z bólem serca odmówiłem."
    Konopski "Oczywiście wyłącznie z ich winy. Dawałem im już wcześniej wiele szans na poprawę."
    Konopski "..."
    Konopski "Dokładnie tak to wyglądało. Samo wspomnienie niemal wywołuje łzy."
    Konopski "Ale trzeba iść dalej."

