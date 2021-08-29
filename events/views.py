
from django.core.checks import messages
from django.db import reset_queries
from django.shortcuts import redirect, render,HttpResponse
from django.contrib import messages
from .models import BreakTheStrategy, CollageMaking, Designathon, TechQuiz, TechnicalPresentation,RoboPresetation,Rangoli,Electroinsight,ProjectDisplay


# Views for return deatials of events and
def designathon(request):
    return render(request,'events/designathon.html')

def break_strategy(request):
    return render(request,'events/break_strategy.html')

def tech_quiz(request):
    return render(request,'events/tech_quiz.html')

def electroinsight(request):
    return render(request,'events/electroinsight.html')

def roborace(request):
    return render(request,'events/roborace.html')

def technical_presentation(request):
    return render(request,'events/technical_presentation.html')

def project_display(request):
    return render(request,'events/project_display.html')

def rangoli(request):
    return render(request,'events/rangoli.html')

def collage_making(request):
    return render(request,'events/collage_making.html')


# Views for returning html pages of forms for each events  handling post requests
def designathon_register(request):
    if(request.method=='POST'):
        teamname = request.POST['teamname']
        institution = request.POST['institution']
        college = request.POST['college']

        name1 = request.POST['name1']
        phonenumber1 = request.POST['phonenumber1']
        email1 = request.POST['email1']
        branch1 = request.POST['branch1']
        semester1 = request.POST['semester1']
        rollno1 = request.POST['rollno1']
        file1 = request.FILES['file1']

        name2 = request.POST['name2']
        phonenumbe2 = request.POST['phonenumber2']
        email2 = request.POST['email2']
        branch2 = request.POST['branch2']
        semester2 = request.POST['semester2']
        rollno2 =request.POST['rollno2']
        file2 = request.FILES['file2']

        name3 = request.POST['name3']
        phonenumbe3 = request.POST['phonenumber3']
        email3 = request.POST['email3']
        branch3 = request.POST['branch3']
        semester3 = request.POST['semester3']
        rollno3 = request.POST['rollno3']
        file3 = request.FILES['file3']

        name4 = request.POST['name4']
        phonenumbe4 = request.POST['phonenumber4']
        email4 = request.POST['email4']
        branch4 = request.POST['branch4']
        semester4 = request.POST['semester4']
        rollno4 = request.POST['rollno4']
        file4 = request.FILES['file4']

        a = Designathon(college=college,teamname=teamname,type_institution=institution,name1=name1,email1=email1,branch1=branch1,semester1=semester1,phone1 = phonenumber1,id1 = file1,rollno1=rollno1 , name2=name2,email2=email2,branch2=branch2,semester2=semester2,phone2 = phonenumbe2,id2 = file2,rollno2=rollno2, name3=name3,email3=email3,branch3=branch3,semester3=semester3,phone3 = phonenumbe3,id3 = file3,rollno3=rollno3, name4=name4,email4=email4,branch4=branch4,semester4=semester4,phone4 = phonenumbe4,id4 = file4,rollno4=rollno4 )
        a.save()
        messages.success(request,"Registration successfull. Thankyou for registration.")
        return redirect("designathon_register")




    return render(request,'events/designathon_register.html')

def break_strategy_register(request):
    if(request.method=="POST"):
        file = request.FILES['id_proof']
        name = request.POST['name']
        email = request.POST['email']
        phonenumber = request.POST['phonenumber']
        instituion = request.POST['institution']
        college_school = request.POST['college']
        branch_class = request.POST['branch']
        semester = int(request.POST['semester'])
        rollno = int(request.POST['rollno'])
      
        entry = BreakTheStrategy(name=name,email=email,phone=phonenumber,college_school=college_school,branch_class=branch_class,semester=semester,roll_no=rollno,id1=file,type_institution=instituion)
        entry.save()
        messages.success(request,"Registration successfull. Thankyou for registration.")
        return redirect('break_strategy')
    return render(request,'events/break_strategy_register.html')

def technical_presentation_register(request):
    if(request.method=="POST"):
        file = request.FILES['id_proof']
        name = request.POST['name']
        email = request.POST['email']
        phonenumber = request.POST['phonenumber']
        instituion = request.POST['institution']
        college_school = request.POST['college']
        branch_class = request.POST['branch']
        semester = int(request.POST['semester'])
        rollno = int(request.POST['rollno'])
      
        entry = TechnicalPresentation(name=name,email=email,phone=phonenumber,college_school=college_school,branch_class=branch_class,semester=semester,roll_no=rollno,id1=file,type_institution=instituion)
        entry.save()
        messages.success(request,"Registration successfull. Thankyou for registration.")
        return redirect('technical_presentation')
    return render(request,'events/technical_presentation_register.html')

def tech_quiz_register(request):
    if(request.method=="POST"):
        file = request.FILES['id_proof']
        name = request.POST['name']
        email = request.POST['email']
        phonenumber = request.POST['phonenumber']
        instituion = request.POST['institution']
        college_school = request.POST['college']
        branch_class = request.POST['branch']
        semester = int(request.POST['semester'])
        rollno = int(request.POST['rollno'])
      
        entry = TechQuiz(name=name,email=email,phone=phonenumber,college_school=college_school,branch_class=branch_class,semester=semester,roll_no=rollno,id1=file,type_institution=instituion)
        entry.save()
        messages.success(request,"Registration successfull. Thankyou for registration.")
        return redirect('tech_quiz')
    return render(request,'events/tech_quiz_register.html')

def electroinsight_register(request):
    if(request.method=='POST'):
        teamname = request.POST['teamname']
        institution = request.POST['institution']
        college = request.POST['college']

        name1 = request.POST['name1']
        phonenumber1 = request.POST['phonenumber1']
        email1 = request.POST['email1']
        branch1 = request.POST['branch1']
        semester1 = request.POST['semester1']
        rollno1 = request.POST['rollno1']
        file1 = request.FILES['file1']

        name2 = request.POST['name2']
        phonenumbe2 = request.POST['phonenumber2']
        email2 = request.POST['email2']
        branch2 = request.POST['branch2']
        semester2 = request.POST['semester2']
        rollno2 =request.POST['rollno2']
        file2 = request.FILES['file2']
        a = Electroinsight(college=college,teamname=teamname,type_institution=institution,name1=name1,email1=email1,branch1=branch1,semester1=semester1,phone1 = phonenumber1,id1 = file1,rollno1=rollno1 , name2=name2,email2=email2,branch2=branch2,semester2=semester2,phone2 = phonenumbe2,id2 = file2,rollno2=rollno2 )
        a.save()
        messages.success(request,"Registration successfull. Thankyou for registration.")
        return redirect("electroinsight")




    return render(request,'events/electroinsight_register.html')

def roborace_register(request):
    if(request.method=="POST"):
        teamname = request.POST['teamname']
        institution = request.POST['institution']
        college = request.POST['college']

        name1 = request.POST['name1']
        phonenumber1 = request.POST['phonenumber1']
        email1 = request.POST['email1']
        branch1 = request.POST['branch1']
        semester1 = request.POST['semester1']
        rollno1 = request.POST['rollno1']
        file1 = request.FILES['file1']

        name2 = request.POST['name2']
        phonenumbe2 = request.POST['phonenumber2']
        email2 = request.POST['email2']
        branch2 = request.POST['branch2']
        semester2 = request.POST['semester2']
        rollno2 =request.POST['rollno2']
        file2 = request.FILES['file2']

        name3 = request.POST['name3']
        phonenumbe3 = request.POST['phonenumber3']
        email3 = request.POST['email3']
        branch3 = request.POST['branch3']
        semester3 = request.POST['semester3']
        rollno3 = request.POST['rollno3']
        file3 = request.FILES['file3']

        a = RoboPresetation(college=college,teamname=teamname,type_institution=institution,name1=name1,email1=email1,branch1=branch1,semester1=semester1,phone1 = phonenumber1,id1 = file1,rollno1=rollno1 , name2=name2,email2=email2,branch2=branch2,semester2=semester2,phone2 = phonenumbe2,id2 = file2,rollno2=rollno2, name3=name3,email3=email3,branch3=branch3,semester3=semester3,phone3 = phonenumbe3,id3 = file3,rollno3=rollno3 )
        a.save()
        messages.success(request,"Registration successfull. Thankyou for registration.")
        return redirect("roborace")
    return render(request,'events/roborace_register.html')


def project_display_register(request):
    if(request.method=='POST'):
        teamname = request.POST['teamname']
        institution = request.POST['institution']
        college = request.POST['college']
        projectname = request.POST['project']
        name1 = request.POST['name1']
        phonenumber1 = request.POST['phonenumber1']
        email1 = request.POST['email1']
        branch1 = request.POST['branch1']
        semester1 = request.POST['semester1']
        rollno1 = request.POST['rollno1']
        file1 = request.FILES['file1']

        name2 = request.POST['name2']
        phonenumbe2 = request.POST['phonenumber2']
        email2 = request.POST['email2']
        branch2 = request.POST['branch2']
        semester2 = request.POST['semester2']
        rollno2 =request.POST['rollno2']
        file2 = request.FILES['file2']

        a = ProjectDisplay(college=college,teamname=teamname,type_institution=institution,name1=name1,email1=email1,branch1=branch1,semester1=semester1,phone1 = phonenumber1,id1 = file1,rollno1=rollno1 , name2=name2,email2=email2,branch2=branch2,semester2=semester2,phone2 = phonenumbe2,id2 = file2,rollno2=rollno2,projectname=projectname )
        a.save()
        messages.success(request,"Registration successfull. Thankyou for registering for the event.")
        return redirect('project_display')

    return render(request,'events/project_display_register.html')

def rangoli_register(request):
    if(request.method=='POST'):
        teamname = request.POST['teamname']
        institution = request.POST['institution']
        college = request.POST['college']

        name1 = request.POST['name1']
        phonenumber1 = request.POST['phonenumber1']
        email1 = request.POST['email1']
        branch1 = request.POST['branch1']
        semester1 = request.POST['semester1']
        rollno1 = request.POST['rollno1']
        file1 = request.FILES['file1']

        name2 = request.POST['name2']
        phonenumbe2 = request.POST['phonenumber2']
        email2 = request.POST['email2']
        branch2 = request.POST['branch2']
        semester2 = request.POST['semester2']
        rollno2 =request.POST['rollno2']
        file2 = request.FILES['file2']
        a = Rangoli(college=college,teamname=teamname,type_institution=institution,name1=name1,email1=email1,branch1=branch1,semester1=semester1,phone1 = phonenumber1,id1 = file1,rollno1=rollno1 , name2=name2,email2=email2,branch2=branch2,semester2=semester2,phone2 = phonenumbe2,id2 = file2,rollno2=rollno2 )
        a.save()
        messages.success(request,"Registration successfull. Thankyou for registration.")
        return redirect("rangoli")

    return render(request,'events/rangoli_register.html')

def collage_making_register(request):
    if(request.method=="POST"):
        file = request.FILES['id_proof']
        name = request.POST['name']
        email = request.POST['email']
        phonenumber = request.POST['phonenumber']
        instituion = request.POST['institution']
        college_school = request.POST['college']
        branch_class = request.POST['branch']
        semester = int(request.POST['semester'])
        rollno = int(request.POST['rollno'])
       
        
        entry = CollageMaking(name=name,email=email,phone=phonenumber,college_school=college_school,branch_class=branch_class,semester=semester,roll_no=rollno,id1=file,type_institution=instituion)
        entry.save()
        messages.success(request,"Registration successfull. Thankyou for registration.")
        return redirect('collage_making')
    return render(request,'events/collage_making_register.html')