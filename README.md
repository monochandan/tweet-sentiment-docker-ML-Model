# ML model deployment in docker : Twiteer sentiment analysis

- scikit-learn==1.5.0
- nltk==3.8.1
- flask==3.0.3 
- flask-cors==4.0.1
- python==3.10

# Build an image (Dockerize) and run on Docker container:

## Use VS code

## Downloade project (git bash):
    
    git clone https://github.com/monochandan/tweet-sentiment-docker-ML-Model.git // clone the repository in the local computer

## Open in VS code

    cd api // rediect to api directory

    docker compose up --build // build the image in local computer

  ## Then in browser:

      http://localhost:500

  <img width="233" alt="image" src="https://github.com/user-attachments/assets/6ef40af8-355f-46a8-9509-8093bd519742">


# Directly run on Docker without building an image locally:


## Run in command prompt or powershell:

    docker run -p5000:5000 chandanmonotosh554/mlapp

## Then in browser:

      http://localhost:500

  <img width="233" alt="image" src="https://github.com/user-attachments/assets/6ef40af8-355f-46a8-9509-8093bd519742">  

  



  
