This is a super simple appengine template for my own sake; maybe you'll find it useful too.

It shows how to use 3rd party libs and uses Flask for HTTP serving and shows the monkey-patching stuff to get requests working. These are just more familiar to me than the builtin appengine things

Download the Google Cloud SDK [https://cloud.google.com/sdk/downloads]

```
virtualenv -p python2.7 ve
. ve/bin/activate
pip install -t lib -r requirements.txt
dev_appserver.py app.yaml
# serves on localhost:8080

# make sure you're on the right app
gcloud config list

# and deploy
gcloud app deploy
```
