from model_utils.models import TimeStampedModel
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import (
	AbstractBaseUser, PermissionsMixin
)
from custom_user.managers import UserManager

class AbstractEmailUser(TimeStampedModel, AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(verbose_name='Email address', max_length = 255, unique = True, db_index = True)
	# Base user stuff
	is_active = models.BooleanField(default = True)
	is_superuser = models.BooleanField(default = False)
	objects = UserManager()
	USERNAME_FIELD = 'email'
	def get_full_name(self):
		# The user is identified by their email address
		return self.email
	def get_short_name(self):
		# The user is identified by their email address
		return self.email
	# On Python 3: def __str__(self):
	def __unicode__(self):
		return self.email
	def has_perm(self, perm, obj = None):
		"Does the user have a specific permission?"
		# Simplest possible answer: Yes, always
		return True
	def has_module_perms(self, app_label):
		"Does the user have permissions to view the app `app_label`?"
		# Simplest possible answer: Yes, always
		return True
	@property
	def is_staff(self):
		"Is the user a member of staff?"
		# Simplest possible answer: All admins are staff
		return self.is_admin

	class Meta:
		abstract = True

