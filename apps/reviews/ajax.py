from dajax.core import dajax

def like(request, id):
    if request.method == 'POST':
        dajax = Dajax()
        user = request.user
        review = get_object_or_404(Review, id=id)
        like = Like.objects.get_or_create(review_id=review.id)

        try:
            user_liked = Like.objects.get(user=user, review_id=review.id)
        except:
            user_liked = None

        if user_liked:
            user_liked.total_likes -= 1
            user_liked.user.remove(request.user)
            user_liked.save()

        else:
            list(like)
            like[0].user.add(request.user)
            like[0].total_likes += 1
            like[0].save()

    return redirect(reverse_lazy('reviews:review_list'))
