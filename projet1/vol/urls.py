from django.urls import path
from . import views
urlpatterns = [
    path('vols/', views.index, name='vols'),
    path('vols/del_vol/<int:id>', views.del_vol, name='del_vol'),
    path('aeroports/',views.list_air,name='aeroports'),
    path('aeroports/del_air/<int:id>',views.del_air,name='del_air'),
    path('vols/update_vol/<int:id>',views.update_vol,name='update_vol'),
    path('vols/update_vol/update_vol_action/<int:id>', views.update_vol_action, name='update_vol_action'),
    path('vols/add_vol/',views.add_vol,name='add_vol'),
    path('vols/add_vol/add_vol_action/',views.add_vol_action,name='add_vol_action'),
    path('users/',views.list_users,name='users'),
    path('users/create_user/', views.create_compte, name='create_compte'),
    path('users/create_user/add_user_action/', views.create_user_action, name='create_user_action'),
    path('users/del_user/<int:id>', views.del_user, name='del_user'),
    path('users/update_user/<int:id>', views.update_user, name='update_user'),
    path('users/update_user/update_user_action/<int:id>', views.update_user_action, name='update_user_action'),
    path('', views.connect, name='connect'),
    path('login/', views.signIn, name='signIn'),
    path('login/login/', views.signIn, name='signIn'),
    path('disconnect/', views.signOut, name='disconnect'),

]