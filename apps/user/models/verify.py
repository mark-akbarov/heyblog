from django.db import models
from core.base_model import BaseModel


class VerifyUser(BaseModel):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    code = models.CharField(max_length=25)
    is_active = models.BooleanField(default=False)