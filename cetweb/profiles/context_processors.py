from profiles.models import Profile
def tmp_profile(request):
    for profile in Profile.objects.all():
        if profile.company:
            return {"tmp_profile":profile}
    return {"tmp_profile":None}
