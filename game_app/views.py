import json

from django.http import JsonResponse
from django.db.models import Q, F

from rest_framework.generics import *
from rest_framework import status, response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated


from .serializers import *
from .permission import ModeratorPermission


# ----- Studio ---- #

@permission_classes([IsAuthenticated, ModeratorPermission, ])
class StudioViewSet(ModelViewSet):
    """ Метаконтроллер для работы с StudioSerializer: Create, Update(patch) and Delete """

    queryset = Studio.objects.all()
    serializer_class = StudioSerializer
    http_method_names = ["post", "patch", "delete"]


class StudioDetailView(RetrieveAPIView):
    """ Класс-контроллер(generic) для организации GET-запросов StudioSerializer:
            вывода информации о конкретной студии """

    queryset = Studio.objects.all()
    serializer_class = StudioSerializer


class StudioListFilterViews(ListAPIView):
    """ Класс-контроллер(generic) для организации GET-запросов StudioSerializer:
        вывода списка студий, фильтрация по ключевым параметрам """

    queryset = Studio.objects.all()
    serializer_class = StudioSerializer

    def get(self, request, *args, **kwargs):

        search_name = request.GET.get('name', None)

        if search_name:
            self.queryset = self.queryset.filter(
                name__icontains=search_name
            )

        return super().get(request, *args, **kwargs)


# ----- Author ---- #

@permission_classes([IsAuthenticated, ModeratorPermission, ])
class AuthorViewSet(ModelViewSet):
    """ Метаконтроллер для работы с AuthorSerializer: Create, Update(patch) and Delete """

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    http_method_names = ["post", "patch", "delete"]


class AuthorDetailView(RetrieveAPIView):
    """ Класс-контроллер(generic) для организации GET-запросов AuthorSerializer:
            вывода информации о конкретном авторе """

    queryset =Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorListFilterViews(ListAPIView):
    """ Класс-контроллер(generic) для организации GET-запросов AuthorSerializer:
        вывода списка авторов, фильтрация по ключевым параметрам """

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get(self, request, *args, **kwargs):

        search_author_q = None

        # Поиск по имени:
        search_name = request.GET.get("name", None)
        if search_name:
            if search_author_q is None:
                search_author_q = Q(name__icontains=search_name)
            else:
                search_author_q |= Q(name__icontains=search_name)

        # Поиск по возрасту:
        search_age = request.GET.get("age", None)
        if search_age:
            if search_author_q is None:
                search_author_q = Q(age__icontains=search_age)
            else:
                search_author_q |= Q(age__icontains=search_age)

        # Поиск по стране:
        search_country = request.GET.get("country", None)
        if search_country:
            if search_author_q is None:
                search_author_q = Q(country__icontains=search_country)
            else:
                search_author_q |= Q(country__icontains=search_country)

        if search_author_q:
            self.queryset = self.queryset.filter(search_author_q)

        return super().get(request, *args, **kwargs)


# ----- Genre ----- #

@permission_classes([IsAuthenticated, ModeratorPermission, ])
class GenreViewSet(ModelViewSet):
    """ Метаконтроллер для работы с GenreSerializer: Create, Update(patch) and Delete """

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    http_method_names = ["post", "patch", "delete"]


class GenreDetailView(RetrieveAPIView):
    """ Класс-контроллер(generic) для организации GET-запросов GenreSerializer:
            вывода информации о конкретном жанре """

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreListFilterViews(ListAPIView):
    """ Класс-контроллер(generic) для организации GET-запросов GenreSerializer:
        вывода списка жанров, фильтрация по ключевым параметрам """

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    def get(self, request, *args, **kwargs):

        search_name = request.GET.get('name', None)

        if search_name:
            self.queryset = self.queryset.filter(
                name__icontains=search_name
            )

        return super().get(request, *args, **kwargs)


# --- SystemRequirements -----#

@permission_classes([IsAuthenticated, ModeratorPermission, ])
class SystemRequirementsViewSet(ModelViewSet):
    """ Метаконтроллер для работы с SystemRequirementsSerializer: Create, Update(patch) and Delete """

    queryset = SystemRequirements.objects.all()
    serializer_class = SystemRequirementsSerializer
    http_method_names = ["post", "patch", "delete"]


class SystemRequirementsDetailView(RetrieveAPIView):
    """ Класс-контроллер(generic) для организации GET-запросов SystemRequirementsSerializer:
            вывода информации о конкретном системном требовании """

    queryset = SystemRequirements.objects.all()
    serializer_class = SystemRequirementsSerializer


class SystemRequirementsListFilterViews(ListAPIView):
    """ Класс-контроллер(generic) для организации GET-запросов SystemRequirementsSerializer:
        вывода списка жанров, фильтрация по ключевым параметрам """

    queryset = SystemRequirements.objects.all()
    serializer_class = SystemRequirementsSerializer

    def get(self, request, *args, **kwargs):

        search_sys_req_q = None

        # Поиск по GPU:
        search_cpu = request.GET.get("cpu", None)
        if search_cpu:
            if search_sys_req_q is None:
                search_sys_req_q = Q(name_cpu__icontains=search_cpu)
            else:
                search_sys_req_q |= Q(name_cpu__icontains=search_cpu)

        # Поиск по GPU:
        search_gpu = request.GET.get("gpu", None)
        if search_gpu:
            if search_sys_req_q is None:
                search_sys_req_q = Q(name_gpu__icontains=search_gpu)
            else:
                search_sys_req_q |= Q(name_gpu__icontains=search_gpu)

        # Поиск по RAM:
        search_ram = request.GET.get("ram", None)
        if search_ram:
            if search_sys_req_q is None:
                search_sys_req_q = Q(amount_type_memory__icontains=search_ram)
            else:
                search_sys_req_q |= Q(amount_type_memory__icontains=search_ram)

        # Поиск по OS:
        search_os = request.GET.get("os", None)
        if search_os:
            if search_sys_req_q is None:
                search_sys_req_q = Q(os__icontains=search_os)
            else:
                search_sys_req_q |= Q(os__icontains=search_os)

        if search_sys_req_q:
            self.queryset = self.queryset.filter(search_sys_req_q)

        return super().get(request, *args, **kwargs)


# --- Game -----#

class GameDetailView(RetrieveAPIView):
    """ Класс-контроллер(generic) для организации GET-запросов GameSerializer:
            вывода информации о конкретной игре """

    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GameListFilterViews(ListAPIView):
    """ Класс-контроллер(generic) для организации GET-запросов SystemRequirementsSerializer:
        вывода списка жанров, фильтрация по ключевым параметрам """

    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def get(self, request, *args, **kwargs):

        search_game_q = None

        # Поиск по name:
        search_name = request.GET.get("name", None)
        if search_name:
            if search_game_q is None:
                search_game_q = Q(name__icontains=search_name)
            else:
                search_game_q |= Q(name__icontains=search_name)

        # Поиск по studio:
        search_studio = request.GET.get("studio", None)
        if search_studio:
            if search_game_q is None:
                search_game_q = Q(studio__icontains=search_studio)
            else:
                search_game_q |= Q(studio__icontains=search_studio)

        # Поиск по author:
        search_author = request.GET.get("author", None)
        if search_author:
            if search_game_q is None:
                search_game_q = Q(country__icontains=search_author)
            else:
                search_game_q |= Q(country__icontains=search_author)

        # Поиск по author:
        search_genre = request.GET.get("genre", None)
        if search_author:
            if search_game_q is None:
                search_game_q = Q(genre__icontains=search_genre)
            else:
                search_game_q |= Q(genre__icontains=search_genre)

        if search_game_q:
            self.queryset = self.queryset.filter(search_game_q)

        return super().get(request, *args, **kwargs)


@permission_classes([IsAuthenticated, ModeratorPermission, ])
class GameCreateViews(CreateAPIView):
    """ Класс-контроллер(generic) для организации CREATE-запросов GameSerializer (создании страницы об игре) """

    queryset = Game
    serializer_class = GameSerializer

    # POST: создание новой статьи про игру
    def post(self, request, *args, **kwargs):

        data_game = json.loads(request.body)

        game_create = Game.objects.create(
            name=data_game['name'],
            descriptions=data_game['descriptions'],
            date_release=data_game['date_release'],
            price=data_game['price'],
        )

        name_cpu, studio_game, author_game, genre_game = None, None, None, None

        if 'system_requirements' in data_game:
            name_cpu = SystemRequirements.objects.get(name_cpu=data_game['system_requirements'])
            game_create.system_requirements = name_cpu

        if 'studio' in data_game:
            studio_game = Studio.objects.get(name=data_game['studio'])
            studio_game.game_set.add(game_create)

        if 'author' in data_game:
            author_game = Author.objects.get(name=data_game['author'])
            author_game.game_set.add(game_create)

        if 'genre' in data_game:
            genre_game = Genre.objects.get(name=data_game['genre'])
            genre_game.game_set.add(game_create)

        if name_cpu and studio_game and author_game and genre_game:
            game_json = {
                'name': game_create.name,
                'descriptions': game_create.descriptions,
                'studio': game_create.studio.name,
                'author': game_create.author.name,
                'genre': game_create.genre.name,
                'date_release': game_create.date_release,
                'system_requirements': game_create.system_requirements.name_cpu,
                'price': game_create.price
            }
        else:
            game_json = {
                'name': game_create.name,
                'descriptions': game_create.descriptions,
                'date_release': game_create.date_release,
                'price': game_create.price
            }

        serializer = GameCreateSerializer(game_json)

        return response.Response(serializer.data, status=status.HTTP_201_CREATED)


@permission_classes([IsAuthenticated, ModeratorPermission, ])
class GameUpdateViews(UpdateAPIView):
    """ Класс-контроллер(generic) для организации CREATE-запросов GameSerializer (обновлении страницы об игре) """

    queryset = Game
    serializer_class = GameSerializer


@permission_classes([IsAuthenticated, ModeratorPermission])
class GameDestroyView(DestroyAPIView):
    """ Класс-контроллер(generic) для организации DELETE-запросов GameSerializer (удаление страницы об игре) """

    queryset = Game.objects.all()
    serializer_class = GameSerializer


@permission_classes([IsAuthenticated, ])
class GameLikeViews(UpdateAPIView):
    """ Класс-контроллер(generic) для организации PUT-запросов GameSerializer (обновление игр) """

    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def put(self, request, *args, **kwargs):

        like_data = request.GET.get('status', None)

        if like_data:
            if 'up' in like_data:
                Game.objects.filter(pk__in=request.data).update(like=F('like') + 1)
            elif 'down' in like_data:
                Game.objects.filter(pk__in=request.data).update(like=F('like') - 1)

        return JsonResponse(
            GameSerializer(Game.objects.filter(pk__in=request.data), many=True).data,
            safe=False
        )
