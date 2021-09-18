# -*- coding: utf-8 -*-
"""
A ui for modeling one region in Six Winters.

@author: phill
"""

import sys
import argparse

from PyQt5.QtWidgets import QApplication, QGridLayout, QWidget, QListWidget, \
    QPushButton, QLabel, QListWidgetItem, QDialog, QComboBox
    
from PyQt5.QtGui import QFont

from PyQt5.QtCore import Qt

from mission_deck import MissionDeck
from sixwinters import SixWinters
from location_deck import LocationDeck

# Retrieve choices for characters, region, and year
class MissionDialog(QDialog):
    
    def __init__(self, rnames, parent = None):
        
        super().__init__(parent)
        
        grid = QGridLayout(self)
        
        row = 0
        
        grid.addWidget(QLabel("Region"), row, 0)     
        grid.addWidget(QLabel("Year"), row, 2)

        self.rcb = QComboBox()
        self.rcb.addItems(rnames)        
        grid.addWidget(self.rcb, row, 1)

        self.ycb = QComboBox()
        self.ycb.addItems(["1", "2", "3", "4", "5", "6"])
        grid.addWidget(self.ycb, row, 3)
        
        row = 1
        
        self.button_ok = QPushButton("OK")
        grid.addWidget(self.button_ok, row, 9)
        self.button_ok.clicked.connect(self.ok_clicked)
        
    def ok_clicked(self):
        self.close()
        
    def get_inputs(self):
        
        return (self.rcb.currentText(),
                self.ycb.currentText())
    
def update_mission_card_labels():
    
    md_draw_label.setText(str(mdeck.draw_size()))
    md_discard_label.setText(str(mdeck.discard_size()))
    md_top_card_label.setText(str(mdeck.top_trigger()))
    timer_label.setText(sw.get_phase())
    stage_label.setText(str(sw.month))
    
def location_clicked_0():
    location_clicked(0)

def location_clicked_1():
    location_clicked(1)

def location_clicked_2():
    location_clicked(2)

def location_clicked(loc):

    selected_items = locs[loc].selectedItems()

    if len(selected_items) > 0:
        selected_card = selected_items[0].data(Qt.UserRole)
        selected_effect.setText('Effect: '+selected_card.effect)
        selected_activation.setText('Activation: '+selected_card.activation)
        selected_overcome.setText('Overcome: '+selected_card.overcome)
        selected_bust.setText('Bust: '+selected_card.bust)
        selected_sr.setText(selected_card.skill)
        selected_defense.setText(selected_card.defense)
        selected_difficulty.setText(selected_card.difficulty)
        selected_attack.setText(selected_card.attack)
        selected_name.setText(selected_card.name + '     ' + selected_card.tags)
        
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
    
    triggers = mdeck.draw_triggers(sw.month)
    
    if triggers:
        sw.apply_triggers(triggers)
    else:
        triggers = ["", "", ""]
        sw.next_phase()
    
    trigger_label_1.setText(triggers[0])
    trigger_label_2.setText(triggers[1])
    trigger_label_3.setText(triggers[2])
    
    update_mission_card_labels()
    
if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--region")
    parser.add_argument("--year")
    args = parser.parse_args()
    
    sw = SixWinters()
    sw_font = QFont('sixwinters')
    sw_font.setPointSize(12)
    app = QApplication(sys.argv)
    
    custom_font = QFont()
    custom_font.setWeight(12);
    app.setFont(custom_font, "QLabel")
    
    region = "Empire"
    year = 1
    
    if args.region:
        
        if args.region == 'redbank':
            region = 'Red Bank'
        elif args.region == 'settled':
            region = 'Settled Lands'
        elif args.region == 'empire':
            region = 'Empire'
        
    else:
        
        # Retrieve Mission Info
        md = MissionDialog(["Empire", "Red Bank", "Settled Lands"])
        md.setWindowTitle("Load Mission")
        md.show()
        md.exec_()
        
        (region, year) = md.get_inputs()
    
    # Transfer these to arguments at some point
    stage = 'Starting'
    
    # Load decks    
    mdeck = MissionDeck(region, stage, 
                        '../../csv/mission-cards-obstacles.csv',
                        '../../csv/mission-cards-scenes.csv',
                        '../../csv/mission-cards-threats.csv')
    
    ldeck = LocationDeck('../../csv/location-cards.csv', region, stage)
    
    lcard1 = ldeck.draw()
    lcard2 = ldeck.draw()
    lcard3 = ldeck.draw()
    
    w = QWidget()
    w.setWindowTitle('Six Winters')
    
    grid = QGridLayout(w)

    row = 0
    
    title_label = QLabel("Six Winters " + region + " Tableau")
    header_font = title_label.font()
    header_font.setPointSize(12)
    title_label.setFont(header_font)
    
    grid.addWidget(title_label, row, 0, 1, 6, alignment=Qt.AlignCenter) 
    
    row = row + 1

    grid.addWidget(QLabel("Top"), row, 0) 
    
    md_top_card_label = QLabel()
    md_top_card_label.setFont(sw_font)
    grid.addWidget(md_top_card_label, row, 1)
    
    grid.addWidget(QLabel("Draw"), row, 2) 
    
    md_draw_label = QLabel()
    grid.addWidget(md_draw_label, row, 3)

    grid.addWidget(QLabel("Discard"), row, 4) 
    
    md_discard_label = QLabel()
    grid.addWidget(md_discard_label, row, 5)
    
    row = row + 1 
    
    grid.addWidget(QLabel(""), row, 0) 
    
    row = row + 1 
    
    mlabel = QLabel("Locations")
    mlabel.setFont(header_font)
    grid.addWidget(mlabel, row, 0, 1, 6, alignment=Qt.AlignCenter)
    
    # Location card details
    
    row = row + 1 

    loc_1_name = QLabel(lcard1.name)
    grid.addWidget(loc_1_name, row, 0)
    
    loc_1_tags = QLabel(lcard1.tags)
    grid.addWidget(loc_1_tags, row, 1)

    loc_2_name = QLabel(lcard2.name)
    grid.addWidget(loc_2_name, row, 2)
    
    loc_2_tags = QLabel(lcard2.tags)
    grid.addWidget(loc_2_tags, row, 3)

    loc_3_name = QLabel(lcard3.name)
    grid.addWidget(loc_3_name, row, 4)
    
    loc_3_tags = QLabel(lcard3.tags)
    grid.addWidget(loc_3_tags, row, 5)
    
    row = row + 1
        
    loc_1_sr = QLabel("xxMAIDEN " + lcard1.skill + " " + lcard1.resource)
    loc_1_sr.setFont(sw_font)
    grid.addWidget(loc_1_sr, row, 0)    

    draw_loc_0 = QPushButton("Draw")
    draw_loc_0.clicked.connect(draw_mission_card_0)
    grid.addWidget(draw_loc_0, row, 1)

    loc_2_sr = QLabel("xxMOTHER " + lcard2.skill + " " + lcard2.resource)
    loc_2_sr.setFont(sw_font)
    grid.addWidget(loc_2_sr, row, 2)  
    
    draw_loc_1 = QPushButton("Draw")
    draw_loc_1.clicked.connect(draw_mission_card_1)
    grid.addWidget(draw_loc_1, row, 3)

    loc_3_sr = QLabel("xxCRONE " + lcard3.skill + " " + lcard3.resource)
    loc_3_sr.setFont(sw_font)
    grid.addWidget(loc_3_sr, row, 4)  
    
    draw_loc_2 = QPushButton("Draw")
    draw_loc_2.clicked.connect(draw_mission_card_2)
    grid.addWidget(draw_loc_2, row, 5)    

    row = row + 1 
        
    locs = [QListWidget(), QListWidget(), QListWidget()]
    
    locs[0].itemClicked.connect(location_clicked_0)
    locs[1].itemClicked.connect(location_clicked_1)
    locs[2].itemClicked.connect(location_clicked_2)
    
    grid.addWidget(locs[0], row, 0, 1, 2)
    grid.addWidget(locs[1], row, 2, 1, 2)
    grid.addWidget(locs[2], row, 4, 1, 2)

    row = row + 1

    selected_name = QLabel("")
    grid.addWidget(selected_name, row, 0, 1, 6, alignment=Qt.AlignCenter)
    
    row = row + 1

    selected_effect = QLabel("Effect: ")
    grid.addWidget(selected_effect, row, 0, 1, 3)    
    selected_activation = QLabel("Activation: ")
    grid.addWidget(selected_activation, row, 3, 1, 3)
    
    row = row + 1
    
    selected_overcome = QLabel("Overcome: ")
    grid.addWidget(selected_overcome, row, 0, 1, 3)  
    selected_bust = QLabel("Bust: ")
    grid.addWidget(selected_bust, row, 3, 1, 3)  
    
    row = row + 1
    
    grid.addWidget(QLabel("Skill"), row, 0)
    grid.addWidget(QLabel("Defense"), row, 1, 1, 2)
    grid.addWidget(QLabel("Difficulty"), row, 3)
    grid.addWidget(QLabel("Attack"), row, 4, 1, 2)
    
    row = row + 1 
    
    selected_sr = QLabel("")
    selected_sr.setFont(sw_font)
    grid.addWidget(selected_sr, row, 0)
    
    selected_defense = QLabel("")
    selected_defense.setFont(sw_font)
    grid.addWidget(selected_defense, row, 1, 1, 2)
    
    selected_difficulty = QLabel("")
    selected_difficulty.setFont(sw_font)
    grid.addWidget(selected_difficulty, row, 3)
    
    selected_attack = QLabel("")
    selected_attack.setFont(sw_font)
    grid.addWidget(selected_attack, row, 4, 1, 2)

    row = row + 1 

    lbutton = QPushButton("<--")
    lbutton.clicked.connect(mission_card_left)
    grid.addWidget(lbutton, row, 0)   

    rbutton = QPushButton("-->")
    rbutton.clicked.connect(mission_card_right)
    grid.addWidget(rbutton, row, 1)
    
    loc_discard = QPushButton("Discard")
    loc_discard.clicked.connect(discard_mission_card)    
    grid.addWidget(loc_discard, row, 2)
    
    loc_burn = QPushButton("Burn")
    loc_burn.clicked.connect(burn_mission_card)    
    grid.addWidget(loc_burn, row, 3)
    
    md_shuffle = QPushButton("Shuffle")
    md_shuffle.clicked.connect(shuffle_mission_cards)    
    grid.addWidget(md_shuffle, row, 4, 1, 2)

    row = row + 1 

    grid.addWidget(QLabel(""), row, 0)
    
    row = row + 1 
    
    tlabel = QLabel("Triggers")
    grid.addWidget(tlabel, row, 0)
    
    grid.addWidget(QLabel("Phase"), row, 2)
    
    timer_label = QLabel()
    timer_label.setFont(sw_font)
    grid.addWidget(timer_label, row, 3)
    
    grid.addWidget(QLabel("Stage"), row, 4)
    
    stage_label = QLabel()
    grid.addWidget(stage_label, row, 5)
    
    row = row + 1 
    
    trigger_button = QPushButton("Draw Trigger")
    trigger_button.clicked.connect(draw_triggers)
    grid.addWidget(trigger_button, row, 0, 1, 2)
    
    trigger_label_1 = QLabel()
    trigger_label_1.setFont(sw_font)
    grid.addWidget(trigger_label_1, row, 3)

    trigger_label_2 = QLabel()
    trigger_label_2.setFont(sw_font)
    grid.addWidget(trigger_label_2, row, 4)

    trigger_label_3 = QLabel()
    trigger_label_3.setFont(sw_font)
    grid.addWidget(trigger_label_3, row, 5)   
    
    # Initialize board
    update_mission_card_labels()
        
    w.show()
    sys.exit(app.exec_())