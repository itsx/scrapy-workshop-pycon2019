# scrapy-workshop-pycon2019
Pycon.cz 2019 scrapy workshop

:hamster: :frog: This workshop should learn basic work with a [Scrapy](https://scrapy.org/community/) framework.

---

## Contact

   tomas.bartek3@gmail.com
   
## Resources

  - Scrapy  
    - [scrapy official documentation](https://docs.scrapy.org/en/latest/) - good to read all :)
    - [scrapinghub sample projects Github](https://github.com/scrapinghub/sample-projects) - :exclamation: spider and test web scraped during this workshop is one of the sample projects from this repo
    - [scrapinghub organisation Github](https://github.com/scrapinghub) - many extremely useful projects, which extends
      scrapy in some way: Spidermon (monitoring), Splash (javascript engine), etc.
    - [scrapinghub blog](https://blog.scrapinghub.com/) - actualities, examples, best-prectices, etc.
   - XPath  
     - [XPath tutorial](http://www.zvon.org/comp/r/tut-XPath_1.html#Pages~List_of_XPaths)  
     - [XPath concise](http://plasmasturm.org/log/xpath101/)  
     - [XPath tutorial czech](https://www.interval.cz/clanky/zaklady-jazyka-xpath/) - in czech language

---  
## Prerequisites
### Git
[Git](https://git-scm.com/) is a version control software that records changes
to a file or set of files. Git is especially helpful for software developers
as it allows changes to be tracked (including who and when) when working on a
project.

To download Git, go to the following link and choose the correct version for your
operating system: <https://git-scm.com/downloads>.
### Docker
[Docker](https://www.docker.com/) is a software to develope and run containerized applications. 
Application runs isolated in a container and is independent on the underlying operating system. The same container
can be run on any OS, where docker is installed. For a purpose of this tutorial I prepared container containing Scrapy
installed on a top of Ubuntu OS, to prevent possible problems with direct Scrapy installation on various operating systems.  
  [Docker installation for Ubuntu](https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-using-the-repository)  
  [Docker installation for Windows](https://docs.docker.com/v17.12/docker-for-windows/install/) (Windows 10 64bit: Pro, Enterprise or Education)  
  [Docker installation for Mac](https://docs.docker.com/v17.12/docker-for-mac/install/)  


### Installation of Scrapy directly to a operation system (Alternative)
[Scrapy installation guide](http://docs.scrapy.org/en/latest/intro/install.html) - For a brave one, who wants to try 
installation directly to a OS. There are some python libraries, which themselves depend on non-Python packages that might require additional installation steps depending on your platform.

[Scrapy installation quide - Windows](http://docs.scrapy.org/en/latest/intro/install.html#platform-specific-installation-notes) - In a case you are not able to run docker on your Windows, install Scrapy directly.
## Setup

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
