# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Mon Sep 14 10:34:37 2009

import wx

# begin wxGlade: dependencies
import wx.grid
# end wxGlade

# begin wxGlade: extracode

# end wxGlade

class dataSimulator(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: dataSimulator.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.grid_1 = wx.grid.Grid(self, -1, size=(1, 1))

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: dataSimulator.__set_properties
        self.SetTitle("Configure Simulation")
        self.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.grid_1.CreateGrid(10, 3)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: dataSimulator.__do_layout
        grid_sizer_2 = wx.FlexGridSizer(1, 1, 0, 0)
        grid_sizer_2.Add(self.grid_1, 1, wx.EXPAND, 0)
        self.SetSizer(grid_sizer_2)
        grid_sizer_2.Fit(self)
        self.Layout()
        # end wxGlade

# end of class dataSimulator


