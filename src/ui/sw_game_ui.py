# -*- coding: utf-8 -*-
"""
A simple version of the SixWinters boardgame, handling deck management
to enable rapid prototyping of card decks.

The dice, locations, and character tokens are still handled physically.
"""

import sys

from PyQt5.QtWidgets import QApplication, QGridLayout, QWidget, QListWidget, \
    QPushButton, QLabel, QDialog, QComboBox, QListWidgetItem
    
from PyQt5.QtGui import QFont

from PyQt5.QtCore import Qt

from character_deck import CharacterDeck
from mission_deck import MissionDeck

# Retrieve choices for characters, region, and year
class MissionDialog(QDialog):
    
    def __init__(self, cnames, rnames, parent = None):
        
        super().__init__(parent)
        
        grid = QGridLayout(self)
        
        scale = ["0", "1", "2", "3", "4", "5", "6"]
        
        row = 0
        grid.addWidget(QLabel("Character"), row, 0)
        grid.addWidget(QLabel("Trait"), row, 2)
        grid.addWidget(QLabel("Trait"), row, 4)
        grid.addWidget(QLabel("Commitment"), row, 6)
        grid.addWidget(QLabel("Discord"), row, 8)
        
        self.ccb1 = QComboBox()
        self.ccb1.addItems(cnames)
        grid.addWidget(self.ccb1, row, 1)

        self.tcb1 = QComboBox()
        grid.addWidget(self.tcb1, row, 3)

        self.tcb2 = QComboBox()
        grid.addWidget(self.tcb2, row, 5)
        
        self.comcb1 = QComboBox()
        self.comcb1.addItems(scale)        
        grid.addWidget(self.comcb1, row, 7)

        self.dcb1 = QComboBox()
        self.dcb1.addItems(scale)          
        grid.addWidget(self.dcb1, row, 9)        
        
        row = 1
        grid.addWidget(QLabel("Character"), row, 0)
        grid.addWidget(QLabel("Trait"), row, 2)
        grid.addWidget(QLabel("Trait"), row, 4)
        grid.addWidget(QLabel("Commitment"), row, 6)
        grid.addWidget(QLabel("Discord"), row, 8)        

        self.ccb2 = QComboBox()
        self.ccb2.addItems(cnames)        
        grid.addWidget(self.ccb2, row, 1)

        self.tcb3 = QComboBox()
        grid.addWidget(self.tcb3, row, 3)

        self.tcb4 = QComboBox()
        grid.addWidget(self.tcb4, row, 5)
        
        self.comcb2 = QComboBox()
        self.comcb2.addItems(scale)          
        grid.addWidget(self.comcb2, row, 7)

        self.dcb2 = QComboBox()
        self.dcb2.addItems(scale)          
        grid.addWidget(self.dcb2, row, 9)       
        
        row = 2
        grid.addWidget(QLabel("Region"), row, 0)     
        grid.addWidget(QLabel("Year"), row, 2)

        self.rcb = QComboBox()
        self.rcb.addItems(rnames)        
        grid.addWidget(self.rcb, row, 1)

        self.ycb = QComboBox()
        self.ycb.addItems(["1", "2", "3", "4", "5", "6"])
        grid.addWidget(self.ycb, row, 3)
        
        row = 3
        
        self.button_ok = QPushButton("OK")
        grid.addWidget(self.button_ok, row, 9)
        self.button_ok.clicked.connect(self.ok_clicked)
        
    def ok_clicked(self):
        self.close()
        
    def get_inputs(self):
        
        return (self.ccb1.currentText(),
                self.ccb2.currentText(),
                self.rcb.currentText())
        
def draw_character_card():
    
    next_card = cdeck.draw()
    
    if next_card is None:
        cdeck.shuffle()
        next_card = cdeck.draw()
        
    if next_card is None:
        return
    
    cdeck_hand.addItem(str(next_card))
    cd_draw_label.setText(str(cdeck.draw_size()))

def play_character_card():
    
    print(cdeck_hand.currentRow())
    
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    
    # Load decks
    cdeck = CharacterDeck('../../csv/character-cards.csv')
    mdeck = MissionDeck('../../csv/mission-cards.csv')    
    
    # Retrieve Mission Info
    md = MissionDialog(cdeck.characters(),
                       mdeck.regions()) 
    md.setWindowTitle("Load Mission")
    md.show()
    md.exec_()
    
    (c1, c2, region) = md.get_inputs()
    cdeck.filter_characters(c1, 0, 0, c2, 0 ,0)
    mdeck.filter_regions(region)
    
    # Retrieve Location Info
    # TBD
    
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
    
    c1_label = QLabel(c1)
    grid.addWidget(c1_label, row, 0)
    
    c2_label = QLabel(c2)
    grid.addWidget(c2_label, row, 1)     
    
    grid.addWidget(QLabel("Draw"), row, 4) 
    
    cd_draw_label = QLabel(str(cdeck.draw_size()))
    grid.addWidget(cd_draw_label, row, 5)

    grid.addWidget(QLabel("Discard"), row, 6) 
    
    cd_discard_label = QLabel(str(cdeck.discard_size()))
    grid.addWidget(cd_discard_label, row, 7)
    
    row = 5    
    
    cdeck_hand = QListWidget()
    grid.addWidget(cdeck_hand, row, 0, 1, 8)
    
    row = 6
    
    cd_play = QPushButton("Play")
    cd_play.clicked.connect(play_character_card)
    grid.addWidget(cd_play, row, 0, 1, 2)
    
    cd_draw = QPushButton("Draw")
    cd_draw.clicked.connect(draw_character_card)
    grid.addWidget(cd_draw, row, 2, 1, 2)
    
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