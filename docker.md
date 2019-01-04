# docker-compose
rebuild images from any changed and restart containers:
docker-compose up -d --build

rebuild and restart a single service that changed:
docker-compose up -d --build worker
