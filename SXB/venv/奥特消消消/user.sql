/*
Navicat MySQL Data Transfer

Source Server         : mysql
Source Server Version : 50520
Source Host           : localhost:3306
Source Database       : python

Target Server Type    : MYSQL
Target Server Version : 50520
File Encoding         : 65001

Date: 2020-12-25 15:08:07
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `user`
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT 'user',
  `password` varchar(20) DEFAULT ' ',
  `boun` int(11) DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('1', '孙豪', '123', '99999999');
INSERT INTO `user` VALUES ('2', '小王', '111', '11');
INSERT INTO `user` VALUES ('3', '小刘', '222', '22');
INSERT INTO `user` VALUES ('4', '小杨', '333', '33');
INSERT INTO `user` VALUES ('5', '小李', '444', '44');
INSERT INTO `user` VALUES ('6', '欣欣', '555', '0');
INSERT INTO `user` VALUES ('7', '夫赖', '777', '0');
INSERT INTO `user` VALUES ('8', '劲夫', '666', '0');
INSERT INTO `user` VALUES ('9', '大球', ' 888', '0');
INSERT INTO `user` VALUES ('10', '二球', '111', null);
INSERT INTO `user` VALUES ('11', '三球', '000', null);
INSERT INTO `user` VALUES ('14', 'admin', 'admin', '0');
