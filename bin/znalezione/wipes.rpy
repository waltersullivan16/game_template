#init python:
#    wipe_path = gpj("gui","transitions", "wipes")
#
#    def make_trans(name, time=1.0, parts=8):
#        return ImageDissolve(gpj(wipe_path, name), time, parts)
#
#    TRANSITIONS = {}
#
#    transitions_list = [f.split('.')[0] for f in os.listdir(wipe_path)]# if os.path.isfile(f)]
#    for t in transitions_list:
#        TRANSITIONS[t] = make_trans(t)
