CREATE TABLE Users
(
  username VARCHAR(50) NOT NULL,
  userpass VARCHAR(50) NOT NULL,
  userID INT NOT NULL,
  fullname VARCHAR(100) NOT NULL,
  PRIMARY KEY (userID)
);

CREATE TABLE Customer
(
  phoneNumber VARCHAR(50) NOT NULL,
  address VARCHAR(100) NOT NULL,
  userID INT NOT NULL,
  PRIMARY KEY (userID),
  FOREIGN KEY (userID) REFERENCES Users(userID)
);

CREATE TABLE Admins
(
  type VARCHAR(50) NOT NULL,
  userID INT NOT NULL,
  PRIMARY KEY (userID),
  FOREIGN KEY (userID) REFERENCES Users(userID),
);

CREATE TABLE Manufacturer
(
  manufacturerID INT NOT NULL,
  name VARCHAR(100) NOT NULL,
  PRIMARY KEY (manufacturerID)
);

CREATE TABLE Category
(
  categoryID INT NOT NULL,
  name VARCHAR(50) NOT NULL,
  subCategoryOf_categoryID INT NOT NULL,
  PRIMARY KEY (categoryID),
  FOREIGN KEY (subCategoryOf_categoryID) REFERENCES Category(categoryID)
);

CREATE TABLE Product
(
  productID INT NOT NULL,
  name VARCHAR(100) NOT NULL,
  adminID INT NOT NULL,
  manufacturerID INT NOT NULL,
  categoryID INT NOT NULL,
  PRIMARY KEY (productID),
  FOREIGN KEY (adminID) REFERENCES Admins(userID),
  FOREIGN KEY (manufacturerID) REFERENCES Manufacturer(manufacturerID),
  FOREIGN KEY (categoryID) REFERENCES Category(categoryID)
);

CREATE TABLE Product_images
(
  images VARCHAR(100) NOT NULL,
  productID INT NOT NULL,
  PRIMARY KEY (images, productID),
  FOREIGN KEY (productID) REFERENCES Product(productID)
);

CREATE TABLE Price
(
  startDate DATE NOT NULL,
  endDate DATE NOT NULL,
  value INT NOT NULL,
  productID INT NOT NULL,
  PRIMARY KEY (startDate, productID),
  FOREIGN KEY (productID) REFERENCES Product(productID)
);

CREATE TABLE Promotion
(
  code VARCHAR NOT NULL,
  startDate DATE NOT NULL,
  endDate DATE NOT NULL,
  percentage INT NOT NULL,
  adminID INT NOT NULL,
  PRIMARY KEY (code),
  FOREIGN KEY (adminID) REFERENCES Admins(UserID)
);

CREATE TABLE Stock_Order
(
  stockOrderID INT NOT NULL,
  date DATE NOT NULL,
  adminID INT NOT NULL,
  manufacturerID INT NOT NULL,
  PRIMARY KEY (stockOrderID),
  FOREIGN KEY (adminID) REFERENCES Admins(userID),
  FOREIGN KEY (manufacturerID) REFERENCES Manufacturer(manufacturerID)
);

CREATE TABLE Shopping_Cart
(
  scID INT NOT NULL,
  customerID INT NOT NULL,
  PRIMARY KEY (scID),
  FOREIGN KEY (customerID) REFERENCES Customer(userID)
);

CREATE TABLE Delivery_Firm
(
  deliveryFirmID INT NOT NULL,
  address VARCHAR(100) NOT NULL,
  name VARCHAR(100) NOT NULL,
  PRIMARY KEY (deliveryFirmID)
);

CREATE TABLE Delivery_Agent
(
  deliveryAgentID INT NOT NULL,
  name VARCHAR(100) NOT NULL,
  deliveryFirmID INT NOT NULL,
  PRIMARY KEY (deliveryAgentID),
  FOREIGN KEY (deliveryFirmID) REFERENCES Delivery_Firm(deliveryFirmID)
);

CREATE TABLE Orders
(
  orderID INT NOT NULL,
  status VARCHAR(50) NOT NULL,
  date DATE NOT NULL,
  totalPrice INT NOT NULL,
  adminID INT NOT NULL,
  customerID INT NOT NULL,
  scID INT NOT NULL,
  deliveryFirmID INT NOT NULL,
  code VARCHAR NOT NULL,
  PRIMARY KEY (orderID),
  FOREIGN KEY (adminID) REFERENCES Admins(userID),
  FOREIGN KEY (customerID) REFERENCES Customer(userID),
  FOREIGN KEY (scID) REFERENCES Shopping_Cart(scID),
  FOREIGN KEY (deliveryFirmID) REFERENCES Delivery_Firm(deliveryFirmID),
  FOREIGN KEY (code) REFERENCES Promotion(code)
);



CREATE TABLE isInside
(
  quantity INT NOT NULL,
  productID INT NOT NULL,
  stockOrderID INT NOT NULL,
  PRIMARY KEY (productID, stockOrderID),
  FOREIGN KEY (productID) REFERENCES Product(productID),
  FOREIGN KEY (stockOrderID) REFERENCES Stock_Order(stockOrderID)
);

CREATE TABLE hasProduct
(
  quantity INT NOT NULL,
  orderID INT NOT NULL,
  productID INT NOT NULL,
  PRIMARY KEY (orderID, productID),
  FOREIGN KEY (orderID) REFERENCES Orders(orderID),
  FOREIGN KEY (productID) REFERENCES Product(productID)
);

CREATE TABLE isIn
(
  quantity INT NOT NULL,
  productID INT NOT NULL,
  scID INT NOT NULL,
  PRIMARY KEY (productID, scID),
  FOREIGN KEY (productID) REFERENCES Product(productID),
  FOREIGN KEY (scID) REFERENCES Shopping_Cart(scID)
);


CREATE TABLE isOf
(
  categoryID INT NOT NULL,
  productID INT NOT NULL,
  PRIMARY KEY (categoryID, productID),
  FOREIGN KEY (categoryID) REFERENCES Category(categoryID),
  FOREIGN KEY (productID) REFERENCES Product(productID)
);