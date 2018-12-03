# users/views.py
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView, CreateView
from .models import Usuario, Estudiante, Tutor
from django.shortcuts import redirect, render
from .forms import StudentSignUpForm, TutorSignUpForm


def login(request):
    return render(request, 'login.html')

class SignUp(generic.CreateView):
    form_class = StudentSignUpForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
def home(request):
    if request.user.is_authenticated:
        if request.user.is_tutor:
            return redirect('../core/lista_campus.html')
        else:
            return redirect('../core/lista_campus.html')
    return render(request, '../core/home_page.html')

class EstudianteSignUpView(CreateView):
    model = Usuario
    form_class = StudentSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('')

class TutorSignUpView(CreateView):
    model = Usuario
    form_class = TutorSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'tutor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('')

'''
@method_decorator([login_required, estudiante_required], name='dispatch')
class StudentInterestsView(UpdateView):
    model = Estudiante
    form_class = StudentInterestsForm
    template_name = 'classroom/students/interests_form.html'
    success_url = reverse_lazy('students:quiz_list')

    def get_object(self):
        return self.request.user.student

    def form_valid(self, form):
        messages.success(self.request, 'Interests updated with success!')
        return super().form_valid(form)


@method_decorator([login_required, student_required], name='dispatch')
class QuizListView(ListView):
    model = Quiz
    ordering = ('name', )
    context_object_name = 'quizzes'
    template_name = 'classroom/students/quiz_list.html'

    def get_queryset(self):
        student = self.request.user.student
        student_interests = student.interests.values_list('pk', flat=True)
        taken_quizzes = student.quizzes.values_list('pk', flat=True)
        queryset = Quiz.objects.filter(subject__in=student_interests) \
            .exclude(pk__in=taken_quizzes) \
            .annotate(questions_count=Count('questions')) \
            .filter(questions_count__gt=0)
        return queryset


@method_decorator([login_required, student_required], name='dispatch')
class TakenQuizListView(ListView):
    model = TakenQuiz
    context_object_name = 'taken_quizzes'
    template_name = 'classroom/students/taken_quiz_list.html'

    def get_queryset(self):
        queryset = self.request.user.student.taken_quizzes \
            .select_related('quiz', 'quiz__subject') \
            .order_by('quiz__name')
return queryset
'''