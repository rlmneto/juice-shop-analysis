

# Juice Shop - Relatório de Análise de Segurança

**Objetivo:** Análise de vulnerabilidades e desafios de segurança na aplicação Juice Shop

**Data:** 12 de Janeiro de 2026

---

## 1. Resumo Executivo

Este relatório documenta a análise de segurança realizada na aplicação Juice Shop, incluindo identificação de tecnologias, mapeamento de endpoints, testes de vulnerabilidades e exploração de falhas de autenticação.

---

## 2. Reconhecimento - Stack Tecnológico

A seguinte stack foi identificada através da análise com Wappalyzer:

| Categoria | Tecnologia |
|-----------|------------|
| **Frontend - Framework** | Angular, Zone.js |
| **Frontend - Biblioteca** | jQuery |
| **Frontend - Mobile** | Onsen UI |
| **Backend - Runtime** | Node.js |
| **Backend - Linguagem** | TypeScript |
| **Infraestrutura - CDN** | Cloudflare, cdnjs |
| **Recursos** | Font Awesome |

---

## 3. Descobertas e Testes de Vulnerabilidade

### 3.1. Descoberta de Endpoints Ocultos

**Vulnerabilidade:** Divulgação de Informações Sensíveis

**Método de Descoberta:** Análise do código JavaScript (DevTools - F12)

**Resultado:**
- Endpoint descoberto: `/score-board`
- Severidade: Média (expõe o progresso dos desafios)

---

### 3.2. Teste de Autenticação - Credenciais Padrão

**Vulnerabilidade:** Credenciais Administrativas Fracas / Força Bruta

**Metodologia:**
- Coleta de emails através da análise de comentários de produtos (API: `/rest/products/{id}/reviews`)
- Testes de força bruta contra o endpoint `/rest/user/login`

**Resultados Obtidos:**
- Conta administrativa comprometida
- Email: `admin@juice-sh.op`
- Senha: `admin123`
- Status: Acesso obtido

---

### 3.3. Teste de XSS (Cross-Site Scripting)

**Vulnerabilidade:** DOM-based XSS

**Metodologia:**
1. **Teste 1 - Campo de Comentários**
   - Payload: `<iframe src="javascript:alert('xss')">`
   - Resultado: Payload bloqueado/neutralizado

2. **Teste 2 - Campo de Busca**
   - Payload: `<iframe src="javascript:alert('xss')">`
   - Resultado: Execução de script confirmada
   - Severidade: Alta

---

### 3.4. Acesso a Documentos Confidenciais

**Vulnerabilidade:** Enumeração de Diretórios / Divulgação de Informações

**Método de Descoberta:** Análise do arquivo `main.js` - identificação de referências a FTP

**Exploração:**
- Endpoint: `http://localhost:3000/ftp`
- Resultado: Diretório acessível e exposto
- Severidade: Alta

---

### 3.5. Teste de SQL Injection - Bypass de Autenticação

**Vulnerabilidade:** SQL Injection no Formulário de Login

**Metodologia:** Injeção de operadores SQL no campo de email

**Teste Inicial:**
- Payload: `admin@juice-sh.op' --`
- Objetivo: Comentar verificação de senha usando `--`
- Resultado: Bypass de autenticação bem-sucedido

**Contas Afetadas:**
- `jim@juice-sh.op' --`
- `bender@juice-sh.op' --`

**Severidade:** Crítica (permite autenticação sem senha válida)

---

## 4. Análise da API REST

### 4.1. Endpoint de Reviews de Produtos

**URI:** `GET /rest/products/{id}/reviews`

**Resposta Típica:**
```json
{
    "status": "success",
    "data": [{
        "message": "I'd stand on my head to make you a deal for this piece of art.",
        "author": "stan@juice-sh.op",
        "product": 42,
        "likesCount": 0,
        "likedBy": [],
        "_id": "kR7CoSG95QY2cXLa9",
        "liked": true
    }, {
        "message": "Just when my opinion of humans couldn't get any lower, along comes Stan...",
        "author": "bender@juice-sh.op",
        "product": 42,
        "likesCount": 0,
        "likedBy": [],
        "_id": "q4ocEYoEo2RWgpyRg",
        "liked": true
    }]
}
```

**Vulnerabilidade Identificada:** Divulgação de Endereços de Email

A resposta contém o campo `author` com endereços de email de usuários, permitindo:
- Enumeração de usuários do sistema
- Criação de listas para testes de força bruta
- Phishing e ataques direcionados

**Severidade:** Média

---

## 5. Enumeração de Usuários

### Metodologia

Foi desenvolvido script Python (`email_map.py`) para extrair sistematicamente todos os emails disponíveis através da API de reviews.

**Técnica:** Iteração sobre IDs de produtos (1-30) com requests HTTP GET

### Resultados da Enumeração

Emails identificados no sistema:
- `admin@juice-sh.op`
- `uvogin@juice-sh.op`
- `bender@juice-sh.op`
- `mc.safesearch@juice-sh.op`
- `jim@juice-sh.op`

**Impacto:** Facilita ataques de força bruta direcionados contra contas específicas

---

## 6. Testes Automatizados

### Script de Força Bruta

**Arquivo:** `brute-force.py`

**Funcionalidade:**
- Testagem de senhas contra o endpoint `/rest/user/login`
- Wordlist utilizada: `best1050.txt` (1050 senhas comuns)
- Alvo: Conta administrativa `admin@juice-sh.op`

**Resultado:** Senha descoberta: `admin123`

**Tempo de execução:** Reduzido (~30 segundos), demonstrando fraca implementação de rate-limiting

---

## 7. Matriz de Vulnerabilidades

| # | Vulnerabilidade | Severidade | Status | CVSS |
|---|---|---|---|---|
| 1 | Enumeração de Usuários via API | Média | Confirmado | 5.3 |
| 2 | XSS em Campo de Busca | Alta | Confirmado | 7.1 |
| 3 | SQL Injection em Login | Crítica | Confirmado | 9.8 |
| 4 | Acesso Não Autorizado a FTP | Alta | Confirmado | 7.5 |
| 5 | Credenciais Administrativas Fracas | Alta | Confirmado | 8.2 |
| 6 | Falta de Rate Limiting | Média | Confirmado | 5.9 |

---

## 8. Conclusões

Durante a análise de segurança do Juice Shop, foram identificadas **6 vulnerabilidades críticas e de alta severidade**, incluindo:

**Sucessos Alcançados:**
- Mapeamento completo do stack tecnológico
- Exploração bem-sucedida de SQL Injection
- Contorno de autenticação via manipulação de queries SQL
- Execução de XSS em campo de busca
- Enumeração completa de usuários do sistema
- Acesso a recursos restritos

**Padrão de Vulnerabilidades Identificadas:**
- Falta de validação e sanitização de entrada
- Proteção inadequada de autenticação
- Divulgação indevida de informações sensíveis
- Ausência de controles de rate-limiting
- Controle de acesso inadequado

**Recomendações:**
1. Implementar prepared statements para prevenir SQL Injection
2. Validar e sanitizar todas as entradas do usuário
3. Implementar rate-limiting nos endpoints de autenticação
4. Aplicar Content Security Policy (CSP) para prevenir XSS
5. Remover divulgação de emails de endpoints públicos
6. Implementar autenticação multifator (MFA)

---

## 9. Ferramentas e Técnicas Utilizadas

- **DevTools (F12)** - Análise de código JavaScript e Network
- **Burp Suite / Caido** - Interceptação e análise de requisições HTTP
- **Python + Requests** - Automação de testes
- **Wappalyzer** - Fingerprinting de tecnologias
- **Análise Manual** - Code review e lógica de aplicação

---

**Relatório Preparado por:** Analista de Segurança  
**Data:** 12 de Janeiro 2026  
**Status:** Análise Completa