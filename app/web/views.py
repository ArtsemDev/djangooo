from django.views.decorators.http import require_POST
from django.views.generic import ListView, DetailView
from django.http.response import HttpResponseRedirect

from .forms import CommentForm, FeedbackForm
from .models import Post


class PostListView(ListView):
    model = Post
    ordering = "-date_created"
    template_name = "post-list.html"
    paginate_by = 2

    def get_ordering(self):
        order_by = self.request.GET.get("order_by")

        if not order_by:
            return self.ordering

        if hasattr(self.model, order_by.removeprefix("-")):
            return order_by

        return self.ordering


class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
    extra_context = {
        "comment_form": CommentForm(),
        "feedback_form": FeedbackForm(),
    }


@require_POST
def process_comment(request, slug):
    form = CommentForm(request.POST)
    print(form.is_valid(), "comment")
    return HttpResponseRedirect(redirect_to=request.headers.get("Referer"))


@require_POST
def process_feedback(request, slug):
    print(request.headers)
    form = FeedbackForm(request.POST)
    print(form.is_valid(), "feedback")
    return HttpResponseRedirect(redirect_to=request.headers.get("Referer"))
