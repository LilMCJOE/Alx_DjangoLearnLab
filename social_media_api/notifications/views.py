from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Notification

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_notifications(request):
    notifications = request.user.notifications.all().order_by('-timestamp')
    # Serialize notifications as needed
    serializer = NotificationSerializer(notifications, many=True)  # Create NotificationSerializer
    return Response(serializer.data)
