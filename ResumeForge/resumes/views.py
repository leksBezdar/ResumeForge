import json

from django.http import JsonResponse
from django.http import HttpResponse
from django.http import HttpRequest
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .forms import ResumeForm

from .models import Resume


@method_decorator(csrf_exempt, name='dispatch')
class ResumeFormView(View):
    def post(self, request: HttpRequest):
        
        data = json.loads(request.body.decode('utf-8'))       
        form = ResumeForm(data)

        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'errors': form.errors}, status=400)
        

@method_decorator(csrf_exempt, name='dispatch')
class GetAllResumesView(View):
    def get(self, request: HttpRequest):
        full_name = request.GET.get('full_name', None)

        if full_name:
            resumes = Resume.objects.filter(full_name__icontains=full_name)
        else:
            resumes = Resume.objects.all()

        resumes_list = [{'full_name': resume.full_name, 'email': resume.email, 'phone_number': resume.phone_number,
                         'education': resume.education, 'experience': resume.experience, 'skills': resume.skills}
                        for resume in resumes]

        data = {'resumes': resumes_list}
        json_data = json.dumps(data, ensure_ascii=False).encode('utf-8')
        
        return HttpResponse(json_data, content_type='application/json')

