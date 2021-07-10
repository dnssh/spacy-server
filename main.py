# Run
# uvicorn main:app --reload --port 8080


from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import spacy
import json

nlp= spacy.load("en_core_web_sm")

class TextToAnnotate( BaseModel ):
	text: str

app =FastAPI()


@app.get('/get')
def get():
	return 'hello'

@app.post("/auto_annotate")
async def auto_annotate(document: TextToAnnotate):
	doc=nlp(document.text)
	ent_label_list=[
	{"label":ent.label_,"start_offset":ent.start_char,"end_offset":ent.end_char } for ent in doc.ents
	]
	response=json.dumps(ent_label_list)
	resp=json.loads(response)
	return resp

if __name__ == "__main__":
	host='127.0.0.1'
	uvicorn.run("auto_annotate:app", host=host, port=8080)




		
