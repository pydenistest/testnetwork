from django.shortcuts import render


# Create your views here.


def index_main(request):
    context = {
        "": 0,
    }

    if request.method == "POST":
        context["InputText"] = request.POST["InputText"][::-1]

    return render(request,
                  template_name="myapp/index_main.html",
                  context=context, )
