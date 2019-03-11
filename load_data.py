import pandas as pd
import datetime
import csv


def load_data():
    # TODO: load diff files acc to month.
    bf_menu = pd.read_csv('/Users/quahjingwen/Desktop/bf_menu.csv')
    dinz_menu = pd.read_csv('/Users/quahjingwen/Desktop/dinz_menu.csv')
    return bf_menu, dinz_menu


def format_date(tdy_raw):
    tdy_str = format(tdy_raw, '%Y-%m-%d')
    return tdy_str


def format_menu(menu):
    dtime = str(datetime.datetime.today() + datetime.timedelta(hours=8))
    res = menu.dropna().to_string(index=False, header=False, na_rep="")

    words_to_bold = ['Breakfast', 'Dinner']
    words_to_italicized = ['Choose 1', 'Drinks', 'Meat', 'Side Dish', '-Soup-', 'Main', 'Vegetable', 'Dessert', 'Set A', 'Set B']
    res.replace(" ", "")
    for word in words_to_bold:
        res = res.replace(word, '*{0}*'.format(word.upper()))
    for word in words_to_italicized:
        res = res.replace(word, '\n_{0}_'.format(word))
    res = res.replace("/restart", "")
    res = res.replace("  ", "")
    res = res.replace("\n ", "\n")
    return res + "\n "


def get_indv_menus(type, raw_date):
    bf_menu, dinz_menu = load_data()
    if type == 'Breakfast':
        overall_menu = bf_menu
    elif type == 'Dinner':
        overall_menu = dinz_menu
    try:
        dateStr = format_date(raw_date + datetime.timedelta(hours=8))
        res = dateStr + "\n" + format_menu(overall_menu[dateStr])
        return res
    except:
        return "None available "

def get_office_info():
    first_string = "Hall Office (Residential Life)" + "\n" + "Senior Manager: Ms Rashidah Salleh" + "\n" + "eshrs@nus.edu.sg" + "\n" + "Assistant Manager: Mr Foo Chen Loong" + "\n" + "eshfcl@nus.edu.sg" + "\n" + "Management Assistant Officer: Mr Ng Jun Wei" + "\n" + "eshnjw@nus.edu.sg" + "\n"
    second_string = "OHS Eusoff Hall Team" + "\n" + "Senior Executive: Ms Nisha Alex" + "\n" + "ohsna@nus.edu.sg" + "\n" + "Management Assistant Officer: Mr Tan Shau Wei" + "\n" + "ohstsw@nus.edu.sg" + "\n" + "Technical Officer: Mr Rajan" + "\n" + "(Contact not available)"
    return first_string + "\n" + second_string

def get_SCRC_info():
    master = "Master: A/Prof Goh Beng Lan" +  "\n" + "eshhead@nus.edu.sg"
    a = "Resident Fellow, Block A: A/Prof Suthiwan Titima" +  "\n" + "eshts@nus.edu.sg"
    b = "Resident Fellow, Block B: Mr Mark Teng Mah Kiong" +  "\n" + "fastmk@nus.edu.sg"
    c = "Resident Fellow, Block C: Dr Lee Chian Chau" +  "\n" + "uhclcc@nus.edu.sg"
    d = "Resident Fellow, Block D: A/Prof Qiu Anqi" +  "\n" + "eshqa@nus.edu.sg"
    e = "Resident Fellow, Block E: Dr Muhammad Arafat bin Mohamad" +  "\n" + "eshmam@nus.edu.sg"
    return master + "\n" + a + "\n" + b + "\n" + c + "\n" + d + "\n" + e
def get_JCRC_info():
    pres = "President: Matthew Tjoeng Rui Zhi" +  "\n" + "8200 2379"
    a = "Vice President: Arun Ganasarajah" +  "\n" + "9644 4135"
    b = "Vice President: Amos Lim Boon Hao" +  "\n" + "9430 1369"
    c = "Honorary General Secretary: Foo Ming Jing Bryna" +  "\n" + "9699 6605"
    d = "Sports Director: Loo Jian Wei, Raymond" +  "\n" + "9751 0926"
    e = "Performing Arts Director: Eunice Amor Oh Wen Ning" +  "\n" + "8418 8229"
    f = "Social Service Director: Lye Pei Xuan" +  "\n" + "9652 1149"
    g = "Student Affairs Director: Ng Li Ann" +  "\n" + "9752 5185"
    h = "Finance Director: Tan Shih Jia Sandra" +  "\n" + "8228 2317"
    i = "Media Director: Tan Cheng Xin" +  "\n" + "9823 8972"
    return pres + "\n" + a + "\n" + b + "\n" + c + "\n" + d + "\n" + e + "\n" + f + "\n" + g + "\n" + h + "\n" + i

def get_blockcomm_info():
    a = "Head of Block A: Hoo Jinh Hao" +  "\n" + "8168 7844"
    b = "Head of Block B: Sherman Yong Wen Hong" +  "\n" + "9771 9021"
    c = "Head of Block C: Goh Wei Lie" +  "\n" + "8588 1406"
    d = "Head of Block D: Tammy Choo Min Li" +  "\n" + "8183 2157"
    e = "Head of Block E: Melvin Vito" +  "\n" + "9229 6912"
    return a + "\n" + b + "\n" + c + "\n" + d + "\n" + e

def get_culture_info():
    a = "CMC: Jerald Lim & Tan Cynee" +  "\n" + "9225 9022 & 8488 3715"
    b = "Acapella: Ong Wee Koon Daniel (D Block)" +  "\n" + "9771 9021"
    c = "Band: Roy Francis Mohanan (D Block) & Tammy Choo (D Block)" +  "\n" + "8611 6105 & 8183 2157"
    d = "Choir: Ian Chin (B Block)" +  "\n" + "8183 2157"
    e = "Dance: Chua Wei Shan (E Block)" +  "\n" + "9229 6912"
    f = "Drama: Ho Yun Yan Grace (D Block) & Tan Kang Wei (E Block)" +  "\n" + "8223 1810 & 8533 8544"
    g = "Dance Production: Danny Hua (D Block) & Goh Wei Zhang (D Block)" +  "\n" + "9847 9233 & 9113 1751"

    return a + "\n" + b + "\n" + c + "\n" + d + "\n" + e + "\n" + f + "\n" + g

def get_ss_info():
    a = "Eusoff Expeditions: Liu Ming Hao, Ang Hui Wen, Koh Yu Rui" +  "\n" + "932 6780, 9690 9934 & 9232 6445"
    b = "EVC Salvation Army: Kelly Gan" +  "\n" + "8333 4277"
    c = "EVC Elderly Service: Damian Chong & Sarah Priyanka" +  "\n" + "9632 9638 & 9656 4726"
    d = "EVC MINDS: Qi Lu & Nicole Tan" +  "\n" + "8410 6486 & 9697 8552"
    e = "Green Committee: Tan Ke En" +  "\n" + "9017 7522"
    return a + "\n" + b + "\n" + c + "\n" + d + "\n" + e 

def get_sports_info():
    pres = "SMC: S Nandakumar & Eyu Yan Yan" +  "\n" + "8368 5794 & 9088 3311"
    a = "Badminton:" +  "\n" + "Shaun Tay Wei Jun (B Block) & Wang Jia Yi, Joanna (A Block)"
    b = "Basketball:" +  "\n" + "Leong Heng Wei (D Block) & Chua Jin Xia, Valerie (B Block)"
    c = "Floorball:" +  "\n" + "Terry Tay Hoe Kiat (B Block) & Celeste Chia Xue Qi (E Block)"
    q = "Frisbee:" +  "\n" + "Isaac Sekkappan (A Block)"
    d = "Football:" +  "\n" + "Cheah Chun Kai Amos (B Block) & Zheng Qi Qi (C Block)"
    e = "Handball:" +  "\n" + "Tomoyuki Lewis Ban (B Block) & Joey Lam Ying (C Block)"
    f = "Netball:" +  "\n" + "Natalie Rodrigues (B Block)"
    g = "Road Relay:" +  "\n" + "Lee Jun Yi (B Block) & Ler Siang Hwee Stacia (C Block)"
    h = "Softball:" +  "\n" + "Malcolm Rhys Lim Jian Jun (B Block)"
    i = "Squash:" +  "\n" + "Shaun Yip Shao Wei (E Block) & Sen Fong Ling (E Block)"
    j = "Swim:" +  "\n" + "Daryl Ho (C Block) & Ong Lijing (A Block)"
    k = "Table Tennis:" +  "\n" + "Tan Carlin (A Block) & Elaine Lee Yan Min (B Block)"
    l = "Track:" +  "\n" + " Koh Wei’En Benjamin (D Block) & Larrinna Haverkamp (B Block)"
    m = "Takraw:" +  "\n" + "Irfan Dinnie bin Zaihan (A Block)"
    n = "Tennis:" +  "\n" + "Loh Keat Siang Wilbert (E Block) & Thng Hui Min Felicia (E Block)"
    o = "Touch Rugby:" +  "\n" + "Wesley Woo (B Block) & Lim Wan Ling (E Block)"
    p = "Volleyball:" +  "\n" + "Poon Pei Jie (D Block) & Ng Yen Yi (E Block)"
    return pres + "\n" + a + "\n" + b + "\n" + c + "\n" + q + "\n" + d + "\n" + e + "\n" + f + "\n" + g + "\n" + h + "\n" + i +"\n" + j + "\n" + k +"\n" + l + "\n" + m + "\n" + n + "\n" + o + "\n" + p 

def get_othercomm_info():
    a = "Special Projects Team (SPT): Joy Li Yi Jing" +  "\n" + "9187 6507"
    b = "Hall Relations Board: Hoo Jinh Hao" +  "\n" + "8168 7844"
    c = "Hall Promotion Board: Tham Rui Min Corrine & Poon Pei Jie" +  "\n" + "8109 4999 & 9234 2549"
    d = "Auditor Committee: Ang Wen Mei" +  "\n" + "9387 6608"
    e = "Elections Committee: Richard Tan Boon Chye" +  "\n" + "9841 8483"
    f = "Finance Committee: Tan Shih Jia Sandra" +  "\n" + "8228 2317"
    g = "EusoffWorks: Nguyen Tien Trung Kien & Kevin Yeong Yu Heng" +  "\n" + "9246 7870 & 9072 0273"
    h = "Eusoff Hackers: Foong Yi Zhuan" +  "\n" + "9118 9751"
    return a + "\n" + b + "\n" + c + "\n" + d + "\n" + e + "\n" + f + "\n" + g + "\n" + h

def get_sponsorship_info():
    a = "Seeking out sponsorships as part of a Eusoff Hall committee/CCA related event or activity is encouraged if the external 3 rd  parties involved are able to provide assets (i.e monetary sponsorships, goods services, etc. ) that will improve the quality of event or help the CCA achieve their set goals for said event or activity."
    b = "Any agreement that is being made between the Eusoff Hall CCA and an outside 3 rd  party that involve an exchange of goods, services or monetary sponsorship, in return for Eusoff Hall’s compliance to any agreed terms and conditions- must be approved by the 31s  t  JCRC before the deal is officially finalized."
    c = "Long term deals or partnerships that may exceed 1 Academic Year, can be continued and built upon, if deemed beneficial to the CCA and Eusoff Hall. Hence proper maintenance of relations and follow-ups with all external 3rd parties are essential ."
    d = "The respective CCA head and members are responsible for upholding the terms of their agreement with the respective 3r  d  party sponsor in order to fulfill all promises or agreements made. Any failure to do so would not only result in the loss of potential sponsors for future events but also tarnish the reputation of Eusoff Hall and its residents. Hence if such a situation arises, the 31 st  JCRC has the right to revise and monitor the respective committee/CCA rights for seeking out sponsorships in the future."
    e = "For AY 18/19 all sponsorship related matters can be addressed to Vice President Arun Ganasarajah for help and guidance."
    return a + "\n" + "\n" + b + "\n" + "\n" + c + "\n" + "\n" + d + "\n" + "\n"+ e

def get_pdpa_info():
    a = "Compliance with the Personal Data Protection Act (PDPA) is an important requirement that must be adhered to with respect to the collection, usage and disclosure of personal data."
    b = "Personal data refers to data pertaining to an individual who can be identified from the given information. This information, whether true or false, will need to be handled under the guidelines of the PDPA. Personal information includes NRIC number, NUS Matriculation number, home address and mobile number etc."
    c = "As organizers of Eusoff Hall activities, CCA heads and members will have access to confidential and personal data that are submitted by students and hence collected by the respective CCA."
    d = "The following are guidelines that the organisers should take note and adhere to:"
    e = "A. The PDPA comprises rules governing the collection, use, disclosure and care of personal data, with the objective to safeguard consumers’ personal data against misuse applies to all organisations in which personal details are used for any marketing purposes. It encompasses provision for individuals to opt out of receiving marketing phone calls, mobile text messages, and faxes from organization."
    f = "B. The first phase of PDPA, Do Not Call (DNC) Registry, will come into force on 2 January 2014. This regime under the PDPA does not allow organisations to send messages of marketing nature to Singapore telephone numbers, including mobile numbers."
    g = "C. All NUS Student Organisations are responsible in safekeeping all personal data in their possession or under their control. (E.g. Student details should not be accessible by the public through online platforms like facebook, websites, google docs etc. All personal information needs to be password protected or filed away in confidentiality)"
    h = "D. The CCA is required to appoint one or more committee members to ensure compliance across the committee. (E.g. A member of the student group, such as the CCA head should be appointed to ensure that all members comply with PDPA in the conduct of events)"
    i = "E. Each CCA must ensure that written consent is given by students for use or disclosure of their personal data. - E.g Students’ consent is required for the organizer of the event to disclose their personal details to sponsors"
    j = "F. Each CCA is required to provide a point of contact for students to change their details in order to ensure accuracy."
    return a + "\n" + "\n" + b + "\n" + "\n" + c + "\n" + "\n" + d + "\n" + "\n"+ e + "\n" + f + "\n" + g + "\n" + h + "\n" + i +"\n" + j

def get_finance_info():
    a = "All receipts are to be submitted to the treasurers for claims within 30 days from the date of purchase. No late, photocopied or lost receipts will be accepted. The Committee Head is advised to appoint a person who is highly responsible and meticulous as the treasurer, so as to ensure an efficient reimbursement process. A Finance Guidebook will be provided and treasurers are required to familiarise themselves with finance procedures. During school term, there will be two finance sessions per week, held at night."
    b = "All committees are to take note that for purchases above $500, they have to first source for various suppliers, complete the Summary of Quotation Form and then request for approval from the RF-in-charge before confirming any purchases. If in doubt, just approach the Finance Committee for clarifications." 
    c = "A Finance Briefing Session will be held for all Heads and Treasurers at a later date."   
    return a + "\n" + "\n" + b + "\n" + "\n" + c
    
def get_external_info():
    a = "SRC Fields, SRC Tennis Courts, USC Squash Courts, MPSH"
    b = "A. Inform and book through Sports Director, if not the SMC Facilities Manager"
    c = "B. Only applicable for official hall trainings"
    d = "C. Most bookings would already have been done after discussion with the sports captains"
    return a + "\n" + "\n" + b + "\n" + c + "\n" + d

def get_internal_info():
    a = "MPC, Function Hall, Squash Courts"
    b = "A. Inform and book through Sports Director, if not the SMC Facilities Manager"
    c = "B. For Function Hall, given that it has multi-purpose, only inform Sports Director or SMC FM if it is  sports-related"
    d = "C. Only applicable for official hall trainings"
    e = "D. Most bookings would already have been done after discussion with the sports captains"
    return a + "\n" + "\n" + b + "\n" + c + "\n" + d + "\n" + e

def get_cultural_info():
    a = "Dance Studio, Band Room"
    b = "A. Inform and book through Performing Arts Director"
    c = "B. Only applicable for official hall practices"
    d = "C. Most bookings would already have been done after discussion with the cultural heads"
    return a + "\n" + "\n" + b + "\n" + c + "\n" + d

def get_common_info():
    a = "Blue Oyster, Pool Room"
    b = "A. Go to NUSync website to submit a form request based on the available dates in the Calendar. Do not book on a day with another prior booking"
    c = "B. Personally inform the Student Affairs Director (Li Ann) at least 3 days in advance"
    d = "C. Last minute bookings will not be entertained"
    e = "D. Collect the keys from the Student Affairs Director (Li Ann) and return her the next day by 12 noon"
    f = "NUSync website:  https://orgsync.com/login/national-university-of-singapore"
    return a + "\n" + "\n" + b + "\n" + c + "\n" + d + "\n" + e + "\n" + "\n" + f

def get_others_info():
    a = "Function Hall, Meeting Rooms 1 & 2"
    b = "A. Go to NUSync website to submit a form request based on the available dates in the Calendar. Do not book on a day with another prior booking"
    c = "B. Personally inform the Honorary General Secretary (Bryna) at least 3 days in advance"
    d = "C. Last minute bookings will not be entertained"
    e = "D. Collect the keys from the Hall Office and return her the next day by 12 noon"
    f = "*NOTE:* Booking of Function Hall for events  (e.g. Block suppers, ad-hoc events, meetings) should be done primarily through the Honorary General Secretary"
    g = "NUSync website:  https://orgsync.com/login/national-university-of-singapore"
    return a + "\n" + "\n" + b + "\n" + c + "\n" + d + "\n" + e + "\n" + "\n" + f + "\n" + "\n" + g

def get_rooms_info():
    a = "Seminar Rooms"
    b = "A. Go to NUSync website to submit a form request based on the available dates in the Calendar. Do not book on a day with another prior booking"
    c = "B. Last minute bookings will not be entertained"
    d = "C. Collect the keys from the Hall Office and return her the next day by 12 noon"
    e = "NUSync website:  https://orgsync.com/login/national-university-of-singapore"
    return a + "\n" + "\n" + b + "\n" + c + "\n" + d + "\n" + "\n" + e

def get_printer_info():
    a = "Printer"
    b = "A. For any printer issues,  (printing card, printing machine),  please contact Dominic  directly  at 98353933"
    c = "B. In the event there is no paper, please retrieve it from the cabinet and replenish it yourselves"
    return a + "\n" + "\n" + b + "\n" + c

def get_media_equipment_info():
    header = "Booking of Media Equipment"
    a = "A. Booking of Equipment"
    b = "To book media equipment such as cameras, tripods and/or memory cards, you can contact EusoffWorks Logistics Heads Leong Heng Wei (9150 3423) and/or Benedict Chua (8339 8726) with the following format –"
    c = "Equipment required:"
    d = "Reason for Booking:"
    e = "Proposed Time & Date of Equipment Checkout:"
    f = "Proposed Time & Date of Equipment Return:"
    l = "*Do note* that requests not pertaining to Hall events may be rejected"
    g = "B. Post-Usage/Return of Equipment"
    h = "1. Return of equipment should be facilitated by a EusoffWorks Main Committee member"
    i = "2. Any damage of equipment out of carelessness will be covered by the borrower"
    j = "3. Content pertaining to the Hall should be archived in the EusoffWorks database with the format provided in the EusoffWorks Guide"
    k = "4. Memory cards should be formatted prior to return"
    return header + "\n" + "\n" + a + "\n" + b + "\n" + c + "\n" + d + "\n" + e + "\n" + f + "\n" + "\n" + l + "\n" + "\n" + g + "\n"+ h + "\n" + i + "\n" + j + "\n" + k

def get_ew_room_info():
    header = "Usage of EusoffWorks Room for Editing Purposes"
    a = "A. Requests for the usage of the EusoffWorks room for editing purposes should be processed through Tan Chengxin (9823 8972) and/or Kevin Yeong (9072 0273)"
    b = "*Do note* that requests not pertaining to Hall events may be rejected"
    return header + "\n" + "\n" + a + "\n" + "\n" + b

def get_media_services_info():
    header = "Booking of Media Services"
    a = "A. Booking of media services such as photo taking should be processed through our Client Relations Officers (CROs) Jonathan Leong (9698 9992) and/or Charles Lee (9789 9226)"
    b = "B. Bookings should be made 17 days (photo & video)/21 days (audio) prior to event date"
    c = "C. Approval for late booking is subject to availability"
    return header + "\n" + "\n" + a + "\n" + b + "\n" + c 

def get_report_info():
    header = "Report Damage of Facilities"
    a = "For any damage of facilities in common area or residents' rooms, you can either:"
    b = "1. Directly inform your respective *blockheads*, who will inform the hall's technician of the problem"
    c = "OR"
    d = "2. Notify the maintanence team via the UHMS portal"
    e = "A. Login to UHMS portal: https://uhms.nus.edu.sg/"
    f = "B. Click on the Maintenance button in the header"
    g = "C. Click on New Job to report the damage of facility"
    return  header + "\n" + a + "\n" + "\n" + b + "\n" + "\n" + c + "\n" + "\n"+ d + "\n" + e + "\n" + f + "\n" + g 

def get_compulsory_info():
    header = "*Attendance for compulsory Eusoff Hall events*"
    a = "All residents have to attend/take part in at least  2  of the following events for Semester 1 and 1 event from Semester 2:"
    b = "Semester 1 Events:"
    c = "A. Formal dinner"
    d = "B. La Soireé"
    e = "C. Annual General Meeting"
    f = "D. Conversations over Dinner"
    g = "E. Social Service Week"
    h = "F. Skills specific classes e.g. Photoshop courses (TBC)"
    i = "Semester 2 Events:"
    j = "A. La Soiree"
    k = "B. Skills specific classes e.g. Photoshop courses (TBC)"
    l = "C. Conversations over dinner"
    impt= "Residents who *fail to attend/participate in the minimum number of hall events* will result in their *hall points being void* and they shall be *disqualified from being eligible for a place in Eusoff Hall for the next Academic Year*."
    return header + "\n" + "\n" + a + "\n" + "\n" + b + "\n" + c + "\n"+ d + "\n" + e + "\n" + f + "\n" + g + "\n" + h + "\n" + "\n"+ i + "\n"+ j + "\n"+ k + "\n"+ l + "\n" + "\n" + impt

def get_graduating_info():
    header = "*Removal of Hall Points for Graduating Residents*"
    a = "All Final Year Students are not eligible to receiving hall CCA points. Year 3s who have decided to graduate may choose to opt out of receiving points. Year 4s who are not graduating in their fourth year and need points have to contact any JCRC member to opt in for points eligibility."
    return header + "\n" + "\n" + a 

def get_cca_points_info(): 
    header = "*CCA Points*"
    a = "Every CCA has a total of only 70\%\ of the total possible points that all its members can receive. For illustration: A Committee has 15 members, and the maximum points a member can possibly receive is 10. Hence the total possible points that CCA has is 15 x 10 = 150 Points. The CCA Head can only distribute 150 x 70% = 105 Points to all its members. In other words, there are 105 Points to be distributed amongst all its 15 members."
    return header + "\n" + "\n" + a 

def get_bonus_points_info(): 
    header = "*Bonus Points*"
    a = "Points are also given to residents for commendation. Points are awarded subject to discretion of the JCRC." 
    b = "Dean’s Listers in Semester 1 will receive 8 points to commend their academic excellence."
    c = "Leadership points are given to residents who stepped up to a leadership role in their respective group."
    d = "Merit points are given to outstanding members whose performance exceed the basic obligations of the CCA."
    e = "Merit points that may be awarded are as shown above in the photos"
    f = "Other Merit points may be awarded to outstanding leaders deemed by the JCRC Ex-Officio, which shall not exceed 10\%\ of the leaders in Eusoff Hall."
    g = "Members may give demerit points as penalties for unsatisfactory performance."
    return header + "\n" + "\n" + a + "\n"  + b + "\n" + c + "\n"+ d + "\n" + e + "\n" + f + "\n" + g

def get_external_cca_info(): 
    header = "*External CCA Points*"
    a = "Participation in NUS co-curricular activities (CCAs) will be taken into account towards the resident’s total CCA points in hall. However, the number of external CCA points he receives will be capped at 25\%\ of his total hall points." 
    b = "External CCAs refer to University Student Groups that are registered with the Office of Student Affairs. Only groups approved by the Office of Student Affairs are recognised for the purpose of awarding CCA Points."
    c = "External CCA points will generally mirror the points of their equivalent CCA in hall."
    d = "Residents have to submit an endorsement form for their external CCA points to be counted towards their total CCA points in hall, subjected to the discretion of the JCRC."
    e = "To illustrate two scenarios:"
    f = "a) Student A Has 50 Hall Points. His NUS External CCA is worth 10 points in Hall. 50 Hall Points x 25% = 12.5 ≈ 12. His External CCA therefore is worth 10 Hall Points. His total Hall Points = 50 + 10 = 60"
    g = "b) Student B Has 30 Hall Points. His NUS External CCA is worth 10 points in Hall. 30 Hall Points x 25% = 7.5 ≈ 7 His External CCA therefore is worth 7 Hall Points (round down) His total Hall Points = 30 + 7 = 37"
    return header + "\n" + "\n" + a + "\n"  + b + "\n" + c + "\n"+ d + "\n" + "\n" + e + "\n" + f + "\n" + g

def get_exchange_info(): 
    header = "*Points for Residents Going for/Returning from Exchange*"
    a = "Residents, who are only able to stay in Hall for one semester within one Academic Year due to involvement in Student Exchange Programme or NUS Overseas College, will have their points for that semester doubled, up to the maximum amount of points the CCA would be able to offer."
    return header + "\n" + "\n" + a 

def get_monitoring_info():
    header = "*Monitoring of Points System*"
    a = "Points will be reviewed once every academic year, during the Annual General Meeting. There will be a mid-term review to determine if the points awarded per CCA are sufficient, and will take place at the end of semester 1. A Points Defence session will be held towards the end of the academic year."
    b = "Committee Heads will have to submit the point allocation of their members to the respective JCRC Ex-Officio by the stipulated date given to them, FAILURE OF WHICH ALL POINTS MAY BE FORFEITED FOR THAT CCA."
    return header + "\n" + "\n" + a + "\n" + b 

def get_masters_list_info():
    header = "*Master’s List*"
    a = "A resident must fulfill both of the following requirements to be eligible for a Master’s List spot."
    b = "A. Join a minimum of two CCAs, both of which m  ust not  be under the same branch e.g. if person A is in a sport, to be considered, his or her other CCA cannot be a sport."
    c = "B. To have a minimum of 16 points."
    d = "*Only* National Team players are eligible for the Master’s List regardless."
    return header + "\n" + "\n" + a + "\n" + b + "\n" + c + "\n" + d

def get_demerit_info(): 
    header = "*Demerit Point Structure (DPS) for Housing Offences*"
    a = "The Demerit Point Structure (DPS) is to be read in conjunction with the Housing Agreement. Please be familiarized with the following guidelines:"
    b = "1.1 Each residential year begins on 1 June and ends on 31 May."
    c = "1.2 Demerit points (below 16 points) accumulated within a residential year are reset to ‘0’ on 1 June."
    d = "1.3 Housing Agreement is terminated upon accumulation of 16 demerit points (or more) within one residential year."
    e = "1.4 Housing Agreement is terminated upon accumulation of 25 demerit points throughout all residential years and eligibility for on campus housing will be withdrawn for the rest of the candidature."
    return header + "\n" + "\n" + a + "\n" + b + "\n" + c + "\n" + d + "\n" + e

def get_pal_info():
    header = "*Peer Assisted Learning (PAL)*"
    a = "This is an initiative put forth by Associate Professor Goh Beng Lan, in hopes of helping the year 1s adjust effectively to university and hall life so that they can get the most out of their university experience."
    b = "As the name implies, PAL is a programme only for first year undergraduates where a qualified senior will guide you on just about anything related to university. There will be 4 PAL sessions per semester for you to ask your PAL mentors any questions from Hall related things to finding a good professor for your module."
    return header + "\n" + "\n" + a + "\n" + b

def get_eoty_info(): 
    header = "*Eusoffian of the Year Award - (1 recipient)*"
    a = "A. This exclusive award is given to one resident who has made the most outstanding cumulative contributions to Eusoff Hall for at least three years (inclusive of current year)."
    b = "B. The resident must have contributed to at least two different hall activities since admission. (Cultural/Committee/Sports)"
    c = "C. The resident must have contributed to at least one activity in the current academic year."
    d = "D. The resident must be nominated and selected for a general award for the activity contributed to in the current academic year. (Merit Award/ Colors Award)"
    e = "E. The resident must have previously received either a Top Field Award or a Hall Excellence Award (Outstanding Service Award/ Distinguished Service Award)."
    f = "F. Only seniors in at least their third year of residence are eligible for this award."
    g = "G. The resident should exhibit good character and serve as an exemplary role model in the Hall."
    return header + "\n" + "\n" + a + "\n" + b + "\n" + c + "\n" + d + "\n" + e + "\n" + f+ "\n" + g

def get_topfield_info(): 
    header = "*Top Field Awards:*"
    a = "A. Sportsman/Sportswoman of the Year Award - (2 recipients, 1 from each gender)"
    b = "This award is given to one resident who has made the most outstanding contribution in Hall sports during the current academic year. Both seniors and freshmen are eligible for this award."
    c = "B. Cultural Medallion Award - (1 recipient)"
    d = "This award is given to one resident who has the most outstanding contribution in Hall cultural groups or Hall committees requiring cultural talent during the current academic year. Both seniors and freshmen are eligible for this award."
    e = "C. Committee Medallion Award - (1 recipient)"
    f = "This award is given to one resident who has made the most outstanding contribution in Hall committees during the current academic year. Both seniors and freshmen are eligible for this award."
    return header + "\n" + "\n" + a + "\n" + b + "\n" + "\n" + c + "\n" + d + "\n" + "\n" + e + "\n" + f

def get_hallex_info(): 
    header = "*Hall Excellence Awards*"
    a = "A. Distinguished Service Award - (20 recipients)"
    b = "1. This exclusive award is given to residents who have made outstanding cumulative contributions to Eusoff Hall for at least three years (inclusive of current year)."
    c = "2. The resident must have contributed to at least two different hall activities since admission."
    d = "3. The resident must have contributed to at least one activity in the current academic year."
    e = "4. The resident must be nominated and selected for a general award for the activity contributed to in the current academic year."
    f = "5. The resident must have previously received a general award (excluding certificate of commendation) in any category."
    g = "6. Only seniors in at least their third year of residence are eligible for this award."
    h = "A. Outstanding Service Award - (30 recipients)"
    i = "1. This exclusive award is given to residents who have made outstanding cumulative contributions to Eusoff Hall for at least three years (inclusive of current year)."
    j = "2. The resident must have contributed to at least two different hall activities since admission."
    k = "3. The resident must have contributed to at least one activity in the current academic year."
    l = "4. The resident must be nominated and selected for a general award for the activity contributed to in the current academic year."
    m = "5. The resident must have previously received a general award (excluding certificate of commendation) in any category."
    n = "6. Only seniors in at least their third year of residence are eligible for this award."
    return header + "\n" + "\n" + a + "\n" + b + "\n" + c + "\n"+ d + "\n" + e + "\n" + f + "\n" + g + "\n" + "\n" + h + "\n"+ i + "\n"+ j + "\n"+ k + "\n"+ l + "\n" + m + "\n" + n

def get_general_awards_info():
    header = "*General Awards*"
    a = "A. Merit Award (voted by committee heads) - (capped at 80 recipients)"
    b = "1. This award is given to residents who have made outstanding contributions to the committee or cultural scene of Eusoff Hall."
    c = "2. Both seniors and freshmen are eligible for this award."
    d = "B. Colours Award (voted by captains) - (capped at 80 recipients)"
    e = "1. This award is given to residents who have made outstanding contributions to the sporting scene of Eusoff Hall."
    f = "2. Both seniors and freshmen are eligible for this award."
    g = "C. Rookie of the Year (Male/Female) - (1 recipient)"
    h = "1. This award is given to one freshman resident who has made the most outstanding contribution to any Hall activity, be it cultural groups, committees, and/or sports during the current academic year."
    i = "2. Only first year residents (i.e. freshmen and new seniors) are eligible for this award."
    return header + "\n" + "\n" + a + "\n" + b + "\n" + c + "\n" + "\n"+ d + "\n" + e + "\n" + f + "\n" + g + "\n" + "\n" + h + "\n"+ i
