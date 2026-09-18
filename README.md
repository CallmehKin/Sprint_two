# EV ChargeOps — Sprint 02

Protótipo funcional do Enterprise Challenge 2026 — GoodWe.

## 1. Objetivo

Implementar a proposta definida na Sprint 01: registrar sessões de recarga, calcular consumo individual e cobrança/rateio, persistir os dados e integrar um módulo de IA ao fluxo principal.

## 2. O que está implementado

- API REST com FastAPI;
- persistência local com SQLite para demonstração;
- usuários e carregadores;
- registro e consulta de sessões;
- cálculo automático de custo de energia;
- taxa de manutenção e custo total;
- dashboard web;
- regressão linear para previsão de energia;
- K-Means para perfis de uso;
- Isolation Forest para sinalização de anomalias;
- testes unitários da lógica central;
- documentação automática da API.

## 3. Continuidade com a Sprint 01

A Sprint 01 definiu o fluxo:

`Veículo → Carregador GoodWe → API → Backend → Banco → IA → Dashboard`

Também definiu rateio baseado em consumo real, previsão de demanda, K-Means e Isolation Forest.

Nesta Sprint 02, o núcleo foi implementado com dados simulados para permitir execução local e reprodução da demonstração.

## 4. Decisões e limitações

### SQLite em vez de PostgreSQL
A Sprint 01 previa PostgreSQL. Para esta entrega, SQLite foi adotado como banco local do protótipo para reduzir dependências e facilitar a execução pelo avaliador. As entidades e regras de negócio permanecem separadas para permitir migração futura.

### Dados simulados
A integração física com o HCA G2 e a API GoodWe não é apresentada como implementada nesta Sprint. O sistema usa dados simulados para demonstrar o fluxo funcional solicitado.

### Rateio
A Sprint 01 definiu o rateio a partir do consumo real, tarifa, tempo/ocupação e manutenção. Como a Sprint 01 não especificou valores operacionais para a taxa de ocupação, esta Sprint implementa a parcela completamente definida e reproduzível: `energia × tarifa + manutenção`. A taxa de ocupação permanece como evolução documentada, evitando inventar um parâmetro que não foi especificado.

## 5. Estrutura

```text
EV_ChargeOps_Sprint2/
├── app/
│   ├── ai.py
│   ├── database.py
│   ├── logic.py
│   └── main.py
├── data/
├── docs/
├── evidencias/
├── static/
├── tests/
├── link_video.txt
├── requirements.txt
└── README.md
```

## 6. Como executar

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Acesse:

- Dashboard: `http://127.0.0.1:8000`
- Swagger/API: `http://127.0.0.1:8000/docs`
- Health check: `http://127.0.0.1:8000/api/health`

## 7. Demonstração

1. Abrir o dashboard.
2. Mostrar indicadores e sessões.
3. Abrir `/docs`.
4. Executar `POST /api/sessoes`.
5. Mostrar o cálculo automático do custo.
6. Executar `/api/ia/treinar`.
7. Executar `/api/ia/diagnostico`.
8. Executar `/api/ia/prever`.
9. Explicar a relação entre IA e dados persistidos.

## 8. Testes

```bash
pytest -q
```

## 9. Documentação para a equipe

- `docs/roteiro_video_sprint2.txt` — roteiro de até 3 minutos;
- `docs/GUIA_GRUPO_SPRINT2.md` — divisão sugerida e perguntas prováveis;
- `docs/MAPA_RUBRICA.md` — relação entre rubrica e evidências;
- `docs/relatorio_sprint2.md` — relatório técnico;
- `docs/checklist.md` — checklist de entrega.

## 10. Autoria e uso de IA

Ferramentas de IA podem apoiar desenvolvimento e depuração, mas a equipe deve revisar, testar e compreender o código entregue.
