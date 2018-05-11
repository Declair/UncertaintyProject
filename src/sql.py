#!/usr/bin/python
# -*- coding: UTF-8 -*-

loginSql = "SELECT c_account, c_password FROM t_user WHERE c_account = %s"

modelSql = "SELECT c_project FROM t_project"

model_d_Sql = "SELECT arg_name FROM model_arg ORDER BY arg_id"

get_model_Sql = "SELECT m.model_name, a.arg_name, a.dis_type, a.dis_arg FROM model_arg a, model m  WHERE m.model_id = a.model_id AND a.arg_name = "