from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model


User = get_user_model()

@api_view()
def mention_suggestions(request):
    suggestions = []

    query = request.query_params.get("q", "").lower().strip()[:100]
    if query:
        queryset = User.objects.filter(username__startswith=query, is_active=True).order_by(
            "username"
        )[:10]
        print(queryset)
        for user in queryset:
            try:
                avatar = user
            except:
                pass
            suggestions.append({"username": user.username, "avatar": avatar})
    else:
        pass
    return Response({'kim':'hahami'})
