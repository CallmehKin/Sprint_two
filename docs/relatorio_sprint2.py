# Relatório técnico — Sprint 02

## 1. Continuidade da Sprint 01
A Sprint 01 definiu o EV ChargeOps como plataforma de gestão de recarga compartilhada, com backend, persistência, dashboard e IA. A Sprint 02 implementa o núcleo dessa arquitetura.

## 2. Lógica central
Cada sessão relaciona usuário e carregador, período de utilização, energia e tarifa. O sistema calcula:
`custo_energia = energia_kwh × tarifa_kwh`
e:
`custo_total = custo_energia + taxa_manutencao`.

## 3. IA
A IA está integrada ao backend. A regressão linear recebe hora, duração e tarifa para estimar energia. O K-Means organiza sessões em perfis de uso. O Isolation Forest sinaliza registros potencialmente anômalos.

## 4. Persistência
Foi usado SQLite para tornar a demonstração local simples. A estrutura das tabelas é compatível conceitualmente com a modelagem PostgreSQL prevista na Sprint 01. A decisão é um desvio controlado e está registrada no README.

## 5. Evidências
O dashboard apresenta indicadores e sessões. A documentação automática do FastAPI permite executar as operações da API. A demonstração deve registrar uma sessão, consultar o resultado e executar as funções de IA.

## 6. Limitações
A integração física com o HCA G2 e a API GoodWe não é necessária para demonstrar o núcleo desta Sprint e não deve ser apresentada como já implementada. Os dados utilizados são simulados.

## 7. Próximas evoluções
Migrar persistência para PostgreSQL, integrar fonte real/simulada compatível com GoodWe, autenticação, controle de acesso, monitoramento contínuo e aprimorar os modelos com dados históricos maiores.
