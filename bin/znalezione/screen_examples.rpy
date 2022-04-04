screen grid_test:
     grid 2 3:
         text "Top-Left"
         text "Top-Right"

         text "Center-Left"
         text "Center-Right"

         text "Bottom-Left"
         text "Bottom-Right"

screen buttons():
    hbox:
        textbutton "Save" action ShowMenu("save")
        textbutton "Prefs" action ShowMenu("preferences")
        textbutton "Skip" action Skip()
        textbutton "Auto" action Preference("auto-forward", "toggle")
