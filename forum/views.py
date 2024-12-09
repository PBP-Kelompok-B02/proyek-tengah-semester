import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .models import Forum, Reply

# Create your views here.
def show_forum(request):
    user = request.user
    forums = Forum.objects.all().order_by('-created_at')

    context = {
        'user': user,
        'forums': forums,
    }
    return render(request, 'forum.html', context)

def show_json(request):

     # Ambil semua data forum
    forums = Forum.objects.prefetch_related('replies').all()

    # Ambil parameter query string dari request
    query = request.GET.get('query', '')  # Untuk pencarian berdasarkan judul/deskripsi
    sort = request.GET.get('sort', 'created_at')  # Default sorting by created_at
    sort_order = request.GET.get('order', 'desc')  # Default descending order

   
    # Filter berdasarkan query
    if query:
        forums = forums.filter(title__icontains=query) | forums.filter(description__icontains=query) | forums.filter(reply__content__icontains=query)

    # Sorting data
    if sort_order == 'asc':
        forums = forums.order_by(sort)  # Ascending order
    else:
        forums = forums.order_by(f'-{sort}')  # Descending order

    # Konversi data forum dan reply ke format JSON
    data = []
    for forum in forums:
        forum_data = {
            'id': forum.id,
            'title': forum.title,
            'description': forum.description,
            'created_at': forum.created_at,
            'created_by': forum.created_by.username,
            'replies': []
        }

        # Gunakan replies (sesuai related_name)
        replies = forum.replies.all().order_by('created_at')
        for reply in replies:
            reply_data = {
                'id': reply.id,
                'content': reply.content,
                'created_at': reply.created_at,
                'created_by': reply.created_by.username
            }
            forum_data['replies'].append(reply_data)

        data.append(forum_data)

    return JsonResponse(data, safe=False)

@login_required
def create_forum(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        # Buat topik diskusi baru dan assign created_by dengan request.user
        Forum.objects.create(
            title=title,
            description=description,
            created_by=request.user  # Tambahkan user sebagai pembuat
        )

        # Redirect setelah forum berhasil dibuat
        return redirect('forum:show_forum')
    return render(request, 'create_forum.html')

def submit_forum(request):
    if request.method == 'POST':
        # Handle form submission here
        title = request.POST.get('title')
        description = request.POST.get('description')

        if title and description:
            new_forum = Forum.objects.create(
                title=title,
                description=description,
                created_by=request.user  # Menggunakan user yang sudah login
            )
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid data'})
    
    return JsonResponse({'success': False, 'message': 'Invalid request'})

@login_required
@require_POST
def delete_forum(request, forum_id):
    forum = get_object_or_404(Forum, id=forum_id, created_by=request.user)
    forum.delete()
    return JsonResponse({'success': True})

@login_required
@require_POST
def reply_forum(request, forum_id):
    forum = get_object_or_404(Forum, id=forum_id)
    content = request.POST.get('content')
    
    if content:
        reply = Reply.objects.create(
            forum=forum,
            created_by=request.user,
            content=content
        )
        
        return JsonResponse({
            'success': True,
            'reply': {
                'id': reply.id,
                'content': reply.content,
                'username': reply.created_by.username,
            }
        })
    return JsonResponse({'success': False, 'error': 'Content is required'}, status=400)


@login_required
@require_POST
def delete_reply(request, reply_id):
    reply = get_object_or_404(Reply, id=reply_id, created_by=request.user)
    reply.delete()
    return JsonResponse({'success': True})

@csrf_exempt
def submit_forum_mobile(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            title = data['title']
            description = data['description']

            new_forum = Forum.objects.create(
                title=title,
                description=description,
                created_by=request.user
            )
            
            return JsonResponse({
                "status": "success",
                "message": "Forum created successfully",
                "forum": {
                    "id": new_forum.id,
                    "title": new_forum.title,
                    "description": new_forum.description,
                }
            })
        except Exception as e:
            return JsonResponse({
                "status": "error",
                "message": str(e)
            })
    return JsonResponse({"status": "error", "message": "Invalid request method"})

@csrf_exempt
def reply_forum_mobile(request, forum_id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            content = data['content']
            forum = Forum.objects.get(id=forum_id)
            
            reply = Reply.objects.create(
                forum=forum,
                content=content,
                created_by=request.user
            )
            
            return JsonResponse({
                "status": "success",
                "message": "Reply added successfully",
                "reply": {
                    "id": reply.id,
                    "content": reply.content,
                }
            })
        except Exception as e:
            return JsonResponse({
                "status": "error",
                "message": str(e)
            })
    return JsonResponse({"status": "error", "message": "Invalid request method"})

@csrf_exempt
def delete_forum_mobile(request, forum_id):
    if request.method == 'POST':
        try:
            forum = get_object_or_404(Forum, id=forum_id, created_by=request.user)
            forum.delete()
            return JsonResponse({
                "status": "success",
                "message": "Forum deleted successfully"
            })
        except Exception as e:
            return JsonResponse({
                "status": "error",
                "message": str(e)
            })
    return JsonResponse({"status": "error", "message": "Invalid request method"})

@csrf_exempt
def delete_reply_mobile(request, reply_id):
    if request.method == 'POST':
        try:
            reply = get_object_or_404(Reply, id=reply_id, created_by=request.user)
            reply.delete()
            return JsonResponse({
                "status": "success",
                "message": "Reply deleted successfully"
            })
        except Exception as e:
            return JsonResponse({
                "status": "error",
                "message": str(e)
            })
    return JsonResponse({"status": "error", "message": "Invalid request method"})