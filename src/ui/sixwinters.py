# -*- coding: utf-8 -*-

class SixWinters():
    
    def __init__(self):
    
        self.phases  = ["xxMAIDEN", "xxMOTHER", "xxCRONE"]
        self.phase = 0
        self.month = 1
        
    def get_phase(self):
        
        return self.phases[self.phase]
    
    def next_phase(self):
        
        self.phase = self.phase + 1
        
        if self.phase >= 3:
            self.phase = 0
            self.month = self.month + 1
            
    def apply_triggers(self, triggers):
        
        for nt in triggers:
            if nt == self.phases[self.phase]:
                self.next_phase()
                return