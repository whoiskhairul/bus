def bus(source,destination = 0):
    context = {}
    dict = {
        'Airport To Bangabandhu Avenue Paribohon' : ['Fulbaria', 'Golap Shah Mazar', 'GPO', 'Paltan', 'Press Club', 'High Court', 'Motsho Bhaban', 'Shahbagh',
            'Bangla Motor', 'Kawran Bazar', 'Farmgate', 'Bijoy Sarani', 'Jahangir Gate', 'Mohakhali', 'Banani', 'Kakoli',
            'Staff Road', 'MES', 'Sheora', 'Kuril Bishwa Road', 'Khilkhet', 'Airport', 'Jasimuddin', 'Rajlakshmi',
            'Azampur', 'House Building', 'Abdullahpur'],

        'BRTC Bus Service' : ['Motijheel', 'Gulistan', 'GPO', 'Paltan', 'Press Club', 'High Court', 'Motsho Bhaban', 'Shahbagh',
            'Bangla Motor', 'Kawran Bazar', 'Farmgate', 'Bijoy Sarani', 'Jahangir Gate', 'Mohakhali', 'Banani', 'Kakoli',
            'Staff Road', 'MES', 'Sheora', 'Kuril Bishwa Road', 'Khilkhet', 'Airport', 'Jasimuddin', 'Rajlakshmi', 'Azampur',
            'House Building', 'Abdullahpur', 'Tongi'],

        'VIP 27 Paribahan' : ['Azimpur', 'Nilkhet', 'New Market', 'City College', 'Kalabagan', 'Dhanmondi 32', 'Dhanmondi 27',
            'Khamarbari', 'Bijoy Sarani', 'Jahangir Gate', 'Mohakhali', 'Banani', 'Kakoli', 'Staff Road', 'MES',
            'Sheora', 'Kuril Bishwa Road', 'Khilkhet', 'Airport', 'Jasimuddin', 'Rajlakshmi', 'Azampur',
            'House Building', 'Abdullahpur', 'Tongi', 'Station Road', 'Mill gate', 'Board Bazar', 'Gazipur Chowrasta'],

        'Victor Classic' : ['Sadarghat', 'Ray Shaheb Bazar', 'Naya Bazar', 'Golap Shah Mazar', 'GPO', 'Paltan', 'Kakrail', 'Shantinagar',
            'Malibagh Mor', 'Mouchak', 'Malibagh Railgate', 'Rampura', 'Merul', 'Madhya Badda', 'Badda', 'Uttar Badda',
            'Shahjadpur', 'bashtola', 'Natun Bazar', 'Nadda', 'Bashundhara', 'Kuril Bishwa Road', 'Khilkhet', 'Airport',
            'Jasimuddin', 'Rajlakshmi', 'Azampur', 'House Building', 'Diabari'],

        'Victor Paribahan' : ['Sadarghat', 'Ray Shaheb Bazar', 'Naya Bazar', 'Golap Shah Mazar', 'GPO', 'Paltan', 'Kakrail', 'Shantinagar',
            'Malibagh Mor', 'Mouchak', 'Malibagh Railgate', 'Rampura', 'Merul', 'Madhya Badda', 'Badda', 'Uttar Badda',
            'Shahjadpur', 'bashtola', 'Natun Bazar', 'Nadda', 'Bashundhara', 'Kuril Bishwa Road', 'Khilkhet', 'Airport',
            'Jasimuddin', 'Rajlakshmi', 'Azampur', 'House Building', 'Diabari'],

        'Ramzan Paribahanon' : ['Gabtoli', 'Technical', 'Kallyanpur', 'Shyamoly', 'Shishu Mela', 'College Gate', 'Asad Gate', 'Mohammadpur',
            'Shankar', 'Star kabab', 'Dhanmondi 15', 'Jigatola', 'City College', 'Science Lab', 'Bata Signal', 'Kataban',
            'Shahbagh', 'Motsho Bhaban', 'Kakrail', 'Shantinagar', 'Mouchak', 'Malibagh Railgate', 'Rampura', 'Banasree',
            'Demra Staff Quarter'],

        'Achim Paribahan' : ['Gabtoli', 'Technical', 'Ansar Camp', 'Mirpur 1', 'Sony Hall', 'Mirpur 2', 'Mirpur 10', 'Mirpur 11',
            'Purobi', 'Kalshi', 'ECB Chottor', 'MES', 'Sheora', 'Kuril Bishwa Road', 'Bashundhara', 'Jamuna Future Park',
            'Nadda', 'Natun Bazar', 'Bashtola', 'Shahjadpur', 'Uttar Badda', 'Badda', 'Madhya Badda', 'Merul', 'Rampura',
            'Banasree', 'Meradia bazar', 'Staff Quarter'],

        '6_no Bus' : ['Kamalapur', 'Motijheel', 'Gulistan', 'GPO', 'Paltan', 'Kakrail', 'Shantinagar', 'Malibagh Mor', 'Mouchak',
            'Moghbazar', 'Bangla Motor', 'Kawran Bazar', 'Farmgate', 'Bijoy Sarani', 'Jahangir Gate', 'Mohakhali',
            'Wireless Mor', 'Gulshan 1', 'Gulshan 2', 'Natun Bazar'],

        '8_no' : ['Jatrabari', 'Jonopath Mor', 'Sayedabad', 'Motijheel', 'Daynik Bangla Mor', 'Paltan', 'Press Club',
            'High Court', 'Shahbagh', 'Bangla Motor', 'Kawran Bazar', 'Farmgate', 'Khamarbari', 'Asad Gate',
            'College Gate', 'Shishu Mela', 'Shyamoli', 'Kallyanpur', 'Technical', 'Gabtoli'],

        'Agradut Boishakhi' : ['Natun Bazar', 'Bashtola', 'Shajadpur', 'Badda', 'Gulshan 1', 'Gulshan Bridge', 'Wireless Mor', 'Mohakhali',
            'Jahangir Gate', 'Bijoy Sarani', 'Agargaon', 'Shishu Mela', 'Shyamoli', 'Kallyanpur', 'Technical',
            'Gabtoli'  'Hemayetpur', 'Savar'],

        'Akash Paribahan' : ['Kodomtoli', 'Keraniganj', 'Babu Bazar', 'Naya Bazar', 'Golap Shah Mazar', 'GPO', 'Paltan', 'Kakrail',
            'Shantinagar', 'Malibagh Mor', 'Mouchak', 'Malibagh Railgate', 'Rampura', 'Merul', 'Madhya Badda', 'Badda',
            'Uttar Badda', 'Shahjadpur', 'bashtola', 'Natun Bazar', 'Nadda', 'Bashundhara', 'Kuril Bishwa Road',
            'Khilkhet', 'Airport', 'Jasimuddin', 'Rajlakshmi', 'Azampur', 'House Building', 'Diabari'],

        'Akik Paribahan' : ['Gabtoli', 'Technical', 'Ansar Camp', 'Mirpur 1', 'Sony Hall', 'Mirpur 2', 'Mirpur 10', 'Mirpur 11',
            'Purobi', 'Kalshi', 'ECB Chottor', 'MES', 'Sheora', 'Kuril Bishwa Road', 'Bashundhara', 'Jamuna Future Park',
            'Nadda', 'Natun Bazar', 'Bashtola', 'Shahjadpur', 'Uttar Badda'],

        'Al Makka Transport' : ['Motijheel', 'Gulistan', 'GPO', 'Paltan', 'Kakrail', 'Shantinagar', 'Malibagh Mor', 'Mouchak', 'Moghbazar',
            'Nabisco', 'Mohakhali', 'Chairman Bari', 'Kakoli', 'Banani', 'ECB Chottor', 'Kalshi', 'Purobi', 'Mirpur 10',
            'Mirpur 2', 'Mirpur 1'],

        'Alif Enterprise' : ['Mirpur 1', 'Mirpur 2', 'Sony Hall', 'Mirpur 10', 'Kazipara', 'Shewrapara', 'Agargaon', 'Bijoy Sarani',
            'Jahangir Gate', 'Mohakhali', 'Wireless Mor', 'Gulshan 1', 'Badda', 'Rampura Bridge', 'Banasree'],

        'Alif Enterprise 2' : ['Shia Masjid', 'Japan Garden City', 'Adabor', 'Shyamoli', 'Shishu Mela', 'Agargaon', 'Ziya Uddan',
            'Bijoy Sarani', 'Jahangir Gate', 'Mohakhali', 'Wireless Mor', 'Gulshan 1', 'Link Road', 'Badda',
            'Madhya Badda', 'Merul', 'Rampura', 'Banasree'],

        'Alif Enterprise 3' : ['Shia Masjid', 'Japan Garden City', 'Adabor', 'Shyamoli', 'Shishu Mela', 'Agargaon', 'Ziya Uddan',
            'Bijoy Sarani', 'Jahangir Gate', 'Mohakhali', 'Chairman Bari', 'Kakoli', 'Banani', 'Staff Road', 'MES',
            'Sheora', 'Kuril Bishwa Road', 'Khilkhet', 'Airport', 'Jasimuddin', 'Rajlakshmi', 'Azampur',
            'House Building', 'Abdullahpur'],

        'Bhuiyan Paribahan' : ['Shia Masjid', 'Japan Garden City', 'Adabor', 'Shyamoli', 'Shishu Mela', 'Agargaon', 'Ziya Uddan',
            'Bijoy Sarani', 'Jahangir Gate', 'Mohakhali', 'Chairman Bari', 'Kakoli', 'Banani', 'Staff Road', 'MES',
            'Sheora', 'Kuril Bishwa Road', 'Khilkhet', 'Airport', 'Jasimuddin', 'Rajlakshmi', 'Azampur',
            'House Building', 'Abdullahpur'],

        'Alaik Paribahan' : ['Balughat', 'Signal', 'CMH', 'Garrison', 'Adamjee College', 'Workshop', 'Jahangir Gate', 'Farmgate',
            'Kawran Bazar'],

        'Ashulia Classic' : ['Satrasta', 'Nabisco', 'Mohakhali', 'Chairman Bari', 'Kakoli', 'Banani', 'Staff Road', 'MES', 'Sheora',
            'Kuril Bishwa Road', 'Khilkhet', 'Airport', 'Jasimuddin', 'Rajlakshmi', 'Azampur', 'House Building',
            'Abdullahpur', 'Kamarpara', 'Ashulia Bazar', 'Zirabo', 'Fantasy Kingdom', 'Jamgora', 'Baipayl', 'Nobinagar'],

        'Ayat Paribahan' : ['Mohammadpur', 'Asad Gate', 'Khamarbari', 'Farmgate', 'Bijoy Sarani', 'Jahangir Gate', 'Mohakhali',
            'Wireless Mor', 'Gulshan 1', 'Natun Bazar', 'Badda', 'Uttar Badda', 'Shahjadpur', 'bashtola', 'Natun Bazar',
            'Nadda', 'Bashundhara', 'Kuril Bishwa Road'],

        'BRTC Bus Service 2' : ['Mohammadpur', 'Asad Gate', 'Khamarbari', 'Farmgate', 'Bijoy Sarani', 'Jahangir Gate', 'Mohakhali',
            'Wireless Mor', 'Gulshan 1', 'Natun Bazar', 'Badda', 'Uttar Badda', 'Shahjadpur', 'bashtola', 'Natun Bazar',
            'Nadda', 'Bashundhara', 'Kuril Bishwa Road'],

        'Bahon Paribahan' : ['Mirpur 14', 'Mirpur 10', 'Mirpur 2', 'Mirpur 1', 'Ansar Camp', 'Bangla College', 'Technical', 'Darussalam',
            'Kallyanpur', 'Shyamoli', 'Shishu Mela', 'College Gate', 'Asad Gate', 'Dhanmondi 27', 'Dhanmondi 32',
            'Kalabagan', 'Science Lab', 'Kataban', 'Shahbagh', 'High Court', 'Press Club', 'Paltan', 'Daynik Bangla Mor',
            'Motijheel', 'Arambagh', 'Kamalapur', 'Mugdapara', 'Basabo', 'Khilgaon'],

        'Balaka Paribahan' : ['Sayedabad', 'Manik Nagar', 'TT Para', 'Kamalapur', 'Malibagh', 'Mouchak', 'Moghbazar', 'Satrasta',
            'Nabisco', 'Mohakhali', 'Chairman Bari', 'Kakoli', 'Banani', 'Staff Road', 'MES', 'Sheora',
            'Kuril Bishwa Road', 'Khilkhet', 'Airport', 'Jasimuddin', 'Rajlakshmi', 'Azampur', 'House Building',
            'Abdullahpur', 'Tongi', 'Gazipur Chowrasta'],

        'Basumati Transport' : ['Gabtoli', 'Technical', 'Ansar Camp', 'Mirpur 1', 'Sony Hall', 'Mirpur 2', 'Mirpur 10', 'Mirpur 11',
            'Purobi', 'Kalshi', 'ECB Chottor', 'MES', 'Sheora', 'Kuril Bishwa Road', 'Khilkhet', 'Airport', 'Jasimuddin',
            'Rajlakshmi', 'Azampur', 'House Building', 'Abdullahpur', 'Tongi', 'Gazipur Chowrasta'],

        'Best Transport' : ['Jatrabari', 'Sayedabad', 'Ittefaq', 'Motijheel', 'Daynik Bangla Mor', 'Paltan', 'Press Club', 'High Court',
            'Motsho Bhaban', 'Shahbagh', 'Bangla Motor', 'Kawran Bazar', 'Farmgate', 'Khamarbari', 'Agargaon', 'Taltola',
            'Shewrapara', 'Kazipara', 'Mirpur 10'],

        'Bihanga Paribahan' : ['Sadarghat', 'Ray Shaheb Bazar', 'Naya Bazar', 'Golap Shah Mazar', 'GPO', 'Paltan', 'Press Club',
            'High Court', 'Motsho Bhaban', 'Shahbagh', 'Bangla Motor', 'Kawran Bazar', 'Farmgate', 'Khamarbari',
            'Agargaon', 'Taltola', 'Shewrapara', 'Kazipara', 'Mirpur 10', 'Mirpur 11', 'Purobi', 'Pallabi', 'Duaripara'],

        'Bihanga Paribahan 2' : ['Azimpur', 'Nilkhet', 'New Market', 'City College', 'Kalabagan', 'Dhanmondi 32', 'Dhanmondi 27', 'Asad Gate',
            'College Gate', 'Shishu Mela', 'Shyamoli', 'Kallyanpur', 'Technical', 'Bangla College', 'Ansar Camp',
            'Mirpur 1', 'Mirpur 2', 'Proshika Mor', 'Rupnagar', 'Duaripara'],

        'Bikalpa Auto Service' : ['Motijheel', 'Gulistan', 'Paltan', 'Press Club', 'High Court', 'Motsho Bhaban', 'Shahbagh', 'Bangla Motor',
            'Kawran Bazar', 'Farmgate', 'Khamarbari', 'Agargaon', 'Taltola', 'Shewrapara', 'Kazipara', 'Mirpur 10',
            'Mirpur 11', 'Purobi', 'Pallabi', 'Mirpur 12'],

        'Bikash Paribahan' : ['Azimpur', 'Nilkhet', 'New Market', 'City College', 'Kalabagan', 'Dhanmondi 32', 'Dhanmondi 27',
            'Khamarbari', 'Bijoy Sarani', 'Jahangir Gate', 'Mohakhali', 'Banani', 'Kakoli', 'Staff Road', 'MES',
            'Sheora', 'Kuril Bishwa Road', 'Khilkhet', 'Airport', 'Jasimuddin', 'Rajlakshmi', 'Azampur',
            'House Building', 'Abdullahpur', 'Kamarpara', 'Dhour'],

        'Dewan' : ['Azimpur', 'New Market', 'City College', 'Science Lab', 'Kataban', 'Shahbagh', 'Bangla Motor',
            'Kawran Bazar', 'Farmgate', 'Bijoy Sarani', 'Jahangir Gate', 'Mohakhali', 'Wireless Mor', 'Gulshan 1',
            'Badda', 'Shahjadpur', 'Natun Bazar', 'Nadda', 'Bashundhara', 'Jamuna Future Park', 'Kuril Bishwa Road'],
        'Dhaka Chaka' : ['Police Plaza', 'Gulshan 1', 'Gulshan 2'],

        'Dhaka Chaka 2' : ['Banani', 'Gulshan 2', 'Kakoli', 'Natun Bazar'],

        'Dishari Paribahan' : ['Keraniganj', 'Babu Bazar', 'Naya Bazar', 'Golap Shah Mazar', 'GPO', 'Paltan', 'Press Club', 'High Court',
            'Motsho Bhaban', 'Shahbagh', 'Bangla Motor', 'Kawran Bazar', 'Farmgate', 'Khamarbari', 'Asad Gate',
            'College Gate', 'Shishu Mela', 'Shyamoli', 'Kallyanpur', 'Technical', 'Bangla College', 'Ansar Camp',
            'Mirpur 1', 'Chiriakhana'],

        'Green Dhaka' : ['Motijheel', 'Gulistan', 'GPO', 'Paltan', 'Kakrail', 'Shantinagar', 'Malibagh Mor', 'Mouchak',
            'Malibagh Railgate', 'Rampura', 'Merul', 'Madhya Badda', 'Badda', 'Uttar Badda', 'Shahjadpur', 'bashtola',
            'Natun Bazar', 'Nadda', 'Bashundhara', 'Kuril Bishwa Road', 'Khilkhet', 'Airport', 'Jasimuddin',
            'Rajlakshmi', 'Azampur', 'House Building', 'Abdullahpur'],

        'Himachol' : ['Metro Hall', 'Chashara', 'Shibu Market', 'Jalkuri', 'Sign Board', 'Matuail', 'Rayerbag', 'Shonir Akhra',
            'Jatrabari', 'Jonopath Mor', 'Gulistan', 'GPO', 'Paltan', 'Press Club', 'High Court', 'Motsho Bhaban',
            'Shahbagh', 'Bangla Motor', 'Kawran Bazar', 'Farmgate', 'Khamarbari', 'Agargaon', 'Taltola', 'Shewrapara',
            'Kazipara', 'Mirpur 10', 'Mirpur 11', 'Purobi', 'Pallabi', 'Mirpur 12'],

        'Khajababa Paribahan' : ['Jatrabari', 'Sayedabad', 'Gulistan', 'GPO', 'Paltan', 'Press Club', 'High Court', 'Motsho Bhaban',
            'Shahbagh', 'Bangla Motor', 'Kawran Bazar', 'Farmgate', 'Khamarbari', 'Agargaon', 'Taltola', 'Shewrapara',
            'Kazipara', 'Mirpur 10', 'Mirpur 11', 'Purobi', 'Pallabi', 'Mirpur 12'],

        'Labbaik Paribahan' : ['Sign Board', 'Matuail', 'Rayerbag', 'Shonir Akhra', 'Jatrabari', 'Jonopath Mor', 'Sayedabad', 'Manik Nagar',
            'Basabo', 'Khilgaon', 'Rajarbagh', 'Malibagh Mor', 'Mouchak', 'Moghbazar', 'Bangla Motor', 'Kawran Bazar',
            'Farmgate', 'Khamarbari', 'Asad Gate', 'College Gate', 'Shishu Mela', 'Shyamoli', 'Kallyanpur', 'Technical',
            'Gabtoli', 'Aminbazar', 'Hemayetpur', 'Savar'],

        'Shadhin Paribahan' : ['Staff Quarter', 'Demra', 'Banasree', 'Rampura', 'Malibagh Railgate', 'Mouchak', 'Moghbazar', 'Bangla Motor',
            'Kawran Bazar', 'Farmgate', 'Khamarbari', 'Asad Gate', 'Mohammadpur', 'Bosila'],

        'tanjil Paribahan' : ['Sadarghat', 'Ray Shaheb Bazar', 'Naya Bazar', 'Golap Shah Mazar', 'GPO', 'Paltan', 'Press Club',
            'High Court', 'Motsho Bhaban', 'Shahbagh', 'Bangla Motor', 'Kawran Bazar', 'Farmgate', 'Khamarbari',
            'Asad Gate', 'College Gate', 'Shishu Mela', 'Shyamoli', 'Kallyanpur', 'Technical', 'Ansar Camp', 'Mirpur 1',
            'Chiriakhana'],

        'Trust Transporot Services' : ['Mirpur DOHS', 'Kalshi', 'ECB Chottor', 'Garrison', 'Adamjee College', 'Workshop', 'Jahangir Gate',
            'Farmgate', 'Kawran Bazar', 'Bangla Motor', 'Shahbagh', 'High Court', 'Press Club', 'Paltan',
            'Daynik Bangla Mor', 'Motijheel'],

        'Welcome' : ['Gulistan', 'Paltan', 'Paltan', 'Press Club', 'High Court', 'Motsho Bhaban', 'Shahbagh', 'Bangla Motor',
            'Kawran Bazar', 'Farmgate', 'Khamarbari', 'Asad Gate', 'College Gate', 'Shishu Mela', 'Shyamoli',
            'Kallyanpur', 'Technical', 'Gabtoli', 'Aminbazar', 'Hemayetpur', 'Savar', 'Nandan Park'],

    }
    
    x = 0
    if source and destination:
        for i in dict:
            if source in dict[i] and destination in dict[i]:
                x+=1
                context[x] = i

    else:
        bus_name = source
        x = dict[bus_name]
        context = {i:x[i] for i in range(len(x))}

    return context



def bus_stopage_list():
    dict = {
        0: 'Abdullahpur', 1: 'Adabor', 2: 'Adamjee College', 3: 'Agargaon', 4: 'Airport', 5: 'Aminbazar',
        6: 'Ansar Camp', 7: 'Arambagh', 8: 'Asad Gate', 9: 'Ashulia Bazar', 10: 'Azampur', 11: 'Azimpur',
        12: 'Babu Bazar', 13: 'Badda', 14: 'Baipayl', 15: 'Balughat', 16: 'Kakoli', 17: 'Banani', 18: 'Banasree',
        19: 'Bangla College', 20: 'Bangla Motor', 21: 'Basabo', 22: 'Bashtola', 23: 'Bashundhara', 24: 'Bijoy Sarani',
        25: 'Bosila', 26: 'CMH', 27: 'Chairman Bari', 28: 'Chashara', 29: 'Chiriakhana', 30: 'City College',
        31: 'College Gate', 32: 'Darussalam', 33: 'Daynik Bangla Mor', 34: 'Demra', 35: 'Dhanmondi 27',
        36: 'Dhanmondi 32', 37: 'Dhour', 38: 'Diabari', 39: 'Duaripara', 40: 'ECB Chottor', 41: 'Fantasy Kingdom',
        42: 'Farmgate', 43: 'Fulbaria', 44: 'GPO', 45: 'Gabtoli', 46: 'Garrison', 47: 'Gazipur Chowrasta',
        48: 'Golap Shah Mazar', 49: 'Gulistan', 50: 'Gulshan 1', 51: 'Gulshan 2', 52: 'Gulshan Bridge',
        53: 'Hemayetpur', 54: 'High Court', 55: 'House Building', 56: 'Ittefaq', 57: 'Jahangir Gate', 58: 'Ittefaq',
        59: 'Jamgora', 60: 'Jamuna Future Park', 61: 'Japan Garden City', 62: 'Jasimuddin', 63: 'Jatrabari',
        64: 'Jonopath Mor', 65: 'Kakoli', 66: 'Kakrail', 67: 'Kalabagan', 68: 'Kallyanpur', 69: 'Kalshi',
        70: 'Kamalapur', 71: 'Kamarpara', 72: 'Kataban', 73: 'Kawran Bazar', 74: 'Kazipara', 75: 'Keraniganj',
        76: 'Khamarbari', 77: 'Khilgaon', 78: 'Khilkhet', 79: 'Kodomtoli', 80: 'Kuril Bishwa Road', 81: 'Link Road',
        82: 'MES', 83: 'Madhya Badda', 84: 'Malibagh Mor', 85: 'Malibagh Railgate', 86: 'Manik Nagar',
        87: 'Motsho Bhaban', 88: 'Matuail', 89: 'Matuail', 90: 'Merul', 91: 'Mirpur 1', 92: 'Mirpur 10',
        93: 'Mirpur 11', 94: 'Mirpur 12', 95: 'Mirpur 14', 96: 'Mirpur 2', 97: 'Mirpur DOHS', 98: 'Moghbazar',
        99: 'Mohakhali', 100: 'Mohammadpur', 101: 'Motijheel', 102: 'Motsho Bhaban', 103: 'Mouchak', 104: 'Mugdapara',
        105: 'Nabisco', 106: 'Nadda', 107: 'Nandan Park', 108: 'Natun Bazar', 109: 'Naya Bazar', 110: 'New Market',
        111: 'Nilkhet', 112: 'Pallabi', 113: 'Paltan', 114: 'Police Plaza', 115: 'Press Club', 116: 'Proshika Mor',
        117: 'Purobi', 118: 'Rajarbagh', 119: 'Rajlakshmi', 120: 'Rampura', 121: 'Rampura Bridge',
        122: 'Ray Shaheb Bazar', 123: 'Rampura', 124: 'Rampura Bridge', 125: 'Rayerbag', 126: 'Rupnagar',
        127: 'Sadarghat', 128: 'Satrasta', 129: 'Savar', 130: 'Sayedabad', 131: 'Science Lab', 132: 'Shahbagh',
        133: 'Shahzadpur', 134: 'Shantinagar', 135: 'Sheora', 136: 'Shewrapara', 137: 'Shia Masjid', 138: 'Shishu Mela',
        139: 'Shonir Akhra', 140: 'Shyamoli', 141: 'Signal', 142: 'Sony Hall', 143: 'Staff Quarter', 144: 'Staff Road',
        145: 'Station Road', 146: 'TT Para', 147: 'Taltola', 148: 'Technical', 149: 'Tongi', 150: 'Uttar Badda',
        151: 'Wireless Mor', 152: 'Workshop', 153: 'Zirabo',
    }
    return dict



if __name__ == "__main__":
    pass