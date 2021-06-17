# -*- coding: utf-8 -*-
"""
A simple version of the SixWinters boardgame, handling deck management
to enable rapid prototyping of card decks.

The dice, locations, and character tokens are still handled physically.
"""

import sys

from PyQt5.QtWidgets import QApplication, QGridLayout, QWidget, QListWidget, \
    QPushButton, QLabel
    
from PyQt5.QtGui import QFont

from PyQt5.QtCore import Qt

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    
    w = QWidget()
    w.setWindowTitle('Six Winters')
    
    grid = QGridLayout(w)

    row = 0
    
    title_label = QLabel("Six Winters Player Tableau")
    header_font = title_label.font()
    header_font.setPointSize(12)
    title_label.setFont(header_font)
    
    grid.addWidget(title_label, row, 0, 1, 8, alignment=Qt.AlignCenter)
    
    row = 1  
           
    grid.addWidget(QLabel("Timers"), row, 2)
    
    timer_label = QLabel("0")
    grid.addWidget(timer_label, row, 3)
    
    grid.addWidget(QLabel("Stage"), row, 4)
    
    stage_label = QLabel("0")
    grid.addWidget(stage_label, row, 5)
    
    row = 2
    
    grid.addWidget(QLabel(""), row, 0) 
    
    row = 3
    
    clabel = QLabel("Character Deck")
    header_font.setPointSize(12)
    clabel.setFont(header_font)
    grid.addWidget(clabel, row, 0, 1, 8, alignment=Qt.AlignCenter)
    
    row = 4
    
    c1_label = QLabel("Thea")
    grid.addWidget(c1_label, row, 0)
    
    c2_label = QLabel("Keel")
    grid.addWidget(c2_label, row, 1)     
    
    grid.addWidget(QLabel("Draw"), row, 4) 
    
    cd_draw_label = QLabel("0")
    grid.addWidget(cd_draw_label, row, 5)

    grid.addWidget(QLabel("Discard"), row, 6) 
    
    cd_discard_label = QLabel("0")
    grid.addWidget(cd_discard_label, row, 7)
    
    row = 5    
    
    cdeck_hand = QListWidget()
    grid.addWidget(cdeck_hand, row, 0, 1, 8)
    
    row = 6
    
    cd_draw = QPushButton("Play")
    grid.addWidget(cd_draw, row, 0, 1, 2)
    
    cd_play = QPushButton("Draw")
    grid.addWidget(cd_play, row, 2, 1, 2)
    
    cd_shuffle = QPushButton("Shuffle")
    grid.addWidget(cd_shuffle, row, 4, 1, 2)
    
    cd_fill = QPushButton("Fill")
    grid.addWidget(cd_fill, row, 6, 1, 2)

    row = 7
    
    grid.addWidget(QLabel(""), row, 0) 
    
    row = 8
    
    mlabel = QLabel("Mission Deck")
    mlabel.setFont(header_font)
    grid.addWidget(mlabel, row, 0, 1, 8, alignment=Qt.AlignCenter)
    
    row = 9
    
    loc_label = QLabel("Empire")
    grid.addWidget(loc_label, row, 0)    

    grid.addWidget(QLabel("Top"), row, 2) 
    
    md_top_card_label = QLabel("Fire")
    grid.addWidget(md_top_card_label, row, 3)
    
    grid.addWidget(QLabel("Draw"), row, 4) 
    
    md_draw_label = QLabel("0")
    grid.addWidget(md_draw_label, row, 5)

    grid.addWidget(QLabel("Discard"), row, 6) 
    
    md_discard_label = QLabel("0")
    grid.addWidget(md_discard_label, row, 7)
    
    row = 10
    
    draw_loc_1 = QPushButton("Location 1 Draw")
    grid.addWidget(draw_loc_1, row, 0, 1, 2)

    draw_loc_2 = QPushButton("Location 2 Draw")
    grid.addWidget(draw_loc_2, row, 2, 1, 2)

    draw_loc_3 = QPushButton("Location 3 Draw")
    grid.addWidget(draw_loc_3, row, 4, 1, 2)

    draw_loc_4 = QPushButton("Location 4 Draw")
    grid.addWidget(draw_loc_4, row, 6, 1, 2)
        
    row = 11
    
    loc1 = QListWidget()
    grid.addWidget(loc1, row, 0, 1, 2)

    loc2 = QListWidget()
    grid.addWidget(loc2, row, 2, 1, 2)

    loc3 = QListWidget()
    grid.addWidget(loc3, row, 4, 1, 2)

    loc4 = QListWidget()
    grid.addWidget(loc4, row, 6, 1, 2)
    
    row = 12
    
    grid.addWidget(QLabel("None Selected"), row, 0, 1, 8)     

    row = 13

    lbutton = QPushButton("<--")
    grid.addWidget(lbutton, row, 0)
    
    rbutton = QPushButton("-->")
    grid.addWidget(rbutton, row, 1)
    
    loc_discard = QPushButton("Discard")
    grid.addWidget(loc_discard, row, 2, 1, 2)
    
    loc_burn = QPushButton("Burn")
    grid.addWidget(loc_burn, row, 4, 1, 2)
    
    md_shuffle = QPushButton("Shuffle")
    grid.addWidget(md_shuffle, row, 6, 1, 2)
    
    row = 14
    
    grid.addWidget(QLabel(""), row, 0)     
    
    row = 15
    
    tlabel = QLabel("Triggers")
    tlabel.setFont(header_font)
    grid.addWidget(tlabel, row, 0, 1, 8, alignment=Qt.AlignCenter)   
    
    row = 16
    
    trigger_button = QPushButton("Trigger")
    grid.addWidget(trigger_button, row, 0, 1, 2)
    
    trigger_label_1 = QLabel("None")
    grid.addWidget(trigger_label_1, row, 2, 1, 2)

    trigger_label_2 = QLabel("None")
    grid.addWidget(trigger_label_2, row, 4, 1, 2)

    trigger_label_3 = QLabel("None")
    grid.addWidget(trigger_label_3, row, 6, 1, 2)

    row = 17
    
    grid.addWidget(QLabel(""), row, 0) 
    
    row = 18
    
    alabel = QLabel("Achievements")
    alabel.setFont(header_font)
    grid.addWidget(alabel, row, 0, 1, 8, alignment=Qt.AlignCenter)   
    
    row = 19
    
    a_label_1 = QLabel("None")
    grid.addWidget(a_label_1, row, 0, 1, 3)
    
    a_complete_1 = QPushButton("Complete")
    grid.addWidget(a_complete_1, row, 3)

    a_label_2 = QLabel("None")
    grid.addWidget(a_label_2, row, 4, 1, 3)
    
    a_complete_2 = QPushButton("Complete")
    grid.addWidget(a_complete_2, row, 7)  
        
    w.show()
    sys.exit(app.exec_())