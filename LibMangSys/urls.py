from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('administrator/studentdetails',views.viewstuddetails, name="stud-detail"),
    path('administrator',views.administrator, name="administrator"),    
    path('deletestudent',views.deletestudent, name="delete-stud"),    
    path('logout',views.logout, name="logout"),
    path('editstudent/<int:id>',views.editstudent, name="edit-student"),
    path('addbook',views.addbook,name="add-book"),
    path('viewallbooks',views.viewallbooks,name="view-all-books"),
    path('editbook/<int:id>',views.editbook, name="edit-book"),
    path('deletebook',views.deletebook, name="delete-book"),
    path('issuebook',views.issuebook, name="issue-book"),
    path('viewissuedbook',views.viewissuedbook, name="issued-book"),
    path('returnbook',views.returnbook, name="return-book"),
    
    path('studregistration',views.studregistration, name="stud-registration"),
    path('studentlogin',views.studlogin, name="stud-login"),
    path('studentpanel',views.studpanel, name="stud-panel"),
    path('fine',views.fine, name="fine"),

    
    # path('administrator/deletestudent/<int:id>',views.deletestudent, name="delete=stud"),    
]
