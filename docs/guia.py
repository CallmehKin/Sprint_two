# Guia da equipe — EV ChargeOps | Sprint 02

## Objetivo
Entregar um protótipo funcional que implemente a proposta da Sprint 01: registrar sessões de recarga, calcular consumo e cobrança/rateio individual, e integrar IA ao fluxo principal.

## Divisão sugerida entre os 4 integrantes

### Integrante 1 — Lógica central e backend
Explicar:
- FastAPI e rotas REST;
- entidades usuário, carregador e sessão;
- cadastro de sessão;
- cálculo `custo_energia = energia_kWh × tarifa`;
- taxa de manutenção e custo total;
- persistência no SQLite.

### Integrante 2 — IA
Explicar:
- regressão linear: previsão de energia;
- K-Means: perfis de utilização;
- Isolation Forest: possíveis anomalias;
- por que a IA é estrutural e usa dados das sessões.

### Integrante 3 — Dashboard e evidências
Explicar:
- indicadores de sessões, energia e faturamento;
- tabela de sessões;
- chamadas para treino, diagnóstico e previsão;
- documentação `/docs` da FastAPI.

### Integrante 4 — Arquitetura, decisões e continuidade
Explicar:
- relação com a Sprint 01;
- fluxo Veículo → GoodWe → API → Backend → Banco → IA → Dashboard;
- dados simulados nesta Sprint;
- decisão documentada de usar SQLite no protótipo;
- próximos passos: GoodWe real/PostgreSQL.

## Perguntas prováveis do professor

**Por que SQLite se a Sprint 01 previa PostgreSQL?**
> Porque esta Sprint prioriza um protótipo local reproduzível. A troca reduz dependências e não altera as entidades nem as regras de negócio. O desvio está documentado no README.

**A API GoodWe está integrada de verdade?**
> Não nesta versão. Os dados são simulados. A integração real é uma evolução posterior e não deve ser apresentada como implementada.

**Como o custo é calculado?**
> Primeiro multiplicamos energia consumida pela tarifa. Depois acrescentamos a taxa de manutenção configurada para a sessão.

**Onde a IA entra no fluxo?**
> Depois que as sessões estão persistidas, o módulo lê os dados e produz previsão, agrupamentos e diagnóstico de anomalias. Os resultados são acessíveis pela API e pelo dashboard.

**Por que usar K-Means?**
> Porque a Sprint 01 definiu clusterização para identificar perfis de utilização. O K-Means agrupa sessões com características semelhantes.

**O que o Isolation Forest retorna?**
> Ele sinaliza registros que apresentam comportamento diferente do conjunto usado no treinamento. Isso é um sinal para investigação, não uma prova de falha ou fraude.

**O que é autoria no contexto desta entrega?**
> A equipe deve conseguir explicar as decisões e cada parte relevante do código, testar a execução e justificar as escolhas técnicas.

## Antes de gravar
1. Criar ambiente virtual.
2. Instalar `requirements.txt`.
3. Rodar `uvicorn app.main:app --reload`.
4. Abrir o dashboard.
5. Abrir `/docs`.
6. Testar criação de sessão.
7. Treinar IA.
8. Executar diagnóstico.
9. Executar previsão.
10. Gravar até 3 minutos.
11. Colocar o link não listado em `link_video.txt`.
12. Fazer commits descritivos.
