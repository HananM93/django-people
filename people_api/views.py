from django.shortcuts import render
from rest_framework.views import APIView    # <- as super to your class
from rest_framework.response import Response  # <- to send data to the frontend
from rest_framework import status # <- to include status codes in your response
from .serializers import PersonSerializer # <- to format data to and from the database, enforces schema
from .models import Person
from django.shortcuts import get_object_or_404

# class (People)

#  GET     /people - index
#  POST    /people - create

# class  (PeopleDetail) - use primary key (pk) as argument to access id

#  GET     /people/:id - show
#  PUT     /people/:id - update
#  DELETE  /people/:id - delete


# Create your views here.
class People(APIView):

  def get(self, request):
    # Index Request
    print(request)
   
    people = Person.objects.all()
    # Use serializer to format table data to JSON
    data = PersonSerializer(people, many=True).data
    return Response(data)


  def post(self, request):
    # Post Request
    print(request.data)
    # format data for postgres
    person = PersonSerializer(data=request.data)
    if person.is_valid():
      person.save()
      return Response(person.data, status=status.HTTP_201_CREATED)
    else: 
      return Response(person.errors, status=status.HTTP_400_BAD_REQUEST)


class PersonDetail(APIView):

  def get(self, request, pk):
    # Show Request
    print(request)
    person = get_object_or_404(Person, pk=pk)
    data = PersonSerializer(person).data
    return Response(data)

  def put(self, request, pk):
    # Update Request
    print(request)
    person = get_object_or_404(Person, pk=pk)
    updated = PersonSerializer(person, data=request.data, partial=True)
    if updated.is_valid():
      updated.save()
      return Response(updated.data)
    else:
      return Response(updated.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk):
    # Delete Request
    print(request)
    person = get_object_or_404(Person, pk=pk)
    person.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)