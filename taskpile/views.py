from django.http import HttpResponseRedirect, HttpResponse, HttpResponseServerError
from django.views.generic.simple import direct_to_template, redirect_to
from django.template.loader import render_to_string
from django.shortcuts import render_to_response, get_object_or_404
from extra_context import render_response

from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.utils import simplejson
from django.conf import settings

from taskpile.models import Task, UserProfile
from datetime import datetime, timedelta

@login_required
def homepage(request):
    
    curr_user = request.user
    user_tasks = curr_user.tasks_assigned.filter(completed = False)
    completed_tasks = curr_user.tasks_assigned.filter(completed = True)[:6]

    if UserProfile.objects.filter(user=curr_user).count() == 0:
        new_profile = UserProfile()
        new_profile.user = curr_user
        new_profile.save()
    
    teammates = curr_user.get_profile().teammates.all()
    
    project_members = []
    all_users = User.objects.all()
    for user in teammates:
        if user == curr_user:
            continue
        else:
            user_block = {}
            user_block['username'] = user.username
            user_block['active_tasks'] = user.tasks_assigned.filter(completed = False)
            user_block['completed_tasks'] = user.tasks_assigned.filter(completed = True)[:6]
            project_members.append(user_block)
            

    return render_response(request, "tasks/homepage.html",
                           {'mytasks': user_tasks,
                            'completed_tasks': completed_tasks,
                            'project_members': project_members,
                            }
                           )


@login_required
def ajax_create_task(request):
 
    if request.is_ajax() and request.POST and request.user.is_authenticated():
        
        task_entry = request.POST['task_entry']
        assigned_username = request.POST['assigned_user']

        assigned_user = User.objects.get(username = assigned_username)

        task = Task()
        task.summary = task_entry
        task.creator = request.user
        task.assigned_user = assigned_user
        task.completed = False
        task.save()
        #task.assigned_users.add(request.user)

        task_html = render_to_string("tasks/active_task.html", 
                                      { 'task': task })
                                    

        response = {'task_html': task_html,
                    'assigned_user': assigned_username,
                    }

        return HttpResponse(simplejson.dumps(response), mimetype="application/json")
    else:
        return HttpResponseServerError()

@login_required
def ajax_complete_task(request):

    if request.is_ajax() and request.POST and request.user.is_authenticated():
        task_id = request.POST['task_id']
        assigned_username = request.POST['assigned_user']
        assigned_user = User.objects.get(username = assigned_username)

        task = Task.objects.get(id = task_id, assigned_user = assigned_user)
        if task.completed == True:
            return HttpResponseServerError()

        task.completed = True
        task.time_completed = datetime.now()
        task.save()

        task_html = render_to_string("tasks/completed_task.html",
                                     {'task': task })

        response = {'task_id': task_id,
                    'task_html': task_html,
                    'assigned_user': assigned_username,
                    }
        return HttpResponse(simplejson.dumps(response), mimetype="application/json")

    else:
        return HttpResponseServerError()


@login_required
def ajax_mark_task_incomplete(request):
 
    if request.is_ajax() and request.POST and request.user.is_authenticated():
        task_id = request.POST['task_id']
        assigned_username = request.POST['assigned_user']
        assigned_user = User.objects.get(username = assigned_username)

        task = Task.objects.get(id = task_id, assigned_user = assigned_user)
        if task.completed == False:
            return HttpResponseServerError()
        task.completed = False
        task.time_completed = None
        task.save()

        task_html = render_to_string("tasks/active_task.html", 
                                      { 'task': task })
                                    

        response = {'task_html': task_html,
                    'assigned_user': assigned_username,
                    }

        return HttpResponse(simplejson.dumps(response), mimetype="application/json")
    else:
        return cccc


"""
def login(request):
   
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username = username , password = password)
    if user != None and user.is_active:
        pass
    else:
        pass
    

    return render_response(request, "homepage.html")
"""
