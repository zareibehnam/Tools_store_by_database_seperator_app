
-- ###                                                  CREATE TABLES                                                         #####

CREATE TABLE if not EXISTS Customer ( C_id int NOT NULL AUTO_INCREMENT, c_name varchar(20), 
                        c_lastname varchar(20) NOT NULL, c_address varchar(50),c_phone_number varchar(50)
                        , c_email varchar(20), PRIMARY KEY (C_id));

-- ###########################################################################

CREATE TABLE if not EXISTS Payment ( pay_id int NOT NULL AUTO_INCREMENT, pay_type varchar(20) NOT NULL,
                       pay_status varchar(20) NOT NULL, PRIMARY KEY (pay_id));

-- #################################################################################

CREATE TABLE if NOT EXISTS Factor (F_id int NOT NULL AUTO_INCREMENT, pay_id int NOT NULL, C_id int NOT NULL,
                     f_data char(8) NOT NULL, f_total_price int NOT NULL, 
                     number_of_pro int NOT NULL, PRIMARY KEY (F_id),
                     FOREIGN KEY (pay_id) REFERENCES Payment(pay_id) ON DELETE CASCADE , 
                     FOREIGN KEY (C_id) REFERENCES Customer(C_id) ON DELETE CASCADE );

-- ###################################################################

CREATE TABLE if NOT EXISTS Category (Cat_id int NOT NULL AUTO_INCREMENT, cat_manufactor varchar(50) NOT NULL,
                       cat_type varchar(50) NOT NULL, cat_name varchar(20), cat_price int NOT NULL,
                       cat_status varchar(20) NOT NULL, number_of_pro int, PRIMARY KEY (Cat_id));

-- ######################################################################

CREATE TABLE if NOT EXISTS Factor_Pro(Pro_id int NOT NULL , F_id int NOT NULL,
                        CONSTRAINT PK_FP PRIMARY KEY (Pro_id, F_id), 
                        FOREIGN KEY (Pro_id) REFERENCES Product (Pro_id) ON DELETE CASCADE  ,
                        FOREIGN KEY (F_id) REFERENCES Factor (F_id) ON DELETE CASCADE );

-- ##########################################################################

CREATE TABLE if NOT EXISTS Product (Pro_id int NOT NULL AUTO_INCREMENT, Cat_id int NOT NULL, type_tool varchar(50) NOT NULL,
                      brand varchar(20), PRIMARY KEY (Pro_id), 
                      FOREIGN KEY (Cat_id) REFERENCES Category (Cat_id) ON DELETE CASCADE);

-- #######################################################################

 --  ###                                              SHOW PROCEDURES on Tools_Store                                                      ###

SELECT  routine_schema,  
        routine_name,  
        routine_type 
FROM information_schema.routines 
WHERE routine_schema = 'Tools_store' 
ORDER BY routine_name;  

-- ########################################################
                                --  CREATE PROCEDURE INSERT AND GET ALL INFORMATION                                  #####

DELIMITER $$

CREATE PROCEDURE Register_customer1(IN name_ text,IN lastname_ text,
                                   IN address_ text, IN phone_number_ text, IN email_ text )
BEGIN
  INSERT INTO Customer (c_name,c_lastname,c_address, c_phone_number,c_email) VALUES (name_,lastname_,address_,phone_number_,email_);
END$$

DELIMITER ;

-- ###################################################

DELIMITER $$

CREATE PROCEDURE get_customer()
BEGIN
      SELECT* FROM Customer;  
END$$

DELIMITER ;

-- ###################################################

DELIMITER $$

drop PROCEDURE if EXISTS get_main_information;
CREATE PROCEDURE if not EXISTS get_main_information()
BEGIN
  SELECT c_name,c_lastname,c_phone_number,cat_name,cat_price,f_data,pay_type,pay_status
  FROM Payment  JOIN Factor ON  Payment.pay_id = Factor.pay_id
  JOIN Factor_Pro on Factor_Pro.F_id = Factor.F_id
  JOIN Product on Factor_Pro.Pro_id = Product.Pro_id
  JOIN Category on Product.Pro_id = Category.Cat_id
  JOIN Customer on Customer.C_id = Factor.C_id;
END$$

DELIMITER ;

-- ####################################################

DELIMITER $$

CREATE PROCEDURE Register_product(IN cat_id_ int,IN type_tool_ varchar(20),
                                   IN brand_ varchar(20))
BEGIN
  INSERT INTO Product (Cat_id,type_tool,brand) VALUES (cat_id_,type_tool_,brand_);
END$$

DELIMITER ;

-- #####################################################

DELIMITER $$

CREATE PROCEDURE get_product()
BEGIN
  SELECT * from Product ;
END$$

DELIMITER ;

-- #############################################################

DELIMITER $$

CREATE PROCEDURE Register_category(IN cat_manufactor_ varchar(20),IN cat_type_ varchar(20),
                                   IN cat_name_ varchar(20),IN cat_price_  int ,IN cat_status_ varchar(20),
                                   IN number_of_pro_ int)
BEGIN
  INSERT INTO Category (cat_manufactor,cat_type,cat_name,cat_price,cat_status,number_of_pro)
      VALUES           (cat_manufactor_,cat_type_,cat_name_,cat_price_,cat_status_,number_of_pro_);
END$$

DELIMITER ;

-- ######################################################################

DELIMITER $$

CREATE PROCEDURE get_category()
BEGIN
  SELECT * from Category;
END$$

DELIMITER ;

-- ######################################################################

DELIMITER $$

CREATE PROCEDURE Register_payment(IN pay_type_ varchar(20),IN pay_status_ varchar(20))
BEGIN
  INSERT INTO Payment (pay_type,pay_status)
      VALUES           (pay_type_,pay_status_);
END$$

DELIMITER ;

-- ######################################################################

DELIMITER $$

CREATE PROCEDURE Register_factor(IN pay_id_ int,IN c_id_ int,IN f_data_ char(8),IN f_total_price_ int ,IN number_of_pro_ int)

BEGIN
  INSERT INTO Factor (pay_id,C_id,f_data,f_total_price,number_of_pro)
      VALUES           (pay_id_,c_id_,f_data_,f_total_price_,number_of_pro_);
END$$

DELIMITER ;

-- ####################################################################

DELIMITER $$

CREATE PROCEDURE get_factor()

BEGIN
  SELECT * FROM Factor;
END$$

DELIMITER ;

-- #############################################################################

DELIMITER $$

CREATE PROCEDURE Register_factor_pro(IN Pro_id_ int,IN F_id_ int)

BEGIN
  INSERT INTO Category (Pro_id,F_id)
      VALUES           (Pro_id_,F_id_);
END$$

DELIMITER ;

-- #################################################################

-- ###                                          CREATE PROCEDURES SEARCH                                ###

-- ##########################################################################                                            

DELIMITER $$  
CREATE FUNCTION Get_Customer_id(phone_number_ text)
RETURNS int
DETERMINISTIC
BEGIN 
  DECLARE id int ;
  SET id = 0;   
  SEt id = (SELECT C_id FROM Customer WHERE c_phone_number = phone_number_);
  return id;
END$$  

DELIMITER ;  

-- #########################################################################
-- SELECT FUNCTION name_func(arg);
-- ##########################################################

DELIMITER $$

CREATE PROCEDURE search_customer_by_phone_number(in phone_number_ text)

BEGIN
  SELECT * FROM Customer WHERE c_phone_number=phone_number_;
END$$

DELIMITER ;

-- ##############################################################
DELIMITER $$

CREATE PROCEDURE search_product_by_name(in name_ text)

BEGIN
  SELECT * FROM Category WHERE cat_name=name_;
END$$

DELIMITER ;
-- ####################################################################################
                                      -- delete

DELIMITER $$

CREATE PROCEDURE delete_customer_by_phone_number(in phone_number_ text)

BEGIN
  DELETE FROM Customer WHERE c_phone_number=phone_number_;
END$$

DELIMITER ;
