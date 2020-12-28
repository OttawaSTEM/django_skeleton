from django.views.generic.base import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"

async def websocket_view(socket):
    await socket.accept()
    # await socket.send_text('Hello from web server!')
    # await socket.close()

    while True:
        message = await socket.receive_text()
        await socket.send_text(f'Web server got this "{message}"!')