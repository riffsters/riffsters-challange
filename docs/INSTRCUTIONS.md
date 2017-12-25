#Instructions for how to run the docker locally
1. Pull the image: **docker pull riffo/my_challange**
2. Run docker locally with the following command: **docker run -e "AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}" -e "AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}" -d -p 5000:5000 riffo/my_challange**
3. Enter in your browser the following address to get:
   * secret: http://127.0.0.1:5000/secret
   * health: http://127.0.0.1:5000/health
