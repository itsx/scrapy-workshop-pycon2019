# scrapy-workshop-pycon2019
pycon 2019 scrapy workshop


## Setup:

1. Clone this repository. From your console.
   ```
   git clone https://github.com/itsx/scrapy-workshop-pycon2019.git
   ```
2. Change into the newly created repository:
   ```
   cd scrapy-workshop-pycon2019
   ```
3. From this directory run docker-compose command to start the container with installed scrapy:
   ```
   sudo docker-compose up -d
   ```
   (For windows users don't use sudo)

   Now you can check that docker container is running with the command:
   ```
   sudo docker-compose ps
   ```

5. Finally attach to a running container, and check version of installed scrapy:
   ```
   sudo docker exec -it scrapy bash
   scrapy --version
   ```
