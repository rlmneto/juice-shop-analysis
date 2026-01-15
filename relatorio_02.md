# Juice Shop - Relatório de Análise de Segurança

**Objetivo:** Análise de vulnerabilidades e desafios de segurança na aplicação Juice Shop - Broken Access Control

**Data:** 14 de Janeiro de 2026

---

## 1. Resumo Executivo

Este relatório documenta a análise de segurança realizada na aplicação Juice Shop, incluindo identificação de tecnologias, mapeamento de endpoints, testes de vulnerabilidades e exploração de falhas de autenticação.

---

## 2. Descobertas e Testes de Vulnerabilidade

### 2.1. Web3 Sandbox

**Vulnerabilidade:** Endpoint Exposto

**Método de Descoberta:** Inspeção do arquivo `main.js` para referências ao termo "web3"

**Resultado:**
- Endpoint descoberto: `/web3-sandbox`
- Severidade: Média (pode expor funcionalidades experimentais ou sensíveis)

---

### 2.2. Admin Section

**Vulnerabilidade:** Acesso Não Autorizado à Seção Administrativa

**Método de Descoberta:** Tentativa manual de acessar URLs comuns relacionadas à administração

**Resultado:**
- Endpoints descobertos: `/admin`, `/administration`
- Severidade: Alta (permite acesso a áreas administrativas sem autenticação adequada)

---

### 2.3. View Basket

**Vulnerabilidade:** Controle de Acesso Quebrado

**Método de Descoberta:** Análise de requisições HTTP para o carrinho de compras

**Exploração:**
1. Identificação de IDs sequenciais no parâmetro do carrinho
2. Modificação do ID para `1`, resultando no acesso ao carrinho de outro usuário

**Evidências:**
- **Print 1:** Requisição HTTP para o endpoint `/rest/basket/6`, evidenciando o uso de um token de autenticação e a modificação do ID para acessar o próprio carrinho:

  ![Requisição HTTP - Meu Carrinho (Endpoint /rest/basket/6)](attachment://images/image.png)

- **Print 2:** Resposta do servidor ao acessar o endpoint `/rest/basket/1`, demonstrando que o carrinho de outro usuário foi acessado com sucesso:

  ![Resposta do Servidor - Endpoint /rest/basket/1](attachment://images/image1.png)

- **Print 3:** Visualização do carrinho de outro usuário após a modificação do ID para `1`:

  ![Carrinho de Outro Usuário - ID 1](attachment://images/image2.png)

- **Print 4:** Visualização do próprio carrinho ao acessar o endpoint `/rest/basket/6`:

  ![Meu Carrinho - ID 6](attachment://images/image3.png)

**Severidade:** Crítica (exposição de dados de outros usuários)

---

## 3. Conclusões

Durante a análise de segurança do Juice Shop, foram identificadas vulnerabilidades significativas, incluindo controle de acesso quebrado e endpoints administrativos expostos. As descobertas destacam a necessidade de melhorias urgentes na validação de entrada e nos controles de acesso.

**Recomendações:**
1. Implementar validação rigorosa de entrada para prevenir acesso não autorizado.
2. Proteger endpoints administrativos com autenticação robusta.
3. Revisar e corrigir controles de acesso em todas as funcionalidades sensíveis.

---

**Relatório Preparado por:** Analista de Segurança  
**Data:** 14 de Janeiro de 2026  
**Status:** Análise Completa