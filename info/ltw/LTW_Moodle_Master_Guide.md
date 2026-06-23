# 🎯 LTW — Guia Mestre para Perguntas Moodle
> Baseado nas questões do `sample_moodle.pdf` · Cobre todos os tipos de perguntas
> Cada secção tem: o padrão da pergunta → estratégia de resolução → exemplos resolvidos passo a passo

---

## Índice de Tipos de Perguntas

| # | Tipo | Tópico | Dificuldade |
|---|------|---------|-------------|
| [1](#tipo-1-regex---pesquisa-numa-string-contains) | Regex — CONTAINS (pesquisa livre) | Expressões Regulares | ⭐⭐⭐ |
| [2](#tipo-2-regex---validação-completa-is) | Regex — IS (validação completa) | Expressões Regulares | ⭐⭐⭐ |
| [3](#tipo-3-especificidade-css-e-cascata) | Especificidade CSS + Cascata | CSS | ⭐⭐⭐⭐ |
| [4](#tipo-4-semântica-html) | Semântica HTML | HTML | ⭐ |
| [5](#tipo-5-código-php---funções-de-output) | Código PHP — funções de output | PHP | ⭐⭐⭐ |

---

## TIPO 1: Regex — Pesquisa numa String (CONTAINS)

### O que é?

A pergunta pede uma regex que encontre um padrão **em qualquer posição** numa string. A string pode ter mais conteúdo antes e depois do padrão. **Não usas âncoras `^` e `$`**.

### Como identificar?

> *"Write a regular expression that matches if the input **CONTAINS** …"*
> *"The [pattern] may appear **anywhere** in the input string."*

### Estratégia de Resolução (5 passos)

```
1. Ler os exemplos true/false com atenção
2. Identificar o formato EXATO (quantos dígitos? que separadores?)
3. Construir a regex parte a parte
4. Verificar com os exemplos negativos (o que deve dar false)
5. NÃO adicionar ^ e $ (a pesquisa é parcial)
```

---

### Exemplo Resolvido — Pergunta 1 do PDF

**Enunciado:**
> Write a regular expression that matches if the input **CONTAINS** a date in the format `YYYY-MM-DD`, where:
> - `YYYY` is exactly four digits
> - `MM` is exactly two digits, and the first digit is either `0` or `1`
> - `DD` is exactly two digits, and the first digit is `0`, `1`, `2`, or `3`

**Exemplos:**
| Input | Resultado |
|-------|-----------|
| `"Today is 2024-05-28."` | `true` |
| `"1999-12-31 was New Year's Eve."` | `true` |
| `"The date 2024-5-8 is invalid."` | `false` |
| `"No date here."` | `false` |
| `"Ends with date 2024-07-20"` | `true` |
| `"Start2023-01-01Middle"` | `true` |

**Raciocínio passo a passo:**

```
Formato: YYYY - MM - DD

YYYY → exatamente 4 dígitos → \d{4}

MM   → 2 dígitos onde o 1º é 0 ou 1
      → 0 seguido de qualquer dígito: 0[0-9]
      → 1 seguido de qualquer dígito: 1[0-9]
      → MAS meses vão de 01 a 12, então:
        01–09 → 0[1-9]
        10–12 → 1[0-2]
      → Combinado: (0[1-9]|1[0-2])

DD   → 2 dígitos onde o 1º é 0, 1, 2 ou 3
      → Mas o enunciado diz "first digit is 0, 1, 2, or 3"
      → Então aceita 00–09, 10–19, 20–29, 30–39 (incluindo 00, 32, etc.)
      → Simplificado: [0-3][0-9]
      
      Se quisermos dias válidos (01–31):
        01–09 → 0[1-9]
        10–29 → [12][0-9]
        30–31 → 3[01]
      → (0[1-9]|[12][0-9]|3[01])

Separadores: -

Sem âncoras (CONTAINS)!
```

**Resposta:**
```
\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])
```

**Verificação com os exemplos negativos:**
- `"2024-5-8"` → MM tem 1 dígito → `\d{4}` encontra `2024`, mas depois `-5` não casa com `-(0[1-9]|1[0-2])` ✅ dá `false`
- `"No date here."` → não existe sequência `\d{4}-...` ✅ dá `false`

---

### Template para Regex CONTAINS

```
[padrão sem ^ e $]
```

**Componentes frequentes:**
```
\d{N}           → exatamente N dígitos
\d{N,M}         → entre N e M dígitos
[a-z]+          → uma ou mais letras minúsculas
[A-Za-z0-9]+   → alfanumérico
(A|B)           → alternativa: A ou B
X?              → X é opcional
.               → qualquer caractere
```

---

## TIPO 2: Regex — Validação Completa (IS)

### O que é?

A pergunta pede uma regex que valide se **toda a string** corresponde ao padrão. A string não pode ter nada antes nem depois. **Usas âncoras `^` no início e `$` no fim**.

### Como identificar?

> *"Write a regex that checks if the input **IS** a valid …"*
> *"Your answer must match the **entire** string."*
> *Nos exemplos: `"50000"` ou `"4100-12a"` são inválidos (demasiado longo ou carácter errado)*

### Estratégia de Resolução (5 passos)

```
1. Ler os exemplos false e perceber o que os torna inválidos
2. Identificar o formato completo da string (do início ao fim)
3. Construir a regex com ^ no início e $ no fim
4. Usar ? para partes opcionais
5. Verificar: nada antes nem depois deve ser aceite
```

---

### Exemplo Resolvido — Pergunta 2 do PDF

**Enunciado:**
> Write a regex that checks if the input **IS** a valid **postal code**. A postal code can either be:
> - `XXXX` (exactly 4 digits)
> - or `XXXX-YYY` (4 digits, a hyphen, then exactly 3 digits)

**Exemplos:**
| Input | Resultado |
|-------|-----------|
| `"4100-123"` | `true` |
| `"5000"` | `true` |
| `"1234-567"` | `true` |
| `"123-4567"` | `false` |
| `"abcd-123"` | `false` |

**Raciocínio passo a passo:**

```
Formato 1: XXXX         → \d{4}
Formato 2: XXXX-YYY     → \d{4}-\d{3}

Formato 2 = Formato 1 + (-YYY), onde (-YYY) é opcional → (-\d{3})?

Combinado: \d{4}(-\d{3})?

IMPORTANTE: é validação completa, então:
  → Adicionar ^ no início e $ no fim
  → ^ garante que não há nada antes de XXXX
  → $ garante que não há nada depois de YYY

"123-4567" falha porque \d{4} espera 4 dígitos antes de -
  → "123" só tem 3 → falha ✅
"50000" falha porque após \d{4} temos "0" que não é - nem fim de string
  → mas com a regex ^... $ o "0" extra faz falhar ✅
```

**Resposta:**
```
^\d{4}(-\d{3})?$
```

**Anatomia da resposta:**
```
^          início da string (nada antes)
\d{4}      exatamente 4 dígitos
(          início do grupo opcional
  -        hífen literal
  \d{3}    exatamente 3 dígitos
)?         o grupo inteiro é opcional (0 ou 1 vez)
$          fim da string (nada depois)
```

---

### Template para Regex IS (Validação)

```
^[padrão completo]$
```

**Estruturas opcionais comuns:**
```
^X$             → string é exatamente X
^X(Y)?$         → X seguido opcionalmente de Y
^(X|Y)$         → string é X ou Y
^X{N}$          → exatamente N repetições de X
^X{N,M}$        → entre N e M repetições de X
```

---

### Cheat Sheet: CONTAINS vs IS

| | CONTAINS | IS (validação) |
|--|----------|----------------|
| **Âncoras** | Sem `^` e `$` | Com `^` e `$` |
| **Texto extra** | Permitido antes/depois | Não permitido |
| **Frase-chave** | "contains", "anywhere" | "is a valid", "must match" |
| **Exemplo** | `\d{4}-\d{2}-\d{2}` | `^\d{4}-\d{2}-\d{2}$` |

---

## TIPO 3: Especificidade CSS e Cascata

### O que é?

Dado um bloco de HTML e várias regras CSS, determinar qual a cor (ou outro estilo) aplicada a um elemento específico, incluindo pseudo-classes como `:hover`.

### Como identificar?

> *"What will be the **color** of the `<li>` containing the text X when the mouse pointer is on top of it?"*
> *"Consider the following HTML and CSS. What color does element X get?"*

### Estratégia de Resolução (6 passos)

```
1. Marcar o elemento alvo no HTML
2. Listar TODAS as regras CSS que se aplicam a esse elemento
3. Calcular a especificidade de cada regra aplicável
4. Descartar regras que não se aplicam (estado, relação, etc.)
5. Ordenar por especificidade → a maior ganha
6. Em caso de empate → a última na folha de estilos ganha
```

**Fórmula de especificidade: (a, b, c)**

| Tipo | Contribui | Exemplos |
|------|-----------|---------|
| ID `#` | a | `#menu` → (1,0,0) |
| Classe `.`, Pseudo-classe `:`, Atributo `[]` | b | `.active` → (0,1,0) · `:hover` → (0,1,0) · `[type]` → (0,1,0) |
| Elemento, Pseudo-elemento | c | `li` → (0,0,1) · `::before` → (0,0,1) |
| Universal `*` | nada | → (0,0,0) |

**Comparação:** Compara-se da esquerda para a direita: a primeiro, depois b, depois c.
- `(1,0,0)` > `(0,9,9)` — ID sempre ganha sobre classes
- `(0,2,0)` > `(0,1,5)` — mais classes ganha, mesmo que tenha mais elementos
- `(0,1,1)` > `(0,1,0)` — mesmo número de classes, mais elementos ganha

---

### Exemplo Resolvido — Pergunta 3 do PDF

**HTML:**
```html
<div id="main">
  <ul class="menu" data-type="primary">
    <li class="item active">Home</li>
    <li class="item">About</li>          <!-- ← elemento alvo -->
    <li class="item special">Services</li>
  </ul>
</div>
```

**CSS:**
```css
/* Regra A */ li { color: black; }
/* Regra B */ .menu > li.active { color: blue; }
/* Regra C */ ul[data-type="primary"] li.item { color: green; }
/* Regra D */ #main li.item:nth-child(2) { color: red; }
/* Regra E */ .menu li.item.special:hover { color: purple; }
/* Regra F */ li.item:nth-child(2) { color: orange; }
```

**Pergunta:** Cor do `<li>About</li>` quando o **rato está por cima** (hover)?

---

**Passo 1 — Identificar o elemento:**
- É o 2.º filho de `<ul>` → `nth-child(2)` aplica-se
- Tem classes: `item`
- Não tem: `active`, `special`

**Passo 2 — Verificar cada regra:**

| Regra | Seletor | Aplica ao `<li>About`? | Porquê |
|-------|---------|------------------------|--------|
| A | `li` | ✅ | é um li |
| B | `.menu > li.active` | ❌ | precisa de classe `active` |
| C | `ul[data-type="primary"] li.item` | ✅ | é um li.item dentro de ul[data-type="primary"] |
| D | `#main li.item:nth-child(2)` | ✅ | é filho nº2, tem classe item, está dentro de #main |
| E | `.menu li.item.special:hover` | ❌ | precisa de classe `special` |
| F | `li.item:nth-child(2)` | ✅ | é o 2º filho e tem classe item; `:hover` está ativo |

> ⚠️ **IMPORTANTE:** `:hover` é uma pseudo-classe que se aplica quando o rato está por cima. Regras com `:hover` **só se aplicam** nessa condição. O enunciado diz "when the mouse pointer is on top of it", então `:hover` está ativo!

**Passo 3 — Calcular especificidade das regras aplicáveis (A, C, D, F):**

| Regra | Seletor | IDs (a) | Classes/PseudoC/Attr (b) | Elementos (c) | Específ. |
|-------|---------|---------|--------------------------|---------------|----------|
| A | `li` | 0 | 0 | 1 (`li`) | **(0,0,1)** |
| C | `ul[data-type="primary"] li.item` | 0 | 1 (`[data-type]`) + 1 (`.item`) = 2 | 2 (`ul`, `li`) | **(0,2,2)** |
| D | `#main li.item:nth-child(2)` | 1 (`#main`) | 1 (`.item`) + 1 (`:nth-child`) = 2 | 1 (`li`) | **(1,2,1)** |
| F | `li.item:nth-child(2)` | 0 | 1 (`.item`) + 1 (`:nth-child`) = 2 | 1 (`li`) | **(0,2,1)** |

**Passo 4 — Ordenar e determinar o vencedor:**

```
(1,2,1) > (0,2,2) > (0,2,1) > (0,0,1)
   D    >    C    >    F    >    A
```

**Vencedor: Regra D → `color: red`** ✅

---

### Como Calcular a Especificidade Rapidamente

**Conta da seguinte forma:**

```css
#main li.item:nth-child(2)
  │    │  │       │
  │    │  │       └── pseudo-class → b++   [b=2]
  │    │  └────────── classe → b++         [b=2]
  │    └───────────── elemento → c++       [c=1]
  └────────────────── id → a++             [a=1]

Especificidade: (1, 2, 1)
```

**Tabela de referência rápida:**
```
*                          → (0,0,0)
li                         → (0,0,1)
p.intro                    → (0,1,1)
ul li                      → (0,0,2)
.menu > li                 → (0,1,1)
[type="text"]              → (0,1,0)
li:hover                   → (0,1,1)
li:nth-child(2)            → (0,1,1)
#sidebar                   → (1,0,0)
#sidebar p                 → (1,0,1)
#sidebar p.bio             → (1,1,1)
ul[data-type] li.item      → (0,2,2)
#main li.item:nth-child(2) → (1,2,1)
```

---

### Pseudo-classes e o Estado `:hover`

Quando a pergunta menciona "**when the mouse pointer is on top of it**" ou "**ao passar o rato**":
- `:hover` **ESTÁ ATIVO** → regras com `:hover` são consideradas
- Regras sem `:hover` também continuam a aplicar-se
- Calcula a especificidade normalmente (`:hover` contribui +1 para b)

**Armadilha comum:**
```css
.menu li.item.special:hover { color: purple; }
```
Esta regra só se aplica a elementos com classes `item` **E** `special`. Se o elemento só tem `item`, esta regra não se aplica, mesmo com hover ativo.

---

## TIPO 4: Semântica HTML

### O que é?

Dado uma descrição de conteúdo, escolher o elemento HTML semanticamente correto.

### Como identificar?

> *"Which one of the following is the **semantically correct** tag to use for an element containing …?"*
> *"What is the **best semantic** HTML tag for …?"*

### Estratégia de Resolução

```
1. Identificar o TIPO de conteúdo descrito
2. Eliminar tags não-semânticas (<div>, <span>) e tags inventadas
3. Aplicar as definições corretas dos elementos semânticos
```

---

### Guia Completo de Semântica HTML5

**Estrutura da página:**

| Tag | Semântica | Usar para |
|-----|-----------|-----------|
| `<header>` | Cabeçalho | Logótipo, título principal, nav superior |
| `<footer>` | Rodapé | Direitos de autor, links secundários |
| `<nav>` | Navegação | Menus de navegação principal |
| `<main>` | Conteúdo principal | Conteúdo único da página (único por página!) |
| `<article>` | Artigo independente | Posts de blog, notícias, comentários, widgets |
| `<section>` | Secção temática | Capítulos, partes de uma página (com heading) |
| `<aside>` | Conteúdo tangencial | Barras laterais, publicidade, links relacionados |
| `<div>` | Sem semântica | Apenas para agrupamento visual/layout |

**Elementos de texto:**

| Tag | Semântica | Usar para |
|-----|-----------|-----------|
| `<h1>`–`<h6>` | Heading | Títulos hierárquicos |
| `<p>` | Parágrafo | Texto corrido |
| `<strong>` | Importância | Texto importante (negrito) |
| `<em>` | Ênfase | Texto com ênfase (itálico) |
| `<mark>` | Destaque | Texto destacado/marcado |
| `<time>` | Tempo | Datas e horas (`datetime="2024-01-15"`) |
| `<abbr>` | Abreviatura | Siglas com expansão no `title` |
| `<blockquote>` | Citação longa | Citação de outra fonte |
| `<q>` | Citação inline | Citação curta |
| `<figure>` | Figura | Imagem, diagrama, código com legenda |
| `<figcaption>` | Legenda | Legenda de `<figure>` |
| `<pre>` | Pré-formatado | Código, texto com whitespace significativo |
| `<code>` | Código | Código inline ou em bloco |

---

### Exemplo Resolvido — Pergunta 4 do PDF

**Enunciado:**
> Which one of the following is the semantically correct tag to use for an element containing **ads** for other websites?
> - a. `<sidebar>` 
> - b. `<aside>`
> - c. `<ads>`
> - d. `<nav>`

**Raciocínio:**
- `<sidebar>` → **NÃO EXISTE** em HTML5 (tag inventada, eliminar)
- `<ads>` → **NÃO EXISTE** em HTML5 (tag inventada, eliminar)
- `<nav>` → navegação principal/secundária, não para publicidade
- `<aside>` → conteúdo tangencial/secundário; a spec HTML5 menciona explicitamente anúncios como caso de uso!

**Resposta: `<aside>`** ✅

**Definição W3C de `<aside>`:**
> "Represents a portion of a document whose content is only **indirectly related** to the document's main content. Asides are frequently presented as sidebars or call-out boxes. **Advertising** is related to a page but does not form part of the main content."

---

### Distinções Críticas para o Exame

| `<article>` vs `<section>` |
|---------------------------|
| `<article>` → conteúdo **independente e redistribuível** (pode existir fora do contexto da página) |
| `<section>` → agrupamento **temático** com relação ao conteúdo circundante |

| `<nav>` vs `<aside>` |
|----------------------|
| `<nav>` → links de **navegação** (para dentro do site) |
| `<aside>` → conteúdo **tangencial** (publicidade, links externos, barra lateral) |

| `<strong>` vs `<b>` |
|---------------------|
| `<strong>` → **importância semântica** |
| `<b>` → apenas estilo visual (bold), sem significado |

| `<em>` vs `<i>` |
|-----------------|
| `<em>` → **ênfase semântica** |
| `<i>` → apenas estilo visual (itálico), sem significado |

---

## TIPO 5: Código PHP — Funções de Output

### O que é?

Escrever uma função PHP que recebe dados (normalmente um array associativo) e faz output de HTML formatado.

### Como identificar?

> *"Write a PHP function named `X` that receives an associative array with the following structure: …"*
> *"The function should print an HTML block containing: …"*
> *"Calling the function as … should output the following HTML: …"*

### Estratégia de Resolução (5 passos)

```
1. Ler a estrutura do array de input cuidadosamente
2. Ler o HTML de output esperado e identificar cada parte
3. Mapear cada chave do array → tag HTML correspondente
4. Identificar arrays aninhados → forEach/foreach loop
5. Usar htmlspecialchars() para escapar o output (boa prática)
```

---

### Exemplo Resolvido — Pergunta 5 do PDF

**Enunciado:**
> Write a PHP function named `drawAuthor` that receives an associative array:
> ```php
> [
>   'name' => 'Author Name',
>   'birthYear' => 1950,
>   'books' => ['Book Title 1', 'Book Title 2', ...]
> ]
> ```
> Should output:
> ```html
> <h3>José Saramago</h3>
> <p>Born in 1922</p>
> <ul>
>   <li>Blindness</li>
>   <li>The Gospel According to Jesus Christ</li>
> </ul>
> ```

**Mapeamento:**
```
$author['name']      → dentro de <h3>...</h3>
$author['birthYear'] → dentro de <p>Born in ...</p>
$author['books']     → array → <ul> com um <li> por livro (foreach)
```

**Resposta:**
```php
<?php
function drawAuthor($author) {
    echo "<h3>" . htmlspecialchars($author['name']) . "</h3>";
    echo "<p>Born in " . htmlspecialchars($author['birthYear']) . "</p>";
    echo "<ul>";
    foreach ($author['books'] as $book) {
        echo "<li>" . htmlspecialchars($book) . "</li>";
    }
    echo "</ul>";
}
?>
```

**Por que usar `htmlspecialchars()`?**
- Converte `<` em `&lt;`, `>` em `&gt;`, `"` em `&quot;`, etc.
- Previne XSS (Cross-Site Scripting)
- Boa prática que o exame valoriza

---

### Template Geral para Funções de Output PHP

```php
<?php
function drawSomething($data) {
    // 1. Elemento simples
    echo "<tag>" . htmlspecialchars($data['campo']) . "</tag>";
    
    // 2. Elemento com texto fixo + valor
    echo "<p>Texto fixo " . htmlspecialchars($data['campo']) . "</p>";
    
    // 3. Lista (array aninhado)
    echo "<ul>";
    foreach ($data['lista'] as $item) {
        echo "<li>" . htmlspecialchars($item) . "</li>";
    }
    echo "</ul>";
    
    // 4. Lista com array de objetos
    foreach ($data['objetos'] as $obj) {
        echo "<div>";
        echo "<h4>" . htmlspecialchars($obj['nome']) . "</h4>";
        echo "<p>" . htmlspecialchars($obj['descricao']) . "</p>";
        echo "</div>";
    }
}
?>
```

---

### Padrões Comuns em PHP que aparecem no exame

**Acesso a arrays:**
```php
$array['chave']          // array associativo simples
$array['chave']['sub']   // array aninhado
```

**Loop em array indexado (lista):**
```php
foreach ($array as $item) {
    echo "<li>" . htmlspecialchars($item) . "</li>";
}
```

**Loop em array associativo:**
```php
foreach ($array as $chave => $valor) {
    echo "<dt>" . htmlspecialchars($chave) . "</dt>";
    echo "<dd>" . htmlspecialchars($valor) . "</dd>";
}
```

**Verificar se existe:**
```php
if (isset($data['campo'])) { ... }
if (!empty($data['lista'])) { ... }
```

**Alternativa com echo curto (igualmente válido):**
```php
function drawAuthor($author) { ?>
    <h3><?= htmlspecialchars($author['name']) ?></h3>
    <p>Born in <?= htmlspecialchars($author['birthYear']) ?></p>
    <ul>
        <?php foreach ($author['books'] as $book): ?>
            <li><?= htmlspecialchars($book) ?></li>
        <?php endforeach; ?>
    </ul>
<?php }
```

---

## 🔑 Resumo Final — O que saber de cada tipo

### Tipo 1 (Regex CONTAINS)
- ❌ Sem `^` e `$`
- ✅ Foco no padrão interno
- Verificar os exemplos `false` para entender o que deve falhar

### Tipo 2 (Regex IS/Validação)
- ✅ `^` no início e `$` no fim — **SEMPRE**
- ✅ Usar `(parte)?` para partes opcionais
- Verificar inputs que são muito longos ou com chars errados

### Tipo 3 (Especificidade CSS)
- Fórmula: **(IDs, Classes+PseudoClasses+Atributos, Elementos)**
- Comparar da esquerda para a direita
- Pseudo-classes (`:hover`, `:nth-child`) contribuem para **b**
- `:hover` só ativo se o enunciado disser que o rato está por cima
- Se empate → última regra na folha de estilos

### Tipo 4 (Semântica HTML)
- Tags inventadas (`<sidebar>`, `<ads>`) → eliminar imediatamente
- `<aside>` = conteúdo lateral/tangencial/publicidade
- `<nav>` = navegação
- `<article>` = conteúdo independente
- `<section>` = agrupamento temático

### Tipo 5 (PHP Output)
- Ler o array de input → mapear para tags HTML
- Arrays → `foreach` loop
- `htmlspecialchars()` em todo o output (segurança + boa prática)
- Sintaxe: `echo "<tag>" . $var . "</tag>";`

---

## 📋 Quick Reference — Regex

### Caracteres e Classes
```
\d      [0-9]           dígito
\w      [A-Za-z0-9_]   palavra
\s      [ \t\n\r]       espaço
.       qualquer (exceto \n)
[abc]   a, b ou c
[a-z]   a até z
[^abc]  não a, b nem c
```

### Quantificadores
```
?       0 ou 1 (opcional)
*       0 ou mais
+       1 ou mais
{n}     exatamente n
{n,m}   entre n e m
{n,}    pelo menos n
```

### Âncoras
```
^   início da string
$   fim da string
\b  limite de palavra
```

### Grupos
```
(abc)    grupo de captura
(?:abc)  grupo sem captura
(a|b)    alternativa: a ou b
```

### Exemplos Prontos
```
^\d{4}$                     → exatamente 4 dígitos
^\d{4}(-\d{3})?$            → código postal PT
^\d{4}-(0[1-9]|1[0-2])-\d{2}$  → data YYYY-MM-DD parcial
^[a-zA-Z0-9]+$              → alfanumérico
^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$  → email simples
```

---

## 📋 Quick Reference — Especificidade CSS

### Calcular (a, b, c)

```
Seletor                           → (a, b, c)
────────────────────────────────────────────
*                                 → (0, 0, 0)
li                                → (0, 0, 1)
.classe                           → (0, 1, 0)
:hover                            → (0, 1, 0)
:nth-child(2)                     → (0, 1, 0)
[attr="val"]                      → (0, 1, 0)
#id                               → (1, 0, 0)
li.classe                         → (0, 1, 1)
li:hover                          → (0, 1, 1)
.menu li.item                     → (0, 2, 1)
ul[data-type] li.item             → (0, 2, 2)
#main li                          → (1, 0, 1)
#main li.item:nth-child(2)        → (1, 2, 1)
```

### Desempate
1. Maior **a** ganha → se igual...
2. Maior **b** ganha → se igual...
3. Maior **c** ganha → se igual...
4. **Última** na folha de estilos ganha

---

*Guia criado com base em `sample_moodle.pdf` · FEUP LTW · 2025/2026*
