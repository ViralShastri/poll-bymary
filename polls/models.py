import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    id = models.IntegerField()
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    notMuchVotes = models.IntegerField(null=True)
    theSkyeVotes = models.IntegerField(null=True)
    from django.db import models

    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        was_published_recently.admin_order_field = 'pub_date'
        was_published_recently.boolean = True
        was_published_recently.short_description = 'Published recently?'
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    id = models.IntegerField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
        
class Post(models.Model):
    id = models.IntegerField()
    author = models.ForeignKey(Question, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    id = models.IntegerField()
    post = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text




    