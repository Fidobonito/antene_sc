Antenes SC es una aplicación que permite a los usuarios gestionar servidores en la nube. Cada servidor creado contiene un entorno virtual (emulador) que sigue funcionando incluso después de que el usuario haya salido.

Los usuarios pueden:

-Registrarse o iniciar sesión con su cuenta de Facebook, Google o número de teléfono.
-Crear y gestionar servidores ilimitados.
-Realizar operaciones directamente en los servidores.

  Requisitos Previos

Python 3.7 o superior
Flask (instalado desde pip)
Navegador web para probar la aplicación

Instalación

Clona este repositorio o descarga los archivos.
Instala las dependencias:
bash
Copiar código
pip install -r requirements.txt
Inicia el servidor:
bash
Copiar código
python app.py
Abre tu navegador y visita http://localhost:5000.
Características
Inicio de Sesión: Soporte para Facebook, Google y autenticación con número telefónico.
Creación de Servidores: Los usuarios pueden crear múltiples servidores nombrados automáticamente (Servidor 1, Servidor 2, etc.).
Persistencia de Datos: Los servidores siguen funcionando incluso si el usuario cierra sesión.
Archivos Principales
app.py
El backend principal de la aplicación, implementado con Flask. Este archivo gestiona rutas, autenticación y operaciones de servidor.

templates/
Carpeta con las vistas HTML. Contiene:

index.html: Página de bienvenida.
login.html: Página de inicio de sesión.
servers.html: Página de gestión de servidores.
static/
Carpeta de recursos estáticos que incluye:

styles.css: Estilos para la interfaz de usuario.
scripts.js: Funciones para gestionar servidores.
requirements.txt
Lista de las dependencias necesarias para ejecutar el proyecto.

Próximas Mejoras
Integrar emuladores reales para cada servidor.
Implementar soporte para dispositivos iOS.
Mejorar la interfaz gráfica con frameworks como Bootstrap o Material Design.
Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.
