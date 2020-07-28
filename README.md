# Experiments on language intensity

Let's see if sentiment detection is adequate to detect subtle variations in sentences.

## Requirements

Get a google cloud key and save it as `gcloud_key.json`

Run StanfordNLP container (python scripts connect to it on localhost:9000)

```bash
docker run -itd -p 9000:9000 --name corenlp graham3333/corenlp-complete
```

Install requirements

```bash
virtualenv venv
pip install -r requirements.txt
```

Run `install.sh` to install sentiStrength.


## Run

Run the streamlit application (runs on default port 8501)

```bash
streamlit run app.py
```

If you want to reach it from outside your LAN

```bash
ssh -R intensity:80:localhost:8501 serveo.net
```
