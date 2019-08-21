from .models import Category


def get_categories_tree(request, parent=None, join_posters=False):
    # if not request.user_acl['visible_categories']:
    #     return []

    if parent:
        queryset = parent.get_descendants().order_by('lft')
    else:
        queryset = Category.objects.all_categories()
    
    # queryset_with_acl = queryset.filter(id__in=request.user_acl['visible_categories'])
    # if join_posters:
    #     print('quang')
    #     # ken = queryset_with_acl
    # print('kakak', queryset_with_acl)
        
    flat_list = []

    return flat_list
