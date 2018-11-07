from django.shortcuts import render

from datetime import datetime

posts = [
    {
        'title': 'Mont blanc',
        'user' : {
            'name': 'Yosh',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/600/?random'
    },
    {
        'title': 'Title 1',
        'user': {
            'name': 'Yosh',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/600/?random'
    },
    {
        'title': 'Title 2',
        'user': {
            'name': 'Yosh',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/600/?random'
    },
    {
        'title': 'Title 3',
        'user': {
            'name': 'Yosh',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/600/?random'
    }, 
]

# Create your views here.
def list_posts(request):
    return render(request, 'posts/feed.html', {'posts': posts})

    