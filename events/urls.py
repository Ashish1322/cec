"""cecday URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    # Urls for returning events details and handling post request of forms
    path('designathon', views.designathon,name='designathon'),
    path('break-the-strategy',views.break_strategy,name='break_strategy'),
    path('technical-presentation',views.technical_presentation,name='technical_presentation'),
    path('tech-quiz', views.tech_quiz,name='tech_quiz'),
    path('electroinsight', views.electroinsight,name='electroinsight'),
    path('roborace', views.roborace,name='roborace'),
    path('project-display', views.project_display,name='project_display'),
    path('rangoli', views.rangoli,name='rangoli'),
    path('collage-making', views.collage_making,name='collage_making'),

    # Urls for return form for every event
    path('designathon-register', views.designathon_register,name='designathon_register'),
    path('break-the-strategy-register',views.break_strategy_register,name='break_strategy_register'),
    path('tech-quiz-register', views.tech_quiz_register,name='tech_quiz_register'),
    path('electroinsight-register', views.electroinsight_register,name='electroinsight_register'),
    path('roborace-register', views.roborace_register,name='roborace_register'),
    path('technical-presentation-register', views.technical_presentation_register,name='technical_presentation_register'),
    path('project-display-register', views.project_display_register,name='project_display_register'),
    path('rangoli-register', views.rangoli_register,name='rangoli_register'),
    path('collage-making-register', views.collage_making_register,name='collage_making_register'),
]
