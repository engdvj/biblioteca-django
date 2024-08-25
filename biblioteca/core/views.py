from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from django.http import JsonResponse
from .models import Autor, Categoria, Livro
from .serializers import LivroSerializer, AutorSerializer, CategoriaSerializer
import json

# Views para Livros

@csrf_exempt
def livro_list_create(request):
    if request.method == 'GET':
        livros = Livro.objects.all()
        serializer = LivroSerializer(livros, many=True)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})  # Garantir UTF-8

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            serializer = LivroSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, json_dumps_params={'ensure_ascii': False})
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON inválido'}, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def livro_detail(request, pk):
    try:
        livro = Livro.objects.get(pk=pk)
    except Livro.DoesNotExist:
        return JsonResponse({'error': 'Livro não encontrado'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LivroSerializer(livro)
        return JsonResponse(serializer.data, json_dumps_params={'ensure_ascii': False})

    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            serializer = LivroSerializer(livro, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, json_dumps_params={'ensure_ascii': False})
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON inválido'}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        livro.delete()
        return JsonResponse({'message': 'Livro deletado com sucesso'}, status=status.HTTP_204_NO_CONTENT)

# Views para Autores

@csrf_exempt
def autor_list_create(request):
    if request.method == 'GET':
        autores = Autor.objects.all()
        serializer = AutorSerializer(autores, many=True)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})  # Garantir UTF-8

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            serializer = AutorSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, json_dumps_params={'ensure_ascii': False})
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON inválido'}, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def autor_detail(request, pk):
    try:
        autor = Autor.objects.get(pk=pk)
    except Autor.DoesNotExist:
        return JsonResponse({'error': 'Autor não encontrado'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AutorSerializer(autor)
        return JsonResponse(serializer.data, json_dumps_params={'ensure_ascii': False})

    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            serializer = AutorSerializer(autor, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, json_dumps_params={'ensure_ascii': False})
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON inválido'}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        autor.delete()
        return JsonResponse({'message': 'Autor deletado com sucesso'}, status=status.HTTP_204_NO_CONTENT)

# Views para Categorias

@csrf_exempt
def categoria_list_create(request):
    if request.method == 'GET':
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})  # Garantir UTF-8

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            serializer = CategoriaSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, json_dumps_params={'ensure_ascii': False})
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON inválido'}, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def categoria_detail(request, pk):
    try:
        categoria = Categoria.objects.get(pk=pk)
    except Categoria.DoesNotExist:
        return JsonResponse({'error': 'Categoria não encontrada'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategoriaSerializer(categoria)
        return JsonResponse(serializer.data, json_dumps_params={'ensure_ascii': False})

    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            serializer = CategoriaSerializer(categoria, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, json_dumps_params={'ensure_ascii': False})
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON inválido'}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        categoria.delete()
        return JsonResponse({'message': 'Categoria deletada com sucesso'}, status=status.HTTP_204_NO_CONTENT)
