
import json
from global_variables import vars

def upload_to_supabase(file: dict, name: str) -> None:
    # Convertir el diccionario a JSON
    json_data = json.dumps(file)
    # Convertir el JSON a bytes
    json_bytes = json_data.encode('utf-8')
    # Subir a Supabase Storage
    vars.SUPABASE.storage.from_(vars.BUCKET_ES).upload(
        file=json_bytes,
        path=f"/{name}.json",
        file_options={"content-type": "application/json"}
    )

def files_in_supabase() -> None:
    return vars.SUPABASE.storage.from_(vars.BUCKET_ES).list()
