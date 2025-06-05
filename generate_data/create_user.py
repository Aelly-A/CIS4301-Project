from random import randint
from uuid import uuid4

first_names = ["John", "George", "Paul", "Richard", "Matthew", "Brant", "Ian", "Camillo", "Evan", "Stephen",
               "Steven", "Tony", "Bruce", "Charles", "William", "Joshua", "Garrett", "Shawn", "James", "Kenneth",
               "Benjamin", 'Aaron', "Leonardo", "Myles", "Calvin", "Cole", "Shane", "Romeo", "Cody", "Toby",
               "Francisco", "Fernando", "Desmond", "Rocky", "Xander", "Pablo", "Juan", "Yusuf", "Tripp", "Enrique",
               "Raymond", "Roberto", "Samir", "Keegan", "Jordan", "Kendrick", "Corey", "Quincy", "Alberto", "Alvin",
               "Simon", "Theodore", "Kenji", "Jackie", "Trenton", "Akash", "Andrew", "Anuj", "Arjun", "Arnav", "Rishab",
               "Rohan", "Rushi", "Shreya", "Iman", "Jay", "Irene", "Maureen", "Jessica", "Cynthia", "Jane", "Linda",
               "Patricia", "Barbara", "Julianna", "Anna", "Michelle", "Molly", "Jude", "Carol", "Joan", "Loretta",
               "Elizabeth", "Mary", "Nancy", "Lilly", "Rita", "Sadie", "Valerie", "Vera", "Julia", "Jennifer",
               "Eleanor", "Emma", "Charlotte", "Mia", "Sydney", "Ava", "Sofia", "Abigail", "Sydney", "Chloe", "Emily",
               "Scarlett", "Zoe", "Ella", "Lucy", "Grace", "Ruby", "Alice", "Natalie", "Aubrey", "Juliette", "Summer",
               "Karla", "Alexandra", "Elaina", "Lilith", "Kamila", "Kamala", "Kendall", "Vanessa", "Candace", "Mya",
               "Melissa"]

last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
              "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "White",
              "Lee", "Harris", "Clark", "Lewis", "Walker", "Hall", "Allen", "Young", "King", "Wright", "Scott",
              "Torres", "Nguyen", "Hill", "Green", "Adams", "Baker", "Nelson", "Carter", "Mitchell", "Perez", "Roberts",
              "Turner", "Phillips", "Campbell", "Parker", "Evans", "Edwards", "Collins", "Stewart", "Sanchez", "Morris",
              "Rogers", "Reed", "Cook", "Morgan", "Bell", "Murphy", "Bailey", "Rivera", "Cooper", "Richardson", "Cox",
              "Howard", "Ward", "Flores", "Kim", "Ramirez", "James", "Watson", "Brooks", "Kelly", "Sanders", "Price",
              "Bennett", "Wood", "Barnes", "Ross", "Henderson", "Coleman", "Jenkins", "Perry", "Powell", "Long",
              "Patterson", "Hughes", "Flores", "Washington", "Butler", "Simmons", "Foster", "Gonzales", "Bryant",
              "Alexander", "Russell", "Griffin", "Diaz", "Hayes", "Myers", "Ford"]
addresses = [
    "7307 SE 16th Ave, Gainesville, FL 32605",
    "960 SW 10th Ave, Gainesville, FL 32605",
    "1308 NE 35th Pl, # 589, Gainesville, FL 32603",
    "5463 SW Newberry Rd, Apt 314, Gainesville, FL 32606",
    "453 NW 6th St, Suite 635, Gainesville, FL 32606",
    "9731 SE 31st Pl, Unit 815, Gainesville, FL 32609",
    "3766 SE 2nd Pl, Apt 453, Gainesville, FL 32606",
    "7716 SE 2nd Pl, Suite 722, Gainesville, FL 32606",
    "3493 SW 10th Ave, Gainesville, FL 32603",
    "8604 SE 15th Pl, Gainesville, FL 32611",
    "8042 SW 8th Ave, Gainesville, FL 32611",
    "1625 NE 20th Ave, Gainesville, FL 32605",
    "8284 SE Archer Rd, Apt 372, Gainesville, FL 32609",
    "1349 SE 37th Dr, Gainesville, FL 32601",
    "1622 SW 13th St, Unit 790, Gainesville, FL 32605",
    "618 NE 10th Ave, Apt 155, Gainesville, FL 32611",
    "5104 NE Williston Rd, Gainesville, FL 32606",
    "2280 NE 5th Ave, Gainesville, FL 32607",
    "2983 NW 21st Ter, Gainesville, FL 32603",
    "914 SW 75th St, Suite 499, Gainesville, FL 32608",
    "693 SE 31st Pl, Gainesville, FL 32606",
    "5389 SE Newberry Rd, Apt 291, Gainesville, FL 32610",
    "7814 NE 12th St, Unit 436, Gainesville, FL 32609",
    "2058 NW Main St, Apt 283, Gainesville, FL 32606",
    "3478 SE 15th Pl, Suite 617, Gainesville, FL 32607",
    "1596 SW 13th St, Apt 150, Gainesville, FL 32611",
    "8746 NW Tower Rd, Gainesville, FL 32610",
    "4732 SW Williston Rd, Apt 896, Gainesville, FL 32601",
    "6568 NW 2nd Pl, Suite 266, Gainesville, FL 32607",
    "403 SE 6th St, Gainesville, FL 32603",
    "6199 NW 15th St, Apt 302, Gainesville, FL 32603",
    "4805 SW Depot Ave, Unit 319, Gainesville, FL 32606",
    "3742 SW 75th St, Gainesville, FL 32601",
    "709 SE 5th Ave, Apt 151, Gainesville, FL 32605",
    "2776 NE 39th Ave, Apt 164, Gainesville, FL 32611",
    "9482 NW 31st Pl, Gainesville, FL 32603",
    "684 SE 8th Ave, Suite 492, Gainesville, FL 32607",
    "3270 NW 23rd Ave, Gainesville, FL 32606",
    "5820 NE Waldo Rd, Apt 217, Gainesville, FL 32601",
    "7287 NE 12th St, Apt 554, Gainesville, FL 32608",
    "2657 SW 91st Blvd, Apt 119, Gainesville, FL 32611",
    "7845 SW 2nd Pl, Gainesville, FL 32605",
    "6060 SW 91st St, Apt 689, Gainesville, FL 32601",
    "8461 NW 34th St, Suite 318, Gainesville, FL 32608",
    "4563 SE 31st Pl, Apt 508, Gainesville, FL 32610",
    "1520 SE 10th Ave, Gainesville, FL 32609",
    "7744 NW 8th Ave, Apt 155, Gainesville, FL 32610",
    "4899 NW 15th Pl, Gainesville, FL 32611",
    "3890 NW 6th St, Suite 388, Gainesville, FL 32601",
    "1513 SW 23rd Ave, Gainesville, FL 32607",
    "9058 NE 10th Ave, Apt 254, Gainesville, FL 32611",
    "716 SW 91st Blvd, Gainesville, FL 32608",
    "993 SE 23rd Ave, Apt 776, Gainesville, FL 32603",
    "8352 NE 6th St, Apt 140, Gainesville, FL 32603",
    "6660 SE 15th St, Gainesville, FL 32601",
    "546 NE 12th St, Apt 449, Gainesville, FL 32609",
    "4885 NW Archer Rd, Gainesville, FL 32603",
    "7482 NE 91st St, Apt 767, Gainesville, FL 32607",
    "3484 SW 21st Ter, Apt 437, Gainesville, FL 32610",
    "4793 NW 91st Blvd, Gainesville, FL 32611",
    "6586 NE 20th Ave, Apt 181, Gainesville, FL 32607",
    "1389 SE 91st Blvd, Apt 742, Gainesville, FL 32606",
    "2106 NW 10th Ave, Gainesville, FL 32605",
    "3627 NE 31st Pl, Apt 682, Gainesville, FL 32609",
    "6814 SE 16th Ave, Suite 787, Gainesville, FL 32610",
    "912 SW 8th Ave, Gainesville, FL 32603",
    "1050 NE 13th St, Apt 658, Gainesville, FL 32609",
    "1548 NW 12th St, Gainesville, FL 32601",
    "5021 SE 15th Pl, Apt 119, Gainesville, FL 32608",
    "781 SW 13th St, Gainesville, FL 32606",
    "1936 SE 23rd Ave, Suite 330, Gainesville, FL 32603",
    "1299 NW 6th St, Apt 399, Gainesville, FL 32606",
    "2584 SW 23rd Ave, Apt 418, Gainesville, FL 32607",
    "3850 NW 75th St, Suite 345, Gainesville, FL 32611",
    "1410 NE 20th Ave, Gainesville, FL 32605",
    "919 SW Tower Rd, Apt 260, Gainesville, FL 32608",
    "6185 NW University Ave, Apt 497, Gainesville, FL 32606",
    "3477 SE 15th Pl, Apt 574, Gainesville, FL 32607",
    "4519 SE 21st Ter, Apt 852, Gainesville, FL 32603",
    "2807 NE 8th Ave, Apt 391, Gainesville, FL 32611",
    "3263 NW Williston Rd, Apt 201, Gainesville, FL 32609",
    "7545 NE 75th St, Apt 729, Gainesville, FL 32601",
    "217 SW 6th St, Gainesville, FL 32606",
    "1354 NE 15th Pl, Apt 670, Gainesville, FL 32610",
    "528 NW 10th Ave, Apt 784, Gainesville, FL 32605",
    "6677 SW Newberry Rd, Suite 837, Gainesville, FL 32607",
    "4083 SW 91st Blvd, Gainesville, FL 32608",
    "8901 NW 91st Blvd, Apt 390, Gainesville, FL 32611",
    "2597 NE 15th Pl, Suite 603, Gainesville, FL 32610",
    "1141 NW 31st Pl, Gainesville, FL 32607",
    "7940 SE 39th Ave, Apt 503, Gainesville, FL 32605",
    "3436 SE Archer Rd, Apt 470, Gainesville, FL 32611",
    "6023 SW 10th Ave, Suite 444, Gainesville, FL 32608",
    "4319 SW 15th St, Apt 528, Gainesville, FL 32601",
    "9923 NE 6th St, Gainesville, FL 32603",
    "5180 NW Tower Rd, Apt 217, Gainesville, FL 32610",
    "3262 SW 31st Pl, Apt 422, Gainesville, FL 32611",
    "1277 SE University Ave, Apt 391, Gainesville, FL 32601",
    "2011 SW 75th St, Gainesville, FL 32605",
    "3118 SE 23rd Ave, Apt 544, Gainesville, FL 32606",
    "9300 NW 8th Ave, Apt 627, Gainesville, FL 32609",
    "644 NE 39th Ave, Gainesville, FL 32610",
    "728 SW 15th Pl, Apt 711, Gainesville, FL 32608",
    "1995 NE 91st St, Gainesville, FL 32601",
    "8854 SW Archer Rd, Apt 183, Gainesville, FL 32603",
    "2466 SE Depot Ave, Apt 602, Gainesville, FL 32607",
    "1601 NW Main St, Suite 845, Gainesville, FL 32611",
    "743 NE 23rd Ave, Gainesville, FL 32609",
    "1381 NW 8th Ave, Apt 106, Gainesville, FL 32605",
    "5147 SW 91st Blvd, Apt 740, Gainesville, FL 32608",
    "6382 NE 31st Pl, Suite 200, Gainesville, FL 32601",
    "9115 SW 21st Ter, Gainesville, FL 32603",
    "4891 NE 91st Blvd, Apt 367, Gainesville, FL 32609",
    "7090 SW 6th St, Apt 144, Gainesville, FL 32606",
    "3846 NW 8th Ave, Gainesville, FL 32605",
    "5261 NE 31st Pl, Apt 613, Gainesville, FL 32603",
    "2064 NW Tower Rd, Apt 712, Gainesville, FL 32607",
    "8910 SW Williston Rd, Apt 262, Gainesville, FL 32611",
    "3008 NE 10th Ave, Gainesville, FL 32610",
    "943 SW 21st Ter, Apt 748, Gainesville, FL 32605",
    "1235 NW 13th St, Apt 525, Gainesville, FL 32603"
]
phone_numbers = [
    "786-480-3786", "941-543-7342", "954-946-1591", "941-622-2266", "818-403-6400", "850-203-2430",
    "602-844-3188", "212-469-2302", "754-927-2738", "813-387-5032", "503-339-1784", "305-768-1534",
    "813-944-7794", "941-838-8492", "863-753-8421", "954-621-1967", "646-309-8274", "801-467-3793",
    "954-823-1495", "850-414-3293", "863-651-7281", "772-680-5193", "727-376-2074", "415-300-5849",
    "202-416-6431", "321-864-2673", "941-528-8015", "352-275-9104", "813-776-2413", "718-283-7491",
    "813-338-4981", "321-525-3825", "407-945-1194", "904-831-9670", "850-271-3951", "213-685-7013",
    "954-982-1243", "863-920-3794", "352-920-2638", "941-284-6619", "727-238-7715", "415-957-7626",
    "863-754-8124", "407-392-5810", "941-810-5227", "786-791-3489", "516-304-6921", "212-782-2501",
    "561-235-9571", "352-813-6882", "813-952-7772", "202-316-3029", "801-737-1582", "386-618-5317",
    "305-634-7756", "850-751-6007", "202-756-1964", "305-718-2712", "727-882-4609", "617-453-7186",
    "941-396-8440", "561-608-3210", "954-232-8911", "407-912-2874", "503-207-1523", "352-963-4385",
    "813-938-9245", "213-746-1644", "863-459-3894", "727-381-6732", "407-377-5108", "772-568-6921",
    "202-846-7321", "904-234-7617", "718-759-8310", "941-646-1431", "850-246-3384", "213-412-9052",
    "305-989-5631", "954-720-9052", "602-913-4614", "352-874-1387", "813-765-1433", "561-974-5836",
    "503-869-7044", "212-845-7711", "727-746-9855", "850-476-9472", "954-782-2174", "718-820-2931",
    "813-970-5382", "386-916-4233", "561-310-7669", "407-988-1425", "321-417-5623", "941-718-9216",
    "202-990-4980", "863-701-9442", "352-763-8020", "415-379-9472", "954-876-4400", "727-558-3781",
    "801-914-2856", "305-391-6875", "941-358-6324", "850-628-1752", "212-536-6030", "407-691-8405",
    "954-243-1809", "863-320-6987", "602-661-7238", "321-868-2024", "718-358-3718", "941-682-9043",
    "813-204-4976", "305-202-9816", "850-333-7060", "646-509-3615", "772-942-7306", "386-705-4342",
    "786-273-4398", "305-781-6494", "212-354-8080", "954-712-9138", "407-604-2354", "727-408-6059",
    "503-684-3331", "863-248-3732", "941-720-4691", "850-943-3910", "321-639-7892", "561-741-3850",
    "386-319-2035", "702-819-5772", "917-875-2942", "904-740-5159", "813-984-2746", "352-206-4605",
    "718-560-7416", "954-320-1123", "202-436-1812", "813-275-4681", "602-340-7704", "801-671-4198",
    "305-478-1962", "516-687-9223", "561-970-6412", "727-217-3549", "321-572-8042", "941-356-4993",
    "202-674-3152", "212-784-3061", "850-647-2895", "772-930-1804", "863-618-7024", "954-693-1581",
    "305-243-7137", "407-421-9782", "386-298-4012", "954-227-8439", "646-741-6321", "801-426-6985"
]

used_names = ['']
used_emails = ['']
used_ids = ['']

delimiters = [".", "", "-"]
emails = ["gmail.com", "yahoo.com", "icloud.com", "outlook.com", "ufl.edu", "aol.com"]

from User import User

with open("../data/user.sql", "w") as file:
    file.write("DROP TABLE IF EXISTS User;\n")
    file.write("CREATE TABLE User (")
    file.write("account_id VARCHAR(16) PRIMARY KEY, ")
    file.write("name VARCHAR(32), ")
    file.write("address VARCHAR(64), ")
    file.write("phone_number VARCHAR(16), ")
    file.write("email VARCHAR(32));\n")

    for i in range(121):
        full_name = ''
        while full_name in used_names:
            first_name = first_names[randint(0, len(first_names) - 1)]
            last_name = last_names[randint(0, len(last_names) - 1)]
            full_name = first_name + " " + last_name
        used_names.append(full_name)

        email = ''

        while email in used_emails:
            use_full_name = randint(0, 3)
            if use_full_name == 0:
                starter = first_name + delimiters[randint(0, len(delimiters) - 1)] + last_name[0]
            elif use_full_name == 1:
                starter = first_name[0] + delimiters[randint(0, len(delimiters) - 1)] + last_name
            else:
                starter = first_name + delimiters[randint(0, len(delimiters) - 1)] + last_name

            email = starter + "@" + emails[randint(0, len(emails) - 1)]

        email = email.lower()
        address = addresses[i]
        phone_number = phone_numbers[i]

        account_id = ''
        while account_id in used_ids:
            temp_uuid = str(uuid4())
            account_id = temp_uuid[-12:]

        used_ids.append(account_id)

        file.write(f'INSERT INTO USER (account_id, name, address, phone_number, email) VALUES ("{account_id}", "{full_name}", "{address}", "{phone_number}", "{email}");\n')




