# -*- coding: utf-8 -*-

import wx

from src import config
from src import sql
import mysql.connector

class NavPanel(wx.Panel):
    
    def __init__(self, parent = None):
        
        wx.Panel.__init__(self, parent, wx.ID_ANY, wx.DefaultPosition, 
                          wx.DefaultSize, wx.TAB_TRAVERSAL)

        bSizer = wx.BoxSizer(wx.VERTICAL)

        self.m_treeCtrl4 = wx.TreeCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                       wx.TR_DEFAULT_STYLE)

        db_config = config.datasourse
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            args = ()
            cursor.execute(sql.model_d_Sql, args)
            record = cursor.fetchall()
        except mysql.connector.Error as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

        """左侧树状图"""
        root = self.m_treeCtrl4.AddRoot('选择模型实验')
        tree = [[0] * len(record)] * len(record)
        i = 0
        for model in record:
            tree[i] = self.m_treeCtrl4.AppendItem(root, model[0])
            i += 1
        bSizer.Add(self.m_treeCtrl4, 1, wx.ALL | wx.EXPAND, 5)
        """双击选择模型"""
        self.m_treeCtrl4.Bind(wx.EVT_TREE_ITEM_ACTIVATED,self.SelectModel)

        """"""""""""""""""""
        self.SetSizer(bSizer)
        self.Layout()
        bSizer.Fit(self)

    def SelectModel(self, event):
        item = self.m_treeCtrl4.GetSelection()
        print (self.m_treeCtrl4.GetItemText(item))
        # self.m_treeCtrl4.SetPyData(item, {"Source": "C:\hi.png", "Opacity": item})
        # print self.m_treeCtrl4.GetPyData(item)