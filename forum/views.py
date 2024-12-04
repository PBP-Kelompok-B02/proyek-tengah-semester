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
    # Ambil parameter query string dari request
    query = request.GET.get('query', '')  # Untuk pencarian berdasarkan judul/deskripsi
    sort = request.GET.get('sort', 'created_at')  # Default sorting by created_at
    sort_order = request.GET.get('order', 'desc')  # Default descending order

    # Ambil semua data forum
    forums = Forum.objects.all()

    # Filter berdasarkan query
    if query:
        forums = forums.filter(title__icontains=query) | forums.filter(description__icontains=query)

    # Sorting data
    if sort_order == 'asc':
        forums = forums.order_by(sort)  # Ascending order
    else:
        forums = forums.order_by(f'-{sort}')  # Descending order

    # Ambil semua reply yang terkait dengan forum menggunakan prefetch_related
    forums = forums.prefetch_related('reply_set')

    # Konversi data forum dan reply ke format JSON
    data = []
    for forum in forums:
        replies = list(forum.reply_set.values(
            'id', 'content', 'created_at', 'created_by__username'
        ))

        data.append({
            'id': forum.id,
            'title': forum.title,
            'description': forum.description,
            'created_at': forum.created_at,
            'created_by': forum.created_by.username,
            'replies': replies,  # Menambahkan data reply
        })

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