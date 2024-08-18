from django.db import models
class AnagramCheck(models.Model):
  word1=models.CharField(max_length=100)
  word2=models.CharField(max_length=100)
  is_anagram=models.BooleanField()
  checked_at=models.DateTimeField(auto_now_add=True)
