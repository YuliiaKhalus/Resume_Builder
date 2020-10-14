from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Resume, PersonalInfo, WorkExperience, Skill, Education
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache


def home(request):
    return render(request, 'builder/home.html')


class ResumeList(LoginRequiredMixin, ListView):
    allow_empty = True
    model = Resume
    context_object_name = 'resumes'
    template_name = 'builder/dashboard.html'

    def get_queryset(self):
        queryset = super(ResumeList, self).get_queryset()
        queryset = queryset.filter(author=self.request.user).order_by('-updated_at')
        return queryset


class ResumeCreateView(LoginRequiredMixin, CreateView):
    model = Resume
    fields = ['title', 'style']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ResumeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Resume
    success_url = '/dashboard/'

    def test_func(self):
        resume = self.get_object()
        if self.request.user == resume.author:
            return True
        return False


class ResumeStyleUpdateView(LoginRequiredMixin, UpdateView):
    model = Resume
    fields = ['title', 'style']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ResumeDetailView(LoginRequiredMixin, DetailView):
    model = Resume


class PersonalInfoCreateView(LoginRequiredMixin, CreateView):
    model = PersonalInfo
    fields = ['first_name', 'last_name', 'job_title', 'email',
              'mobile', 'address', 'personal_profile', 'image']

    def form_valid(self, form):
        form.instance.resume = Resume.objects.get(id=self.kwargs.get('resume_id'))
        return super().form_valid(form)


class PersonalInfoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = PersonalInfo
    fields = ['first_name', 'last_name', 'job_title', 'email',
              'mobile', 'address', 'personal_profile', 'image']

    def form_valid(self, form):
        form.instance.resume = Resume.objects.get(id=self.kwargs.get('resume_id'))
        return super().form_valid(form)

    def test_func(self):
        personal_info = self.get_object()
        if self.request.user == personal_info.resume.author:
            return True
        return False


class WorkExperienceCreateView(LoginRequiredMixin, CreateView):
    model = WorkExperience
    fields = ['job_title', 'company', 'from_date', 'to_date', 'description']

    def form_valid(self, form):
        form.instance.resume = Resume.objects.get(id=self.kwargs.get('resume_id'))
        return super().form_valid(form)


class WorkExperienceUpdateView(LoginRequiredMixin, UpdateView):
    model = WorkExperience
    fields = ['job_title', 'company', 'from_date', 'to_date', 'description']

    def form_valid(self, form):
        form.instance.resume = Resume.objects.get(id=self.kwargs.get('resume_id'))
        return super().form_valid(form)


class WorkExperienceDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = WorkExperience

    def get_success_url(self):
        we = self.get_object()
        return reverse('resume-detail', kwargs={'pk': we.resume.pk})

    def test_func(self):
        we = self.get_object()
        if self.request.user == we.resume.author:
            return True
        return False


class SkillCreateView(LoginRequiredMixin, CreateView):
    model = Skill
    fields = ['skill']

    def form_valid(self, form):
        form.instance.resume = Resume.objects.get(id=self.kwargs.get('resume_id'))
        return super().form_valid(form)


class SkillUpdateView(LoginRequiredMixin, UpdateView):
    model = Skill
    fields = ['skill']

    def form_valid(self, form):
        form.instance.resume = Resume.objects.get(id=self.kwargs.get('resume_id'))
        return super().form_valid(form)


class SkillDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Skill

    def get_success_url(self):
        skill = self.get_object()
        return reverse('resume-detail', kwargs={'pk': skill.resume.pk})

    def test_func(self):
        skill = self.get_object()
        if self.request.user == skill.resume.author:
            return True
        return False


class EducationCreateView(LoginRequiredMixin,  CreateView):
    model = Education
    fields = ['alma_mater', 'from_date', 'to_date', 'qualification']

    def form_valid(self, form):
        form.instance.resume = Resume.objects.get(id=self.kwargs.get('resume_id'))
        return super().form_valid(form)


class EducationUpdateView(LoginRequiredMixin,  UpdateView):
    model = Education
    fields = ['alma_mater', 'from_date', 'to_date', 'qualification']

    def form_valid(self, form):
        form.instance.resume = Resume.objects.get(id=self.kwargs.get('resume_id'))
        return super().form_valid(form)


class EducationDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Education

    def get_success_url(self):
        ed = self.get_object()
        return reverse('resume-detail', kwargs={'pk': ed.resume.pk})

    def test_func(self):
        ed = self.get_object()
        if self.request.user == ed.resume.author:
            return True
        return False


def about(request):
    return render(request, 'builder/about.html', {'title': 'About'})


@method_decorator(never_cache, name='dispatch')
class ResumePreview(LoginRequiredMixin, DetailView):
    model = Resume
    template_name = 'builder/resume_preview.html'



