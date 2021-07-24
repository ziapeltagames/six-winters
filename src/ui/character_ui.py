# -*- coding: utf-8 -*-
"""
A ui for modeling character deck in Six Winters.

@author: phill
"""

import sys

from PyQt5.QtWidgets import QApplication, QGridLayout, QWidget, QListWidget, \
    QPushButton, QLabel, QListWidgetItem, QDialog, QComboBox
    
from PyQt5.QtGui import QFont

from PyQt5.QtCore import Qt

from character_deck import CharacterDeck

# Retrieve choices for characters, region, and year
class CharacterDialog(QDialog):
    
    def __init__(self, cnames, parent = None):
        
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
        
        self.button_ok = QPushButton("OK")
        grid.addWidget(self.button_ok, row, 9)
        self.button_ok.clicked.connect(self.ok_clicked)
        
    def ok_clicked(self):
        self.close()
        
    def get_inputs(self):
        
        return (self.ccb1.currentText(),
                self.tcb1.currentText(),
                self.tcb2.currentText(),
                self.ccb2.currentText(),
                self.tcb3.currentText(),
                self.tcb4.currentText())

def update_character_card_labels():
    
    cd_draw_label.setText(str(cdeck.draw_size()))
    cd_discard_label.setText(str(cdeck.discard_size()))
    
# Create a widget item, associate the card with it, and add it to list
def draw_character_card():
    
    next_card = cdeck.draw()
    
    if next_card is None:
        cdeck.shuffle()
        next_card = cdeck.draw()
        
    if next_card is None:
        return
    
    qlwi = QListWidgetItem(str(next_card), cdeck_hand)
    qlwi.setData(Qt.UserRole, next_card)
    cdeck_hand.addItem(qlwi)
    
    update_character_card_labels()

# Remove the widget from the list, and add the card to the discard pile
def play_character_card():
    
    if len(cdeck_hand.selectedItems()) < 1:
        return
    
    row = cdeck_hand.currentRow()
    played_card = cdeck_hand.takeItem(row).data(Qt.UserRole)
    cdeck.discard(played_card)
    
    update_character_card_labels()
    
def shuffle_character_cards():
    
    cdeck.shuffle()
    update_character_card_labels()

def fill_character_cards():
    
    while cdeck_hand.count() < 3:    
        draw_character_card()
    
if __name__ == "__main__":
    
    sw_font = QFont('sixwinters')
    sw_font.setPointSize(12)
    app = QApplication(sys.argv)
    
    custom_font = QFont()
    custom_font.setWeight(12);
    app.setFont(custom_font, "QLabel")
    
    cdeck = CharacterDeck('../../csv/character-cards.csv')
    
    cd = CharacterDialog(cdeck.characters())
    cd.setWindowTitle("Load Characters")
    cd.show()
    cd.exec_()
    
    (c1, t1, t2, c2, t3, t4) = cd.get_inputs()
    
    cdeck.filter_characters(c1, 0, 0, c2, 0, 0)
    
    w = QWidget()
    w.setWindowTitle('Six Winters Character Deck ' + c1 + ' ' + c2)
    
    grid = QGridLayout(w)
    
    row = 0
           
    clabel = QLabel('Six Winters Character Deck ' + c1 + ' ' + c2)
    header_font = clabel.font() 
    header_font.setPointSize(12)
    clabel.setFont(header_font)
    grid.addWidget(clabel, row, 0, 1, 6, alignment=Qt.AlignCenter)
    
    row = row + 1 
    
    c1_label = QLabel(c1)
    grid.addWidget(c1_label, row, 0)
    
    c2_label = QLabel(c2)
    grid.addWidget(c2_label, row, 1)     
    
    grid.addWidget(QLabel("Draw"), row, 2) 
    
    cd_draw_label = QLabel(str(cdeck.draw_size()))
    grid.addWidget(cd_draw_label, row, 3)

    grid.addWidget(QLabel("Discard"), row, 4) 
    
    cd_discard_label = QLabel(str(cdeck.discard_size()))
    grid.addWidget(cd_discard_label, row, 5)
    
    row = row + 1 
    
    cdeck_hand = QListWidget()
    grid.addWidget(cdeck_hand, row, 0, 1, 6)
    
    row = row + 1 

    cd_play = QPushButton("Play")
    cd_play.clicked.connect(play_character_card)
    grid.addWidget(cd_play, row, 0, 1, 2)
    
    cd_draw = QPushButton("Draw")
    cd_draw.clicked.connect(draw_character_card)
    grid.addWidget(cd_draw, row, 4)
    
    cd_shuffle = QPushButton("Shuffle")
    cd_shuffle.clicked.connect(shuffle_character_cards)
    grid.addWidget(cd_shuffle, row, 5)
    
    cd_fill = QPushButton("Fill")
    cd_fill.clicked.connect(fill_character_cards)
    grid.addWidget(cd_fill, row, 2, 1, 2)
    
    row = row + 1 
    
    grid.addWidget(QLabel(""), row, 0)
    
    w.show()
    sys.exit(app.exec_())