CREATE TABLE Costumer ( C_id int NOT NULL AUTO_INCREMENT, c_name varchar(200), 
                        c_lastname varchar(200) NOT NULL, c_phone_number char(11),
                        c_address varchar(255), c_email varchar(200), PRIMARY KEY (C_id));


CREATE TABLE Payment ( pay_id int NOT NULL AUTO_INCREMENT, pay_type varchar(100) NOT NULL,
                       pay_status varchar(100) NOT NULL, PRIMARY KEY (pay_id));



CREATE TABLE Factor (F_id int NOT NULL AUTO_INCREMENT, pay_id int NOT NULL, C_id int NOT NULL,
                     f_data char(8) NOT NULL, f_total_price int NOT NULL, 
                     number_of_pro int NOT NULL, PRIMARY KEY (F_id),
                     FOREIGN KEY (pay_id) REFERENCES Payment(pay_id), 
                     FOREIGN KEY (C_id) REFERENCES Costumer(C_id));


CREATE TABLE Category (Cat_id int NOT NULL AUTO_INCREMENT, cat_manufactor varchar(100) NOT NULL,
                       cat_type varchar(100) NOT NULL, cat_color varchar(100), cat_price int NOT NULL,
                       cat_status varchar(20) NOT NULL, number_of_pro int, PRIMARY KEY (Cat_id));



CREATE TABLE Factor_Pro (Pro_id int NOT NULL AUTO_INCREMENT, F_id int NOT NULL,
                        CONSTRAINT PK_FP PRIMARY KEY (Pro_id, F_id), FOREIGN KEY (Pro_id) REFERENCES Product (Pro_id),
                        FOREIGN KEY (F_id) REFERENCES Factor (F_id));


CREATE TABLE Product (Pro_id int NOT NULL AUTO_INCREMENT, Cat_id int NOT NULL, type_t varchar(100) NOT NULL,
                      brand varchar(100), PRIMARY KEY (Pro_id), FOREIGN KEY (Cat_id) REFERENCES Category (Cat_id));


CREATE TABLE Factor_Pro (Pro_id int NOT NULL AUTO_INCREMENT, F_id int NOT NULL, CONSTRAINT PK_FP PRIMARY KEY (Pro_id, F_id), 
                        FOREIGN KEY (Pro_id) REFERENCES Product (Pro_id), FOREIGN KEY (F_id) REFERENCES Factor (F_id));



SELECT  routine_schema,  
        routine_name,  
        routine_type 
FROM information_schema.routines 
WHERE routine_schema = 'Tools_Store' 
ORDER BY routine_name;  


DELIMITER $$

CREATE PROCEDURE Register_costumer(IN name_ varchar(200),IN lastname_ varchar(200),
                                   IN address_ varchar(255),IN phone_number_ char(11),IN email_ varchar(200))
BEGIN
  INSERT INTO Costumer (c_name,c_lastname,c_phone_number,c_address,c_email) VALUES ( name_,lastname_,phone_number_,address_,email_);
END$$

DELIMITER ;


DELIMITER $$

CREATE PROCEDURE get_costumer()
BEGIN
      SELECT* FROM Costumer;  
END$$

DELIMITER ;