from django.db import models

class BaseModel(models.Model):
	date_created = models.DateTimeField(auto_now_add = True, editable=False)
	date_updated = models.DateTimeField(auto_now = True, editable=False)
	class Meta:
		abstract = True
		ordering = ['-date_created']
		get_latest_by = 'date_created'