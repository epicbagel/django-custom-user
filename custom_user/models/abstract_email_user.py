from model_utils.models import TimeStampedModel
from model_utils import FieldTracker
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin)
from custom_user.managers import UserManager

class AbstractEmailUser(TimeStampedModel, AbstractBaseUser, PermissionsMixin):
	objects = UserManager()
	USERNAME_FIELD = 'email'
	# Track any changes to the email field by default. Useful when
	# integrating with CRM systems
	tracker = FieldTracker(fields=['email'])
	email = models.EmailField(verbose_name='Email address', max_length = 255, unique = True, db_index = True)
	# Base user stuff
	is_active = models.BooleanField(default = True)
	# The user is identified by their email address
	def get_full_name(self): return self.email
	# The user is identified by their email address
	def get_short_name(self): return self.email
	# On Python 3: def __str__(self):
	def __unicode__(self): u"%s" % return self.email
	@property
	def is_staff(self):
		return self.is_superuser
	class Meta:
		abstract = True

