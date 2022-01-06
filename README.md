# NeMo Virtual Assistant
<p>
  <img src="https://img.shields.io/badge/build-passed-green" alt="alternatetext">
  <img src="https://img.shields.io/badge/status- dev-yellow" alt="alternatetext">
  <img src="https://img.shields.io/badge/version-1.0%20-blue" alt="alternatetext">
  <img src="https://img.shields.io/badge/Python-3.7|3.8-blue" alt="alternatetext">
  <img src="https://img.shields.io/badge/NeMo-1.5.1-red" alt="alternatetext">
  <img src="https://img.shields.io/badge/Rasa-3.0.2-py" alt="alternatetext">
</p>

NVIDIA NeMo is a conversational AI toolkit built for researchers working on automatic speech recognition (ASR), natural language processing (NLP), and text-to-speech synthesis (TTS). The primary objective of NeMo is to help researchers from industry and academia to reuse prior work (code and pretrained models and make it easier to create new conversational AI models.
The project is based on this framework and, within the use of Rasa NLU processes, we can build and integrate components for a conversional AI. The aim of the project is to build an artificial intelligence agent to support people in specific task domains, generally the dataset of the NLU can merge, integrate and transform the supported tasks. Furthermore, we can have a chat for the trascriptions of the speeches between the agent and the customers to save a speech status in the session.

## Rasa 
Project integrates NeMo framework with the Rasa NLU. Rasa helps you build contextual assistants capable of having layered conversations with lots of back-and-forth. In order for a human to have a meaningful exchange with a contextual assistant, the assistant needs to be able to use context to build on things that were previously discussed – Rasa enables you to build assistants that can do this in a scalable way.

## Requirements
<ul>
<li>Python 3.6, 3.7 or 3.8</li>
<li>Pytorch 1.10.0 or above</li>
</ul>

## Step-to-Step Guide

In the future version, we will provide some additional information to run using Docker containers. At the moment, we can follow only these steps: <br>
- <b>Step 1</b>: Running `sh init.sh`
- <b>Step 2</b>: Set the current environment to the virtual env with `source venv/bin/activate` 
- <b>(Optional)</b>: In case of _Windows Distributions_: `.\venv\bin\activate`
- <b>Step 3</b>: `cd /nlu && rasa run --enable-api`
- <b>Step 4</b>: Open a second shell and digit `python manage.py runserver 9000`
- <b>Step 5</b>: Open the browser and go to the url _http://locahost:9000/jarvis/index_ to interact with the Jarvis AI

If you have troubles with dependencies open an issue here and be sure to follow each step of https://rasa.com/docs/rasa/installation/. For more information about the modelling on the _Natural Language Understanding_, visits the previous link.

## Docker setup

For an easy setup of the dependencies, build and run the image from the Dockerfile following these steps: <br>
- <b>Step 1</b>: `cd server`
- <b>Step 2</b>: `npm init` and `npm install -i express`
- <b>Step 3</b>: `nodemon server.js`

For the rasa setup (you need to open an other terminal):
- <b>Step 0</b>: Type `docker network create jarvis-net`
- <b>Step 1</b>: Go into the rasa project folder with the Dockerfile and type `sudo docker image build -f Dockerfile_actions.dockerfile -t rasa-actions .`
- <b>Step 2</b>: Go into the rasa project folder with the Dockerfile and type `sudo docker image build -f Dockerfile_shell.dockerfile -t rasa-shell .`
- <b>Step 3</b>: Type `sudo docker run -it -p 5055:5055 --network jarvis-net --mount "type=bind,source=$(pwd)/,target=/app" rasa-actions`
- <b>Step 3</b>: Going in the main directory the third terminal and type `cd rasa && sudo docker run -it -p 5005:5005 --network jarvis-net --mount "type=bind,source=$(pwd)/,target=/app" rasa-shell`

## Contributors
- Andrea Gurioli (@andreagurioli1995)
- Giovanni Pietrucci (@giovanniPi997)
- Mario Sessa (@kode-git)
