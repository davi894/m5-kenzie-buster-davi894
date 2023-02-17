from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializer import MovieSerializer, MovieOrderSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView, status
from rest_framework.response import Response
from users.pemissions import UserPermission
from .models import Movie



class MovieView(APIView, PageNumberPagination):

    authentication_classes = [JWTAuthentication]
    permission_classes = [UserPermission]

    def post(self, req, pk=None):
        serializer = MovieSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(user=req.user)

        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, req):
        movies = Movie.objects.all()

        result_page = self.paginate_queryset(
            movies,
            req,
            view=self,
        )
        serializer = MovieSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)


class MovieOrderView(APIView):
    authentication_classes = [JWTAuthentication]

    def post(self, req, movie_id):

        if not req.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        movie_dict = Movie.objects.get(id=movie_id)
        movie = MovieOrderSerializer(data=req.data)

        movie.is_valid(raise_exception=True)

        movie.save(user_movie=req.user, movie=movie_dict)

        return Response(movie.data, status.HTTP_201_CREATED)


class MovieViewId(APIView):
    authentication_classes = [JWTAuthentication]

    def get(self, req, movie_id):

        movie = Movie.objects.get(id=movie_id)
        serializer = MovieSerializer(movie).data
        return Response(serializer, status.HTTP_200_OK)

    def delete(self, req, movie_id):

        if not req.user.is_employee:
            return Response(status=status.HTTP_403_FORBIDDEN)
        else:
            movie = Movie.objects.get(id=movie_id)
            movie.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
