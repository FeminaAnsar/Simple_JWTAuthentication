from .models import Book
from .serializers import BookSerializer,RegisterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from .pagination import CustomPagination


class RegisterView(APIView):
    def post(self,request):
        serializer=RegisterSerializer(data=request.data)

        if serializer.is_valid():
            user=serializer.save()
            refresh=RefreshToken.for_user(user)
            return Response({"message":"User Created."})
        else:
            return Response(serializer.errors)


class BookCreateList(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset=Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def post(self, request, *args, **kwargs):
        response=super().post(request,*args, **kwargs)
        return Response({"message":"created new book",'status':200})

class BookList(generics.ListAPIView):
    queryset=Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = CustomPagination


class BookDetail(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]


class BookUpdate(generics.UpdateAPIView):
    queryset=Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        instance=self.get_object()
        if instance.author != request.user:
            return Response({"Message":"You need permission to update this book"})
        return super().patch(request,*args,**kwargs)


    def put(self,request,*args,**kwargs):
        instance = self.get_object()
        if instance.author != request.user:
            return Response({"Message":"You need permission to update this book"})
        return super().put(request, *args, **kwargs)


class BookDelete(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self,request,*args,**kwargs):
        instance = self.get_object()
        if instance.author != request.user:
            return Response({"message":"You need permission to delete this book"})
        response=super().delete(request, *args, **kwargs)
        return Response({'message':'Book Deleted'})



# Create your views here.
