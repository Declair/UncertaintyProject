/*
Navicat MySQL Data Transfer

Source Server         : Ghost
Source Server Version : 50173
Source Host           : 118.89.198.205:3306
Source Database       : work

Target Server Type    : MYSQL
Target Server Version : 50173
File Encoding         : 65001

Date: 2018-04-01 14:38:05
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for sampling_result
-- ----------------------------
DROP TABLE IF EXISTS `sampling_result`;
CREATE TABLE `sampling_result` (
  `result_id` int(11) NOT NULL,
  `result_value` float(9,3) NOT NULL,
  PRIMARY KEY (`result_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for t_project
-- ----------------------------
DROP TABLE IF EXISTS `t_project`;
CREATE TABLE `t_project` (
  `c_project` varchar(255) CHARACTER SET utf8 DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
