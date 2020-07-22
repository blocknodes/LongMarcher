from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import FileForm
# Create your views here.

FILE_BASE_DIR = '/work/notes/'

def get_content(request, file_name):
    file_path = FILE_BASE_DIR + file_name
    if request.method == 'POST':
        form = FileForm(request.POST)
        if form.is_valid():
            file_content = form.cleaned_data['content']
            f = open(file_path, 'w+')
            f.write(file_content)
            #import pdb;pdb.set_trace()
            f.close()
            return HttpResponseRedirect(request.path_info)
        else:
            return HttpResponse('Not valid field')

    else:
        #should use a+ in case of file not existing
        f = open(file_path, 'a+')
        f.seek(0)
        file_content = f.read()
        f.close()
        form = FileForm()
        form.initial = {'content': file_content}

    return render(request, 'onlineEditor/index.html', {'form': form})
    #return HttpResponse('Hello online editor!')
