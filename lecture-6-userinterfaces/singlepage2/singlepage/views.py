from django.shortcuts import render
from django.http import Http404, HttpResponse

# Create your views here.
def index(request):
    return render(request, "singlepage/index.html")

texts = [
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam ullamcorper nulla vel ligula tincidunt auctor. Mauris varius ligula condimentum, viverra nunc nec, dictum leo. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Curabitur ante lorem, ornare ac arcu a, viverra ultrices nisi. Suspendisse efficitur enim ut velit porta fermentum. Sed quis hendrerit dolor, a pretium quam. Vivamus id enim nulla. Vivamus a est id lorem interdum pharetra eget at lorem. Curabitur nibh magna, consectetur vitae pharetra laoreet, condimentum at velit. Nunc sem lacus, semper facilisis luctus id, gravida eu felis.",
    "Vivamus a lectus eget elit sollicitudin vehicula. Curabitur congue rutrum diam, sed varius enim facilisis eu. Morbi interdum ipsum et varius maximus. Praesent pellentesque mattis lacus, elementum rutrum nisl tincidunt sed. Morbi id elit nulla. Ut vel lorem et erat dignissim vestibulum sit amet ut turpis. Nam nulla quam, sodales in dui id, fringilla ultrices massa. Pellentesque ac mattis risus. Suspendisse id dignissim erat, eget finibus justo. Duis feugiat, arcu in fringilla convallis, urna est facilisis mi, et iaculis sapien tortor vitae libero. Praesent dignissim leo nec nunc pellentesque rhoncus sed id enim. Aliquam vel elementum ex. Sed metus justo, pharetra vel fringilla sit amet, tincidunt sit amet ex. Aenean rhoncus pulvinar gravida. Aliquam erat volutpat.",
    "Pellentesque non purus in ante volutpat consectetur ut quis tellus. In tincidunt auctor sem vitae efficitur. Vivamus vel nunc velit. Fusce ac enim facilisis, tempor urna vel, accumsan massa. Cras interdum auctor augue, vel hendrerit nisi bibendum non. Sed finibus cursus diam vitae convallis. In at quam scelerisque, interdum erat in, scelerisque ligula. Praesent ultricies facilisis malesuada. Sed in pharetra ligula. Proin imperdiet ligula eu venenatis faucibus. Nullam nisl sapien, fermentum eu dapibus a, gravida nec urna. Mauris tempor dolor vitae leo pretium fermentum. Nulla facilisi.",
]
def section(request, num):
    if 1 <= num <= 3:
        return HttpResponse(texts[num - 1])
    else:
        raise Http404("No such section")