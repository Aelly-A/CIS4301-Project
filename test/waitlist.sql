DROP TABLE IF EXISTS Waitlist;
CREATE TABLE Waitlist(isbn VARCHAR(16),account_id VARCHAR(16),place_in_line INT,PRIMARY KEY (isbn, account_id));
INSERT INTO Waitlist (isbn, account_id, place_in_line) VALUES ("0451404580", "0f1ea1817d8d", 1);
INSERT INTO Waitlist (isbn, account_id, place_in_line) VALUES ("0471179809", "eeb58ef303b5", 1);
INSERT INTO Waitlist (isbn, account_id, place_in_line) VALUES ("0471179809", "16705b8d6222", 2);
INSERT INTO Waitlist (isbn, account_id, place_in_line) VALUES ("0451404580", "3ebc25339153", 2);
INSERT INTO Waitlist (isbn, account_id, place_in_line) VALUES ("9812462503", "c6d059404c36", 1);
