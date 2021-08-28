from django.shortcuts import render
import parse.parsing as ps
import json

# Create your views here.


ps.main()
def parse(request):
    with open('output.json', 'rb') as f:
        context = json.load(f)
    return render(request, 'parse/index.html', context=context)
    