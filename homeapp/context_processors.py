from blogapp.models import Blog
from homeapp.models import Department,Diagnostic

def get_depertment_to_context(request):
    depertments = Department.objects.all()
    return {
        'depertments': depertments  
    }

def get_blog_to_context(request):
    blogs = Blog.objects.all()
    return {
        'blogs': blogs
    }

def get_diagnostict_to_context(request):
    diagnostics = Diagnostic.objects.all()
    return {
        'diagnostics': diagnostics   
    }
