# EV ChargeOps — Sprint 02

> Protótipo funcional do Enterprise Challenge 2026 — GoodWe.

### 🚀 Demonstração Online

**[ACESSAR O PROTÓTIPO](https://callmehkin.github.io/Sprint_two/)**

**[REPOSITÓRIO NO GITHUB](https://github.com/CallmehKin/Sprint_two)**

---

## 1. Objetivo

Implementar a proposta definida na Sprint 01: registrar sessões de recarga, calcular consumo individual e cobrança/rateio, persistir os dados e integrar um módulo de IA ao fluxo principal.

---

## 2. O que está implementado

- API REST com FastAPI;
- persistência local com SQLite para demonstração;
- cadastro e consulta de usuários e carregadores;
- registro e consulta de sessões;
- cálculo automático de custo de energia;
- taxa de manutenção e cálculo do custo total;
- dashboard web;
- regressão linear para previsão de energia;
- K-Means para identificação de perfis de uso;
- Isolation Forest para sinalização de anomalias;
- testes unitários da lógica central;
- documentação automática da API.

---

## 3. Continuidade com a Sprint 01

A Sprint 01 definiu o seguinte fluxo:

```text
Veículo → Carregador GoodWe → API → Backend → Banco → IA → Dashboard
