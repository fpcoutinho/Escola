from django.http import JsonResponse

def alunos(request):
  if request.method == 'GET':
    alunos = [{'id':1, 'nome':'Appa'}, {'id':2, 'nome':'Mushu'}]
    return JsonResponse(alunos, safe=False)