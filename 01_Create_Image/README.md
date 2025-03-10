# ilionx-webapp

1. Maak een Dockerfile in deze map die de volgende image maakt:
- Gebruik als basis de image 'python:3.13-slim'
- Installeer de 'Flask' Python module
- Plaats de data uit de map 'application' op de /app locatie in de container
- Zorg ervoor dat poort 8080 van de container bereikbaar wordt gemaakt
- Configureer als werklocatie '/app'
- Specificeer als container executable: 'python main.py'

2. Bouw deze container en geef hem de naam 'ilionx-webapp'

3. Maak een container in Docker die gebruik maakt van deze image en de webpagina bereikbaar maakt op poort 80

4. Test de webpagina