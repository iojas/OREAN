from api.models import *
from api import internal
def main(request):
    tags = dict()
    tags['is_project_admin'] = False
    if request.user.is_authenticated():
        try:
            if 'projectID' in request.session and (request.user.is_superuser or UserProject.objects.get(user=request.user, project=request.session['projectID']).manager): 
                tags['is_project_admin'] = True
        except:
            tags['is_project_admin'] = False
        tags['available_projects'] = internal.ListProjects(request)
    return tags
