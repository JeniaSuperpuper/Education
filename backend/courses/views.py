from .serializers import CategorySerializer, Category, CourseSerializer, Course, LessonSerializer, Lesson
from rest_framework import generics, mixins
from django.shortcuts import get_object_or_404


class CategoryList(generics.ListCreateAPIView):
    """
    API endpoint для получения списка всех категорий или создания новой категории.

    GET: Возвращает список всех категорий.
    POST: Создает новую категорию.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint для получения, обновления или удаления категории по её ID.

    GET: Возвращает детали категории.
    PUT: Обновляет категорию.
    PATCH: Частично обновляет категорию.
    DELETE: Удаляет категорию.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CourseList(generics.ListCreateAPIView):
    """
    API endpoint для получения списка всех курсов или создания нового курса.

    GET: Возвращает список всех курсов.
    POST: Создает новый курс.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint для получения, обновления или удаления курса по его ID.

    GET: Возвращает детали курса.
    PUT: Обновляет курс.
    PATCH: Частично обновляет курс.
    DELETE: Удаляет курс.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CategoryCourseList(mixins.ListModelMixin, generics.GenericAPIView):
    """
    API endpoint для получения списка курсов в указанной категории.

    GET: Возвращает список курсов, относящихся к указанной категории.
    """
    serializer_class = CourseSerializer

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        category = get_object_or_404(Category, slug=category_slug)
        return Course.objects.filter(category=category)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CategoryCourseDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    """
    API endpoint для получения деталей курса в указанной категории.

    GET: Возвращает детали курса, относящегося к указанной категории.
    """
    serializer_class = CourseSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        course_slug = self.kwargs['slug']
        category = get_object_or_404(Category, slug=category_slug)
        get_object_or_404(Course, slug=course_slug, category=category)
        return Course.objects.filter(slug=course_slug, category=category)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class LessonList(generics.ListCreateAPIView):
    """
    API endpoint для получения списка всех уроков или создания нового урока.

    GET: Возвращает список всех уроков.
    POST: Создает новый урок.
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint для получения, обновления или удаления урока по его ID.

    GET: Возвращает детали урока.
    PUT: Обновляет урок.
    PATCH: Частично обновляет урок.
    DELETE: Удаляет урок.
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class CategoryCourseLessonsList(mixins.ListModelMixin, generics.GenericAPIView):
    """
    API endpoint для получения списка уроков в указанном курсе и категории.

    GET: Возвращает список уроков, относящихся к указанному курсу и категории.
    """
    serializer_class = LessonSerializer

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        course_slug = self.kwargs['course_slug']
        category = get_object_or_404(Category, slug=category_slug)
        course = get_object_or_404(Course, slug=course_slug, category=category)
        return Lesson.objects.filter(course=course)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CategoryCourseLessonsDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    """
    API endpoint для получения деталей урока в указанном курсе и категории.

    GET: Возвращает детали урока, относящегося к указанному курсу и категории.
    """
    serializer_class = LessonSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        course_slug = self.kwargs['course_slug']
        lesson_slug = self.kwargs['slug']
        category = get_object_or_404(Category, slug=category_slug)
        course = get_object_or_404(Course, slug=course_slug, category=category)
        get_object_or_404(Lesson, course=course, slug=lesson_slug)
        return Lesson.objects.filter(course=course, slug=lesson_slug)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)