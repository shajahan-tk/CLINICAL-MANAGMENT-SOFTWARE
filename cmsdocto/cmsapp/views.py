from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import *
from django.contrib import messages

# Create your views here.

def home(request):
    return redirect('/login')
def signup(request):
    return render(request,'signup.html')
def dash(request):
    return render(request,'dash.html')
def login_form(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user :
            login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('/dash')  # Redirect to '/dash'
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('/login')  # Redirect to '/login'
    return render(request, 'login.html')
def newpatient1(request):
    return render(request,'newpatient1.html')
def todayappointment(request):
    apmnts=Add_patients.objects.all()
    return render(request,'todayappointment.html',{'apmnts':apmnts})
def withpatient(request):
    return render(request,'withpatient.html')
def fastrack(request):
    return render(request,'fastrack.html')
def appointment(request):
    return render(request,'appointment.html')
def search(request):
    searchpatient=Add_patients.objects.all()
    return render(request,'search.html',{'patient':searchpatient})
def ehrreports(request):
    return  render(request,'ehrreports.html')
def telemedicine(request):
    tele=Add_patients.objects.all()
    return render(request,'telemedicine.html',{'telemd':tele})
def settings(request):
    return render(request,'settings.html')
def sample1(request):
    return render(request,'sample1.html')
def clinicsettings(request):
    return render(request,'clinicsettings.html')
def generalsettings(request):
    ptnt=Patientgroup.objects.all()
    mdcl=Medicalcondition.objects.all()
    taxstngs=taxmodel.objects.all()
    pymnt=Paymentmethod.objects.all()
    dcmt=Documenttype.objects.all()
    return render(request,'generalsettings.html',{'ptnt':ptnt,'mdcl':mdcl,'taxstngs':taxstngs,'pymnt':pymnt,'dcmt':dcmt})
def clinciprofile(request):
    if request.method=='POST':
        clinic_name= request.POST['clinic_name']
        phone_no= request.POST['phone_no']
        address= request.POST['address']
        locality= request.POST['locality']
        state= request.POST['state']
        email= request.POST['email']
        tax= request.POST['tax']
        default_language= request.POST['default_language']
        date_start= request.POST['date_start']
        pharmacy_name= request.POST['pharmacy_name']
        specialization= request.POST['specialization']
        mobile_no1= request.POST['mobile_no']
        slogan= request.POST['slogan']
        country= request.POST['country']
        city= request.POST['city']
        website= request.POST['website']
        zip= request.POST['zip']
        default_currency= request.POST['default_currency']
        time_zone= request.POST['time_zone']
        pharmacy_licence_code= request.POST['pharmacy_licence_code']
        c= Clinicprofiles(Clinic_name= clinic_name, Phone_no= phone_no, Address=address, Locality=locality, State=state, Email=email, Tax=tax, Default_language=default_language, Date_start=date_start, Pharmacy_name= pharmacy_name, Specialization=specialization, Mobile_no=mobile_no1,Slogan=slogan, Country=country, City= city, Website=website, Zip=zip, Default_Currency=default_currency, Time_zone=time_zone, Pharmacy_licence_code=pharmacy_licence_code)
        c.save()
        return redirect('/generalsettings')
def patientgroup1(request):
    if request.method =='POST':
        patientgroup=request.POST['patientgroup']
        ptnt=Patientgroup(patientgroup=patientgroup)
        ptnt.save()
        return redirect('/generalsettings')
def medicalconditions(request):
    if request.method =='POST':
        medicalcondition=request.POST['medicalcondition'] 
        mdcl=Medicalcondition(medicalcondition=medicalcondition)
        mdcl.save()
        return redirect('/generalsettings')    
def taxsettings(request):
    if request.method =='POST':
        taxname=request.POST['taxname']  
        taxpercentage=request.POST['taxpercentage'] 
        tax=taxmodel(taxname=taxname, taxpercentage=taxpercentage)
        tax.save()
        return redirect('/generalsettings')   
def paymentmethod(request):
    if request.method =='POST':
        paymentmethod=request.POST['paymentmethod']
        discription=request.POST['discription1']
        pymnt=Paymentmethod(Payment_method=paymentmethod,discription=discription)
        pymnt.save()
        return redirect('/generalsettings')   

def documenttype(request):
    if request.method =='POST':
        documenttype=request.POST['documenttype']
        dcmt=Documenttype(document_type=documenttype)
        dcmt.save()
        return redirect('/generalsettings')



def rp(request):
    return render(request,'rp.html')

def policies(request):
    return render(request,'policies.html')

def pharmacysettings(request):
    return render(request,'pharmacysettings.html')

def staff(request):
    return render(request,'staff.html')

def pathology(request):
    return render(request,'pathology.html')

def dental(request):
    dentalwork=Dentalwork.objects.all()
    addlaboratory=Addlaboratories.objects.all()
    return render(request,'dental.html',{'dentalwork':dentalwork,'addlaboratory':addlaboratory})

def dentalworks(request):
    if request.method =='POST':
        workname=request.POST['workname']
        shade=request.POST['shade']
        worktype=request.POST['worktype']
        alloytype=request.POST['alloytype']
        dntl=Dentalwork(Workname=workname,Shade=shade,Worktype=worktype,Alloytype=alloytype)
        dntl.save()
        return redirect('/dental')
    
def addlaboratories(request):
    if request.method == 'POST':
        labname=request.POST['labname']
        labtype=request.POST['labtype']
        phone=request.POST['phone']
        executive=request.POST['executive']
        address=request.POST['address']
        lbrtry=Addlaboratories(Labname=labname,Labtype=labtype,Phone=phone,Executive=executive,Address=address)
        lbrtry.save()
        return redirect('/dental')

def communication(request):
    cmnctn=Add_patients.objects.all()   
    return render(request,'communication.html',{'cmnctn':cmnctn})

def clinicalnotes(request):
    return render(request,'clinicalnotes.html')

def totalappointment(request):
    return render(request,'totalappointment.html')

def patient(request):
    return render(request,'patient.html')


def invoice(request):
    return render(request,'invoice.html')

def sickleave(request):
    return render(request,'sickleave.html')

def website(request):
    return render(request,'website.html')

def reciept(request):
    return render(request,'reciept.html')

def labreport(request):
    return render(request,'labreport.html')

def prescription(request):
    return render(request,'prescription.html')

def telemedicine(request):
    return render(request,'telemedicine.html')

def files(request):
    return render(request,'files.html')

def emr(request):
    return render(request,'emr.html')

def reports(request):
    return render(request,'reports.html')

def support(request):
    return render(request,'support.html')

def billing(request):
    return render(request,'billing.html')



def signup(request):
    return render(request,'signup.html')

def switch(request):
    return render(request,'switch.html')

def emrsettings(request): 
    treatdisplay=treatmentsitems.objects.all()
    drugdisplay=drugitems.objects.all()
    complaints=complaintsitems.objects.all()
    observation=Addobservation.objects.all()
    diagnosis=Adddiagnosis.objects.all()
    investigation=Addinvestigation.objects.all()
    frequency=Addfrequency.objects.all()
    return render(request,'emrsettings.html',{'treatdisplay':treatdisplay,'druglist':drugdisplay,
                                              'complaints':complaints,'observation':observation,'diagnosis':diagnosis,
                                              'investigation':investigation,'frequency':frequency})

def treatmentlist(request):
    if request.method=='POST':
        procedure=request.POST['procedure']
        charges=request.POST['charges']
        procedurecode=request.POST['procedurecode']
        Duration=request.POST['Duration']
        Session=request.POST['Session']
        abc=treatmentsitems(procedure=procedure,charges=charges,procedurecode=procedurecode,Duration=Duration,Session=Session)
        abc.save()
        return redirect('/emrsettings')

def druglist(request):
    if request.method=='POST':
        unit=request.POST['unit']
        drglist=drugitems(unit=unit)
        drglist.save()
        return redirect('/emrsettings')    
    
def complaintslist(request):
    if request.method=='POST':
        itemname=request.POST['item name']
        manufacture=request.POST['manufacture']
        boxsize=request.POST['box size']
        category=request.POST['category']
        purchaserate=request.POST['purchase']
        packingsize=request.POST['packingsize']
        taxable=request.POST['taxable']
        recorderquantity=request.POST['recorder']
        batchno=request.POST['batchno']
        salesrate=request.POST['salesrate']
        deviceserialnumber=request.POST['deviceserialsnumber']
        hsncode=request.POST['hsncode']
        complaints=complaintsitems(itemname=itemname,manufacture=manufacture,boxsize=boxsize,category=category,purchase=purchaserate,packingsize=packingsize,taxable=taxable,recorder=recorderquantity,batchno=batchno,salesrate=salesrate,deviceserialsnumber=deviceserialnumber,hsncode=hsncode)
        complaints.save()
        return redirect('/emrsettings')
    

def observation(request):
    observation=request.POST['observation']
    obs=Addobservation(observation=observation)
    obs.save()
    return redirect('/emrsettings')  

def diagnosis(request):
    diagnosis=request.POST['diagnosis']
    diagnosiscode=request.POST['diagnosiscode']
    dgn=Adddiagnosis(diagnosis=diagnosis,diagnosiscode=diagnosiscode)
    dgn.save()
    return redirect('/emrsettings')

def investigation(request):
    investigation=request.POST['investigation']
    inv=Addinvestigation(investigation=investigation)
    inv.save()
    return redirect('/emrsettings')

def frequency(request):
    frequency=request.POST['frequency']
    frq=Addfrequency(frequency=frequency)
    frq.save()
    return redirect('/emrsettings')


    # //add new patients//
def newpatient(request):
    if request.method =='POST':
        registration_id= request.POST['registration_id']
        fname= request.POST['fname']
        first_name= request.POST['first_name']
        last_name= request.POST['last_name']
        rec_no= request.POST['rec_no']
        mobile_no= request.POST['mobile_no']
        email= request.POST['email']
        state= request.POST['state']
        city= request.POST['city']
        address= request.POST['address']
        date_of_birth= request.POST['date_of_birth']
        age= request.POST['age']
        phone_no= request.POST['phone_no']
        guardian_name= request.POST['guardian_name']
        op_no= request.POST['op_no']
        passport_no= request.POST['passport_no']
        date_of_discharege= request.POST['date_of_discharege']
        gender= request.POST['gender']
        country= request.POST['country']
        blood_group= request.POST['blood_group']
        medical_histoy= request.POST['medical_histoy']
        paitient_remark= request.POST['paitient_remark']
        medical_condition= request.POST['medical_condition']
        paitient_group= request.POST['paitient_group']
        type= request.POST['type']
        consultation_fee= request.POST['consultation_fee']
        reffered_by= request.POST['reffered_by']
        occupation= request.POST['occupation']
        attachments= request.POST['attachments']
        doctor1= request.POST['doctor1']
        addpaitent= Add_patients.objects.create(Register_id= registration_id, Category=fname, First_name=first_name, Last_name=last_name, Record_no=rec_no, Mobile_no=mobile_no, Email=email, State=state, City=city, Address=address, Date_of_birth=date_of_birth, Age=age, Phone_no=phone_no, Guardian_name=guardian_name, Op_no=op_no, Passport_no=passport_no, Date_of_discharge=date_of_discharege, Gender=gender, Blood_group=blood_group, Medical_history=medical_histoy, Paitient_group=paitient_group, Medical_condititon=medical_condition, Type=type, Consultation_fee=consultation_fee, Reffered_by=reffered_by, Occupation=occupation, Photo=attachments, Doctor=doctor1, Country=country,  Paitient_remark=paitient_remark)
        addpaitent.save()
        return render(request, 'newpatient1.html')
    
def expireddoc(request):
    return render(request,'expireddoc.html')

def profile(request):
    profilepic=Profilepic.objects.all()
    return render(request,'profile.html',{'profile':profilepic})

def profilepic(request):
    if request.method == 'POST':
        profilepic = request.POST['profile_pic']
        profile=Profilepic(profilepic=profilepic)
        profile.save()
        return redirect('/profile')
    
def consentform(request):
    return render(request,'consentform.html')
def certificate(request):
    return render(request,'certificateform.html')


def pharmacysettings(request):
    supplier=pharmacysupplier.objects.all()
    phunit=pharmacyunit.objects.all()
    phitem=pharmacyitems.objects.all()
    phcat=pharmacycategory.objects.all()
    phman=pharmacymanufacture.objects.all()
    return render(request,'pharmacysettings.html',{'supplier':supplier,'pharmacyunit':phunit,'phitem':phitem,'phcat':phcat,'phman':phman})
def pharmacysupply(request):
    if request.method == 'POST':
        suppilername=request.POST['Suppliername']
        companycode=request.POST['companycode']
        companyname=request.POST['companyname']
        contactname=request.POST['contactname']
        email=request.POST['email']
        web=request.POST['web']
        phone=request.POST['phone']
        address=request.POST['address']
        address=request.POST['address']
        phr=pharmacysupplier(suppilername=suppilername,companycode=companycode,companyname=companyname,contactname=contactname,email=email,web=web,phone=phone,address=address)
        phr.save()
        return redirect('/pharmacysettings')

def pharmacyuni(request):
    if request.method == 'POST':
        unit=request.POST['unit']
        hey=pharmacyunit(unit=unit)
        hey.save()
        return redirect('/pharmacysettings')
def pharmacyitem(request):
    if request.method=='POST':
        itemname=request.POST['item name']
        manufacture=request.POST['manufacture']
        boxsize=request.POST['boxsize']
        category=request.POST['category']
        purchaserate=request.POST['purchase']
        packingsize=request.POST['packingsize']
        taxable=request.POST['taxable']
        recorderquantity=request.POST['recorder']
        batchno=request.POST['batchno']
        salesrate=request.POST['salesrate']
        deviceserialnumber=request.POST['deviceserialsnumber']
        hsncode=request.POST['hsncode']
        phritem=pharmacyitems(itemname=itemname,manufacture=manufacture,boxsize=boxsize,category=category,purchase=purchaserate,packingsize=packingsize,taxable=taxable,recorder=recorderquantity,batchno=batchno,salesrate=salesrate,deviceserialsnumber=deviceserialnumber,hsncode=hsncode)
        phritem.save()
        return redirect('/pharmacysettings')
def categories(request):
    if request.method == 'POST':
        itemname = request.POST['itemname']
        manufacture = request.POST['manufacture']
        description = request.POST['description']
        cat=pharmacycategory(itemname=itemname,manufacture=manufacture,description=description)
        cat.save()
        return redirect('/pharmacysettings')
def manufacture(request):
    if request.method =='POST':
        manufacture=request.POST['manufacture']
        companycode=request.POST['companycode']
        companyname=request.POST['companyname']
        contactname=request.POST['contactname']
        email=request.POST['email']
        web=request.POST['web']
        phone=request.POST['phone']
        address=request.POST['address']
        man=pharmacymanufacture(manufacture=manufacture,companycode=companycode,companyname=companyname,contactname=contactname,email=email,web=web,phone=phone,address=address)
        man.save()
        return redirect('/pharmacysettings')
    # pathology ///
def pathology(request):
    header1=header.objects.all()
    lab1=Addlab.objects.all()
    lab2=Addlabtest.objects.all()
    lab3=Addlabtestpakeges.objects.all()
    return render(request,'pathology.html',{'header':header1,'addlab':lab1,'addlabtest':lab2,'items':lab3})
def Header(request):
    if request.method=='POST':
        suppliername=request.POST['suppliername']
        sup=header(suppliername=suppliername)
        sup.save()
        return redirect('/pathology')
def addlab(request):
    if request.method=='POST':
        labname=request.POST['lab_name']
        labcode= request.POST['lab_code']
        companyname= request.POST['company_name']
        contactname= request.POST['contact_name']
        email= request.POST['email']
        web= request.POST['web']
        phone= request.POST['phone']
        address= request.POST['address']
        lab=Addlab(Lab_name=labname,Lab_code=labcode,Company_name=companyname,Contact_name=contactname,Email=email,Web=web,Phone=phone,Address=address)
        lab.save()
        return redirect('/pathology')
def addlabtest(request):
    if request.method=='POST':
        testno= request.POST['test_no']
        testdescription= request.POST['test_description']
        testcharge= request.POST['test_charge']
        carry_out= request.POST['carry_out']
        report= request.POST['report']
        testype= request.POST['test_type']
        reporthead= request.POST['report_head']
        labtest=Addlabtest(Test_no=testno,Test_description=testdescription,Test_charge=testcharge,Carry_out=carry_out,Report=report,Test_type=testype,Report_head=reporthead)
        labtest.save()
        return redirect('/pathology')   
def addlabtestpakages(request):
    if request.method =='POST':
        itemname= request.POST['item_name']
        manufaturedate= request.POST['manufacture_date']
        description= request.POST['description']
        pakages= Addlabtestpakeges(Item_name=itemname,Manufacture_date=manufaturedate,Description=description)
        pakages.save()
        return redirect('/pathology')
def addlabtestdetails(request):
    if request.method =='POST':
        labtest_detail= request.POST['labtest_detail']
        lb=Addlabtestdeatail(labtest_detail=labtest_detail)
        lb.save()
        return redirect('/pathology')  
def vacination(request):
    return render(request, 'vacinationlist.html')
def opcard(request):
    return render(request,'opcard.html')
def rolesandprivileges(request):
    return render(request,'rolesandprivileges.html')
def staffdetails(request):
    return render(request,'staffdetails.html')
def patientdetails(request):
    return render(request,'patientdetails.html')
