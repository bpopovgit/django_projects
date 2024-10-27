from authors.models import Author


def author_profile_exists(request):
    profile_exists = Author.objects.exists()
    return {'author_profile_exists': profile_exists}
