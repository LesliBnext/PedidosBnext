# API Tickets Pedidos 2025

FastAPI para generar tickets (14 tipos) según el Behavior acordado. Devuelve número INC y texto de confirmación específico por tipo.

## Ejecutar local
```bash
pip install -r requirements.txt
uvicorn app:app --host 0.0.0.0 --port 8080 --reload
```

### Probar
```bash
curl -X POST http://localhost:8080/tickets \
  -H "Content-Type: application/json" \
  -d '{"type":"conciliacion_pedido","full_name":"Prueba Usuario","phone":"8123456789","mrq_pe":"PE-123","description":"Prueba"}'
```

## Despliegue en IBM Code Engine
1. Construye la imagen con Docker o Source-to-Image.
2. Despliega y obtén la URL pública (ej. `https://<app>.<region>.codeengine.appdomain.cloud`).
3. Edita `openapi_tickets_14_final.json` y reemplaza `https://REPLACE_WITH_YOUR_API_URL` por tu URL real.
4. Importa ese JSON a IBM watsonx (tool).

## Campos y tipos
- `type` ∈ 14 valores (ver `catalog.py` y OpenAPI).
- `full_name`, `phone` siempre requeridos en el Behavior.
- `mrq_pe`, `description`, `a_envase`, `b_envase`, `c_envase` según la rama.

## Base de datos
- SQLite por defecto (`tickets.db` en la raíz). Puedes migrar a PostgreSQL cambiando la URL en `db.py`.
