# -*- coding: utf-8 -*-
"""
Created on Wed May  5 09:56:19 2021

@author: Thomas Dye
"""

from cuflow import cuflow

class CherryMX(cuflow.Part):
    family="S"
    footprint="CherryMX"
    def pth(self,dc,d):
        dc.board.hole(dc.xy,d)
        p = dc.copy()
        p.n_agon(d/2,30)
        p.contact()
        
        p = dc.copy()
        p.part = self.id
        self.pads.append(p)
    
    def place(self,dc):
        # Mounting Hole
        dc.push()
        dc.board.hole(dc.xy,cuflow.inches(0.157))
        dc.pop()
        # Silkscreen Outline
        self.chamfered(dc, w=16, h=16)
        # Switch Pin 1
        dc.goxy(-5.08,3*1.27)
        dc.push()
        self.pth(dc,cuflow.inches(0.059))
        dc.pop()
        # Switch Pin 2
        dc.goxy(5.08,6*1.27)
        dc.push()
        self.pth(dc,cuflow.inches(0.059))
        dc.pop()
        if(self.LED is True):
            dc.goxy(-1.27,-5.08)
            dc.push()
            self.pth(dc,cuflow.inches(0.039))
            dc.pop()
            dc.goxy(1.27,-5.08)
            dc.push()
            self.pth(dc,cuflow.inches(0.039))
            dc.pop()
        if(self.Diode is True):
            dc.goxy(-3*1.27,-5.08)
            dc.push()
            self.pth(dc,cuflow.inches(0.039))
            dc.pop()
            dc.goxy(3*1.27,-5.08)
            dc.push()
            self.pth(dc,cuflow.inches(0.039))
            dc.pop()
        if(self.MountingPins is True):
            dc.goxy(-5.08,0)
            dc.push()
            self.pth(dc,cuflow.inches(0.059))
            dc.pop()
            dc.goxy(5.08,0)
            dc.push()
            self.pth(dc,cuflow.inches(0.059))
            dc.pop()
        
class CherryMX_Plate(CherryMX):
    LED=False
    Diode=False
    MountingPins=False
    
class CherryMX_PlateLED(CherryMX):
    LED=True
    Diode=False
    MountingPins=False
    
class CherryMX_PlateDiode(CherryMX):
    LED=False
    Diode=True
    MountingPins=False
        
class CherryMX_PCB(CherryMX):
    LED=False
    Diode=False
    MountingPins=True
    
class CherryMX_PCBLED(CherryMX):
    LED=True
    Diode=False
    MountingPins=True
    
class CherryMX_PCBDiode(CherryMX):
    LED=False
    Diode=True
    MountingPins=True

if __name__ == "__main__":
    U=19.05
    brd = cuflow.Board((60,40), trace=0.127, space=0.127, via_hole=0.2, via=0.4, via_space=0.254, silk=0.153)
    dc = brd.DC((30,20))
    dc.left(90)
    dc.forward(1.5*U)
    dc.right(90)
    dc.forward(U)
    dc.push()
    s1 = CherryMX_Plate(dc)
    dc.pop()
    brd.outline()
    brd.check()
    