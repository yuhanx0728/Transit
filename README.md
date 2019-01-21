Tired of having to keep my eyes on the phone to check bus arrivals while getting ready for school every morning, I decided to create a Google Home action that allows me to check the real-time bus status for Pittsburgh public transport.

## Creating the webhook
Realizing that a webhook is necessary to interact with the pittsburgh transport API, I researched and tried out different options(e.g. NodeJS, etc) to construct a webhook. In the end I decided on [flask assistant](https://flask-assistant.readthedocs.io/en/latest/) because of my familiarity with Python. I spent much more time finding a suitable framework than actually writing codes, and through the process I learned choosing a suitable framework that will work and you know how to work with is as important as writing codes in that framework.

## Integrating the webhook
To integrate the webhook into Google Action I have to deploy the webhook to a cloud platform so that it can go live. Again, after much research I decided to deploy my webhook to Heroku. I learned to use Heroku to support the functioning of my webhook and linking the webhook back to my Diagflow.

## Other new stuff that I learned
1. Working with Dialogflow(I know how to make a simple chatbot now);
2. Parsing a JSON object;
3. Working with APIs.

## What I plan to do next
- [ ] Use permanent storage to store user information like home bus stop and schoool bus stop;
- [ ] Upload a demo video.

## How to use Transit
Transit is not open to public *yet*, but just to show you, this is how a conversation would go when you want to check your bus:

"Hi google, ask Transit to check the bus to school."
"The bus is coming in 6 minutes."

"Hi google, ask Transit to check the bus back home."
"Probably no bus is coming right now."
