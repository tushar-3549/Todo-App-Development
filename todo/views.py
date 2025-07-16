from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Task

from .forms import TaskForm

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer

# Create your views here.
def home(request):

    tasks = Task.objects.all()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in.")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('home')
    else:   
        return render(request, 'home.html', {'tasks': tasks})


def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, "You have been Logged Out..")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1'] 
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully registered! Welcome!")
            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'register.html', {'form': form})


def individual_task(request, pk):
    if request.user.is_authenticated:
        individual_task = Task.objects.get(id=pk)
        return render(request, 'task.html', {'individual_task': individual_task})
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('home')


def delete_task(request, pk):
    if request.user.is_authenticated:
        delete_it = Task.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Task Deleted Successfully...")
        return redirect('home')
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('home')



def add_task(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = TaskForm(request.POST)
            if form.is_valid():
                task = form.save(commit=False)
                task.user = request.user 
                task.save()
                messages.success(request, "Task added successfully.")
                return redirect('home')
        else:
            form = TaskForm()
        return render(request, 'add_task.html', {'form': form})
    else:
        messages.error(request, "You must be logged in to add a task.")
        return redirect('home')



def edit_task(request, pk):
    if request.user.is_authenticated:
        task = Task.objects.get(id=pk)
        form = TaskForm(instance=task)

        if request.method == 'POST':
            form = TaskForm(request.POST, instance=task)
            if form.is_valid():
                form.save()
                messages.success(request, "Task updated successfully.")
                return redirect('home')

        return render(request, 'edit_task.html', {'form': form, 'task': task})
    else:
        messages.error(request, "You must be logged in to edit a task.")
        return redirect('home')





# ---------- DRF API VIEWS ----------
class RegisterAPI(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'message': 'User registered successfully.',
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginAPI(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'message': 'Login successful.',
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            })
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)



from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
