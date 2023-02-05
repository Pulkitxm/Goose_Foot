import mysql.connector,random
##['ID','NAME','GENDER','DOB','ADDRESS','EDUCATION','SALARY','STARS','WORK EXPIRIENCE','NOOTN','NOC','Tip']
info=[['1000','Akash Kapoor','M','21.05.2002','Murli Upadhay Est, . Off Aarey Rd, Goregaon ','12TH PASS','20K','3','1YR','3000','2','30K'],
      ['1001','Aakesh Tiwari','M','23.02.2001','B 18 95, G 128 Vishal Bhawan Nehru Place','BA','40k','4.5','5YR','15000','1','2lakhs'],
      ['1002','Advik k','M','11.07.1999', 'Amit Commercial Complex, Vip Road, Karelibaug ','10th pass','70K','5','5YR','15500','1','2.7lakhs'],
      ['1003','Chaitanya','M','1.09.1997','Ft-1 D B, Mani Towers, Sahapur ','12TH PASS','60k','5','7YR','21300','0','30K'],
      ['1004','Darsh','M','6.05.1987',' 228, 2nd Flr, Panchratna, Nr.charni Road, Opera House ','Eng hons','80K','5','10YR','31000','0','6lakhs'],
      ['1005','Chandran','M','8.06.2000',' 82, Church Mission Road ','10TH PASS','50K','3.5','4YR','12000','3','80k'],
      ['1006','Darpan','M','9.03.1999','15policerdblr-53, Chickpet ','12TH PASS','30K','3','1.5YR','4000','4.5','40K'],
      ['1007','Ekansh','M','16.07.1976',' 5, 506, Ram Gopal Ind Estate, Tulsi Pipe Rd, Dadar (west)','Hindi hons','35K','3.5','2YR','5000','4','80K'],
      ['1008','Evak','M','2.05.2001',' No 1, Mohammadpur ','10TH PASS','25K','3','6 months','1700','3','10K'],
      ['1009','Girik','M','21.05.2002',' Anuja Apartment, B-10, 1st Floor, Kastur Park, Shimpoli Road, Borivali (west) ','12TH PASS','47K','4','6YR','18550','1','3','5lakhs'],
      ['1010','Hredhaan','M','30.5.1959',' 24, 2 Nd Flr, Opp Alankar Cinema, 3 Rd Khetwadi Lane, Bansi Bhavan, Khetwad ','12TH PASS','20K','3.5','4 months','12000','0','5K'],
      ['1011','Aadhya','F','3.04.1995','4, Vallabh Society, 90 Ft Road, Opp Bldg No - 203, Ghatkoper (east)','12TH PASS','20K','3','1YR','3000','2','50K'],
      ['1012','Aanya ','F','19.05.2002','Pocket A3, Rohini ','10TH PASS','45K','4.5','4YR','15000','2','80K'],
      ['1013','Bhavna','F','21.07.1993','Shop No 1 &4, Shaheen Building, Mahul Road, Opp Navjivan Society, Chembur ','12TH PASS','62K','5','5YR','15000','1','90K'],
      ['1014','Brinda ','F','2.10.1963','5-5-849, Goshamahal','12TH PASS','30K','3','1YR','3000','2','20K'],
      ['1015','Chhaya','F','01.07.2002','2, 28, Prabhu Kripa, Tilak Rd., Rajawadi, Ghatkoper (east) ','BA','55K','3.5','3YR','17000','4','60K'],
      ['1016','Aarna','F','21.05.2002','4 Gandhi Nagar, D S Road, Worli ','10TH PASS','40K','3','2YR','3750','2','39K'],
      ['1017','Ishani','F','17.08.1994','121-b, Jaygopal Indl Estate, Bhavani Shankar X Road, Dadar (west) ','12TH PASS','49K','4','4YR','12800','2','90K'],
      ['1018','Binita','F','03.03.1978','Plot No 11, Gali No 7, Anand Parbat Indl Area ','12TH PASS','36K','3.5','5YR','15650','5','60K'],
      ['1019','Jeevika','F','25.05.2002','Market Yard Rd, Opp Kamal Nursing Home ','12TH PASS','46K','4','4YR','16000','2','1Lakh'],
      ['1020','Kashvi','F','16.04.1969',' Plot No 30 4th Floor, Village ','10TH PASS','90K','5','8YR','24500','2','1 lakh'],
      ['1021','Hemang','M','14.11.1999','Market Yard Rd, Opp Kamal Nursing Home ','10th PASS','50K','5','5YR','15000','2','90K'],
      ['1022','Inesh','M','25.05.1963','B 18, Dr Mukherjee Nagar','12TH PASS','20K','3','1YR','3000','2','30K'],
      ['1023','Ishaan','M','27.07.2000','23, Prabhat Centre, Sector 1a, Belapur (cbd) ','12TH PASS','90K','5','10YR','30000','0','9lakhs'],
      ['1024','Jairaj','M','21.07.1973',' 4, Heavyindustrialarea, Jodhpur(raj), Heavy Industr ','12TH PASS','20K','3','1YR','3000','2','30K'],
      ['1025','Jihan','M','2.05.1997',' 1, Saakar Building, Raopura ','12TH PASS','20K','3.5','1YR','3750','2','50K'],
      ['1026','Lekh','M','11.05.2001',' Floor, Taj Shopping Arcade, Hotel Taj Mahal Hotel, Colaba ','10TH PASS','50K','3.5','4YR','12000','3','80k'],
      ['1027','Lohit','M','6.11.1975','Murli Upadhay Est, . Off Aarey Rd, Goregaon ','12TH PASS','20K','3','1YR','3000','2','30K'],
      ['1028','ManbirR','M','21.07.1997','Main Market, Laxmi Nagar','Eng hons','80K','5','10YR','31000','0','6lakhs'],
      ['1029','Mayan','M','17.08.1994','101, Omega House, Hiranandani Garden, Powai, Goregaon ','12TH PASS','20K','3','1YR','3000','2','30K'],
      ['1030','Meet','M','11.07.1999',' Kamgar Seva Mandal, E Moses Road, Worl ','12TH PASS','20K','3.5','4 months','12000','0','5K'],
      ['1031','Nishit','M','11.07.1999','Main Market, Laxmi Nagar','12TH PASS','20K','3','1YR','3000','2','30K'],
      ['1032','Nihal','M','21.05.2002',' Lic City Branch 111, Nampally ','Hindi hons','35K','3.5','2YR','5000','4','80K'],
      ['1033','Onkar','M','16.07.1976','474, A2, Shah & Nahar Indl.estate, Dhanraj Mill Com, Lower Parel (west) ','12TH PASS','20K','3','1YR','3000','2','30K'],
      ['1034','Oviyan','M','21.05.2002','113 Bakor Patel Tower, Opp Karelibaug Police Station, Opp Karelibaug Police Station ','12TH PASS','20K','3','1YR','3000','2','30K'],
      ['1035','Onveer','M','8.06.2000','E-4, Nav Samaj Society, Nehru Rd, Vile Parle (east)','12TH PASS','20K','3','1YR','3000','2','30K'],
      ['1036','Parijat','M','11.07.1999','E-4, Nav Samaj Society, Nehru Rd, Vile Parle (east) ','12TH PASS','20K','3','1YR','3000','2','30K'],
      ['1037','Pranjal','M','21.05.2002','20/6, 9th Main, Jayanagar ','12TH PASS','20K','3','1YR','3000','2','30K'],
      ['1038','Pranit','M','17.08.1994','Cross, 7th Block, 2nd Stage, Nagarbhavi ','12th  pass','70K','5','5YR','15500','1','2.7lakhs'],
      ['1039','Rayaan','M','16.07.1976','18/b, 18/b Adarsh Ind Est Market Road, Bhayander (east)','12TH PASS','20K','3','1YR','3000','2','30K'],
      ['1040','Ronit','M','11.07.1999',' G-3 Bhaveshwer Complex, Ghatkopar (west) ','Eng hons','80K','5','10YR','31000','0','6lakhs'],
      ['1041','Reyansh S','F','21.05.2002',' Ff-113, Panorama Complex, Alkapuri ','12TH PASS','20K','3.5','4 months','12000','0','5K'],
      ['1042','Reyansh','F','8.06.2000','C/102, Ttc Ind Area, Off Thane Belapur Rd, Pawane, Chinch Bunder','12TH PASS','20K','3','1YR','3000','2','30K'],
      ['1043','Gulika','F','11.07.1999',' 510/2, Ganda Nala Bazar, Kashmere Gate ','12TH PASS','20K','3','1YR','3000','2','30K'],
      ['1044','Kalki ','F','21.05.2002',' R-883, Ttc Indl Area, Midc, Rabale, Navi Mumbai','10TH PASS','50K','3.5','4YR','12000','3','80k'],
      ['1045','Ekiya','F','11.07.1999','128, 9 & 10 Dividing Road, Sector 10, Faridabad','12TH PASS','70K','5','5YR','15500','1','2.7lakhs'],
      ['1046','Samaksh','M','21.05.2002','3, Link Rd, Opp Paras Marble, Jogeshwari (west) ','10TH PASS','90K','5','8YR','24500','2','1 lakh'],
      ['1047','Sanket','M','11.07.1999',' 268, Uday Park, Masjid Moth ','12TH PASS','20K','3','1YR','3000','2','30K'],
      ['1048','Tuhin','M','21.05.2002','9gdwnstblr-2, Godown Road ','12TH PASS','20K','3','1YR','3000','2','30K'],
      ['1049','Sanat','M','16.07.1976',' 4/27, Industrial Estate, Gorwa ','10TH PASS','90K','5','8YR','24500','2','1 lakh'],
      ['1050','Trijal','M','3.04.1995','Shop No 15, Nr Hanuman Temple, Ganga Bldg, Malad (east) ','12TH PASS','20K','3','1YR','3000','2','30K'],
      ['1051','Tejas','M','8.06.2000','C 154 Phase 2 ','12TH PASS','20K','3','1YR','3000','2','30K'],
      ['1052','Umang','M','11.07.1999','17, Wallers Rd','12TH PASS','20K','3','1YR','3000','2','30K'],
      ['1053','Udarsh','M','21.05.2002','272, 272 Bhaudaji Rd Extention, Sion ','12TH PASS','20K','3','1YR','3000','2','30K'],
      ['1054','Viraj','M','16.07.1976','128, 9 & 10 Dividing Road, Sector 10, Faridabad ','12TH PASS','70K','5','5YR','15500','1','2.7lakhs'],
      ['1055','Vaidik','M','21.05.2002','Shail Kunj,ruby Compound, Ashok Nagar, Kandivali (east) ','12TH PASS','20K','3','1YR','3000','2','30K'],
      ['1056','Yash','M','3.04.1995','5-3-831/8, Goshamahal','12TH PASS','20K','3','1YR','3000','2','30K'],
      ['1057','Yash P','M','21.05.2002','47, Kasawa Kutir, Maninagar','12TH PASS','20K','3','1YR','3000','2','30K'],
      ['1058','Yagnesh','M','21.05.2002',' 3-6-747/b Second Floor, Himayatnagar ','12TH PASS','20K','3','1YR','3000','2','30K'],
      ['1059','Yug','M','16.07.1976',' 510/2, Ganda Nala Bazar, Kashmere Gate, Goregaon ','BA','55K','3.5','3YR','17000','4','60K'],
      ['1060','Rishi','M','17.08.1994','Murli Upadhay Est, . Off Aarey Rd, Goregaon ','10TH PASS','90K','5','8YR','24500','2','1 lakh'],
      ['1061','Ram','M','21.05.2002','3, Link Rd, Opp Paras Marble, Jogeshwari (west) ','BA','55K','3.5','3YR','17000','4','60K'],
      ['1062','Zakir','M','3.04.1995','48, M M Lane, Nagarthpet Corss, Ganigarpet ','12TH PASS','20K','3','1YR','3000','2','30K'],
      ['1063','Laasya','F','21.05.2002','Shop No 15, Nr Hanuman Temple, Ganga Bldg, Malad (east)','10TH PASS','90K','5','8YR','24500','2','1 lakh'],
      ['1064','Mihika','F','21.05.2002','9gdwnstblr-2, Godown Road','Eng hons','80K','5','10YR','31000','0','6lakhs'],
      ['1065','Shravya','F','3.04.1995','2 A, Fari Manol, 13, Ganbow Street, Behind Citi Bank, Fort ','BA','55K','3.5','3YR','17000','4','60K'],
      ['1066','Turvi','F','17.08.1994',' 82/c, Rajashree Building, N G Acharya Marg, Nr Syndicate Bank, Chembur (east) ','12TH PASS','60k','5','7YR','21300','0','30K'],
      ['1067','Yashica','F','11.07.1999','Shail Kunj,ruby Compound, Ashok Nagar, Kandivali (east) ','12TH PASS','20K','3','1YR','3000','2','30K'],
      ['1068','Saanvi','F','3.04.1995','17, Wallers Rd ','12TH PASS','20K','3','1YR','3000','2','30K'],
      ['1069','Sneha','F','21.05.2002',' Highway Corner, Dawri Nagar, Vakola Signal, Above Highway Hotel, Santacruz(e) ','Eng hons','80K','5','10YR','31000','0','6lakhs'],
      ['1070','Tamanna','F','17.08.1994',' 82/c, Rajashree Building, N G Acharya Marg, Nr Syndicate Bank, Chembur (east) ','12TH PASS','20K','3','1YR','3000','2','30K'],
      ['1071','Rachita','F','21.05.2002','105, 17, Vardhaman Chambers, C P Street, Fort','Eng hons','80K','5','10YR','31000','0','6lakhs'],
      ['1072','Rachana','F','16.07.1976','Murli Upadhay Est, . Off Aarey Rd, Goregaon ','12TH PASS','20K','3','1YR','3000','2','30K'],
      ['1073','Bakhshi','M','21.05.2002','2 A, Fari Manol, 13, Ganbow Street, Behind Citi Bank, Fort ','12TH PASS','20K','3.5','4 months','12000','0','5K'],
      ['1074','Balendra','M','17.08.1994',' Highway Corner, Dawri Nagar, Vakola Signal, Above Highway Hotel, Santacruz(e) ','BA','55K','3.5','3YR','17000','4','60K'],
      ['1075','Balhaar','M','11.07.1999','48, M M Lane, Nagarthpet Corss, Ganigarpet ','12TH PASS','20K','3','1YR','3000','2','30K'],
      ['1076','Balveer','M','8.06.2000','2, 2, Amarjyot Shopping Centre, 2, Amarjyot Shopping Centre, Manjalpur','BA','55K','3.5','3YR','17000','4','60K'],
      ['1077','Ekavir','M','16.07.1976','Murli Upadhay Est, . Off Aarey Rd, Goregaon ','BA','40k','4.5','5YR','15000','1','2lakhs'],
      ['1078','Faiyaz','M','21.05.2002','Murli Upadhay Est, . Off Aarey Rd, Goregaon ','BA','55K','3.5','3YR','17000','4','60K'],
      ['1079','Faras','M','17.08.1994','Murli Upadhay Est, . Off Aarey Rd, Goregaon ','BA','40k','4.5','5YR','15000','1','2lakhs'],
      ['1080','Gagan','M','2.10.1963',' 3-6-747/b Second Floor, Himayatnagar ','12TH PASS','20K','3','1YR','3000','2','30K'],
      ['1081','Ishwar','M','16.07.1976','A-3, S J D souza Cmpd, Chandivali Road, Saki Vihar, Next To Kamani Oil Mill, Andheri (east)','BA','40k','4.5','5YR','15000','1','2lakhs'],
      ['1082','Ivaan','M','11.07.1999','1st Flr, K-bldg, Near Indira Dock Red Gate, Walchand Hirachand Mrg, Ballard Estate ','Eng hons','80K','5','10YR','31000','0','6lakhs'],
      ['1083','Kushagra','M','3.04.19952','220, Galaxy Towers ','12TH PASS','60k','5','7YR','21300','0','30K'],
      ['1084','Lakshit','M','8.06.2000','58, Ballygunge Place, Ballygunj','12TH PASS','20K','3','1YR','3000','2','30K'],
      ['1085','Lohit','M','17.08.1994',' 6th Floor,113, Aman Chambers, Mama Parmanand Marg, Girgaon ','BA','40k','4.5','5YR','15000','1','2lakhs'],
      ['1086','Maanas','M','11.07.1999','10, Dattani Shopping Centre, Vasanji Lalji Road, Kandivali (west) ','BA','55K','3.5','3YR','17000','4','60K'],
      ['1087','Udant','M','21.05.2002',' 57, 57, Vimalnath Complex, H T Road, Subhanpura ','Eng hons','80K','5','10YR','31000','0','6lakhs'],
      ['1088','Qushi','F','11.07.1999',' 212, Lucky Arcade, 212,luckyarcd,ctnpetblr-53, Cottonpet ','Eng hons','80K','5','10YR','31000','0','6lakhs'],
      ['1089','Watika','F','8.06.2000','807 Imperial Mahal, 3 Rd Flr Dr. Ambedkar Road, Dadar (c.r.)','BA','40k','4.5','5YR','15000','1','2lakhs'],
      ['1090','Xiti','F','21.05.2002','95 Aj-kauser Road:10, West Marredpally ','12TH PASS','60k','5','7YR','21300','0','30K'],
      ['1091','Xiti k','F','16.07.1976','28, Church Lane','12TH PASS','20K','3','1YR','3000','2','30K'],
      ['1092','Wazir','M','2.10.1963','C 65 Sector 9 ','12TH PASS','20K','3','1YR','3000','2','30K'],
      ['1093','Yatan','M','21.05.2002','A-3, S J D souza Cmpd, Chandivali Road, Saki Vihar, Next To Kamani Oil Mill, Andheri (east) ','Eng hons','80K','5','10YR','31000','0','6lakhs'],
      ['1094','Yuvraj','M','11.07.1999','53/1, 53/1,5th Main, 4th Cross, Chamrajpet ','12TH PASS','60k','5','7YR','21300','0','30K'],
      ['1095','Hina','F','17.08.1994','1st Flr, K-bldg, Near Indira Dock Red Gate, Walchand Hirachand Mrg, Ballard Estate','12TH PASS','20K','3','1YR','3000','2','30K'],
      ['1096','Jhanvi','F','21.05.2002','2, 2, Amarjyot Shopping Centre, 2, Amarjyot Shopping Centre, Manjalpur ','BA','40k','4.5','5YR','15000','1','2lakhs'],
      ['1097','Kriti','F','17.08.1994','C 4, Pitambar Darshan, M M C Road, 2nd X Lane, Mahim ','12TH PASS','60k','5','7YR','21300','0','30K'],
      ['1098','Zashil','M','2.10.1963',' 6th Floor,113, Aman Chambers, Mama Parmanand Marg, Girgaon','BA','55K','3.5','3YR','17000','4','60K'],
      ['1099','Zeeshan','M','8.06.2000',' 212, Lucky Arcade, 212,luckyarcd,ctnpetblr-53, Cottonpet ','12TH PASS','20K','3','1YR','3000','2','30K'],
      ['1100','Kareena','F','3.04.1995',' 4/27, Industrial Estate, Gorwa ','BA','40k','4.5','5YR','15000','1','2lakhs']]
from Control import Database
db_connection = mysql.connector.connect(host= "localhost",user= "root",password= "root")
db_cursor = db_connection.cursor()
try:
    db_cursor.execute('create database '+Database)
    db_cursor.execute('use '+Database)
except:
    db_cursor.execute('use '+Database)

try:
    db_cursor.execute('''create table deliverypartners (
                                                      ID varchar(5),
                                                      NAME varchar(40),
                                                      GENDER varchar(1),
                                                      DOB varchar(30),
                                                      ADDRESS varchar(100),
                                                      EDUCATION varchar(15),
                                                      SALARY varchar(10),
                                                      STARS varchar(15),
                                                      WORK_EXPIRIENCE varchar(20),
                                                      NOOTN varchar(15) ,
                                                      NOC varchar(5),
                                                      Tip varchar(10))
                                                                        ''')

except:
    pass

for i in info:
    db_cursor.execute("insert into deliverypartners  values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11]))
    
    
db_connection.commit()

def randompicker():
    db_cursor.execute('select * from deliverypartners')
    data = db_cursor.fetchall()
    rec = random.choice(data)
    return rec
