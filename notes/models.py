from django.db import models

# Create your models here.
''' Model representing sticky note

     Fields:
    - title: CharField for the note title with a maximum length of 255
    characters.
    - content: TextField for the note content.
    - created_at: DateTimeField set to the current date and time when the
    note is created.

    Relationships:
    - author: ForeignKey representing the author of the note.

    Methods:
    - __str__: Returns a string representation of the note, showing the
    title.

    :param models.Model: Django's base model class.

'''


class Note(models.Model):
    title = models.CharField(max_length=100)  # short text field for note title
    content = models.TextField()  # large text field for the actual note
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # links each note to a user via foreignkey
    author = models.ForeignKey("Author", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


class Author(models.Model):
    ''' Model Representing the author of the note

        Fields:
        - name: CharField for the author's name.
        Methods:
        - __str__: Returns a string representation of the author, showing the
        name.
        :param models.Model: Django's base model class.

    '''
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name