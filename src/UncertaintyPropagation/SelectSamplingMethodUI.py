# -*- coding: utf-8 -*-

###########################################################################
# Created on 2018.5.10
###########################################################################

import wx
import wx.xrc


class SelectSamplingMethodFrame(wx.Frame):

    def __init__(self, parent, message = 'normal 1.0 0.0'):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"选择抽样方法", pos=wx.DefaultPosition, size=wx.Size(500, 300),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.message = message

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))

        bSizer_main = wx.BoxSizer(wx.VERTICAL)

        ''' 样本大小的panel begins '''
        self.m_panel_size = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel_size.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_SCROLLBAR))

        bSizer_size = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText_size = wx.StaticText(self.m_panel_size, wx.ID_ANY, u"数    量", wx.DefaultPosition,
                                               wx.DefaultSize, 0)
        self.m_staticText_size.Wrap(-1)
        bSizer_size.Add(self.m_staticText_size, 0, wx.ALL, 5)

        self.m_textCtrl_size = wx.TextCtrl(self.m_panel_size, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        bSizer_size.Add(self.m_textCtrl_size, 0, wx.ALL, 5)

        self.m_panel_size.SetSizer(bSizer_size)
        self.m_panel_size.Layout()
        bSizer_size.Fit(self.m_panel_size)
        ''' 样本大小的panel ends '''

        bSizer_main.Add(self.m_panel_size, 1, wx.EXPAND | wx.ALL, 5)

        ''' 选择抽样方法的panel begins '''
        self.m_panel_method = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel_method.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_SCROLLBAR))

        bSizer_method = wx.BoxSizer(wx.VERTICAL)

        self.m_radioBtn_random = wx.RadioButton(self.m_panel_method, wx.ID_ANY, u"随机抽样", wx.DefaultPosition,
                                                wx.DefaultSize, 0)
        bSizer_method.Add(self.m_radioBtn_random, 0, wx.ALL, 5)

        self.m_radioBtn_LHS = wx.RadioButton(self.m_panel_method, wx.ID_ANY, u"拉丁超立方抽样", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        bSizer_method.Add(self.m_radioBtn_LHS, 0, wx.ALL, 5)

        self.m_radioBtn_MC = wx.RadioButton(self.m_panel_method, wx.ID_ANY, u"蒙特卡洛方法", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        bSizer_method.Add(self.m_radioBtn_MC, 0, wx.ALL, 5)

        self.m_panel_method.SetSizer(bSizer_method)
        self.m_panel_method.Layout()
        bSizer_method.Fit(self.m_panel_method)
        ''' 选择抽样方法的panel ends '''

        bSizer_main.Add(self.m_panel_method, 3, wx.EXPAND | wx.ALL, 5)

        ''' 确认和重置按钮的panel begins '''
        self.m_panel_ok = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel_ok.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_SCROLLBAR))

        bSizer_ok = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button_ok = wx.Button(self.m_panel_ok, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer_ok.Add(self.m_button_ok, 0, wx.ALL, 5)

        bSizer_ok.AddSpacer(70)

        self.m_button_reset = wx.Button(self.m_panel_ok, wx.ID_ANY, u"重置", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer_ok.Add(self.m_button_reset, 0, wx.ALL, 5)
        self.m_button_reset.Bind(wx.EVT_BUTTON, self.reset_settings)

        self.m_panel_ok.SetSizer(bSizer_ok)
        self.m_panel_ok.Layout()
        bSizer_ok.Fit(self.m_panel_ok)
        ''' 确认和重置按钮的panel ends '''

        bSizer_main.Add(self.m_panel_ok, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer_main)
        self.Layout()

        self.Centre(wx.BOTH)

        self.set_method_enable()  # 初始设置可用的抽样方法

    def __del__(self):
        pass

    def set_method_enable(self):
        """ 根据样本服从的分布来设置可用的抽样方法 """
        info = self.message.split()
        if info[0] == 'normal':
            self.m_radioBtn_MC.Enable(False)
            self.m_radioBtn_LHS.Enable(False)
        elif info[0] == 'exponential':
            self.m_radioBtn_MC.Enable(False)
            self.m_radioBtn_LHS.Enable(False)
        elif info[0] == 'uniform':
            self.m_radioBtn_LHS.Enable(False)
        elif info[0] == 'other':
            self.m_radioBtn_random.Enable(False)
            self.m_radioBtn_LHS.Enable(False)
        else:
            self.m_radioBtn_random.Enable(False)
            self.m_radioBtn_LHS.Enable(False)
            self.m_radioBtn_MC.Enable(False)

    def reset_settings(self, event):
        """ 重置窗口中以输入的数据 """
        self.m_textCtrl_size.Clear()
        self.m_radioBtn_random.SetValue(False)
        self.m_radioBtn_MC.SetValue(False)
        self.m_radioBtn_LHS.SetValue(False)


if __name__ == '__main__':
    app = wx.App(False)
    frame = SelectSamplingMethodFrame(None)
    frame.Show()
    app.MainLoop()