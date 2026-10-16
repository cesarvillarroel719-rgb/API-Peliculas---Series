from django.http import HttpResponse
from rest_framework import viewsets
from .models import Pelicula, Serie
from .serializers import PeliculaSerializer, SerieSerializer

# --- VISTAS DE LA API REST (CRUD COMPLETO) ---

class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer

class SerieViewSet(viewsets.ModelViewSet):
    queryset = Serie.objects.all()
    serializer_class = SerieSerializer


# --- VISTAS HTML EXISTENTES ---

def bienvenida(request):
    html = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>API Películas y Series</title>
        <style>
            * {
                padding: 0;
                margin: 0;
                box-sizing: border-box;
            }

            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%);
                color: #f8fafc;
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 20px;
            }

            .container {
                background: rgba(30, 41, 59, 0.7);
                backdrop-filter: blur(10px);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 16px;
                padding: 40px;
                max-width: 600px;
                width: 100%;
                text-align: center;
                box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.3), 0 10px 10px -5px rgba(0, 0, 0, 0.2);
            }

            .badge {
                background-color: #6366f1;
                color: #ffffff;
                font-size: 0.85rem;
                font-weight: 600;
                padding: 6px 12px;
                border-radius: 20px;
                text-transform: uppercase;
                letter-spacing: 1px;
                display: inline-block;
                margin-bottom: 20px;
            }

            h1 {
                font-size: 2.5rem;
                margin-bottom: 15px;
                font-weight: 700;
                background: linear-gradient(to right, #818cf8, #c084fc);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }

            p {
                color: #94a3b8;
                font-size: 1.1rem;
                line-height: 1.6;
                margin-bottom: 30px;
            }

            .features {
                display: flex;
                justify-content: center;
                flex-wrap: wrap;
                gap: 15px;
                margin-bottom: 35px;
            }

            .feature-tag {
                background: rgba(255, 255, 255, 0.05);
                border: 1px solid rgba(255, 255, 255, 0.1);
                padding: 8px 16px;
                border-radius: 8px;
                font-size: 0.9rem;
                color: #cbd5e1;
            }

            .btn-status {
                display: inline-block;
                background-color: #22c55e;
                color: #ffffff;
                font-weight: 600;
                padding: 12px 24px;
                border-radius: 8px;
                text-decoration: none;
                box-shadow: 0 4px 6px -1px rgba(34, 197, 94, 0.3);
            }

            .footer {
                margin-top: 30px;
                font-size: 0.85rem;
                color: #64748b;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <span class="badge">Backend Django Activo</span>
            <h1>API Películas y Series</h1>
            <p>Este es el sistema centralizado para la gestión de contenido multimedia y registros históricos.</p>
            
            <div class="features">
                <span class="feature-tag">🎬 Películas</span>
                <span class="feature-tag">📺 Series</span>
                <span class="feature-tag">🛡️ Rutas Protegidas</span>
            </div>

            <span class="btn-status">● Sistema Operativo</span>

            <div class="footer">
                Desarrollado para Evaluación Django
            </div>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)

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
    return HttpResponse(html, status=404)