from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
#def search(request):
#    return render(request,'user_info/user_info.html')

def index(request):
    return render(request,'index.html')

def user_signup(request):
    form = UserCreationForm()
    return render(request,'signup.html',{'signup':form})

def user_login(request) :
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username,password = password)
        if user:
            login(request,user)
            return render(request,'thank you.html')
        else :
            return HttpResponse("Username or Password Incorrect")
    return render(request,'login.html')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('login')

def bus(source,destination):
    context = {  }
    key = 0
    airport_to_bangabandhu_avenue = [ 'Fulbaria', 'Golap Shah Mazar', 'GPO','Paltan', 'Press Club', 'High Court', 'Motsho Bhaban', 'Shahbagh',
                'Bangla Motor','Kawran Bazar', 'Farmgate', 'Bijoy Sarani', 'Jahangir Gate', 'Mohakhali', 'Banani','Kakoli', 'Staff Road', 'MES',
                'Sheora','Kuril Bishwa Road', 'Khilkhet', 'Airport','Jasimuddin', 'Rajlakshmi', 'Azampur', 'House Building', 'Abdullahpur']
    x = 0
    y = 0
    for i in range(len(airport_to_bangabandhu_avenue)):
        if (airport_to_bangabandhu_avenue[i] == source):
            x = 1
        if (airport_to_bangabandhu_avenue[i] == destination):
            y = 1
    if (x == 1) and (y == 1):
        key= key+1
        context[key] = ' Airport To Bangabandhu Avenue Paribohon '

    brtc = ['Motijheel', 'Gulistan', 'GPO', 'Paltan', 'Press Club', 'High Court', 'Motsho Bhaban', 'Shahbagh','Bangla Motor', 'Kawran Bazar',
                'Farmgate', 'Bijoy Sarani', 'Jahangir Gate', 'Mohakhali', 'Banani', 'Kakoli','Staff Road', 'MES', 'Sheora', 'Kuril Bishwa Road', 'Khilkhet',
                'Airport', 'Jasimuddin', 'Rajlakshmi','Azampur', 'House Building', 'Abdullahpur', 'Tongi']
    x = 0
    y = 0
    for i in range(len(brtc)):
        if (brtc[i] == source):
            x = 1
        if (brtc[i] == destination):
            y = 1
    if (x == 1) and (y == 1):
        key= key+1
        context[key] = ' BRTC Bus Service'

    vip27 = ['Azimpur', 'Nilkhet', 'New Market', 'City College', 'Kalabagan', 'Dhanmondi 32', 'Dhanmondi 27', 'Khamarbari','Bijoy Sarani', 'Jahangir Gate',
                'Mohakhali', 'Banani', 'Kakoli', 'Staff Road', 'MES', 'Sheora','Kuril Bishwa Road', 'Khilkhet', 'Airport', 'Jasimuddin', 'Rajlakshmi', 'Azampur',
                'House Building','Abdullahpur', 'Tongi', 'Station Road', 'Mill gate', 'Board Bazar', 'Gazipur Chowrasta']
    x = 0
    y = 0
    for i in range(len(vip27)):
        if (vip27[i] == source):
            x = 1
        if (vip27[i] == destination):
            y = 1
    if (x == 1) and (y == 1):
        key= key+1
        context[key] = ' VIP 27 Paribahan'

    victor_classic = ['Sadarghat', 'Ray Shaheb Bazar', 'Naya Bazar', 'Golap Shah Mazar', 'GPO', 'Paltan', 'Kakrail', 'Shantinagar','Malibagh Mor',
                'Mouchak', 'Malibagh Railgate', 'Rampura', 'Merul', 'Madhya Badda', 'Badda','Uttar Badda', 'Shahjadpur', 'bashtola', 'Natun Bazar', 'Nadda',
                'Bashundhara', 'Kuril Bishwa Road','Khilkhet', 'Airport', 'Jasimuddin', 'Rajlakshmi', 'Azampur', 'House Building', 'Diabari']
    x = 0
    y = 0
    for i in range(len(victor_classic)):
        if (victor_classic[i] == source):
            x = 1
        if (victor_classic[i] == destination):
            y = 1
    if (x == 1) and (y == 1):
        key= key+1
        context[key] = ' Victor Classic '

    victor_paribahan = ['Sadarghat', 'Ray Shaheb Bazar', 'Naya Bazar', 'Golap Shah Mazar', 'GPO', 'Paltan', 'Kakrail', 'Shantinagar','Malibagh Mor',
                'Mouchak', 'Malibagh Railgate', 'Rampura', 'Merul', 'Madhya Badda', 'Badda','Uttar Badda', 'Shahjadpur', 'bashtola', 'Natun Bazar', 'Nadda',
                'Bashundhara', 'Kuril Bishwa Road','Khilkhet', 'Airport', 'Jasimuddin', 'Rajlakshmi', 'Azampur', 'House Building', 'Diabari']
    x = 0
    y = 0
    for i in range(len(victor_paribahan)):
        if (victor_paribahan[i] == source):
            x = 1
        if (victor_paribahan[i] == destination):
            y = 1
    if (x == 1) and (y == 1):
        key= key+1
        context[key] = ' Victor Paribahan '

    ramzan = ['Gabtoli', 'Technical', 'Kallyanpur', 'Shyamoly', 'Shishu Mela', 'College Gate', 'Asad Gate', 'Mohammadpur','Shankar', 'Star kabab',
                'Dhanmondi 15', 'Jigatola', 'City College', 'Science Lab', 'Bata Signal','Kataban', 'Shahbagh', 'Motsho Bhaban', 'Kakrail', 'Shantinagar', 'Mouchak',
                'Malibagh Railgate','Rampura', 'Banasree', 'Staff Quarter' ]
    x = 0
    y = 0
    for i in range(len(ramzan)):
        if (ramzan[i] == source):
            x = 1
        if (ramzan[i] == destination):
            y = 1
    if (x == 1) and (y == 1):
        key= key+1
        context[key] = ' Ramzan Paribahanon '

    achim = [ 'Gabtoli' , 'Technical' , 'Ansar Camp' , 'Mirpur 1' , 'Sony Hall' , 'Mirpur 2' , 'Mirpur 10' , 'Mirpur 11' , 'Purobi' , 'Kalshi' ,
                'ECB Chottor' , 'MES' ,'Sheora' , 'Kuril Bishwa Road' , 'Bashundhara' , 'Jamuna Future Park' , 'Nadda' , 'Natun Bazar' ,'Bashtola' ,'Shahjadpur',
                'Uttar Badda' , 'Badda' , 'Madhya Badda' ,'Merul' , 'Rampura' , 'Banasree' , 'Meradia bazar' ,'Staff Quarter' ]
    x = 0
    y = 0
    for i in range(len(achim)):
        if (achim[i] == source):
            x = 1
        if (achim[i] == destination):
            y = 1
    if (x == 1) and (y == 1):
        key= key+1
        context[key] = ' Achim Paribahan '

    bus_6_no = ['Kamalapur', 'Motijheel', 'Gulistan', 'GPO', 'Paltan', 'Kakrail', 'Shantinagar','Malibagh Mor', 'Mouchak', 'Moghbazar', 'Bangla Motor',
                'Kawran Bazar', 'Farmgate','Bijoy Sarani', 'Jahangir Gate', 'Mohakhali', 'Wireless Mor', 'Gulshan 1', 'Gulshan 2','Natun Bazar']
    x = 0
    y = 0
    for i in range(len(bus_6_no)):
        if (bus_6_no[i] == source):
            x = 1
        if (bus_6_no[i] == destination):
            y = 1
    if (x == 1) and (y == 1):
        key = key + 1
        context[key] = ' 6_no Bus'

    bus_8_no = ['Jatrabari', 'Jonopath Mor', 'Sayedabad', 'Motijheel', 'Daynik Bangla Mor','Paltan', 'Press Club', 'High Court', 'Shahbaghh', 'Bangla Motor',
                'Kawran Bazar','Farmgate', 'Khamarbari', 'Asad Gate', 'College Gate', 'Shishu Mela', 'Shyamoli','Kallyanpur', 'Technical', 'Gabtoli']
    x = 0
    y = 0
    for i in range(len(bus_8_no)):
        if (bus_8_no[i] == source):
            x = 1
        if (bus_8_no[i] == destination):
            y = 1
    if (x == 1) and (y == 1):
        key = key + 1
        context[key] = ' 8_no '

    Agradut_Boishakhi = ['Natun Bazar', 'Bashtola', 'Shajadpur', 'Badda', 'Gulshan 1', 'Gulshan Bridge','Wireless Mor', 'Mohakhali', 'Jahangir Gate',
                'Bijoy Sarani', 'Agargaon', 'Shishu Mela','Shyamoli','Kallyanpur', 'Technical', 'Gabtoli'  'Hemayetpur', 'Savar']
    x = 0
    y = 0
    for i in range(len(Agradut_Boishakhi)):
        if (Agradut_Boishakhi[i] == source):
            x = 1
        if (Agradut_Boishakhi[i] == destination):
            y = 1
    if (x == 1) and (y == 1):
        key = key + 1
        context[key] = ' Agradut Boishakhi '

    Akash_paribahan = ['Kodomtoli', 'Keraniganj', 'Babu Bazar', 'Naya Bazar', 'Golap Shah Mazar','GPO', 'Paltan', 'Kakrail', 'Shantinagar', 'Malibagh Mor',
                'Mouchak', 'Malibagh Railgate','Rampura', 'Merul', 'Madhya Badda', 'Badda', 'Uttar Badda', 'Shahjadpur', 'bashtola','Natun Bazar', 'Nadda',
                'Bashundhara', 'Kuril Bishwa Road', 'Khilkhet', 'Airport', 'Jasimuddin','Rajlakshmi', 'Azampur', 'House Building', 'Diabari']
    x = 0
    y = 0
    for i in range(len(Akash_paribahan)):
        if (Akash_paribahan[i] == source):
            x = 1
        if (Akash_paribahan[i] == destination):
            y = 1
    if (x == 1) and (y == 1):
        key = key + 1
        context[key] = ' Akash Paribahan '

    Akik_paribahan = ['Gabtoli', 'Technical', 'Ansar Camp', 'Mirpur 1', 'Sony Hall', 'Mirpur 2','Mirpur 10', 'Mirpur 11', 'Purobi', 'Kalshi', 'ECB Chottor',
                'MES', 'Sheora', 'Kuril Bishwa Road','Bashundhara', 'Jamuna Future Park', 'Nadda', 'Natun Bazar', 'Bashtola', 'Shahjadpur', 'Uttar Badda']
    x = 0
    y = 0
    for i in range(len(Akik_paribahan)):
        if (Akik_paribahan[i] == source):
            x = 1
        if (Akik_paribahan[i] == destination):
            y = 1
    if (x == 1) and (y == 1):
        key = key + 1
        context[key] = ' Akik Paribahan '

    Al_Makka_Transport = ['Motijheel', 'Gulistan', 'GPO', 'Paltan', 'Kakrail', 'Shantinagar','Malibagh Mor', 'Mouchak', 'Moghbazar', 'Nabisco', 'Mohakhali',
                'Chairman Bari', 'Kakoli','Banani', 'ECB Chottor', 'Kalshi', 'Purobi', 'Mirpur 10', 'Mirpur 2', 'Mirpur 1']
    x = 0
    y = 0
    for i in range(len(Al_Makka_Transport)):
        if (Al_Makka_Transport[i] == source):
            x = 1
        if (Al_Makka_Transport[i] == destination):
            y = 1
    if (x == 1) and (y == 1):
        key = key + 1
        context[key] = ' Akash Paribahan '

    Alif_Enterprise = ['Mirpur 1', 'Mirpur 2', 'Sony Hall', 'Mirpur 10', 'Kazipara', 'Shewrapara','Agargaon', 'Bijoy Sarani', 'Jahangir Gate', 'Mohakhali',
                'Wireless Mor', 'Gulshan 1', 'Badda','Rampura Bridge', 'Banasree']
    x = 0
    y = 0
    for i in range(len(Alif_Enterprise)):
        if (Alif_Enterprise[i] == source):
            x = 1
        if (Alif_Enterprise[i] == destination):
            y = 1
    if (x == 1) and (y == 1):
        key = key + 1
        context[key] = ' Alif Enterprise '

    Alif_Enterprise_2 = ['Shia Masjid', 'Japan Garden City', 'Adabor', 'Shyamoli', 'Shishu Mela','Agargaon', 'Ziya Uddan', 'Bijoy Sarani', 'Jahangir Gate',
                'Mohakhali', 'Wireless Mor','Gulshan 1', 'Link Road', 'Badda', 'Madhya Badda', 'Merul', 'Rampura', 'Banasree']
    x = 0
    y = 0
    for i in range(len(Alif_Enterprise_2)):
        if (Alif_Enterprise_2[i] == source):
            x = 1
        if (Alif_Enterprise_2[i] == destination):
            y = 1
    if (x == 1) and (y == 1):
        key = key + 1
        context[key] = ' Alif Enterprise 2'

    Alif_Enterprise_3 = ['Shia Masjid', 'Japan Garden City', 'Adabor', 'Shyamoli', 'Shishu Mela','Agargaon', 'Ziya Uddan', 'Bijoy Sarani', 'Jahangir Gate',
                'Mohakhali', 'Chairman Bari','Kakoli', 'Banani', 'Staff Road', 'MES', 'Sheora', 'Kuril Bishwa Road', 'Khilkhet', 'Airport','Jasimuddin', 'Rajlakshmi',
                'Azampur', 'House Building', 'Abdullahpur']
    x = 0
    y = 0
    for i in range(len(Alif_Enterprise_3)):
        if (Alif_Enterprise_3[i] == source):
            x = 1
        if (Alif_Enterprise_3[i] == destination):
            y = 1
    if (x == 1) and (y == 1):
        key = key + 1
        context[key] = ' Alif Enterprise 3'

    Bhuiyan_Paribahan = ['Shia Masjid', 'Japan Garden City', 'Adabor', 'Shyamoli', 'Shishu Mela','Agargaon', 'Ziya Uddan', 'Bijoy Sarani', 'Jahangir Gate',
                'Mohakhali', 'Chairman Bari','Kakoli', 'Banani', 'Staff Road', 'MES', 'Sheora', 'Kuril Bishwa Road', 'Khilkhet', 'Airport','Jasimuddin', 'Rajlakshmi',
                'Azampur', 'House Building', 'Abdullahpur']
    x = 0
    y = 0
    for i in range(len(Bhuiyan_Paribahan)):
        if (Bhuiyan_Paribahan[i] == source):
            x = 1
        if (Bhuiyan_Paribahan[i] == destination):
            y = 1
    if (x == 1) and (y == 1):
        key = key + 1
        context[key] = ' Bhuiyan Paribahan '

    Alike = ['Balughat', 'Signal', 'CMH', 'Garrison', 'Adamjee College', 'Workshop', 'Jahangir Gate','Farmgate', 'Kawran Bazar']
    x = 0
    y = 0
    for i in range(len(Alike)):
        if (Alike[i] == source):
            x = 1
        if (Alike[i] == destination):
            y = 1
    if (x == 1) and (y == 1):
        key = key + 1
        context[key] = ' Alaik Paribahan '

    Ashulia_Classic = ['Satrasta', 'Nabisco', 'Mohakhali', 'Chairman Bari', 'Kakoli', 'Banani','Staff Road', 'MES', 'Sheora', 'Kuril Bishwa Road',
                'Khilkhet', 'Airport', 'Jasimuddin','Rajlakshmi','Azampur', 'House Building', 'Abdullahpur', 'Kamarpara', 'Ashulia Bazar', 'Zirabo','Fantasy Kingdom',
                'Jamgora', 'Baipayl', 'Nobinagar']
    x = 0
    y = 0
    for i in range(len(Ashulia_Classic)):
        if (Ashulia_Classic[i] == source):
            x = 1
        if (Ashulia_Classic[i] == destination):
            y = 1
    if (x == 1) and (y == 1):
        key = key + 1
        context[key] = ' Ashulia Classic '

    Ayat = ['Kamalapur', 'Rajarbagh', 'Malibagh Mor', 'Mouchak', 'Moghbazar', 'Bangla Motor','Kawran Bazar', 'Farmgate', 'Khamarbari', 'Agargaon',
                'Taltola', 'Shewrapara', 'Kazipara','Mirpur 10', 'Mirpur 2', 'Sony Hall', 'Chiriakhana']
    x = 0
    y = 0
    for i in range(len(Ayat)):
        if (Ayat[i] == source):
            x = 1
        if (Ayat[i] == destination):
            y = 1
    if (x == 1) and (y == 1):
        key = key + 1
        context[key] = ' Ayat Paribahan '

    brtc2 = ['Mohammadpur', 'Asad Gate', 'Khamarbari', 'Farmgate', 'Bijoy Sarani', 'Jahangir Gate','Mohakhali', 'Wireless Mor', 'Gulshan 1', 'Natun Bazar',
                'Badda', 'Uttar Badda', 'Shahjadpur','bashtola', 'Natun Bazar', 'Nadda', 'Bashundhara', 'Kuril Bishwa Road']
    x = 0
    y = 0
    for i in range(len(brtc2)):
        if (brtc2[i] == source):
            x = 1
        if (brtc2[i] == destination):
            y = 1
    if (x == 1) and (y == 1):
        key = key + 1
        context[key] = ' BRTC Bus Service 2'

    Bahon = ['Mirpur 14', 'Mirpur 10', 'Mirpur 2', 'Mirpur 1', 'Ansar Camp', 'Bangla College', 'Technical','Darussalam', 'Kallyanpur', 'Shyamoli',
                'Shishu Mela', 'College Gate', 'Asad Gate', 'Dhanmondi 27','Dhanmondi 32', 'Kalabagan', 'Science Lab', 'Kataban', 'Shahbagh', 'High Court',
                'Press Club', 'Paltan','Daynik Bangla Mor', 'Motijheel', 'Arambagh', 'Kamalapur', 'Mugdapara', 'Basabo', 'Khilgaon']
    x = 0
    y = 0
    for i in range(len(Bahon)):
        if (Bahon[i] == source):
            x = 1
        if (Bahon[i] == destination):
            y = 1
    if (x == 1) and (y == 1):
        key = key + 1
        context[key] = ' Bahon Paribahan '

    Balaka_Paribahan = ['Sayedabad', 'Manik Nagar', 'TT Para', 'Kamalapur', 'Malibagh', 'Mouchak', 'Moghbazar','Satrasta', 'Nabisco', 'Mohakhali',
                'Chairman Bari', 'Kakoli', 'Banani', 'Staff Road', 'MES','Sheora', 'Kuril Bishwa Road', 'Khilkhet', 'Airport', 'Jasimuddin', 'Rajlakshmi',
                'Azampur','House Building', 'Abdullahpur', 'Tongi', 'Gazipur Chowrasta']
    x = 0
    y = 0
    for i in range(len(Balaka_Paribahan)):
        if (Balaka_Paribahan[i] == source):
            x = 1
        if (Balaka_Paribahan[i] == destination):
            y = 1
    if (x == 1) and (y == 1):
        key = key + 1
        context[key] = ' Balaka Paribahan '

    Basumati_Transport = ['Gabtoli', 'Technical', 'Ansar Camp', 'Mirpur 1', 'Sony Hall', 'Mirpur 2','Mirpur 10', 'Mirpur 11', 'Purobi', 'Kalshi',
                'ECB Chottor', 'MES', 'Sheora', 'Kuril Bishwa Road','Khilkhet', 'Airport', 'Jasimuddin', 'Rajlakshmi', 'Azampur', 'House Building',
                'Abdullahpur','Tongi','Gazipur Chowrasta']
    x = 0
    y = 0
    for i in range(len(Basumati_Transport)):
        if (Basumati_Transport[i] == source):
            x = 1
        if (Basumati_Transport[i] == destination):
            y = 1
    if (x == 1) and (y == 1):
        key = key + 1
        context[key] = ' Basumati Transport '

    Best_Transport = ['Jatrabari', 'Sayedabad', 'Ittefaq', 'Motijheel', 'Daynik Bangla Mor', 'Paltan','Press Club', 'High Court', 'Motsho Bhaban',
                'Shahbagh', 'Bangla Motor', 'Kawran Bazar', 'Farmgate','Khamarbari', 'Agargaon', 'Taltola', 'Shewrapara', 'Kazipara', 'Mirpur 10']
    x = 0
    y = 0
    for i in range(len(Best_Transport)):
        if (Best_Transport[i] == source):
            x = 1
        if (Best_Transport[i] == destination):
            y = 1
    if (x == 1) and (y == 1):
        key = key + 1
        context[key] = ' Best Transport '

    Bihanga_paribahan = ['Sadarghat', 'Ray Shaheb Bazar', 'Naya Bazar', 'Golap Shah Mazar', 'GPO', 'Paltan', 'Press Club','High Court', 'Motsho Bhaban',
                'Shahbagh', 'Bangla Motor', 'Kawran Bazar', 'Farmgate', 'Khamarbari','Agargaon', 'Taltola', 'Shewrapara', 'Kazipara', 'Mirpur 10', 'Mirpur 11',
                'Purobi', 'Pallabi','Duaripara']
    x = 0
    y = 0
    for i in range(len(Bihanga_paribahan)):
        if (Bihanga_paribahan[i] == source):
            x = 1
        if (Bihanga_paribahan[i] == destination):
            y = 1
    if (x == 1) and (y == 1):
        key = key + 1
        context[key] = ' Bihanga Paribahan '

    Bihanga_Paribahan_2 = ['Azimpur', 'Nilkhet', 'New Market', 'City College', 'Kalabagan', 'Dhanmondi 32','Dhanmondi 27', 'Asad Gate', 'College Gate',
                'Shishu Mela', 'Shyamoli', 'Kallyanpur','Technical','Bangla College', 'Ansar Camp', 'Mirpur 1', 'Mirpur 2', 'Proshika Mor', 'Rupnagar', 'Duaripara']
    x = 0
    y = 0
    for i in range(len(Bihanga_Paribahan_2)):
        if (Bihanga_Paribahan_2[i] == source):
            x = 1
        if (Bihanga_Paribahan_2[i] == destination):
            y = 1
    if (x == 1) and (y == 1):
        key = key + 1
        context[key] = ' Bihanga Paribahan 2'

    Bikalpa_Auto_service = ['Motijheel', 'Gulistan', 'Paltan', 'Press Club', 'High Court', 'Motsho Bhaban','Shahbagh', 'Bangla Motor', 'Kawran Bazar', 'Farmgate',
                'Khamarbari', 'Agargaon', 'Taltola','Shewrapara','Kazipara', 'Mirpur 10', 'Mirpur 11', 'Purobi', 'Pallabi', 'Mirpur 12']
    x = 0
    y = 0
    for i in range(len(Bikalpa_Auto_service)):
        if (Bikalpa_Auto_service[i] == source):
            x = 1
        if (Bikalpa_Auto_service[i] == destination):
            y = 1
    if (x == 1) and (y == 1):
        key = key + 1
        context[key] = ' Bikalpa Auto Service '

    Bikash_Paribahan = ['Azimpur', 'Nilkhet', 'New Market', 'City College', 'Kalabagan', 'Dhanmondi 32', 'Dhanmondi 27','Khamarbari', 'Bijoy Sarani', 'Jahangir Gate',
                'Mohakhali', 'Banani', 'Kakoli', 'Staff Road', 'MES','Sheora','Kuril Bishwa Road', 'Khilkhet', 'Airport', 'Jasimuddin', 'Rajlakshmi', 'Azampur',
                'House Building','Abdullahpur', 'Kamarpara', 'Dhour']
    x = 0
    y = 0
    for i in range(len(Bikash_Paribahan)):
        if (Bikash_Paribahan[i] == source):
            x = 1
        if (Bikash_Paribahan[i] == destination):
            y = 1
    if (x == 1) and (y == 1):
        key = key + 1
        context[key] = ' Bikash Paribahan '

    dewan = ['Azimpur', 'New Market', 'City College', 'Science Lab', 'Kataban', 'Shahbagh', 'Bangla Motor','Kawran Bazar', 'Farmgate', 'Bijoy Sarani', 'Jahangir Gate',
                'Mohakhali', 'Wireless Mor','Gulshan 1', 'Badda', 'Shahjadpur', 'Natun Bazar', 'Nadda', 'Bashundhara', 'Jamuna Future Park','Kuril Bishwa Road']
    x = 0
    y = 0
    for i in range(len(dewan)):
        if (dewan[i] == source):
            x = 1
        if (dewan[i] == destination):
            y = 1
    if (x == 1) and (y == 1):
        key = key + 1
        context[key] = ' Dewan '

    Dhaka_chaka_1 = ['Police Plaza', 'Gulshan 1', 'Gulshan 2']
    x = 0
    y = 0
    for i in range(len(Dhaka_chaka_1)):
        if (Dhaka_chaka_1[i] == source):
            x = 1
        if (Dhaka_chaka_1[i] == destination):
            y = 1
    if (x == 1) and (y == 1):
        key = key + 1
        context[key] = ' Dhaka Chaka '

    Dhaka_chaka_2 = ['Banani', 'Gulshan 2', 'Natun Bazar']
    x = 0
    y = 0
    for i in range(len(Dhaka_chaka_2)):
        if (Dhaka_chaka_2[i] == source):
            x = 1
        if (Dhaka_chaka_2[i] == destination):
            y = 1
    if (x == 1) and (y == 1):
        key = key + 1
        context[key] = ' Dhaka Chaka 2'

    Dishari_Paribahan = ['Keraniganj', 'Babu Bazar', 'Naya Bazar', 'Golap Shah Mazar', 'GPO','Paltan', 'Press Club', 'High Court', 'Motsho Bhaban', 'Shahbagh',
                'Bangla Motor', 'Kawran Bazar','Farmgate', 'Khamarbari', 'Asad Gate', 'College Gate', 'Shishu Mela', 'Shyamoli', 'Kallyanpur','Technical',
                'Bangla College', 'Ansar Camp', 'Mirpur 1', 'Chiriakhana']
    x = 0
    y = 0
    for i in range(len(Dishari_Paribahan)):
        if (Dishari_Paribahan[i] == source):
            x = 1
        if (Dishari_Paribahan[i] == destination):
            y = 1
    if (x == 1) and (y == 1):
        key = key + 1
        context[key] = ' Dishari Paribahan '

    Green_Dhaka = ['Motijheel', 'Gulistan', 'GPO', 'Paltan', 'Kakrail', 'Shantinagar','Malibagh Mor', 'Mouchak', 'Malibagh Railgate', 'Rampura', 'Merul',
                'Madhya Badda', 'Badda','Uttar Badda', 'Shahjadpur', 'bashtola', 'Natun Bazar', 'Nadda', 'Bashundhara', 'Kuril Bishwa Road','Khilkhet', 'Airport',
                'Jasimuddin', 'Rajlakshmi', 'Azampur', 'House Building', 'Abdullahpur']
    x = 0
    y = 0
    for i in range(len(Green_Dhaka)):
        if (Green_Dhaka[i] == source):
            x = 1
        if (Green_Dhaka[i] == destination):
            y = 1
    if (x == 1) and (y == 1):
        key = key + 1
        context[key] = ' Green Dhaka '

    Himachol = ['Metro Hall', 'Chashara', 'Shibu Market', 'Jalkuri', 'Sign Board', 'Matuail', 'Rayerbag','Shonir Akhra', 'Jatrabari', 'Jonopath Mor', 'Gulistan',
                'GPO', 'Paltan', 'Press Club', 'High Court','Motsho Bhaban', 'Shahbagh', 'Bangla Motor', 'Kawran Bazar', 'Farmgate', 'Khamarbari', 'Agargaon','Taltola',
                'Shewrapara', 'Kazipara', 'Mirpur 10', 'Mirpur 11', 'Purobi', 'Pallabi', 'Mirpur 12']
    x = 0
    y = 0
    for i in range(len(Himachol)):
        if (Himachol[i] == source):
            x = 1
        if (Himachol[i] == destination):
            y = 1
    if (x == 1) and (y == 1):
        key = key + 1
        context[key] = ' Himachol '

    Khajababa_Paribahan = ['Jatrabari', 'Sayedabad', 'Gulistan', 'GPO', 'Paltan', 'Press Club', 'High Court','Motsho Bhaban', 'Shahbagh', 'Bangla Motor',
                'Kawran Bazar', 'Farmgate', 'Khamarbari', 'Agargaon','Taltola', 'Shewrapara', 'Kazipara', 'Mirpur 10', 'Mirpur 11', 'Purobi', 'Pallabi', 'Mirpur 12']
    x = 0
    y = 0
    for i in range(len(Khajababa_Paribahan)):
        if (Khajababa_Paribahan[i] == source):
            x = 1
        if (Khajababa_Paribahan[i] == destination):
            y = 1
    if (x == 1) and (y == 1):
        key = key + 1
        context[key] = ' Khajababa Paribahan '

    Labbaik = ['Sign Board', 'Matuail', 'Rayerbag', 'Shonir Akhra', 'Jatrabari', 'Jonopath Mor', 'Sayedabad','Manik Nagar', 'Basabo', 'Khilgaon', 'Rajarbagh',
                'Malibagh Mor', 'Mouchak', 'Moghbazar', 'Bangla Motor','Kawran Bazar', 'Farmgate', 'Khamarbari', 'Asad Gate', 'College Gate', 'Shishu Mela', 'Shyamoli',
                'Kallyanpur', 'Technical', 'Gabtoli', 'Aminbazar', 'Hemayetpur', 'Savar']
    x = 0
    y = 0
    for i in range(len(Labbaik)):
        if (Labbaik[i] == source):
            x = 1
        if (Labbaik[i] == destination):
            y = 1
    if (x == 1) and (y == 1):
        key = key + 1
        context[key] = ' Labbaik Paribahan '

    Shadhin = ['Staff Quarter', 'Demra', 'Banasree', 'Rampura', 'Malibagh Railgate', 'Mouchak', 'Moghbazar','Bangla Motor', 'Kawran Bazar', 'Farmgate', 'Khamarbari',
                'Asad Gate', 'Mohammadpur', 'Bosila']
    x = 0
    y = 0
    for i in range(len(Shadhin)):
        if (Shadhin[i] == source):
            x = 1
        if (Shadhin[i] == destination):
            y = 1
    if (x == 1) and (y == 1):
        key = key + 1
        context[key] = ' Shadhin Paribahan '

    Tanjil = ['Sadarghat', 'Ray Shaheb Bazar', 'Naya Bazar', 'Golap Shah Mazar', 'GPO', 'Paltan', 'Press Club','High Court', 'Motsho Bhaban', 'Shahbagh',
                'Bangla Motor', 'Kawran Bazar', 'Farmgate', 'Khamarbari','Asad Gate', 'College Gate', 'Shishu Mela', 'Shyamoli', 'Kallyanpur', 'Technical',
                'Ansar Camp','Mirpur 1', 'Chiriakhana']
    x = 0
    y = 0
    for i in range(len(Tanjil)):
        if (Tanjil[i] == source):
            x = 1
        if (Tanjil[i] == destination):
            y = 1
    if (x == 1) and (y == 1):
        key = key + 1
        context[key] = ' tanjil Paribahan '

    Trust_Transport_Services = ['Mirpur DOHS', 'Kalshi', 'ECB Chottor', 'Garrison', 'Adamjee College','Workshop', 'Jahangir Gate', 'Farmgate', 'Kawran Bazar',
                'Bangla Motor', 'Shahbagh','High Court','Press Club', 'Paltan', 'Daynik Bangla Mor', 'Motijheel']
    x = 0
    y = 0
    for i in range(len(Trust_Transport_Services)):
        if (Trust_Transport_Services[i] == source):
            x = 1
        if (Trust_Transport_Services[i] == destination):
            y = 1
    if (x == 1) and (y == 1):
        key = key + 1
        context[key] = ' Trust Transporot Services '

    Welcome = ['Gulistan', 'Paltan', 'Paltan', 'Press Club', 'High Court', 'Motsho Bhaban', 'Shahbagh', 'Bangla Motor','Kawran Bazar', 'Farmgate', 'Khamarbari',
                'Asad Gate', 'College Gate', 'Shishu Mela', 'Shyamoli','Kallyanpur','Technical', 'Gabtoli', 'Aminbazar', 'Hemayetpur', 'Savar', 'Nandan Park']
    x = 0
    y = 0
    for i in range(len(Welcome)):
        if (Welcome[i] == source):
            x = 1
        if (Welcome[i] == destination):
            y = 1
    if (x == 1) and (y == 1):
        key = key + 1
        context[key] = ' Welcome '
    return context

def show_user_info(request) :
    source = ''
    destination = ''
    context = {  }
    #key = 0
    if (request.method == 'POST') :
        source = request.POST['source']
        destination = request.POST['destination']
        context = bus(source,destination)
    

    return render(request,'bus_info.html', {'context' : context})






def show_bus_info(request,bus_name) :

    

    
    context = {}
    arr = []
    if (bus_name == 'Airport To Bangabandhu Avenue Paribohon'):
        arr =  ['Fulbaria', 'Golap Shah Mazar', 'GPO','Paltan', 'Press Club', 'High Court', 'Motsho Bhaban', 'Shahbagh', 'Bangla Motor','Kawran Bazar',
                'Farmgate', 'Bijoy Sarani', 'Jahangir Gate', 'Mohakhali', 'Banani','Kakoli', 'Staff Road', 'MES', 'Sheora', 'Kuril Bishwa Road', 'Khilkhet',
                'Airport','Jasimuddin', 'Rajlakshmi', 'Azampur', 'House Building', 'Abdullahpur']
        for i in range(len(arr)) :
            context[i] = arr[i]

    elif (bus_name == 'BRTC Bus Service'):
        arr =  ['Motijheel', 'Gulistan', 'GPO', 'Paltan', 'Press Club', 'High Court', 'Motsho Bhaban', 'Shahbagh','Bangla Motor', 'Kawran Bazar', 'Farmgate',
                'Bijoy Sarani', 'Jahangir Gate', 'Mohakhali', 'Banani', 'Kakoli','Staff Road', 'MES', 'Sheora', 'Kuril Bishwa Road', 'Khilkhet', 'Airport',
                'Jasimuddin', 'Rajlakshmi','Azampur', 'House Building', 'Abdullahpur', 'Tongi']
        for i in range(len(arr)) :
            context[i] = arr[i]

    elif (bus_name == 'VIP 27 Paribahan'):
        arr =  ['Azimpur', 'Nilkhet', 'New Market', 'City College', 'Kalabagan', 'Dhanmondi 32', 'Dhanmondi 27', 'Khamarbari','Bijoy Sarani', 'Jahangir Gate',
                'Mohakhali', 'Banani', 'Kakoli', 'Staff Road', 'MES', 'Sheora','Kuril Bishwa Road', 'Khilkhet', 'Airport', 'Jasimuddin', 'Rajlakshmi', 'Azampur',
                'House Building','Abdullahpur', 'Tongi', 'Station Road', 'Mill gate', 'Board Bazar', 'Gazipur Chowrasta']
        for i in range(len(arr)) :
            context[i] = arr[i]

    elif (bus_name == 'Victor Classic'):
        arr =  ['Sadarghat', 'Ray Shaheb Bazar', 'Naya Bazar', 'Golap Shah Mazar', 'GPO', 'Paltan', 'Kakrail', 'Shantinagar','Malibagh Mor', 'Mouchak',
                'Malibagh Railgate', 'Rampura', 'Merul', 'Madhya Badda', 'Badda','Uttar Badda', 'Shahjadpur', 'bashtola', 'Natun Bazar', 'Nadda', 'Bashundhara',
                'Kuril Bishwa Road','Khilkhet', 'Airport', 'Jasimuddin', 'Rajlakshmi', 'Azampur', 'House Building', 'Diabari']
        for i in range(len(arr)) :
            context[i] = arr[i]

    elif (bus_name == 'Victor Paribahan'):
        arr =  ['Sadarghat', 'Ray Shaheb Bazar', 'Naya Bazar', 'Golap Shah Mazar', 'GPO', 'Paltan', 'Kakrail', 'Shantinagar','Malibagh Mor', 'Mouchak',
                'Malibagh Railgate', 'Rampura', 'Merul', 'Madhya Badda', 'Badda','Uttar Badda', 'Shahjadpur', 'bashtola', 'Natun Bazar', 'Nadda', 'Bashundhara',
                'Kuril Bishwa Road','Khilkhet', 'Airport', 'Jasimuddin', 'Rajlakshmi', 'Azampur', 'House Building', 'Diabari']
        for i in range(len(arr)) :
            context[i] = arr[i]

    elif (bus_name == 'Ramzan Paribahanon'):
        arr =  ['Gabtoli', 'Technical', 'Kallyanpur', 'Shyamoly', 'Shishu Mela', 'College Gate', 'Asad Gate', 'Mohammadpur','Shankar', 'Star kabab',
                'Dhanmondi 15', 'Jigatola', 'City College', 'Science Lab', 'Bata Signal','Kataban', 'Shahbagh', 'Motsho Bhaban', 'Kakrail', 'Shantinagar', 'Mouchak',
                'Malibagh Railgate','Rampura', 'Banasree', 'Demra Staff Quarter' ]
        for i in range(len(arr)) :
            context[i] = arr[i]

    elif (bus_name == 'Achim Paribahan'):
        arr =  [ 'Gabtoli' , 'Technical' , 'Ansar Camp' , 'Mirpur 1' , 'Sony Hall' , 'Mirpur 2' , 'Mirpur 10' , 'Mirpur 11' , 'Purobi' , 'Kalshi' ,
                'ECB Chottor' , 'MES' ,'Sheora' , 'Kuril Bishwa Road' , 'Bashundhara' , 'Jamuna Future Park' , 'Nadda' , 'Natun Bazar' ,'Bashtola' ,'Shahjadpur' ,
                'Uttar Badda' , 'Badda' , 'Madhya Badda' ,'Merul' , 'Rampura' , 'Banasree' , 'Meradia bazar' ,'Staff Quarter' ]
        for i in range(len(arr)) :
            context[i] = arr[i]

    elif (bus_name == '6_no Bus'):
        arr =  ['Kamalapur', 'Motijheel', 'Gulistan', 'GPO', 'Paltan', 'Kakrail', 'Shantinagar','Malibagh Mor', 'Mouchak', 'Moghbazar', 'Bangla Motor',
                'Kawran Bazar', 'Farmgate','Bijoy Sarani', 'Jahangir Gate', 'Mohakhali', 'Wireless Mor', 'Gulshan 1', 'Gulshan 2','Natun Bazar']
        for i in range(len(arr)) :
            context[i] = arr[i]

    elif (bus_name == '8_no'):
        arr =  ['Jatrabari', 'Jonopath Mor', 'Sayedabad', 'Motijheel', 'Daynik Bangla Mor','Paltan', 'Press Club', 'High Court', 'Shahbagh', 'Bangla Motor',
                'Kawran Bazar','Farmgate', 'Khamarbari', 'Asad Gate', 'College Gate', 'Shishu Mela', 'Shyamoli','Kallyanpur', 'Technical', 'Gabtoli']
        for i in range(len(arr)) :
            context[i] = arr[i]

    elif (bus_name == 'Agradut Boishakhi'):
        arr =  ['Natun Bazar', 'Bashtola', 'Shajadpur', 'Badda', 'Gulshan 1', 'Gulshan Bridge','Wireless Mor', 'Mohakhali', 'Jahangir Gate', 'Bijoy Sarani',
                'Agargaon', 'Shishu Mela','Shyamoli','Kallyanpur', 'Technical', 'Gabtoli'  'Hemayetpur', 'Savar']
        for i in range(len(arr)) :
            context[i] = arr[i]

    elif (bus_name == 'Akash Paribahan'):
        arr =  ['Kodomtoli', 'Keraniganj', 'Babu Bazar', 'Naya Bazar', 'Golap Shah Mazar','GPO', 'Paltan', 'Kakrail', 'Shantinagar',
                'Malibagh Mor', 'Mouchak', 'Malibagh Railgate','Rampura', 'Merul', 'Madhya Badda', 'Badda', 'Uttar Badda', 'Shahjadpur', 'bashtola',
                'Natun Bazar', 'Nadda', 'Bashundhara', 'Kuril Bishwa Road', 'Khilkhet', 'Airport', 'Jasimuddin','Rajlakshmi', 'Azampur', 'House Building',
                'Diabari']
        for i in range(len(arr)) :
            context[i] = arr[i]

    elif (bus_name == 'Akik Paribahan'):
        arr =  ['Gabtoli', 'Technical', 'Ansar Camp', 'Mirpur 1', 'Sony Hall', 'Mirpur 2','Mirpur 10', 'Mirpur 11', 'Purobi', 'Kalshi',
                'ECB Chottor', 'MES', 'Sheora', 'Kuril Bishwa Road','Bashundhara', 'Jamuna Future Park', 'Nadda', 'Natun Bazar', 'Bashtola',
                'Shahjadpur', 'Uttar Badda']
        for i in range(len(arr)) :
            context[i] = arr[i]

    elif (bus_name == 'Al Makka Transport'):
        arr =  ['Motijheel', 'Gulistan', 'GPO', 'Paltan', 'Kakrail', 'Shantinagar','Malibagh Mor', 'Mouchak', 'Moghbazar', 'Nabisco', 'Mohakhali',
                'Chairman Bari', 'Kakoli','Banani', 'ECB Chottor', 'Kalshi', 'Purobi', 'Mirpur 10', 'Mirpur 2', 'Mirpur 1']
        for i in range(len(arr)) :
            context[i] = arr[i]

    elif (bus_name == 'Alif Enterprise'):
        arr =  ['Mirpur 1', 'Mirpur 2', 'Sony Hall', 'Mirpur 10', 'Kazipara', 'Shewrapara','Agargaon', 'Bijoy Sarani', 'Jahangir Gate', 'Mohakhali',
                'Wireless Mor', 'Gulshan 1', 'Badda','Rampura Bridge', 'Banasree']
        for i in range(len(arr)) :
            context[i] = arr[i]

    elif (bus_name == 'Alif Enterprise 2'):
        arr =  ['Shia Masjid', 'Japan Garden City', 'Adabor', 'Shyamoli', 'Shishu Mela','Agargaon', 'Ziya Uddan', 'Bijoy Sarani', 'Jahangir Gate',
                'Mohakhali', 'Wireless Mor','Gulshan 1', 'Link Road', 'Badda', 'Madhya Badda', 'Merul', 'Rampura', 'Banasree']
        for i in range(len(arr)) :
            context[i] = arr[i]

    elif (bus_name == 'Alif Enterprise 3'):
        arr =  ['Shia Masjid', 'Japan Garden City', 'Adabor', 'Shyamoli', 'Shishu Mela','Agargaon', 'Ziya Uddan', 'Bijoy Sarani', 'Jahangir Gate',
                'Mohakhali', 'Chairman Bari','Kakoli', 'Banani', 'Staff Road', 'MES', 'Sheora', 'Kuril Bishwa Road', 'Khilkhet', 'Airport','Jasimuddin',
                'Rajlakshmi', 'Azampur', 'House Building', 'Abdullahpur']
        for i in range(len(arr)) :
            context[i] = arr[i]

    elif (bus_name == 'Bhuiyan Paribahan'):
        arr =  ['Shia Masjid', 'Japan Garden City', 'Adabor', 'Shyamoli', 'Shishu Mela','Agargaon', 'Ziya Uddan', 'Bijoy Sarani', 'Jahangir Gate',
                'Mohakhali', 'Chairman Bari','Kakoli', 'Banani', 'Staff Road', 'MES', 'Sheora', 'Kuril Bishwa Road', 'Khilkhet', 'Airport','Jasimuddin',
                'Rajlakshmi', 'Azampur', 'House Building', 'Abdullahpur']
        for i in range(len(arr)) :
            context[i] = arr[i]

    elif (bus_name == 'Alaik Paribahan'):
        arr =  ['Balughat', 'Signal', 'CMH', 'Garrison', 'Adamjee College', 'Workshop', 'Jahangir Gate','Farmgate', 'Kawran Bazar']
        for i in range(len(arr)) :
            context[i] = arr[i]

    elif (bus_name == 'Ashulia Classic'):
        arr =  ['Satrasta', 'Nabisco', 'Mohakhali', 'Chairman Bari', 'Kakoli', 'Banani','Staff Road', 'MES', 'Sheora', 'Kuril Bishwa Road',
                'Khilkhet', 'Airport', 'Jasimuddin','Rajlakshmi','Azampur', 'House Building', 'Abdullahpur', 'Kamarpara', 'Ashulia Bazar', 'Zirabo',
                'Fantasy Kingdom','Jamgora', 'Baipayl', 'Nobinagar']
        for i in range(len(arr)) :
            context[i] = arr[i]

    elif (bus_name == 'Ayat Paribahan'):
        arr =  ['Mohammadpur', 'Asad Gate', 'Khamarbari', 'Farmgate', 'Bijoy Sarani', 'Jahangir Gate','Mohakhali', 'Wireless Mor', 'Gulshan 1',
                'Natun Bazar', 'Badda', 'Uttar Badda', 'Shahjadpur','bashtola', 'Natun Bazar', 'Nadda', 'Bashundhara', 'Kuril Bishwa Road']
        for i in range(len(arr)) :
            context[i] = arr[i]

    elif (bus_name == 'BRTC Bus Service 2'):
        arr =  ['Mohammadpur', 'Asad Gate', 'Khamarbari', 'Farmgate', 'Bijoy Sarani', 'Jahangir Gate','Mohakhali', 'Wireless Mor', 'Gulshan 1',
                'Natun Bazar', 'Badda', 'Uttar Badda', 'Shahjadpur','bashtola', 'Natun Bazar', 'Nadda', 'Bashundhara', 'Kuril Bishwa Road']
        for i in range(len(arr)) :
            context[i] = arr[i]

    elif (bus_name == 'Bahon Paribahan'):
        arr =  ['Mirpur 14', 'Mirpur 10', 'Mirpur 2', 'Mirpur 1', 'Ansar Camp', 'Bangla College', 'Technical','Darussalam', 'Kallyanpur',
                'Shyamoli', 'Shishu Mela', 'College Gate', 'Asad Gate', 'Dhanmondi 27','Dhanmondi 32', 'Kalabagan', 'Science Lab', 'Kataban', 'Shahbagh',
                'High Court', 'Press Club', 'Paltan','Daynik Bangla Mor', 'Motijheel', 'Arambagh', 'Kamalapur', 'Mugdapara', 'Basabo', 'Khilgaon']
        for i in range(len(arr)) :
            context[i] = arr[i]

    elif (bus_name == 'Balaka Paribahan'):
        arr =  ['Sayedabad', 'Manik Nagar', 'TT Para', 'Kamalapur', 'Malibagh', 'Mouchak', 'Moghbazar','Satrasta', 'Nabisco', 'Mohakhali',
                'Chairman Bari', 'Kakoli', 'Banani', 'Staff Road', 'MES','Sheora', 'Kuril Bishwa Road', 'Khilkhet', 'Airport', 'Jasimuddin',
                'Rajlakshmi','Azampur','House Building', 'Abdullahpur', 'Tongi', 'Gazipur Chowrasta']
        for i in range(len(arr)) :
            context[i] = arr[i]

    elif (bus_name == 'Basumati Transport'):
        arr =  ['Gabtoli', 'Technical', 'Ansar Camp', 'Mirpur 1', 'Sony Hall', 'Mirpur 2','Mirpur 10', 'Mirpur 11', 'Purobi', 'Kalshi',
                'ECB Chottor', 'MES', 'Sheora', 'Kuril Bishwa Road','Khilkhet', 'Airport', 'Jasimuddin', 'Rajlakshmi', 'Azampur', 'House Building',
                'Abdullahpur','Tongi','Gazipur Chowrasta']
        for i in range(len(arr)) :
            context[i] = arr[i]

    elif (bus_name == 'Best Transport'):
        arr =  ['Jatrabari', 'Sayedabad', 'Ittefaq', 'Motijheel', 'Daynik Bangla Mor', 'Paltan','Press Club', 'High Court',
                'Motsho Bhaban', 'Shahbagh', 'Bangla Motor', 'Kawran Bazar', 'Farmgate','Khamarbari', 'Agargaon', 'Taltola', 'Shewrapara',
                'Kazipara', 'Mirpur 10']
        for i in range(len(arr)) :
            context[i] = arr[i]

    elif (bus_name == 'Bihanga Paribahan'):
        arr =  ['Sadarghat', 'Ray Shaheb Bazar', 'Naya Bazar', 'Golap Shah Mazar', 'GPO', 'Paltan', 'Press Club','High Court',
                'Motsho Bhaban', 'Shahbagh', 'Bangla Motor', 'Kawran Bazar', 'Farmgate', 'Khamarbari','Agargaon', 'Taltola', 'Shewrapara',
                'Kazipara', 'Mirpur 10', 'Mirpur 11', 'Purobi', 'Pallabi','Duaripara']
        for i in range(len(arr)) :
            context[i] = arr[i]

    elif (bus_name == 'Bihanga Paribahan 2'):
        arr =  ['Azimpur', 'Nilkhet', 'New Market', 'City College', 'Kalabagan', 'Dhanmondi 32','Dhanmondi 27', 'Asad Gate',
                'College Gate', 'Shishu Mela', 'Shyamoli', 'Kallyanpur','Technical', 'Bangla College', 'Ansar Camp', 'Mirpur 1',
                'Mirpur 2', 'Proshika Mor', 'Rupnagar', 'Duaripara']
        for i in range(len(arr)) :
            context[i] = arr[i]

    elif (bus_name == 'Bikalpa Auto Service'):
        arr =  ['Motijheel', 'Gulistan', 'Paltan', 'Press Club', 'High Court', 'Motsho Bhaban','Shahbagh', 'Bangla Motor',
                'Kawran Bazar', 'Farmgate', 'Khamarbari', 'Agargaon', 'Taltola','Shewrapara','Kazipara', 'Mirpur 10', 'Mirpur 11',
                'Purobi', 'Pallabi', 'Mirpur 12']
        for i in range(len(arr)) :
            context[i] = arr[i]

    elif (bus_name == 'Bikash Paribahan'):
        arr =  ['Azimpur', 'Nilkhet', 'New Market', 'City College', 'Kalabagan', 'Dhanmondi 32', 'Dhanmondi 27',
                'Khamarbari', 'Bijoy Sarani', 'Jahangir Gate', 'Mohakhali', 'Banani', 'Kakoli', 'Staff Road', 'MES',
                'Sheora','Kuril Bishwa Road', 'Khilkhet', 'Airport', 'Jasimuddin', 'Rajlakshmi', 'Azampur', 'House Building',
                'Abdullahpur', 'Kamarpara', 'Dhour']
        for i in range(len(arr)) :
            context[i] = arr[i]

    elif (bus_name == 'Dewan'):
        arr = ['Azimpur', 'New Market', 'City College', 'Science Lab', 'Kataban', 'Shahbagh', 'Bangla Motor',
                'Kawran Bazar', 'Farmgate', 'Bijoy Sarani', 'Jahangir Gate', 'Mohakhali', 'Wireless Mor',
                'Gulshan 1', 'Badda', 'Shahjadpur', 'Natun Bazar', 'Nadda', 'Bashundhara', 'Jamuna Future Park',
                'Kuril Bishwa Road']
        for i in range(len(arr)) :
            context[i] = arr[i]

    elif (bus_name == 'Dhaka Chaka'):
        arr =  ['Police Plaza', 'Gulshan 1', 'Gulshan 2']
        for i in range(len(arr)) :
            context[i] = arr[i]

    elif (bus_name == 'Dhaka Chaka 2'):
        arr =  ['Banani', 'Gulshan 2', 'Natun Bazar']
        for i in range(len(arr)) :
            context[i] = arr[i]

    elif (bus_name == 'Dishari Paribahan'):
        arr =  ['Keraniganj', 'Babu Bazar', 'Naya Bazar', 'Golap Shah Mazar', 'GPO',
                'Paltan', 'Press Club', 'High Court', 'Motsho Bhaban', 'Shahbagh', 'Bangla Motor', 'Kawran Bazar',
                'Farmgate', 'Khamarbari', 'Asad Gate', 'College Gate', 'Shishu Mela', 'Shyamoli', 'Kallyanpur',
                'Technical', 'Bangla College', 'Ansar Camp', 'Mirpur 1', 'Chiriakhana']
        for i in range(len(arr)) :
            context[i] = arr[i]

    elif (bus_name == 'Green Dhaka'):
        arr =  ['Motijheel', 'Gulistan', 'GPO', 'Paltan', 'Kakrail', 'Shantinagar',
                'Malibagh Mor', 'Mouchak', 'Malibagh Railgate', 'Rampura', 'Merul', 'Madhya Badda', 'Badda',
                'Uttar Badda', 'Shahjadpur', 'bashtola', 'Natun Bazar', 'Nadda', 'Bashundhara', 'Kuril Bishwa Road',
                'Khilkhet', 'Airport', 'Jasimuddin', 'Rajlakshmi', 'Azampur', 'House Building', 'Abdullahpur']
        for i in range(len(arr)) :
            context[i] = arr[i]

    elif (bus_name == 'Himachol'):
        arr =  ['Metro Hall', 'Chashara', 'Shibu Market', 'Jalkuri', 'Sign Board', 'Matuail', 'Rayerbag',
                'Shonir Akhra', 'Jatrabari', 'Jonopath Mor', 'Gulistan', 'GPO', 'Paltan', 'Press Club', 'High Court',
                'Motsho Bhaban', 'Shahbagh', 'Bangla Motor', 'Kawran Bazar', 'Farmgate', 'Khamarbari', 'Agargaon',
                'Taltola', 'Shewrapara', 'Kazipara', 'Mirpur 10', 'Mirpur 11', 'Purobi', 'Pallabi', 'Mirpur 12']
        for i in range(len(arr)) :
            context[i] = arr[i]

    elif (bus_name == 'Khajababa Paribahan'):
        arr =  ['Jatrabari', 'Sayedabad', 'Gulistan', 'GPO', 'Paltan', 'Press Club', 'High Court',
                'Motsho Bhaban', 'Shahbagh', 'Bangla Motor', 'Kawran Bazar', 'Farmgate', 'Khamarbari', 'Agargaon',
                'Taltola', 'Shewrapara', 'Kazipara', 'Mirpur 10', 'Mirpur 11', 'Purobi', 'Pallabi', 'Mirpur 12']
        for i in range(len(arr)) :
            context[i] = arr[i]

    elif (bus_name == 'Labbaik Paribahan'):
        arr =  ['Sign Board', 'Matuail', 'Rayerbag', 'Shonir Akhra', 'Jatrabari', 'Jonopath Mor', 'Sayedabad',
                'Manik Nagar', 'Basabo', 'Khilgaon', 'Rajarbagh', 'Malibagh Mor', 'Mouchak', 'Moghbazar', 'Bangla Motor',
                'Kawran Bazar', 'Farmgate', 'Khamarbari', 'Asad Gate', 'College Gate', 'Shishu Mela', 'Shyamoli',
                'Kallyanpur', 'Technical', 'Gabtoli', 'Aminbazar', 'Hemayetpur', 'Savar']
        for i in range(len(arr)) :
            context[i] = arr[i]

    elif (bus_name == 'Shadhin Paribahan'):
        arr =  ['Staff Quarter', 'Demra', 'Banasree', 'Rampura', 'Malibagh Railgate', 'Mouchak', 'Moghbazar',
                'Bangla Motor', 'Kawran Bazar', 'Farmgate', 'Khamarbari', 'Asad Gate', 'Mohammadpur', 'Bosila']
        for i in range(len(arr)) :
            context[i] = arr[i]

    elif (bus_name == 'tanjil Paribahan'):
        arr = ['Sadarghat', 'Ray Shaheb Bazar', 'Naya Bazar', 'Golap Shah Mazar', 'GPO', 'Paltan', 'Press Club',
                'High Court', 'Motsho Bhaban', 'Shahbagh', 'Bangla Motor', 'Kawran Bazar', 'Farmgate', 'Khamarbari',
                'Asad Gate', 'College Gate', 'Shishu Mela', 'Shyamoli', 'Kallyanpur', 'Technical', 'Ansar Camp',
                'Mirpur 1', 'Chiriakhana']
        for i in range(len(arr)) :
            context[i] = arr[i]

    elif (bus_name == 'Trust Transporot Services'):
        arr = ['Mirpur DOHS', 'Kalshi', 'ECB Chottor', 'Garrison', 'Adamjee College',
                'Workshop', 'Jahangir Gate', 'Farmgate', 'Kawran Bazar', 'Bangla Motor', 'Shahbagh',
                'High Court',
                'Press Club', 'Paltan', 'Daynik Bangla Mor', 'Motijheel']
        for i in range(len(arr)) :
            context[i] = arr[i]

    elif (bus_name == 'Welcome'):
        arr = ['Gulistan' , 'Paltan' , 'Paltan' , 'Press Club' , 'High Court' , 'Motsho Bhaban' , 'Shahbagh' , 'Bangla Motor' ,
                'Kawran Bazar' , 'Farmgate' , 'Khamarbari' , 'Asad Gate' , 'College Gate' , 'Shishu Mela' , 'Shyamoli' ,
                'Kallyanpur' , 'Technical' , 'Gabtoli' , 'Aminbazar' , 'Hemayetpur' , 'Savar' , 'Nandan Park']
        for i in range(len(arr)) :
            context[i] = arr[i]


    return render(request,'base.html',{'context':context, 'bus_name': bus_name.upper()})
