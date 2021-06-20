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
from sixwinters import SixWinters
from location_deck import LocationDeck
    
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
                self.rcb.currentText(),
                self.ycb.currentText())
        
class LocationDialog(QDialog):
    
    def __init__(self, lcards, parent = None):
        super().__init__(parent)        
        grid = QGridLayout(self)
        
        row = 0
        self.l1 = QListWidget()
        self.add_items(self.l1, lcards)
        grid.addWidget(self.l1, row, 0, 1, 2)
        
        row = 1
        self.l2 = QListWidget()
        self.add_items(self.l2, lcards)        
        grid.addWidget(self.l2, row, 0, 1, 2)
        
        row = 2
        self.l3 = QListWidget()
        self.add_items(self.l3, lcards)        
        grid.addWidget(self.l3, row, 0, 1, 2)
        
        row = 3
        self.l4 = QListWidget()
        self.add_items(self.l4, lcards)        
        grid.addWidget(self.l4, row, 0, 1, 2)
        
        row = 4
        self.button_ok = QPushButton("OK")
        grid.addWidget(self.button_ok, row, 1)
        self.button_ok.clicked.connect(self.ok_clicked)        
        
    def add_items(self, lwidget, lcards):        
        for card in lcards.cards:
            qlwi = QListWidgetItem(str(card), lwidget)
            qlwi.setData(Qt.UserRole, card)
            lwidget.addItem(qlwi)
        
    def ok_clicked(self):
        self.close()
        
    def get_locs(self):
        lcard1 = self.l1.takeItem(self.l1.currentRow()).data(Qt.UserRole)
        lcard2 = self.l2.takeItem(self.l2.currentRow()).data(Qt.UserRole)
        lcard3 = self.l3.takeItem(self.l3.currentRow()).data(Qt.UserRole)
        lcard4 = self.l4.takeItem(self.l4.currentRow()).data(Qt.UserRole)
        
        return (lcard1, lcard2, lcard3, lcard4)
        
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
        
def update_mission_card_labels():
    
    md_draw_label.setText(str(mdeck.draw_size()))
    md_discard_label.setText(str(mdeck.discard_size()))
    md_top_card_label.setText(str(mdeck.top_trigger()))
    timer_label.setText(str(sw.timers))
    stage_label.setText(str(sw.stage))

def location_clicked_0():
    location_clicked(0)

def location_clicked_1():
    location_clicked(1)

def location_clicked_2():
    location_clicked(2)
    
def location_clicked_3():
    location_clicked(3)
    
# Only one mission card should be selected at a time
def location_clicked(loc):

    selected_items = locs[loc].selectedItems()

    if len(selected_items) > 0:
        selected_card = selected_items[0].data(Qt.UserRole)
        mission_selected_card_label.setText(str(selected_card))
    
    for i, nl in enumerate(locs): 
        
        if i == loc:
            continue
        
        nl.clearSelection()
    
def draw_mission_card_0():
    draw_mission_card(0)

def draw_mission_card_1():
    draw_mission_card(1)
    
def draw_mission_card_2():
    draw_mission_card(2)
    
def draw_mission_card_3():
    draw_mission_card(3)
    
def draw_mission_card(loc):
    
    next_card = mdeck.draw()
    
    if next_card is None:
        mdeck.shuffle()
        next_card = mdeck.draw()
        
    if next_card is None:
        return
    
    qlwi = QListWidgetItem(str(next_card), locs[loc])
    qlwi.setData(Qt.UserRole, next_card)
    locs[loc].addItem(qlwi)
    
    update_mission_card_labels()
    
def discard_mission_card():
    
    loc, card = get_selected_mission_card()
    
    if card is None:
        return
    
    mdeck.discard(card)
    update_mission_card_labels()
    
def burn_mission_card():
    
    get_selected_mission_card()
    update_mission_card_labels()
    
def mission_card_left():
    
    loc, card = get_selected_mission_card()
    if card is None:
        return
    
    loc = loc-1
    if loc<0:
        loc = 3

    qlwi = QListWidgetItem(str(card), locs[loc])
    qlwi.setData(Qt.UserRole, card)
    locs[loc].addItem(qlwi)    
    
def mission_card_right():
    
    loc, card = get_selected_mission_card()
    if card is None:
        return
    
    loc = loc+1
    if loc>3:
        loc = 0

    qlwi = QListWidgetItem(str(card), locs[loc])
    qlwi.setData(Qt.UserRole, card)
    locs[loc].addItem(qlwi)  
    
def get_selected_mission_card():
    
    for i, loc in enumerate(locs):
    
        if len(loc.selectedItems()) < 1:
            continue
        
        row = loc.currentRow()
        
        selected_card = loc.takeItem(row).data(Qt.UserRole)
        return i, selected_card
    
    return -1, None
    
def shuffle_mission_cards():
    
    mdeck.shuffle()
    update_mission_card_labels()
    
# Probably should be in mission deck?
def draw_triggers():
    
    triggers, timer = mdeck.draw_triggers(sw.stage)
    
    if triggers[0] == "None":
        sw.stage = sw.stage + 1
        sw.timers = 0
        
    if timer:
        sw.timers = sw.timers + 1
        if sw.timers > 2:
            sw.timers = 0
            sw.stage = sw.stage + 1
        
    trigger_label_1.setText(triggers[0])
    trigger_label_2.setText(triggers[1])
    trigger_label_3.setText(triggers[2])
    
    update_mission_card_labels()
    
if __name__ == "__main__":
    
    sw = SixWinters()
    sw_font = QFont('sixwinters')
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
    
    (c1, c2, region, year) = md.get_inputs()
    cdeck.filter_characters(c1, 0, 0, c2, 0 ,0)
    mdeck.filter_regions(region)
    
    # Retrieve Location Info
    ldeck = LocationDeck('../../csv/location-cards.csv', region, year)
    
    ld = LocationDialog(ldeck)
    ld.setWindowTitle("Choose Locations")
    ld.show()
    ld.exec_()
    
    (lcard1, lcard2, lcard3, lcard4) = ld.get_locs()

    # Build Achievement Deck

    # Build Mission Deck
    # Have an alternate constructor for the mission deck
    
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
    
    timer_label = QLabel(str(sw.timers))
    grid.addWidget(timer_label, row, 3)
    
    grid.addWidget(QLabel("Stage"), row, 4)
    
    stage_label = QLabel(str(sw.stage))
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
    cd_shuffle.clicked.connect(shuffle_character_cards)
    grid.addWidget(cd_shuffle, row, 4, 1, 2)
    
    cd_fill = QPushButton("Fill")
    cd_fill.clicked.connect(fill_character_cards)
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
    
    md_top_card_label = QLabel(mdeck.top_trigger())
    md_top_card_label.setFont(sw_font)
    grid.addWidget(md_top_card_label, row, 3)
    
    grid.addWidget(QLabel("Draw"), row, 4) 
    
    md_draw_label = QLabel("0")
    grid.addWidget(md_draw_label, row, 5)

    grid.addWidget(QLabel("Discard"), row, 6) 
    
    md_discard_label = QLabel("0")
    grid.addWidget(md_discard_label, row, 7)
    
    row = 10
    
    draw_loc_0 = QPushButton(lcard1.name + " Draw")
    draw_loc_0.clicked.connect(draw_mission_card_0)
    grid.addWidget(draw_loc_0, row, 0, 1, 2)

    draw_loc_1 = QPushButton(lcard2.name + " Draw")
    draw_loc_1.clicked.connect(draw_mission_card_1)
    grid.addWidget(draw_loc_1, row, 2, 1, 2)

    draw_loc_2 = QPushButton(lcard3.name + " Draw")
    draw_loc_2.clicked.connect(draw_mission_card_2)
    grid.addWidget(draw_loc_2, row, 4, 1, 2)

    draw_loc_3 = QPushButton(lcard4.name + " Draw")
    draw_loc_3.clicked.connect(draw_mission_card_3)    
    grid.addWidget(draw_loc_3, row, 6, 1, 2)
        
    row = 11
    
    locs = [QListWidget(), QListWidget(), QListWidget(), QListWidget()]
    locs[0].itemClicked.connect(location_clicked_0)
    locs[1].itemClicked.connect(location_clicked_1)
    locs[2].itemClicked.connect(location_clicked_2)
    locs[3].itemClicked.connect(location_clicked_3)
            
    grid.addWidget(locs[0], row, 0, 1, 2)

    loc2 = QListWidget()
    grid.addWidget(locs[1], row, 2, 1, 2)

    loc3 = QListWidget()
    grid.addWidget(locs[2], row, 4, 1, 2)

    loc4 = QListWidget()
    grid.addWidget(locs[3], row, 6, 1, 2)
    
    row = 12
    
    mission_selected_card_label = QLabel("None Selected")
    grid.addWidget(mission_selected_card_label, row, 0, 1, 8)     

    row = 13

    lbutton = QPushButton("<--")
    lbutton.clicked.connect(mission_card_left)
    grid.addWidget(lbutton, row, 0)
    
    rbutton = QPushButton("-->")
    rbutton.clicked.connect(mission_card_right)
    grid.addWidget(rbutton, row, 1)
    
    loc_discard = QPushButton("Discard")
    loc_discard.clicked.connect(discard_mission_card)    
    grid.addWidget(loc_discard, row, 2, 1, 2)
    
    loc_burn = QPushButton("Burn")
    loc_burn.clicked.connect(burn_mission_card)    
    grid.addWidget(loc_burn, row, 4, 1, 2)
    
    md_shuffle = QPushButton("Shuffle")
    md_shuffle.clicked.connect(shuffle_mission_cards)    
    grid.addWidget(md_shuffle, row, 6, 1, 2)
    
    row = 14
    
    grid.addWidget(QLabel(""), row, 0)     
    
    row = 15
    
    tlabel = QLabel("Triggers")
    tlabel.setFont(header_font)
    grid.addWidget(tlabel, row, 0, 1, 8, alignment=Qt.AlignCenter)   
    
    row = 16
    
    trigger_button = QPushButton("Trigger")
    trigger_button.clicked.connect(draw_triggers)
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