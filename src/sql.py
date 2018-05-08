#!/usr/bin/python
# -*- coding: UTF-8 -*-

loginSql = "SELECT c_account, c_password FROM t_user WHERE c_account = %s"

modelSql = "SELECT c_project FROM t_project"

model_d_Sql = "SELECT distribution_name FROM distribution_model ORDER BY id"