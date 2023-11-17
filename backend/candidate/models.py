from django.db import models
from accounts.models import BaseModel, CustomUser

# Create your models here.

GENDER_CHOICE = (
    ("M", "Male"),
    ("F", "Female"),
    ("P", "Prefer not to say"),
)

EMPLOYMENT_STATUS = (
    ("EM", "Employed"),
    ("UN", "Unemployed"),
    ("SE", "Self-Employed"),
    ("ST", "Student"),
    ("OT", "Other"),
)

JOB_TYPE = (
    ("P", "Part-Time"),
    ("F", "Full-Time"),
)


class Candidate(BaseModel):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=256)
    title = models.CharField(max_length=256, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE)
    employment_status = models.CharField(max_length=2, choices=EMPLOYMENT_STATUS)
    contact_number = models.CharField(max_length=15)
    street = models.CharField(max_length=256)
    city = models.CharField(max_length=128)
    state = models.CharField(max_length=128)
    zip = models.CharField(max_length=32)
    country = models.CharField(max_length=64)
    skills = models.TextField()
    cv = models.FileField(upload_to='cv')
    cv_identifier = models.CharField(max_length=64,blank=True,null=True)
    police_report = models.FileField(upload_to='police_report')
    vulnerable_sector = models.FileField(upload_to='valnerable_sector_report')
    training_document = models.FileField(upload_to='training_report')
    health_report = models.FileField(upload_to='health_report')
    job_type = models.CharField(max_length=1, choices=JOB_TYPE)

    @property
    def email(self):
        return self._email

    @property
    def password(self):
        return self._password

    def __str__(self):
        return f"{self.full_name}"


class Education(BaseModel):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name="educations")
    name = models.CharField(max_length=256)
    qualification = models.CharField(max_length=256)
    date_completed = models.DateField(blank=True,null=True)

    def __str__(self):
        return f"{self.candidate.full_name}/{self.name}"


class Referee(BaseModel):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name="referees")
    name = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    company = models.CharField(max_length=128)
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.candidate.full_name}/{self.name}"

