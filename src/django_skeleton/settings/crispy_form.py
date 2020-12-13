# Crispy Form Theme - Bootstrap 4
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# For Bootstrap 4, change error alert to 'danger'
from django.contrib import messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}