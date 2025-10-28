from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Job
from .serializers import JobSerializer, MyTokenObtainPairSerializer
from .authentication import HRJWTAuthentication

# HR Login — to get JWT token
@api_view(['POST'])
@permission_classes([AllowAny])
def hr_login(request):
    serializer = MyTokenObtainPairSerializer(data=request.data)
    if serializer.is_valid():
        return Response(serializer.validated_data)
    return Response(serializer.errors, status=400)


# Post a new job (only HR)
@api_view(['POST'])
@authentication_classes([HRJWTAuthentication])
@permission_classes([IsAuthenticated])
def create_job(request):
    serializer = JobSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


# Get all jobs
@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_jobs(request):
    jobs = Job.objects.all()
    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data)


# Get job by ID
@api_view(['GET'])
@permission_classes([AllowAny])
def get_job_by_id(request, id):
    try:
        job = Job.objects.get(job_id=id)
    except Job.DoesNotExist:
        return Response({"error": "Job not found"}, status=404)
    serializer = JobSerializer(job)
    return Response(serializer.data)


# Get job by title
@api_view(['GET'])
@permission_classes([AllowAny])
def get_job_by_title(request, title):
    jobs = Job.objects.filter(job_title__icontains=title)
    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data)
