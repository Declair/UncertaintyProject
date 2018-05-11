# -*- coding: utf-8 -*-

import wx

from src import config
from src import sql
import UPShowPanel
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
        node1 = self.m_treeCtrl4.AppendItem(root, "model_test_1")
        node2 = self.m_treeCtrl4.AppendItem(root, "model_test_2")
        for par in record:
             tree[i] = self.m_treeCtrl4.AppendItem(node1, par[0])
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
        select_name = self.m_treeCtrl4.GetItemText(item)
        """不是根节点再进行数据库操作"""
        if self.m_treeCtrl4.RootItem != item:
            db_config = config.datasourse
            try:
                conn = mysql.connector.connect(**db_config)
                cursor = conn.cursor()
                cursor.execute((sql.get_model_Sql + " '" + select_name + "';"))
                record = cursor.fetchall()
            except mysql.connector.Error as e:
                print(e)
            finally:
                cursor.close()
                conn.close()

            """"得到分布类型"""""
            dtype = record[0][3]
            print(dtype)
            """"得到分布参数"""
            par = record[0][2]
            args = par.split(" ")
            for i in args:
                print(i)
            """"参数名称"""""
            # parname = record[0][4]
            # print(parname)
            """""更新UPSP"""
            showPanel = UPShowPanel.ShowPanel()

            # 设置内容
            i = 0
            for row in record:
                showPanel.m_grid4.SetCellValue(i, 0, str(row[0]))
                showPanel.m_grid4.SetCellValue(i, 1, str(row[1]))
                showPanel.m_grid4.SetCellValue(i, 2, str(row[2]))
                showPanel.m_grid4.SetCellValue(i, 3, str(row[3]))
                i = i + 1