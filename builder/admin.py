from django.contrib import admin
from .models import Resume, PersonalInfo, WorkExperience, Skill, Education, ResumeStyle

admin.site.register(Resume)
admin.site.register(PersonalInfo)
admin.site.register(WorkExperience)
admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(ResumeStyle)
