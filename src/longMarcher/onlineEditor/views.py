from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import FileForm
# Create your views here.

def get_content(request, file_name):
    if request.method == 'POST':
        form = FileForm(request.POST)
        if form.is_valid():
            file_content = form.cleaned_data['content']
            f = open('/tmp/%s' %file_name, 'w+')
            f.write(file_content)
            #import pdb;pdb.set_trace()
            f.close()
            return HttpResponseRedirect(request.path_info)
        else:
            return HttpResponse('Not valid field')

    else:
        f = open('/tmp/%s' %file_name, 'r')
        file_content = f.read()
        f.close()
        form = FileForm()
        form.initial = {'content': file_content}

    return render(request, 'onlineEditor/index.html', {'form': form})
    #return HttpResponse('Hello online editor!')
