CREATE TABLE `DEALER`(
  d_name varchar(20),
  ph_no varchar(10),
  d_id varchar(20),
  addr varchar(30),
  constraint pkd primary key (d_id)
);

CREATE TABLE `RTO`(
  RTO_branch varchar(20),
  addr varchar(30),
  RTO_number varchar(10),
  constraint pkr primary key(RTO_branch)
);

CREATE TABLE `VEHICLE` (  
  vehicle_type VARCHAR(20),
  vehicle_no varchar(20),
  vehicle_name varchar(20),
  RTO_branch varchar(20),
  d_id varchar(20),
  constraint pkv primary key(vehicle_no),
  constraint fkv foreign key(RTO_branch) references RTO(RTO_branch),
  constraint fkvv foreign key(d_id) references DEALER(d_id)
);

CREATE TABLE `USER`(
  user_id varchar(20),
  pass varchar(20),
  constraint pku primary key(user_id)
);

CREATE TABLE `OWNER`(
aadhaar_no varchar(20),
`name` varchar(20),
vehicle_no varchar(20),
ph_no varchar(10),
addr varchar(30),
user_id varchar(20),
constraint pko primary key(aadhaar_no),
constraint fko foreign key(user_id) references USER(user_id)
);

CREATE TABLE LICENSE(
  aadhaar_no varchar(20),
  validity date,
  license_no varchar(20),
  cov varchar(20),
  constraint pkl primary key(license_no),
  constraint fkl foreign key(aadhaar_no) references OWNER(aadhaar_no)
);

CREATE TABLE LOG(
  id integer AUTO_INCREMENT,
  vehicle_no varchar(20),
  action varchar(20),
  cdate datetime,
  constraint pklog primary key(id) 
);

create table login (
 username varchar(20),
 password varchar(20),
 constraint fkl12 foreign key(username) references user(user_id));

 ALTER TABLE user
ADD PRIMARY KEY (pass);

INSERT INTO `DEALER` VALUES('Sapphire Honda',1634781647,'001','Bangalore');
INSERT INTO `DEALER` VALUES('Ananda Honda',1624732647,'002','Mangalore');
INSERT INTO `DEALER` VALUES('Advith Honda',1614724647,'003','Udupi');
INSERT INTO `DEALER` VALUES('Nexa Suzuki',1674786547,'004','Mysore');

INSERT INTO `RTO` VALUES('JP Nagar','Bangalore',238);
INSERT INTO `RTO` VALUES('MG Road','Mysore',239);
INSERT INTO `RTO` VALUES('Indiranagar','Udupi',240);
INSERT INTO `RTO` VALUES('Koramangala','Bangalore',241);

INSERT INTO `VEHICLE` VALUES('LMV','2022 BH 1854 AA','Baleno','JP Nagar','001');
INSERT INTO `VEHICLE` VALUES('LMV','2022 BH 1122 BB','Venue','MG Road','002');
INSERT INTO `VEHICLE` VALUES('LMV','2022 BH 1923 CC','Nexon','JP Nagar','003');
INSERT INTO `VEHICLE` VALUES('LMV','2022 BH 7568 DD','Safari','Koramangala','004');

INSERT INTO `OWNER` VALUES('567387593653','Dhriti','2022 BH 1764 EE','7684749485','GB Palya','dhriti123');
INSERT INTO `OWNER` VALUES('567387565743','Niharika','2022 BH 9352 FF','7019336485','E City','niharika323');

INSERT INTO `USER` VALUES('dhriti123','helloworld');
INSERT INTO `USER` VALUES('niharika323','youmetheythem');




CREATE TABLE data_log (
   action VARCHAR(255),
   action_time   TIMESTAMP,
   vehicle_no VARCHAR(20)
);


DELIMITER $$
CREATE TRIGGER ai_data AFTER INSERT ON vehicle
FOR EACH ROW
BEGIN
  INSERT INTO data_log (action, action_time, vehicle_no)
  VALUES('insert', NOW(),  NEW.vehicle_no);
END$$
DELIMITER ;

DELIMITER $$
CREATE TRIGGER ad_data AFTER DELETE ON vehicle
FOR EACH ROW
BEGIN
  INSERT INTO data_log (action, action_time, vehicle_no)
  VALUES('delete', NOW(),  OLD.vehicle_no);
END$$
DELIMITER ;

INSERT INTO `VEHICLE` VALUES('LMV','2022 BH 8391 BB','Venue','MG Road','002');
INSERT INTO `VEHICLE` VALUES('LMV','2022 BH 8390 BB','Venue','MG Road','002');


