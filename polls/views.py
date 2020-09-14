from django.shortcuts import render, redirect
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render


from .models import Question, Choice
from .models import Post, Comment





def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    dataIn = request.POST.copy()
    try:
        question = Question.objects.get(id=question_id)
        if int(dataIn['choice']) == 10:
            currentVotes = question.notMuchVotes
            question.notMuchVotes = currentVotes + 1
        else:
            currentVotes = question.theSkyeVotes
            question.theSkyeVotes = currentVotes + 1
        question.save()
    except:
        pass


    question = get_object_or_404(Question, pk=question_id)
    
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

def makeComment(request):
    someData = {}
    someData['anyData'] = 'anyValue'
    someData['posts'] = Question.objects.order_by('-pub_date')[:5]
    # someData['anyData'] = 'anyValue'
    # someData['anyData'] = 'anyValue'
    # someData['anyData'] = 'anyValue'
    # someData['anyData'] = 'anyValue'

    return render(request, 'polls/make-comment.html', someData)



def postComment(request):
    dataIn = request.POST.copy()
    post = dataIn['post']
    name = dataIn['name']
    comments = dataIn['comments']


    commentModel = Comment()
    commentModel.post = Question.objects.get(id=post)
    commentModel.author = name
    commentModel.text = comments
    commentModel.save()

    return redirect('/polls/comments/list/')


def commentLists(request):
    someData = {}
    someData['anyData'] = 'anyValue'
    someData['comments'] = Comment.objects.order_by('-created_date')
    # someData['anyData'] = 'anyValue'
    # someData['anyData'] = 'anyValue'
    # someData['anyData'] = 'anyValue'
    # someData['anyData'] = 'anyValue'

    # print(someData)

    return render(request, 'polls/comment-lists.html', someData)

  

