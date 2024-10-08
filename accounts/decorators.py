from django.shortcuts import render,HttpResponse
from django.core.exceptions import PermissionDenied


def allowed_users(allowed_roles=[]):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):
			
			group = None
			if request.user.groups.exists():
				group = request.user.groups.all()[0].name 
			if group in allowed_roles:
				return view_func(request, *args, **kwargs)
			else:
				return HttpResponse('You are not allowed')
		return wrapper_func
	return decorator

