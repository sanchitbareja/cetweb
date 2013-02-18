from program.models import Program
def programs(request):
    return {"programs":Program.objects.all()}
