# scrapy-workshop-pycon2019
pycon 2019 scrapy workshop


### How to run scrapy:

Open your console and write these command to checkout the repository from Github to your local machine:
```
git clone https://github.com/itsx/scrapy-workshop-pycon2019.git
```
Change to the newly created repository:
```
cd scrapy-workshop-pycon2019
```
From this directory run docker-compose command to start the container with installed scrapy:
```
sudo docker-compose up -d
```
(For windows users don't use sudo)

Now you can check that docker container is running with the command:
```
sudo docker-compose ps
```

Finally attach to a running container, and check version of installed scrapy
```
sudo docker exec -it scrapy bash
```
```
scrapy --version
```
