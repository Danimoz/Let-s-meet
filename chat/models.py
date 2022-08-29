from django.db import models

# Create your models here.

class ChatRoom(models.Model):
    name = models.CharField(max_length=200)
    meeting_duration = models.PositiveIntegerField(help_text='in minutes', default=30)

    def __str__(self):
        return f'{self.name} - {self.meeting_duration} mins'

class RoomMember(models.Model):
    name = models.CharField(max_length=200)
    uid = models.CharField(max_length=200)
    room = models.ForeignKey(ChatRoom, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name

class RoomAgenda(models.Model):
    agenda_no = models.PositiveIntegerField()
    agenda = models.CharField(max_length=200)
    time = models.PositiveBigIntegerField(help_text='in minutess')
    room = models.ForeignKey(ChatRoom, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.agenda_no}. {self.agenda}'