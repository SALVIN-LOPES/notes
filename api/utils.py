from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer

def getNotesList(request):
    notes = Note.objects.all().order_by('-updated')
    serializer = NoteSerializer(notes,many=True)
    return Response(serializer.data)

def getNoteList(request,pk):
    note = Note.objects.filter(id=pk).first()
    serializer = NoteSerializer(note)
    return Response(serializer.data)

def createNote(request):
    data = request.data
    note = Note.objects.create(
         body = data['body']
    )
    serializer = NoteSerializer(note,many=False)
    return Response(serializer.data)

def updateNote(request,pk):
    data = request.data
    note = Note.objects.filter(id=pk).first()
    serializer = NoteSerializer(instance=note,data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

def deleteNote(request,pk):
    note = Note.objects.filter(id=pk).first()
    note.delete()
    return Response("note was deleted")