#image lexio = Placeholder("boy")
init python:
    def judge_scenep(lpose="main"): {show_scene("judge", [(LexioClass, "main")], ["lawkaj"])}
    def pros_scenep(rpose="main", wpose="main"): {show_scene(
        "prosecution",
        [(RevoClass, "main"), (WardegaClass, "main")],
        ["lawkap"]
    )}
    def defense_scenep(kpose="pmain"): {show_scene(
        "defense", 
        [(KonopskiClass, "pmain")],
        ["lawkad"]
    )}
    def witness_scenep(): {show_scene("witness", [GimperClass])}
