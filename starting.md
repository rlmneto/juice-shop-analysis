

# 🧃 Juice Shop - Análise de Segurança

---

## 📊 Tecnologias Detectadas (Wappalyzer)

| Categoria | Tecnologia |
|-----------|------------|
| **Framework JavaScript** | Angular, Zone.js |
| **Biblioteca JavaScript** | jQuery |
| **Framework Mobile** | Onsen UI |
| **Linguagem de Programação** | TypeScript, Node.js |
| **CDN** | Cloudflare, cdnjs |
| **Script de Fonte** | Font Awesome |

---

## 🔍 Desafios

### Score Board
> Procurando nos arquivos `.js` em Sources (F12) por `"score"`

- ✅ Achado path: `/score-board`

### Login admin
> email nos comentario de produtos e bruto force de senha 
- Email: admin@juice-sh.op
- Senha: admin123

### DOM XSS
> Teste feito enviando <iframe src="javascript:alert(`xss`)">. nos comentario de um produto
- nada ocorreu
> Teste co campo de Pesquisa
- codigo executado (desafio concluido)

### Confidential Document
> olhando o main.js vi algo relacionado a ftp
- entao http://localhost:3000/ftp e estava la

### Error Handling
> Tentado fazer sql injection no login 
- pasasndo uma ' no email

---
Ao ver que nos comentarios tem o email fiz o script email_map.py para colhetalos
Emails encontrados nos reviews:
admin@juice-sh.op
uvogin@juice-sh.op
bender@juice-sh.op
mc.safesearch@juice-sh.op
jim@juice-sh.op

---

### Login Jim
> pegando o email jim@juice-sh.op e adicionando '-- 
- jim@juice-sh.op'--
- significa que estou comentando o restante da verificacao entao a verificacao de email nao entrara no where assim logando sem senha

### Login Bender
> mesma logica de bypass de senha com '--
- bender@juice-sh.op'--