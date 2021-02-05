## Environment Setup

### Pre-requisites
    Following pre-requisites need to be installed to run this app, 
    1. Python3 (Tested on python 3.7.9)
    2. Docker 20.10.1

#### Steps to test the application,
1. Clone the app in your local using clone url
2. Go into main directory `cd rackspace`
3. We can run the app in two ways
    1. With local python using command `python3 billing_system.py`. You can see the pop-up of app.
    2. Using docker need to follow below steps,
        1. Build the image of app using command `sudo docker build -t <image-tag> .`
        2. Check the newly created image using command `docker images`
        3. To create container and run the app using image use command `docker run --name <container-name> <image-id>`

### Note
As the app is created using `Tkinter` python GUI library, getting issue with display while running the using Docker.
Please go through `Dockerifile` for reference. The app is perfectly running with direct command mentioned in method one. 

