# 22.3 Ausgabe verfügbarer Schriftarten

import matplotlib.font_manager as mfm

fpaths = mfm.findSystemFonts() # such nach alle installierte Schriftarten in dem Rechner bzw. .ttf; .otc ... Dateien 

for i in fpaths:
    f = mfm.get_font(i) # ruft der Schriftartsname ab
    print(f.family_name)

