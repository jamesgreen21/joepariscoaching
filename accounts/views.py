from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.db.models import Max

from .models import Profile
from journal.models import Checkin
from .forms import (
    UserRegisterForm,
    UserUpdateForm,
    ProfileRegisterForm,
)
# from marketing.forms import EmailSubscribeForm


@login_required
def profile(request):
    """
    Returns a view that renders the profile page and form
    """
    # subscribe_form = EmailSubscribeForm()
    user = get_object_or_404(Profile, user=request.user.id)
    user_stats = Checkin.objects.filter(journal_id__user_id=request.user.id).order_by('-id').first()
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileRegisterForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )
        if u_form.is_valid() and p_form.is_valid():
            if request.FILES:
                Profile.objects.get(id=request.user.id).image.delete(save=True)
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile has been successfully updated.')
            return redirect('accounts:profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileRegisterForm(instance=request.user.profile)

    context = {
        'title': 'Profile',
        'u_form': u_form,
        'p_form': p_form,
        'user': user,
        'user_stats': user_stats,
        # 'subscribe_form': subscribe_form,
    }

    return render(request, 'profile.html', context)
