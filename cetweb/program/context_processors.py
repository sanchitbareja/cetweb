from program.models import Program
from program.forms import CertificateApplicationForm
def programs(request):
    return {"programs":Program.objects.all()}

def apply_form(request):
    certificate_form = CertificateApplicationForm()
    return {'certificate_form':certificate_form}
