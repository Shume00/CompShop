create table Users
(
  userID serial primary key,
  username varchar(50) unique,
  userpass varchar(50) not null,
  nameOfUser varchar(100) not null
);

create table Customer
(
  userID integer primary key references Users(userID),
  phoneNumber varchar(50) not null,
  address varchar(100) not null
);

create table Admins
(
  userID integer primary key references Users(userID),
  typeOfAdmin varchar(50) not null
);

create table Manufacturer
(
  manufacturerID serial primary key,
  nameOfManufacturer varchar(100) not null
);

create table Category
(
  categoryID serial primary key,
  nameOfCategory varchar(50) not null,
  subCategoryOf integer references Category(categoryID)
);

create table Product
(
  productID serial primary key,
  nameOfProduct varchar(100) not null,
  adminID integer references Admins(userID) not null,
  manufacturerID integer references Manufacturer(manufacturerID) not null,
  categoryID integer references Category(categoryID) not null
);

create table Product_images
(
  productID integer references Product(productID) not null,
  images varchar(10000) not null,
  constraint pk_Product_images primary key (productID, images)
);

create table Price
(
  productID integer references Product(productID) not null,
  startDate date not null,
  endDate date,
  value integer not null,
  constraint pk_Price primary key(productID, startDate)
);

create table Promotion
(
  code char(16) primary key,
  startDate date not null,
  endDate date,
  percentage integer not null,
  adminID integer references Admins(userID) not null
);

create table Stock_Order
(
  stockOrderID serial primary key,
  orderDate date not null,
  adminID integer references Admins(UserID) not null,
  manufacturerID integer references Manufacturer(manufacturerID) not null
);

create table Shopping_Cart
(
  scID serial primary key,
  customerID integer references Customer(userID) not null
);

create table Delivery_Firm
(
  deliveryFirmID serial primary key,
  address varchar(100),
  nameOfDeliveryFirm varchar(100) not null
);

create table Delivery_Agent
(
  deliveryAgentID serial primary key,
  nameOfDeliveryAgent varchar(100),
  deliveryFirmID integer references Delivery_Firm(deliveryFirmID) not null
);

create table Orders
(
  orderID serial primary key,
  status varchar(50) not null,
  dateOfOrder timestamp not null,
  totalPrice integer not null,
  adminID integer references Admins(UserID),
  customerID integer references Customer(UserID) not null,
  scID integer references Shopping_Cart(scID) not null,
  deliveryFirmID integer references Delivery_Firm(deliveryFirmID),
  code char(18) references Promotion(code)
);

create table productIsInsideSO
(
  quantity integer not null,
  productID integer references Product(productID) not null,
  stockOrderID integer references Stock_Order(stockOrderID) not null,
  constraint pk_productIsInsideSO primary key(productID,stockOrderID)
);

create table orderHasProduct
(
  quantity integer not null,
  orderID integer references Orders(orderID) not null,
  productID integer references Product(productID) not null,
  constraint pk_orderHasProduct primary key(orderID, productID)
);

create table productIsInSC
(
  quantity integer not null,
  productID integer references Product(productID) not null,
  scID integer references Shopping_Cart(scID) not null,
  constraint pk_productIsInSC primary key(productID, scID)
);


create table productIsOfCategory
(
  categoryID integer references Category(categoryID) not null,
  productID integer references Product(productID) not null,
  constraint pk_productIsOfCategory primary key(categoryID, productID)
);