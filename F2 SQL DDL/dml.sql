insert into Users (username, userpass, nameofUser) values 
	('andrej', 'andrejandrej', 'Andrej Shumkovski'),
	('mersiha', 'mersihamersiha', 'Mersiha Fejzikj'),
	('petko', 'petkopetko', 'Petko Petkovski');

insert into Customer values 
	(7, '070555000', 'Partizanski Odredi 1'),
	(8, '070555001', 'Partizanski Odredi 2'),
	(9, '070555002', 'Partizanski Odredi 3');

insert into Admins values
	(7, 'General Administrator');

insert into Manufacturer (nameOfManufacturer) values 
	('Kingston'),
	('Corsair'),
	('Gigabyte');

insert into Category (nameOfCategory) values 
	('Cooling'),
	('Memory');

insert into Category (nameOfCategory, subCategoryOf) values 
	('Air Cooling', 5), 
	('Water Cooling', 5);

insert into Product (nameOfProduct, adminID, manufacturerID, categoryID) values 
	('H100i Elite Capellix', 7, 5, 10),
	('8GB 3200Mhz', 7, 4, 6),
	('16GB 4600Mhz', 7, 4, 6);

insert into Product_images values 
	(4, 'https://images.unsplash.com/photo-1618764400608-9e7115eede74?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80'), 
	(5, 'https://images.unsplash.com/photo-1618764400608-9e7115eede74?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80'), 
	(6, 'https://images.unsplash.com/photo-1618764400608-9e7115eede74?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80');

insert into Price (productID, startDate, value) values 
	(4, '2022-12-14', 9990),
	(5, '2022-12-14', 2400),
	(6, '2022-12-14', 4990);

insert into Promotion (code, startDate, endDate, percentage, adminID) values 
	('HAPPYNEWYEAR2022', '2022-12-24', '2023-01-01', 25, 7);

insert into Stock_Order (orderDate, adminID, manufacturerID) values 
	('2022-12-13', 7, 5),
	('2022-12-14', 7, 4),
	('2022-12-10', 7, 6);

insert into Shopping_Cart (customerID) values
	(7),
	(8),
	(9);

insert into Delivery_Firm (address, nameOfDeliveryFirm) values 
	('Industriska BB', 'Post Ekspres'),
	('Varhsavska 24', 'Ekstra Post'),
	('Jane Sandanski 14-2', 'DHL');

insert into Delivery_Agent (nameOfDeliveryAgent, deliveryFirmID) values 
	('Marko Markovski', 1), 
	('Petar Petreski', 2),
	('Nikola Nikolovski', 3);

insert into Orders (status, dateOfOrder, totalPrice, adminID, customerID, scID, deliveryFirmID) values 
	('shipped', '2022-12-12 14:27:44', 9990, 7, 8, 2, 1);

insert into Orders (status, dateOfOrder, totalPrice, adminID, customerID, scID) values 
	('confirmed', '2022-12-13 09:34:19', 11390, 7, 9, 3);

insert into Orders (status, dateOfOrder, totalPrice, customerID, scID) values 
	('new', '2022-12-14 07:56:10', 4990, 8, 2);

insert into ProductisInsideSO values 
	(20, 4, 1), 
	(20, 5, 2),
	(20, 6, 3);

insert into orderHasProduct values 
	(1, 1, 4), 
	(1, 2, 4),
	(1, 2, 5),
	(1, 3, 6);

insert into productIsInSC values 
	(1, 4, 2),
	(2, 5, 3);

insert into productIsOfCategory values 
	(10, 4),
	(6, 5),
	(6, 6);