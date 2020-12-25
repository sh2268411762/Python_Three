/*
Navicat MySQL Data Transfer

Source Server         : mysql
Source Server Version : 50520
Source Host           : localhost:3306
Source Database       : library

Target Server Type    : MYSQL
Target Server Version : 50520
File Encoding         : 65001

Date: 2020-12-25 20:03:13
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `book`
-- ----------------------------
DROP TABLE IF EXISTS `book`;
CREATE TABLE `book` (
  `type` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `author` varchar(255) DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `amount` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of book
-- ----------------------------
INSERT INTO `book` VALUES ('人文', '西游记', '吴承恩', '81', '100');
INSERT INTO `book` VALUES ('人文', '红楼梦', '曹雪芹', '88', '123');

-- ----------------------------
-- Table structure for `borrow`
-- ----------------------------
DROP TABLE IF EXISTS `borrow`;
CREATE TABLE `borrow` (
  `booknam` varchar(255) DEFAULT NULL,
  `author` varchar(255) DEFAULT NULL,
  `ID` varchar(255) DEFAULT NULL,
  `date` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of borrow
-- ----------------------------

-- ----------------------------
-- Table structure for `user`
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `job` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('孙豪', '123', '1');
INSERT INTO `user` VALUES ('李梓豪', '111', '1');
INSERT INTO `user` VALUES ('王翔', '111', '0');
INSERT INTO `user` VALUES ('刘辰鑫', '111', '0');
INSERT INTO `user` VALUES ('杨致远', '123', '0');
INSERT INTO `user` VALUES ('王二蛋', '1111', '1');
