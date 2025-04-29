from fastapi import FastAPI
import uuid
import time

app = FastAPI()

@app.post("/logboek")
def maak_logboek_record():
    trace_id = str(uuid.uuid4())  # Maakt unieke trace voor de hele operatie
    span_id = str(uuid.uuid4())   # Maakt unieke span voor deze specifieke stap
    timestamp = time.time()       # Tijdstip van deze actie
    processing_activity_id = "rvva-001"  # Hardcoded verwerking ID
    status_code = "OK"               # OK (technisch succesvol uitgevoerd)

    logboek_record = {
        "trace_id": trace_id,
        "span_id": span_id,
        "processing_activity_id": processing_activity_id,
        "timestamp": timestamp,
        "status_code": status_code
    }

    print("LOGBOEK-INVOER:")
    print(logboek_record)

    return {"boodschap": "Logboekrecord gemaakt", "log": logboek_record}
