from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.template.context import RequestContext

from UserAdmin.models import userdata
from .forms import *


def home(request):
    #each form name explains its working
    Createform = UserDataForm()
    Readform = UserReadForm()
    Delteform = UserDeleteForm()

    if request.POST:
        #for creation of new users. first they are checked if already exists they are not added
        if (request.POST['operation'] == 'Create'):
            form = UserDataForm(request.POST)
            if form.is_valid():
                firstN = request.POST['first_name']
                lastN = request.POST['last_name']
                IBN = request.POST['iban']
                user = request.user.username
                print (user)
                print("First Name : "  + firstN)
                print("Last Name : " + lastN)
                print("IBAN : " + IBN)
                if ((userdata.objects.filter(owner=request.user.username,first_name=firstN,last_name=lastN, iban=IBN).count()== 0) and
                    (userdata.objects.filter(owner=request.user.username,iban=IBN).count()== 0)):
                    UserToAdd = userdata.objects.create(owner=request.user.username,first_name=firstN,last_name=lastN, iban=IBN)
                    UserToAdd.save()
                    context = {'user': request.user, 'formC': Createform, 'formR': Readform, 'formD': Delteform,
                   'Created': "Record Created Successfully"}
                    return render(request, 'home.html', context)
                else:
                    context = {'user': request.user, 'formC': Createform, 'formR': Readform, 'formD': Delteform,
                   'Created': "Record is not Created"}
                    return render(request, 'home.html', context)

        # for reading of users on the basis of their last name, others can also be addded
        elif (request.POST['operation'] == 'Read'):
            form = UserReadForm(request.POST)
            if form.is_valid():
                LastRN = request.POST['last_name']
                user = request.user.username
                print("last Name : "  + LastRN)
                if userdata.objects.filter(owner=request.user.username,last_name=LastRN).count()>0:
                    readusers = userdata.objects.filter(owner=request.user.username,last_name=LastRN)
                    query_data = {
                        "query_details": readusers
                    }
                    context = {'user': request.user, 'formC': Createform, 'formR': Readform, 'formD': Delteform, 'UserRead':readusers}
                    return render(request, 'home.html', context)

                else:
                    context = {'user': request.user, 'formC': Createform, 'formR': Readform, 'formD': Delteform,
                   'UserReadF': "No data found"}
                    return render(request, 'home.html', context)

        #for deletion of users on the basis of iban as they are unique for any account holder
        elif (request.POST['operation'] == 'Delete'):
            form = UserDeleteForm(request.POST)
            if form.is_valid():
                IBND = request.POST['iban']
                user = request.user.username
                print ("Deleted" )
                if userdata.objects.filter(owner=user,iban=IBND).count()>0:
                    UdataToDelete = userdata.objects.filter(iban=IBND)
                    UdataToDelete.delete()
                    context = {'user': request.user, 'formC': Createform, 'formR': Readform, 'formD': Delteform,
                        'DELETED': "Record Deleted Successfully"}
                    return render(request, 'home.html', context)
                else:
                    context = {'user': request.user, 'formC': Createform, 'formR': Readform, 'formD': Delteform,
                               'DELETED': "Not Deleted"}
                    return render(request, 'home.html', context)


        #simple update logic by matching current and replacing.
        elif (request.POST['operation'] == 'Update'):
            form = UserDataForm(request.POST)
            if form.is_valid():
                firstCN = request.POST['first_name']
                lastCN = request.POST['last_name']
                IBANCR = request.POST['iban']
                NewfirstN = request.POST['Newfname']
                NewlastN = request.POST['Newlname']
                NewIBAN = request.POST['Newiban']
                user = request.user.username
                print("Updated")
                if (userdata.objects.filter(owner=request.user.username,first_name=firstCN, last_name=lastCN, iban=IBANCR).count()>0):
                    userdata.objects.filter(owner=request.user.username,first_name=firstCN, last_name=lastCN, iban=IBANCR).update(
                        first_name=NewfirstN, last_name=NewlastN, iban=NewIBAN)
                    context = {'user': request.user, 'formC':Createform, 'formR':Readform, 'formD': Delteform , 'UPDATE': "Updated Successfully"}
                    return render(request, 'home.html', context)
                else:
                    context = {'user': request.user, 'formC': Createform, 'formR': Readform, 'formD': Delteform,
                    'UPDATE': "Not Updated"}
                    return render(request, 'home.html', context)


    context = {'user': request.user, 'formC':Createform, 'formR':Readform, 'formD': Delteform}
    return render(request, 'home.html', context)
