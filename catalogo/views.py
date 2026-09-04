from django.http import HttpResponse

def bienvenida(request):
    html = """
    <html>
        <head><title>API Películas y Series</title></head>
        <body>
            <h1>Bienvenido a la API de Películas y Series</h1>
            <p>Este es el sistema centralizado para la gestión de contenido multimedia y registros históricos.</p>
        </body>
    </html>
    """
    return HttpResponse(html)

# NUEVA VISTA PARA EL ERROR 404
def mi_error_404(request, exception):
    html = """
    <html>
        <head><title>Error 404 - API Multimedia</title></head>
        <body>
            <h1>Error 404 - Página no encontrada</h1>
            <p>Lo sentimos, la ruta que intentas consultar en nuestra API de Películas y Series no existe.</p>
        </body>
    </html>
    """
    # Es importante devolver el status=404 para que el navegador sepa que es un error real
    return HttpResponse(html, status=404)