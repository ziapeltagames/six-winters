# -*- coding: utf-8 -*-
"""
Generate the achievement cards csv - kind of a pain in straight text
due to the number of grid locations.

Created on Fri Feb 18 12:00:06 2022

@author: phill
"""

import sys
import csv

columns = ["stage","location","name","g11","g12","g13","g14","g21","g22","g23","g24","g31","g32","g33","g34","g41","g42","g43","g44","f11","f12","f13","f14","f21","f22","f23","f24","f31","f32","f33","f34","f41","f42","f43","f44","reward"]

# card_dict = {}
# card_dict['1'] = {}
# card_dict['2'] = {}
# card_dict['3'] = {}

# with open ("D:\\Dropbox\\Ziapelta Games\\Git\\six-winters\\csv\\achievement-cards.csv", "r") as csvfile:
#     reader_variable = csv.reader(csvfile, delimiter=",")
#     for row in reader_variable:
#         if row == [] or row[0] == 'stage':
#             continue
        
#         stage = row[0]
#         location = row[1]
#         name = row[2]
        
#         card_dict[stage][name] = {}
#         card_dict[stage][name]['location'] = location
        
#         for i in range(3, len(columns)):
#             if row[i] == "":
#                 continue
            
#             card_dict[stage][name][columns[i]] = row[i]
            
#     print(card_dict)
    
card_dict = {
    '1': {
        'Local Investments': {
            'location': 'xxEMPIRE xxTECHNOLOGY', 
            'g11': 'WSxxFSQUAREWS', 
            'g12': 'WWxxFSQUAREWW', 
            'g21': 'WWxxFSQUAREWW', 
            'g22': 'LLxxFSQUARELL', 
            'g23': 'WWxxFSQUAREWW', 
            'g32': 'WWxxFSQUAREWW', 
            'g33': 'YExxFSQUAREYE', 
            'f23': 'xxEMPIRE', 
            'f32': 'xxSETTLED', 
            'reward': 'xxTECHNOLOGY'
            }, 
        'Forging Bonds': {
            'location': 'xxREDBANK xxSTABILITY', 
            'g11': 'WSxxFSQUAREWS', 
            'g12': 'WWxxFSQUAREWW', 
            'g22': 'LLxxFSQUARELL', 
            'g23': 'MMxxFSQUAREMM', 
            'g33': 'WExxFSQUAREWE',
            'f12': 'xxREDBANK',
            'f33': 'xxSETTLED',
            'reward': 'xxSTABILITY'}, 
        'Military Secrets': {
            'location': 'xxEMPIRE xxMILITARY', 
            'g11': 'WSxxFSQUAREWS', 
            'g12': 'MMxxFSQUAREMM',
            'g22': 'WWxxFSQUAREWW',
            'g23': 'MMxxFSQUAREMM',
            'g33': 'WExxFSQUAREWE',
            'f22': 'BTxxSIXBT',
            'f33': 'xxEMPIRE',
            'reward': 'xxMILITARY'},
        'Milk and Honey': {
            'location': 'xxSETTLED xxDIPLOMACY',
            'g11': 'WSxxFSQUAREWS',
            'g12': 'WWxxFSQUAREWW',
            'g13': 'WExxFSQUAREWE',
            'f11': 'xxREDBANK',
            'f12': 'xxFOUR',
            'f13': 'xxSETTLED',
            'reward': 'xxDIPLOMACY'},
        'Guidance from Crescent Hold': {
            'location': 'xxEMPIRE xxESPIONAGE',
            'g11': 'WSxxFSQUAREWS',
            'g12': 'WWxxFSQUAREWW',
            'g21': 'WWxxFSQUAREWW',
            'g22': 'WWxxFSQUAREWW',
            'g23': 'WWxxFSQUAREWW',
            'g31': 'WExxFSQUAREWE',
            'g32': 'WWxxFSQUAREWW',
            'f11': 'xxEMPIRE',
            'f21': 'OTxxONEOT',
            'f22': 'OTxxTWOOT',
            'f31': 'xxSETTLED',
            'reward': 'xxESPIONAGE'},
        'Rites of Winter': {
            'location': 'xxSETTLED xxTECHNOLOGY',
            'g11': 'WSxxFSQUAREWS',
            'g12': 'WWxxFSQUAREWW',
            'g22': 'WWxxFSQUAREWW',
            'g23': 'WWxxFSQUAREWW',
            'g33': 'WExxFSQUAREWE',
            'f12': 'YTxxREDBANKYT',
            'f22': 'BTxxBODYBT',
            'f23': 'BTxxSETTLEDBT',
            'f33': 'xxSIX',
            'reward': 'xxSORCERY'},
        'Marching Orders': {
            'location': 'xxEMPIRE xxMILITARY',
            'g11': 'WSxxFSQUAREWS',
            'g12': 'WExxFSQUAREWE',
            'f11': 'xxFIVE',
            'f12': '',
            'reward': 'xxTACTICS'},
        'Cautious Progress': {
            'location': 'xxEMPIRE xxTECHNOLOGY',
            'g11': 'WSxxFSQUAREWS',
            'g22': 'WWxxFSQUAREWW',
            'g33': 'OExxFSQUAREOE',
            'f22': '<',
            'f33': '<',
            'reward': 'xxTHIEVERY'},
        'Traveling Minstrels': {
            'location': 'xxEMPIRE xxESPIONAGE',
            'g11': 'WSxxFSQUAREWS',
            'g22': 'WWxxFSQUAREWW',
            'g23': 'WWxxFSQUAREWW',
            'g32': 'WWxxFSQUAREWW',
            'g33': 'WExxFSQUAREWE',
            'f22': '=',
            'f23': 'xxSETTLED',
            'f32': 'xxEMPIRE',
            'f33': '=',
            'reward': 'xxDISGUISE'},
        'Boars and Bandits': {
            'location': 'xxREDBANK xxSORCERY',
            'g12': 'WSxxFSQUAREWS',
            'g21': 'WWxxFSQUAREWW',
            'g22': 'WWxxFSQUAREWW',
            'g23': 'WWxxFSQUAREWW',
            'g32': 'WExxFSQUAREWE',
            'f21': 'xxFIVE',
            'f22': 'GTxxREDBANKGT',
            'f23': 'BTxxREDBANKBT',
            'reward': 'xxCOMBAT'},
        'Local Repairs': {
            'location': 'xxREDBANK xxMILITARY',
            'g11': 'WSxxFSQUAREWS',
            'g21': 'WWxxFSQUAREWW',
            'g22': 'WWxxFSQUAREWW',
            'g31': 'WExxFSQUAREWE',
            'f21': 'xxTHREE',
            'f22': 'xxFOUR',
            'f31': 'YTxxTHREEYT',
            'reward': 'xxCOMMAND'},
        'Ranging the Frontier': {
            'location': 'xxSETTLED xxTECHNOLOGY',
            'g11': 'WSxxFSQUAREWS',
            'g21': 'WExxFSQUAREWE',
            'f11': 'xxBODY',
            'f21': 'BTxxREDBANKBT',
            'reward': 'xxSURVIVAL'},
        'Foreign Etiquette': {
            'location': 'xxSETTLED xxDIPLOMACY',
            'g11': 'WSxxFSQUAREWS',
            'g12': 'LExxFSQUARELE',
            'f11': 'xxFOUR',
            'reward': 'xxRAPPORT'},
        'Wards Against the Deathless': {
            'location': 'xxSETTLED xxSORCERY',
            'g11': 'WSxxFSQUAREWS',
            'g12': 'WWxxFSQUAREWW',
            'g21': 'WWxxFSQUAREWW',
            'g22': 'WWxxFSQUAREWW',
            'g23': 'WWxxFSQUAREWW',
            'g32': 'WWxxFSQUAREWW',
            'g33': 'WExxFSQUAREWE',
            'f11': 'xxREDBANK',
            'f12': 'xxBODY',
            'f21': 'xxPSYCHE',
            'f22': 'BTxxSIXBT',
            'f23': 'xxBODY',
            'f32': 'xxPSYCHE',
            'reward': 'xxLORE'},
        'Experience Abroad': {
            'location': 'xxSETTLED xxTECHNOLOGY',
            'g11': 'WSxxFSQUAREWS',
            'g21': 'WExxFSQUAREWE',
            'f21': 'xxEMPIRE',
            'reward': 'xxCOMMITMENT'},
        'Unshakable Faith': {
            'location': 'xxSETTLED xxSORCERY',
            'g11': 'WSxxFSQUAREWS',
            'g21': 'BExxFSQUAREBE',
            'f11': 'xxSIX',
            'reward': 'xxCOMMITMENT'},
        'Quick Wins': {
            'location': 'xxEMPIRE xxTECHNOLOGY',
            'g11': 'WSxxFSQUAREWS',
            'g21': 'WWxxFSQUAREWW',
            'g31': 'WExxFSQUAREWE',
            'f21': '=',
            'f31': '=',
            'reward': 'xxCOMMITMENT'}
        },
    '2': {
        'Metals and Guilds': {
            'location': 'xxSETTLED xxTECHNOLOGY',
            'g11': 'WSxxFSQUAREWS',
            'g12': 'GGxxFSQUAREGG',
            'g21': 'LLxxFSQUARELL',
            'g22': 'WWxxFSQUAREWW',
            'g23': 'GGxxFSQUAREGG',
            'g32': 'LLxxFSQUARELL',
            'g33': 'WWxxFSQUAREWW',
            'g34': 'GGxxFSQUAREGG',
            'g43': 'LLxxFSQUARELL',
            'g44': 'WExxFSQUAREWE',
            'f11': 'xxONE',
            'f22': 'YTxxONEYT',
            'f33': 'YTxxONEYT',
            'f44': 'xxONE',
            'reward': 'xxTECHNOLOGY'},
        'Games Without Frontiers': {
            'location': 'xxEMPIRE xxESPIONAGE',
            'g12': 'WSxxFSQUAREWS',
            'g21': 'WWxxFSQUAREWW',
            'g22': 'WWxxFSQUAREWW',
            'g23': 'WWxxFSQUAREWW',
            'g32': 'WWxxFSQUAREWW',
            'g34': 'WWxxFSQUAREWW',
            'g42': 'WExxFSQUAREWE',
            'g43': 'WWxxFSQUAREWW',
            'f12': 'YTxxTWOYT',
            'f21': 'MTxxEMPIREMT',
            'f22': 'xxPSYCHE',
            'f23': 'GTxxEMPIREGT',
            'f32': 'OTxxEMPIREOT',
            'f42': 'xxTWO',
            'reward': 'xxESPIONAGE'},
        'Priming the Mana Forge': {
            'location': 'xxSETTLED xxSORCERY',
            'g11': 'WSxxFSQUAREWS',
            'g21': 'WWxxFSQUAREWW',
            'g22': 'WWxxFSQUAREWW',
            'g31': 'WWxxFSQUAREWW',
            'g33': 'WWxxFSQUAREWW',
            'g41': 'WExxFSQUAREWE',
            'g42': 'WWxxFSQUAREWW',
            'f11': 'BTxxREDBANKBT',
            'f21': 'xxPSYCHE',
            'f31': 'OTxxPSYCHEOT',
            'f33': 'BTxxSETTLEDBT',
            'reward': 'xxSORCERY'},
        'Talk of War': {
            'location': 'xxEMPIRE xxMILITARY',
            'g11': 'WSxxFSQUAREWS',
            'g12': 'WWxxFSQUAREWW',
            'g21': 'WWxxFSQUAREWW',
            'g23': 'WWxxFSQUAREWW',
            'g24': 'WExxFSQUAREWE',
            'g32': 'WWxxFSQUAREWW',
            'f11': 'GTxxTHREEGT',
            'f12': 'xxFOUR',
            'f21': 'xxTHREE',
            'f23': 'xxFOUR',
            'f24': 'MTxxFOURMT',
            'f32': 'xxTHREE',
            'reward': 'xxDIPLOMACY'},
        'On Two Fronts': {
            'location': 'xxSETTLED xxDIPLOMACY',
            'g11': 'WSxxFSQUAREWS',
            'g22': 'WWxxFSQUAREWW',
            'g23': 'WWxxFSQUAREWW',
            'g33': 'OOxxFSQUAREOO',
            'g34': 'WWxxFSQUAREWW',
            'g44': 'WExxFSQUAREWE',
            'f11': 'xxREDBANK',
            'f22': 'xxFIVE',
            'f44': 'xxEMPIRE',
            'reward': 'xxMILITARY'},
        'Bread and Circuses': {
            'location': 'xxREDBANK xxSORCERY',
            'g11': 'WSxxFSQUAREWS',
            'g12': 'WWxxFSQUAREWW',
            'g13': 'WWxxFSQUAREWW',
            'g14': 'LLxxFSQUARELL',
            'g24': 'WWxxFSQUAREWW',
            'g34': 'WExxFSQUAREWE',
            'f11': 'xxREDBANK',
            'f12': '>',
            'f13': '>',
            'f24': '>',
            'f34': '>',
            'reward': 'xxSTABILITY'},
        'Elegant Accoutrements': {
            'location': 'xxEMPIRE xxMILITARY',
            'g11': 'YSxxFSQUAREYS',
            'g21': 'WWxxFSQUAREWW',
            'g31': 'LExxFSQUARELE',
            'f21': 'xxFOUR',
            'reward': 'xxDISGUISE'},
        'Further Sacrifices': {
            'location': 'xxEMPIRE xxESPIONAGE',
            'g12': 'WSxxFSQUAREWS',
            'g22': 'MMxxFSQUAREMM',
            'g23': 'WWxxFSQUAREWW',
            'g32': 'OOxxFSQUAREOO',
            'g34': 'WWxxFSQUAREWW',
            'g42': 'WExxFSQUAREWE',
            'g43': 'WWxxFSQUAREWW',
            'f12': 'xxONE',
            'f22': 'xxPSYCHE',
            'f23': '>',
            'f34': '>',
            'f42': 'xxONE',
            'f43': '>',
            'reward': 'xxTHIEVERY'},
        'Along the Wall': {
            'location': 'xxEMPIRE xxTECHNOLOGY',
            'g11': 'WSxxFSQUAREWS',
            'g12': 'WWxxFSQUAREWW',
            'g22': 'WWxxFSQUAREWW',
            'g23': 'WWxxFSQUAREWW',
            'g33': 'WExxFSQUAREWE',
            'f11': 'xxREDBANK',
            'f12': '>',
            'f22': 'GTxxEMPIREGT',
            'f23': '>',
            'f33': '>',
            'reward': 'xxCOMBAT'},
        'Hard Choices': {
            'location': 'xxREDBANK xxSTABILITY',
            'g11': 'KSxxONEKS',
            'g12': 'xxTWO',
            'g13': 'xxONE',
            'g22': 'YYxxFIVEYY',
            'g24': 'xxTWO',
            'g33': 'YYxxFIVEYY',
            'g34': 'xxONE',
            'g44': 'KExxTWOKE',
            'reward': 'xxCOMMAND'},
        'Ranging the Frontier': {
            'location': 'xxREDBANK xxMILITARY',
            'g11': 'WSxxFSQUAREWS',
            'g12': 'WWxxFSQUAREWW',
            'g13': 'WWxxFSQUAREWW',
            'g22': 'GGxxFOURGG',
            'g24': 'WWxxFSQUAREWW',
            'g33': 'GGxxSIXGG',
            'g34': 'WExxFSQUAREWE',
            'f11': 'E',
            'f12': 'E',
            'f13': 'E',
            'f24': 'E',
            'f34': 'E',
            'reward': 'xxSURVIVAL'},
        'Local Etiquette': {
            'location': 'xxSETTLED xxTECHNOLOGY',
            'g11': 'YSxxSIXYS',
            'g22': 'LExxSIXLE',
            'reward': 'xxRAPPORT'},
        'Allies Abroad': {
            'location': 'xxSETTLED xxDIPLOMACY',
            'g11': 'WSxxFSQUAREWS',
            'g12': 'WWxxFSQUAREWW',
            'g13': 'WWxxFSQUAREWW',
            'g22': 'GTxxSETTLEDGT',
            'g23': 'GTxxSETTLEDGT',
            'g24': 'WExxFSQUAREWE',
            'f12': 'E',
            'f13': 'E',
            'f24': 'E',
            'reward': 'xxTACTICS'},
        'Wards Against the Deathless': {
            'location': 'xxSETTLED xxDIPLOMACY',
            'g11': 'KSxxREDBANKKS',
            'g12': 'xxBODY',
            'g21': 'xxPSYCHE',
            'g22': 'BBxxSIXBB',
            'g23': 'xxBODY',
            'g32': 'xxPSYCHE',
            'g33': 'KExxREDBANKKE',
            'reward': 'xxLORE'},
        'Expert Training': {
            'location': 'xxREDBANK xxMILITARY',
            'g11': 'LSxxFSQUARELS',
            'g21': 'xxTWO',
            'g22': 'xxTHREE',
            'g23': 'xxFOUR',
            'g32': 'xxTWO',
            'g33': 'WExxFSQUAREWE',
            'reward': 'xxCOMMITMENT'},
        'Quick Wins': {
            'location': 'xxSETTLED xxTECHNOLOGY',
            'g11': 'KSxxTWOKS',
            'g21': 'WWxxFSQUAREWW',
            'g22': 'WWxxFSQUAREWW',
            'g32': 'WWxxFSQUAREWW',
            'g33': 'WExxFSQUAREWE',
            'f21': '<',
            'f22': '>',
            'f32': '<',
            'f33': '>',
            'reward': 'xxCOMMITMENT'}
            },
    '3': {
        'Right Tool for the Job': {
            'location': 'xxEMPIRE xxMILITARY',
            'g11': 'KSxxONEKS',
            'g12': 'xxTWO',
            'g13': 'xxTHREE',
            'g24': 'xxFOUR',
            'g34': 'xxFIVE',
            'g44': 'KExxSIXKE',
            'reward': 'xxTECHNOLOGY'},
        'Imperial Safe': {
            'location': 'xxEMPIRE xxMILITARY',
            'g11': 'KSxxEMPIREKS',
            'g12': 'MMxxEMPIREMM',
            'g21': 'OOxxEMPIREOO',
            'g22': 'OOxxSIXOO',
            'g23': 'MMxxEMPIREMM',
            'g32': 'OOxxEMPIREOO',
            'g33': 'GGxxFSQUAREGG',
            'g34': 'xxTHREE',
            'g43': 'xxFOUR',
            'g44': 'KExxEMPIREKE',
            'reward': 'xxESPIONAGE'},
        'At What Price?': {
            'location': 'xxEMPIRE xxMILITARY',
            'g11': 'YSxxFSQUAREYS',
            'g12': 'xxBODY',
            'g22': 'LLxxSIXLL',
            'g23': 'xxPSYCHE',
            'g33': 'MMxxSIXMM',
            'g34': 'xxBODY',
            'g42': 'YExxFSQUAREYE',
            'g43': 'xxPSYCHE',
            'reward': 'xxSORCERY'},
        'Fog of War': {
            'location': 'xxEMPIRE xxMILITARY',
            'g11': 'KSxxEMPIREKS',
            'g12': 'WWxxFSQUAREWW',
            'g22': 'GGxxFSQUAREGG',
            'g23': 'MMxxFSQUAREMM',
            'g33': 'GGxxFSQUAREGG',
            'g34': 'MMxxFSQUAREMM',
            'g44': 'KExxSETTLEDKE',
            'reward': 'xxDIPLOMACY'},
        'Multiple Fronts': {
            'location': 'xxEMPIRE xxMILITARY',
            'g11': 'KSxxEMPIREKS',
            'g22': 'xxREDBANK',
            'g33': 'xxSETTLED',
            'g44': 'KExxEMPIREKE',
            'reward': 'xxMILITARY'},
        'Roads and Boats': {
            'location': 'xxEMPIRE xxMILITARY',
            'g12': 'KSxxREDBANKKS',
            'g21': 'xxREDBANK',
            'g22': 'LLxxTHREELL',
            'g23': 'LLxxFOURLL',
            'g32': 'OOxxFSQUAREOO',
            'g33': 'KExxREDBANKKE',
            'reward': 'xxSTABILITY'},
        'Safehouses': {
            'location': 'xxEMPIRE xxMILITARY',
            'g11': 'KSxxFIVEKS',
            'g12': 'xxEMPIRE',
            'g21': 'xxEMPIRE',
            'g22': 'WWxxFSQUAREWW',
            'g23': 'OOxxTHREEOO',
            'g32': 'OOxxFOUROO',
            'g33': 'WWxxFSQUAREWW',
            'g34': 'OOxxTWOOO',
            'g43': 'OOxxTHREEOO',
            'g44': 'WExxFSQUAREWE',
            'f22': '=',
            'f33': '=',
            'f44': '=',
            'reward': 'xxDISGUISE'},
        'The Resistance': {
            'location': 'xxEMPIRE xxMILITARY',
            'g11': 'WSxxFSQUAREWS',
            'g12': 'WWxxFSQUAREWW',
            'g13': 'WWxxFSQUAREWW',
            'g14': 'MMxxEMPIREMM',
            'g21': 'WWxxFSQUAREWW',
            'g24': 'WWxxFSQUAREWW',
            'g31': 'WWxxFSQUAREWW',
            'g34': 'WWxxFSQUAREWW',
            'g41': 'OOxxEMPIREOO',
            'g42': 'WWxxFSQUAREWW',
            'g43': 'WWxxFSQUAREWW',
            'g44': 'KExxEMPIREKE',
            'f12': '<',
            'f13': '<',
            'f21': '<',
            'f24': '<',
            'f31': '<',
            'f34': '<',
            'f42': '<',
            'f43': '<',
            'reward': 'xxTHIEVERY'},
        'Swordcraft': {
            'location': 'xxEMPIRE xxMILITARY',
            'g11': 'KSxxTWOKS',
            'g21': 'OOxxONEOO',
            'g22': 'WWxxFSQUAREWW',
            'g23': 'GGxxTHREEGG',
            'g32': 'GGxxTWOGG',
            'g33': 'WWxxFSQUAREWW',
            'g34': 'GGxxFOURGG',
            'g43': 'OOxxFOUROO',
            'g44': 'WExxFSQUAREWE',
            'f22': '>',
            'f33': '>',
            'f44': '>',
            'reward': 'xxCOMBAT'},
        'Mustering Aid': {
            'location': 'xxEMPIRE xxMILITARY',
            'g11': 'WSxxFSQUAREWS',
            'g12': 'YYxxONEYY',
            'g21': 'YYxxSETTLEDYY',
            'g22': 'WWxxFSQUAREWW',
            'g23': 'LLxxTHREELL',
            'g32': 'LLxxTWOLL',
            'g33': 'WWxxFSQUAREWW',
            'g34': 'LLxxSETTLEDLL',
            'g43': 'YYxxFOURYY',
            'g44': 'WExxFSQUAREWE',
            'f22': '>',
            'f33': '>',
            'f44': '>',
            'reward': 'xxCOMMAND'},
        'Traveling Gear': {
            'location': 'xxEMPIRE xxMILITARY',
            'g11': 'OSxxTWOOS',
            'g12': 'xxREDBANK',
            'g22': 'OOxxTHREEOO',
            'g23': 'xxREDBANK',
            'g32': 'KExxSETTLEDKE',
            'reward': 'xxSURVIVAL'},
        'Taverns and Tapestries': {
            'location': 'xxEMPIRE xxMILITARY',
            'g11': 'WSxxFSQUAREWS',
            'g12': 'WWxxFSQUAREWW',
            'g13': 'WWxxFSQUAREWW',
            'g14': 'YYxxFSQUAREYY',
            'g24': 'WWxxFSQUAREWW',
            'g34': 'WWxxFSQUAREWW',
            'g43': 'WExxFSQUAREWE',
            'g44': 'YYxxFSQUAREYY',
            'f12': '<',
            'f13': '<',
            'f24': '<',
            'f34': '<',
            'f43': '<',
            'reward': 'xxRAPPORT'},
        'Mutual Sacrifice': {
            'location': 'xxEMPIRE xxMILITARY',
            'g11': 'WSxxFSQUAREWS',
            'g12': 'GGxxFSQUAREGG',
            'g13': 'GGxxFSQUAREGG',
            'g22': 'xxBODY',
            'g24': 'YYxxFSQUAREYY',
            'g33': 'xxBODY',
            'g34': 'WExxFSQUAREWE',
            'reward': 'xxTACTICS'},
        'Hedge Magic': {
            'location': 'xxEMPIRE xxMILITARY',
            'g11': 'BSxxFSQUAREBS',
            'g12': 'WWxxFSQUAREWW',
            'g13': 'WWxxFSQUAREWW',
            'g14': 'BBxxFSQUAREBB',
            'g24': 'WWxxFSQUAREWW',
            'g34': 'WWxxFSQUAREWW',
            'g43': 'WExxFSQUAREWE',
            'g44': 'BBxxFSQUAREBB',
            'f12': '=',
            'f13': '=',
            'f24': '=',
            'f34': '=',
            'f43': '=',
            'reward': 'xxLORE'},
        'Wisdom on the Road': {
            'location': 'xxREDBANK xxMILITARY',
            'g11': 'KSxxREDBANKKS',
            'g21': 'xxEMPIRE',
            'g22': 'OTxxSETTLEDOT',
            'g32': 'OTxxEMPIREOT',
            'g33': 'KExxSETTLEDKE',
            'reward': 'xxCOMMITMENT'}
            }
        }

original_stdout = sys.stdout

with open ("D:\\Dropbox\\Ziapelta Games\\Git\\six-winters\\csv\\achievement-cards.csv", "w") as csvfile:

    sys.stdout = csvfile

    # Print csv header
    for i in range(len(columns) -1):
        print(columns[i], ',', end='', sep='')
    print(columns[-1])
    
    print()
    
    # Print rows
    for next_stage in card_dict.keys():
        for next_name in card_dict[next_stage].keys():
            for next_col in columns:
                if next_col == 'stage':
                    print('"', next_stage, '",', end='', sep='')
                elif next_col =='name':
                    print('"', next_name, '",', end='', sep='')
                else:
                    if next_col in card_dict[next_stage][next_name].keys():
                        print('"', card_dict[next_stage][next_name][next_col], '",', end='', sep='')
                    else:
                        print('""', ',', end='', sep='')
            print()
        print()
        
    sys.stdout = original_stdout