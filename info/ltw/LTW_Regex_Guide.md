# 🔍 Guia Completo de Expressões Regulares (Regex)
> Do zero ao avançado · Exemplos práticos · Focado no exame LTW
> Referência: PHP (`preg_match`) · JavaScript (`/pattern/`) · HTML (`pattern=""`)

---

## Índice

1. [O que é uma Regex?](#1-o-que-é-uma-regex)
2. [Caracteres Literais](#2-caracteres-literais)
3. [Caracteres Especiais — Escaping](#3-caracteres-especiais--escaping)
4. [Classes de Caracteres `[...]`](#4-classes-de-caracteres-)
5. [Atalhos de Classes](#5-atalhos-de-classes)
6. [O Ponto `.`](#6-o-ponto-)
7. [Âncoras — Posição na String](#7-âncoras--posição-na-string)
8. [Quantificadores — Repetições](#8-quantificadores--repetições)
9. [Greedy vs Lazy](#9-greedy-vs-lazy)
10. [Alternação `|`](#10-alternação-)
11. [Grupos `(...)`](#11-grupos-)
12. [Backreferences](#12-backreferences)
13. [Lookaround](#13-lookaround)
14. [Modificadores / Flags](#14-modificadores--flags)
15. [Regex em PHP](#15-regex-em-php)
16. [Regex em JavaScript](#16-regex-em-javascript)
17. [Regex em HTML](#17-regex-em-html)
18. [Como Construir uma Regex do Zero](#18-como-construir-uma-regex-do-zero)
19. [Exemplos de Exame Resolvidos](#19-exemplos-de-exame-resolvidos)
20. [Cheat Sheet Final](#20-cheat-sheet-final)

---

## 1. O que é uma Regex?

Uma **expressão regular** (regex ou regexp) é um padrão que descreve um conjunto de strings. É como um "filtro" que identifica strings que correspondem a uma certa estrutura.

```
Texto:   "O meu telefone é 912345678 e o código postal é 4100-007."
Padrão:  \d{9}
Encontra: "912345678"
```

**Dois modos principais:**

| Modo | Questão-chave | Exemplo de enunciado |
|------|--------------|----------------------|
| **Pesquisa (search/contains)** | O padrão existe em algum sítio? | *"matches if the input **contains**…"* |
| **Validação (validate/is)** | A string inteira é o padrão? | *"checks if the input **is** a valid…"* |

> 🔑 **Regra de ouro:** Validação → `^...$` | Pesquisa → sem âncoras

---

## 2. Caracteres Literais

O mais simples: a regex `casa` corresponde exatamente à sequência de caracteres `c`, `a`, `s`, `a`.

```
Regex:   cat
Texto:   "I have a cat at home"
Match:   "I have a [cat] at home"   ✅

Regex:   cat
Texto:   "catfish"
Match:   "[cat]fish"                ✅ (encontrou "cat" dentro)

Regex:   cat
Texto:   "CAT"
Match:   nenhum                     ❌ (case-sensitive por padrão)
```

**Caracteres alfanuméricos** (letras e números) são literais — correspondem a si próprios.

---

## 3. Caracteres Especiais — Escaping

Alguns caracteres têm significado especial e precisam de ser **escapados com `\`** para serem tratados como literais.

**Os 12 caracteres especiais:**
```
\ ^ $ . | ? * + ( ) [ {
```

```
Regex:   \+        → corresponde ao "+" literal
Regex:   \.        → corresponde ao "." literal
Regex:   \(        → corresponde ao "(" literal
Regex:   \*        → corresponde ao "*" literal
Regex:   \\        → corresponde ao "\" literal
```

**Exemplos:**
```
Regex:   3\.14      Match em: "3.14"    ❌ em "3X14"
Regex:   \(ok\)     Match em: "(ok)"    ❌ em "ok"
Regex:   https?://  Match em: "http://" e "https://"
```

**Dentro de `[...]`** os únicos especiais são: `] \ ^ -`

---

## 4. Classes de Caracteres `[...]`

Uma classe de caracteres corresponde a **exatamente um caractere** de entre os listados.

### 4.1 Classe Simples

```
[abc]    → corresponde a "a", "b" ou "c" (um deles)
[aeiou]  → qualquer vogal
[AEIOU]  → qualquer vogal maiúscula

Exemplo:
  Regex:   gr[ae]y
  Match:   "gray" ✅   "grey" ✅   "griy" ❌   "graey" ❌
```

### 4.2 Intervalos

Usa-se `-` para definir um intervalo (deve estar ENTRE dois caracteres):

```
[a-z]       → qualquer letra minúscula (a até z)
[A-Z]       → qualquer letra maiúscula
[0-9]       → qualquer dígito
[a-zA-Z]    → qualquer letra (maiúscula ou minúscula)
[a-zA-Z0-9] → qualquer letra ou dígito
[a-f]       → letras a, b, c, d, e ou f
[0-9a-fA-F] → dígito hexadecimal
```

```
Regex:   [0-9]{4}
Match:   "1234" ✅   "abcd" ❌   "12" ❌ (só 2 dígitos)
```

### 4.3 Classe Negada `[^...]`

O `^` NO INÍCIO da classe inverte a seleção — corresponde a qualquer caractere que **NÃO** esteja na lista:

```
[^abc]     → qualquer caractere exceto a, b ou c
[^0-9]     → qualquer caractere que não seja dígito
[^a-zA-Z]  → qualquer coisa que não seja letra
[^>]       → qualquer caractere exceto ">"
```

```
Regex:   <[^>]+>      → tag HTML (< seguido de tudo exceto > seguido de >)
Match:   "<strong>" ✅   "<div class='x'>" ✅
```

> ⚠️ `^` só tem significado especial como **primeiro** caractere dentro de `[...]`.
> `[a^b]` corresponde a "a", "^" ou "b" (o ^ é literal aqui).

### 4.4 Caracteres especiais dentro de `[...]`

Dentro de uma classe, apenas estes precisam de escape:
```
]   → \]   (fecha a classe)
\   → \\   (backslash)
^   → \^   (se não for o primeiro, é literal)
-   → \-   ou colocar no início/fim: [-abc] ou [abc-]
```

Todos os outros caracteres especiais são literais dentro de `[...]`:
```
[.+*?]  → corresponde a ".", "+", "*" ou "?"  (são literais aqui)
```

---

## 5. Atalhos de Classes

Abreviações para classes frequentes:

| Atalho | Equivalente | Significado |
|--------|------------|-------------|
| `\d` | `[0-9]` | Dígito |
| `\D` | `[^0-9]` | Não-dígito |
| `\w` | `[A-Za-z0-9_]` | Carácter de "palavra" (inclui underscore) |
| `\W` | `[^A-Za-z0-9_]` | Não-palavra |
| `\s` | `[ \t\r\n\f]` | Espaço em branco (space, tab, newline...) |
| `\S` | `[^ \t\r\n\f]` | Não-espaço |

**Podem ser usados dentro de `[...]`:**
```
[\d\s]      → dígito ou espaço
[^\d]       → o mesmo que \D
[\w-]       → carácter de palavra ou hífen
```

**Exemplos:**
```
\d{3}        → "123", "007", "999"
\w+          → "hello", "hello_world", "var123"
\s+          → " ", "\t", "   " (um ou mais espaços)
\D+          → "abc", "!@#", " " (sem dígitos)
```

---

## 6. O Ponto `.`

O `.` corresponde a **qualquer caractere**, exceto newline (`\n`):

```
Regex:   c.t
Match:   "cat" ✅   "cot" ✅   "c@t" ✅   "ct" ❌   "coat" ❌

Regex:   .+
Match:   qualquer string não-vazia de uma linha
```

> ⚠️ **Armadilha:** `.` não é dígito, letra, etc. — é QUALQUER coisa.
> Para corresponder ao ponto literal, usar `\.`.
>
> `3.14` → corresponderia a "3X14", "3.14", "3!14"...
> `3\.14` → só corresponderia a "3.14"

**Com o modificador `s` (dotall):** `.` passa a incluir `\n`.

---

## 7. Âncoras — Posição na String

As âncoras **não consomem caracteres** — indicam uma posição.

### 7.1 Início e Fim

| Âncora | Posição | Uso |
|--------|---------|-----|
| `^` | Início da string | Garantir que o match começa no início |
| `$` | Fim da string | Garantir que o match termina no fim |

```
Regex:   ^hello
Match:   "hello world" ✅    "say hello" ❌

Regex:   world$
Match:   "hello world" ✅    "world domination" ❌

Regex:   ^hello$
Match:   "hello" ✅          "say hello" ❌   "hello world" ❌
```

**CRUCIAL para validação:**
```
Regex:   \d+          → encontra dígitos em "abc123def" ✅
Regex:   ^\d+$        → a string INTEIRA deve ser dígitos → "abc123def" ❌
```

### 7.2 Limite de Palavra `\b`

Corresponde à posição entre um `\w` e um `\W` (ou início/fim de string):

```
Regex:   \bcat\b
Match:   "the cat sat" ✅     "concatenate" ❌     "cats" ❌

Regex:   \bis\b
Match:   "This island is beautiful"
         Encontra: "is" isolado, NÃO o "is" em "This" ou "island"
```

### 7.3 Modo Multiline

Com o modificador `m`, `^` e `$` passam a corresponder ao início/fim de **cada linha**:

```php
preg_match('/^\d+$/m', "abc\n123\ndef") // encontra "123"
```

---

## 8. Quantificadores — Repetições

Os quantificadores controlam **quantas vezes** o elemento anterior pode repetir.

### 8.1 Quantificadores Base

| Quantificador | Repetições | Memória |
|--------------|-----------|---------|
| `?` | 0 ou 1 | opcional |
| `*` | 0 ou mais | zero ou mais |
| `+` | 1 ou mais | um ou mais |
| `{n}` | exatamente n | exato |
| `{n,m}` | entre n e m | intervalo |
| `{n,}` | pelo menos n | mínimo |
| `{,m}` | no máximo m | máximo |

```
Regex:   colou?r     → "colour" ✅   "color" ✅   "colouur" ❌
Regex:   go+gle      → "gogle" ✅    "google" ✅   "ggle" ❌
Regex:   go*gle      → "ggle" ✅     "gogle" ✅    "google" ✅
Regex:   \d{4}       → "1234" ✅     "12345" ❌    "123" ❌
Regex:   \d{2,4}     → "12" ✅       "1234" ✅     "12345" ❌ (sem âncoras, encontra os primeiros 4)
Regex:   \d{3,}      → "123" ✅      "1234567" ✅  "12" ❌
```

### 8.2 O Quantificador aplica-se ao elemento IMEDIATAMENTE ANTERIOR

```
ab+    → "a" seguido de um ou mais "b": "ab" ✅  "abb" ✅  "a" ❌
(ab)+  → o grupo "ab" repetido: "ab" ✅  "ababab" ✅  "a" ❌
[0-9]+ → um ou mais dígitos
\d{3}  → exatamente 3 dígitos
```

---

## 9. Greedy vs Lazy

### 9.1 Greedy (guloso) — padrão

Por padrão, os quantificadores são **greedy**: tentam capturar o **máximo** possível.

```
Regex:   <.+>
Texto:   "<strong>olá</strong>"
Match:   "<strong>olá</strong>"   (tudo de < até o ÚLTIMO >)
                                   ← tenta capturar o máximo!
```

### 9.2 Lazy (preguiçoso) — adicionar `?`

Adicionar `?` após o quantificador torna-o **lazy**: captura o **mínimo** possível.

```
Regex:   <.+?>
Texto:   "<strong>olá</strong>"
Match:   "<strong>" e depois "</strong>"   (para no primeiro >)
```

| Quantificador | Greedy | Lazy |
|--------------|--------|------|
| `+` | `+` | `+?` |
| `*` | `*` | `*?` |
| `?` | `?` | `??` |
| `{n,m}` | `{n,m}` | `{n,m}?` |

### 9.3 Alternativa mais eficiente: Classe Negada

Em vez de lazy, muitas vezes é melhor usar uma classe negada:

```
<.+?>    → lazy (backtracking intenso, lento)
<[^>]+>  → "< seguido de tudo exceto >, uma ou mais vezes, seguido de >"
           → mais eficiente e equivalente!
```

**Regra prática:** Quando sabes qual o caractere que termina o padrão, usa uma classe negada em vez de lazy.

---

## 10. Alternação `|`

O pipe `|` funciona como um **OR** — corresponde a um de dois padrões:

```
Regex:   gato|cão
Match:   "tenho um gato" ✅    "tenho um cão" ✅    "tenho um peixe" ❌

Regex:   http|ftp|https
Match:   "http" ✅   "ftp" ✅   "https" ✅   "smtp" ❌
```

> ⚠️ **A alternação tem precedência baixa** — aplica-se a TUDO antes e depois:
> ```
> cat|dog food  →  ("cat") | ("dog food")   NÃO   "cat" ou "dog" + " food"!
> (cat|dog) food →  correto: ("cat" ou "dog") + " food"
> ```

**Ordem importa:** O motor tenta o primeiro alternativo primeiro. Se corresponder, não tenta o segundo.

```
Regex:   http|https
Texto:   "https://..."
Match:   "http" ✅  (mas perde o "s"! É melhor: https?://)
```

---

## 11. Grupos `(...)`

Os parênteses servem para:
1. **Agrupar** — aplicar quantificadores/alternação a múltiplos caracteres
2. **Capturar** — guardar o conteúdo para uso posterior
3. **Organizar** a regex logicamente

### 11.1 Agrupamento

```
Regex:   (ab)+
Match:   "ab" ✅   "abab" ✅   "ababab" ✅   "a" ❌

Regex:   (ha){3}
Match:   "hahaha" ✅   "ha" ❌

Regex:   (gato|cão) meu
Match:   "gato meu" ✅   "cão meu" ✅   "peixe meu" ❌
```

### 11.2 Captura — Grupos Numerados

Cada grupo `(...)` é automaticamente **numerado de 1 para a frente** (da esquerda para a direita, pelo parêntese de abertura). O match completo é sempre o grupo **0**.

```
Regex:   (\d{4})-(0[1-9]|1[0-2])-(\d{2})
Texto:   "2024-05-28"

Grupo 0 (match completo): "2024-05-28"
Grupo 1 ((\d{4})):        "2024"
Grupo 2 ((0[1-9]|1[0-2])): "05"
Grupo 3 ((\d{2})):        "28"
```

```
Regex:   ((https?|ftp)://)?([\w.-]+)
Texto:   "http://example.com"

Grupo 0: "http://example.com"
Grupo 1: "http://"
Grupo 2: "http"
Grupo 3: "example.com"
```

> 💡 **Truque para contar grupos:** conta os parênteses de abertura `(` da esquerda para a direita.

### 11.3 Grupo Sem Captura `(?:...)`

Quando queres agrupar sem criar um grupo de captura (mais eficiente, numeração não avança):

```
Regex:   (?:gato|cão) meu    (agrupa mas não captura)
Regex:   (?:https?|ftp)://   (agrupa as alternativas)
```

```
Regex com captura:    (\d{4})(?:-(\d{3}))?
Texto:                "4100-123"
Grupo 1: "4100"   (os 4 dígitos)
Grupo 2: "123"    (os 3 dígitos, sem o hífen)
```

### 11.4 Grupos Opcionais

Tornar um grupo inteiro opcional com `?`:

```
Regex:   ^\d{4}(-\d{3})?$
         ↑              ↑
         Obrigatório    Opcional (grupo inteiro)

Match:   "4100" ✅   "4100-123" ✅   "4100-12" ❌   "4100-1234" ❌
```

---

## 12. Backreferences

Referências a grupos de captura anteriores — reutiliza o **mesmo texto** que foi capturado.

```
Sintaxe: \1 (grupo 1), \2 (grupo 2), etc. — em PHP e JS
         $1, $2, etc. — em substituições (replacement)
```

**Uso: detetar texto duplicado:**
```
Regex:   (\w+) \1
Texto:   "the the dog"
Match:   "the the"   (mesma palavra repetida)

Regex:   (\w)\1
Texto:   "aabcdd"
Match:   "aa" e "dd"   (letra duplicada)
```

**Uso: padrão com início = fim:**
```
Regex:   ([0-9])[0-9]+\1
Texto:   "1231"
Match:   "1231"   (começa e termina com 1)

Texto:   "41231"
Começa em 4 → não encontra 4 no fim → backtrack → começa em 1 → encontra "1231"
```

**Uso: tags HTML balanceadas:**
```
Regex:   <([a-z]+)>.*?</\1>
Texto:   "<p>olá</p>"
Match:   a tag de abertura e fecho são a mesma!
         "<p>olá</p>" ✅
         "<p>olá</div>" ❌
```

---

## 13. Lookaround

Asserções de "olhar em frente/trás" — verificam contexto **sem consumir** caracteres.

> São **zero-length assertions** — dizem "o que vem antes/depois" mas não fazem parte do match.

### 13.1 Lookahead Positivo `(?=...)`

Corresponde se **for seguido** por algo:

```
Sintaxe: X(?=Y)   →   X se seguido de Y

Regex:   \d+(?= euros)
Texto:   "custa 100 euros e mais 50 dólares"
Match:   "100"   (mas "50" não, pois não é seguido de " euros")
```

```
Regex:   (gato|cão)(?=s)
Match:   "gatos" ✅ (o "s" não faz parte do match!)
         "cãos"  ✅
         "gato"  ❌ (não é seguido de "s")
```

### 13.2 Lookahead Negativo `(?!...)`

Corresponde se **NÃO for seguido** por algo:

```
Sintaxe: X(?!Y)   →   X se NÃO seguido de Y

Regex:   (gato|cão)(?!s)
Match:   "gato" ✅   "gatos" ❌ (é seguido de "s")
```

```
Regex:   \d+(?!\.\d)   →   número inteiro (não seguido de ponto + dígito)
Match:   "123" ✅   "123.45" ❌ (o "123" é seguido de ".4")
```

### 13.3 Lookbehind Positivo `(?<=...)`

Corresponde se **for precedido** por algo:

```
Sintaxe: (?<=Y)X   →   X se precedido de Y

Regex:   (?<=€)\d+
Texto:   "€100 e $50"
Match:   "100"   (mas "50" não, não é precedido de "€")
```

```
Regex:   (?<=is)land
Texto:   "England is part of an island"
Match:   "land" em "island" (precedido de "is")
```

### 13.4 Lookbehind Negativo `(?<!...)`

Corresponde se **NÃO for precedido** por algo:

```
Sintaxe: (?<!Y)X   →   X se NÃO precedido de Y

Regex:   (?<!some)thing
Texto:   "There is something about this thing"
Match:   "thing" isolado ✅   "something" ❌
```

### Resumo Lookaround

```
(?=Y)   → Lookahead positivo:  vai ser seguido de Y
(?!Y)   → Lookahead negativo:  NÃO vai ser seguido de Y
(?<=Y)  → Lookbehind positivo: foi precedido de Y
(?<!Y)  → Lookbehind negativo: NÃO foi precedido de Y
```

**Todos são zero-length** — o Y não faz parte do match final!

---

## 14. Modificadores / Flags

Alteram o comportamento da regex. Colocam-se após o delimitador final.

| Flag | PHP | JS | Efeito |
|------|-----|-----|--------|
| `i` | `/pat/i` | `/pat/i` | Case-insensitive (`[a-z]` também corresponde a maiúsculas) |
| `g` | (não existe, usar `preg_match_all`) | `/pat/g` | Global — encontra TODOS os matches |
| `m` | `/pat/m` | `/pat/m` | Multiline — `^` e `$` por início/fim de linha |
| `s` | `/pat/s` | `/pat/s` | Dotall — `.` corresponde também a `\n` |
| `x` | `/pat/x` | — | Extended — permite whitespace e comentários na regex |
| `u` | `/pat/u` | `/pat/u` | Unicode — suporte a UTF-8 |

```php
// i - case insensitive
preg_match('/hello/i', 'HELLO') // true

// m - multiline
preg_match('/^\d+$/m', "abc\n123\ndef") // true (encontra "123")

// s - dotall
preg_match('/início.*fim/s', "início\n\nfim") // true (. cobre \n)
```

```javascript
// g - global (todos os matches)
'cat bat sat'.match(/[a-z]at/g)  // ['cat', 'bat', 'sat']

// i - case insensitive
/hello/i.test('HELLO')  // true

// m - multiline
/^\d+$/m.test("abc\n123\ndef")  // true
```

---

## 15. Regex em PHP

PHP usa **PCRE** (Perl Compatible Regular Expressions).

### 15.1 Delimitadores

O padrão em PHP é delimitado por um carácter que não faça parte do padrão. O mais comum é `/`:

```php
/padrão/
/padrão/i      // com flag i
#padrão#       // alternativa com #
~padrão~       // alternativa com ~
```

> Se o padrão contém `/`, usar `#` ou `~` como delimitador para evitar escaping.

### 15.2 `preg_match` — testar se existe um match

```php
int preg_match(string $pattern, string $subject [, array &$matches])
```

- Devolve **1** se corresponde, **0** se não, **false** em caso de erro
- `$matches[0]` = match completo, `$matches[1]` = grupo 1, etc.

```php
// Verificar se contém um número
if (preg_match('/\d+/', $str)) {
    echo "Contém número";
}

// Extrair grupos
if (preg_match('/^(\d{4})-(\d{2})-(\d{2})$/', '2024-05-28', $m)) {
    echo $m[0]; // "2024-05-28"
    echo $m[1]; // "2024"
    echo $m[2]; // "05"
    echo $m[3]; // "28"
}

// Validar — padrão completo
function validarEmail($email) {
    return preg_match('/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/', $email);
}

function validarTelefone($tel) {
    return preg_match('/^\d{9}$/', $tel);
}

function validarCodigoPostal($cp) {
    return preg_match('/^\d{4}(-\d{3})?$/', $cp);
}
```

### 15.3 `preg_match_all` — todos os matches

```php
int preg_match_all(string $pattern, string $subject [, array &$matches])
```

- Devolve o **número de matches** encontrados
- `$matches[0]` = array com todos os matches completos
- `$matches[1]` = array com todos os matches do grupo 1

```php
$str = "Preços: €100, $50, €200";
preg_match_all('/€(\d+)/', $str, $m);
print_r($m[0]); // ["€100", "€200"]
print_r($m[1]); // ["100", "200"]
```

### 15.4 `preg_replace` — substituir

```php
mixed preg_replace(mixed $pattern, mixed $replacement, mixed $subject)
```

- No replacement, `$1`, `$2`, etc. referenciam grupos de captura
- Ou `\\1`, `\\2` (com backslash)

```php
// Substituição simples
$resultado = preg_replace('/\s+/', ' ', $texto);     // colapsar espaços
$resultado = preg_replace('/[^a-zA-Z0-9]/', '', $str); // só alfanumérico

// Com backreferences no replacement
echo preg_replace('/(gato|cão)/', 'animal ($1)', 'tenho um gato');
// "tenho um animal (gato)"

// Formatar número de telefone
echo preg_replace('/^(\d{3})(\d{3})(\d{3})$/', '$1 $2 $3', '912345678');
// "912 345 678"

// Adicionar tags HTML
$html = preg_replace('/(\w+)/', '<b>$1</b>', 'hello world');
// "<b>hello</b> <b>world</b>"
```

### 15.5 `preg_split` — dividir string

```php
$palavras = preg_split('/[\s,]+/', 'um, dois,três  quatro');
// ["um", "dois", "três", "quatro"]
```

### 15.6 Validação completa — template

```php
function validar($valor, $padrao) {
    // Sempre com ^ e $ para validação completa
    return (bool) preg_match('/^' . $padrao . '$/', $valor);
}

// Funções de validação prontas
function isDigitsOnly($str)      { return preg_match('/^\d+$/', $str); }
function isAlphanumeric($str)    { return preg_match('/^[a-zA-Z0-9]+$/', $str); }
function isDate($str)            { return preg_match('/^\d{4}-\d{2}-\d{2}$/', $str); }
function isPhone($str)           { return preg_match('/^\d{9}$/', $str); }
function isPostalCode($str)      { return preg_match('/^\d{4}(-\d{3})?$/', $str); }
```

---

## 16. Regex em JavaScript

### 16.1 Sintaxe

```javascript
// Literal (preferido — verificado em tempo de compilação)
const re = /padrão/flags;

// Constructor (quando o padrão é dinâmico)
const re = new RegExp('padrão', 'flags');
const re = new RegExp(`\\d{${n}}`, 'i'); // interpolação
```

> ⚠️ Em strings, `\d` precisa de ser `\\d` (o `\` precisa de escape na string).

### 16.2 Métodos de RegExp

```javascript
// test() — boolean, rápido para verificar existência
/^\d{9}$/.test('912345678')    // true
/^\d{9}$/.test('91234567')     // false

// exec() — devolve array com match e grupos, ou null
const m = /(\d{4})-(\d{2})/.exec('2024-05');
// m[0] = "2024-05", m[1] = "2024", m[2] = "05"
// m.index = posição do match
```

### 16.3 Métodos de String

```javascript
// match() — sem flag g: como exec(); com flag g: todos os matches
'4100-123 5000'.match(/\d{4}(-\d{3})?/g)
// ["4100-123", "5000"]

'2024-05'.match(/(\d{4})-(\d{2})/)
// ["2024-05", "2024", "05", index: 0, ...]

// search() — posição do primeiro match ou -1
'zip: 4100-123'.search(/\d{4}/)  // 5

// replace() — substituir (sem g: só o primeiro; com g: todos)
'cat bat cat'.replace(/cat/, 'dog')   // "dog bat cat"
'cat bat cat'.replace(/cat/g, 'dog')  // "dog bat dog"

// Com grupos de captura
'2024-05-28'.replace(/(\d{4})-(\d{2})-(\d{2})/, '$3/$2/$1')
// "28/05/2024"

// split() — dividir por padrão
'um, dois,três  quatro'.split(/[\s,]+/)
// ["um", "dois", "três", "quatro"]

// matchAll() — iterador com todos os matches e grupos (ES2020)
for (const m of '1a 2b 3c'.matchAll(/(\d)(\w)/g)) {
    console.log(m[1], m[2]); // "1" "a", "2" "b", "3" "c"
}
```

### 16.4 Validação em JS

```javascript
function validarTelefone(tel) {
    return /^\d{9}$/.test(tel);
}

function validarEmail(email) {
    return /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/.test(email);
}

function validarData(data) {
    return /^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$/.test(data);
}
```

---

## 17. Regex em HTML

O atributo `pattern` em `<input>` aceita uma regex:

```html
<!-- Nota: NÃO tem delimitadores; ^ e $ são implícitos (valida o campo inteiro) -->
<input type="text" pattern="\d{9}" title="9 dígitos">
<input type="text" pattern="\d{4}(-\d{3})?" title="Código postal">
<input type="text" pattern="[A-Za-z]{2,50}" title="Só letras">
<input type="text" pattern="[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}">
```

> ⚠️ `pattern` **valida o campo inteiro** automaticamente (como se tivesse `^...$`).
> Não precisas de adicionar `^` e `$`.

---

## 18. Como Construir uma Regex do Zero

### Método dos 5 Passos

```
1. IDENTIFICAR o tipo (contains ou is/validação)
2. DECOMPOR o formato em partes
3. TRADUZIR cada parte para regex
4. COMBINAR as partes
5. TESTAR com exemplos positivos E negativos
```

---

### Exemplo A — Data YYYY-MM-DD (validação IS)

**Passo 1 — Tipo:** É uma validação ("is a valid date") → usar `^...$`

**Passo 2 — Decompor:**
```
YYYY - MM - DD
```

**Passo 3 — Traduzir:**
```
YYYY → 4 dígitos quaisquer → \d{4}
-    → hífen literal → -
MM   → meses válidos 01-12:
         01-09 → 0[1-9]
         10-12 → 1[0-2]
       Combinado: (0[1-9]|1[0-2])
-    → hífen literal → -
DD   → dias válidos 01-31:
         01-09 → 0[1-9]
         10-29 → [12][0-9]  (10-19 e 20-29)
         30-31 → 3[01]
       Combinado: (0[1-9]|[12][0-9]|3[01])
```

**Passo 4 — Combinar:**
```
^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$
```

**Passo 5 — Testar:**
```
"2024-05-28" ✅
"1999-12-31" ✅
"2024-5-8"   ❌ (MM e DD sem zero)
"2024-13-01" ❌ (mês 13 inválido)
"2024-00-05" ❌ (mês 00 inválido)
"2024-05-32" ❌ (dia 32 inválido)
```

---

### Exemplo B — Código Postal Português (validação IS)

**Passo 1:** Validação → `^...$`

**Passo 2:**
```
Formato 1: XXXX      (4 dígitos)
Formato 2: XXXX-YYY  (4 dígitos, hífen, 3 dígitos)
```

**Passo 3:**
```
XXXX      → \d{4}
-YYY      → -\d{3}
Opcional  → (-\d{3})?
```

**Passo 4:**
```
^\d{4}(-\d{3})?$
```

**Passo 5:**
```
"4100"     ✅
"4100-123" ✅
"4100123"  ❌ (sem hífen mas 7 dígitos)
"41001234" ❌ (muitos dígitos)
"abc-123"  ❌ (não são dígitos)
"123-456"  ❌ (só 3 dígitos antes do -)
```

---

### Exemplo C — Pesquisa de Data em Texto (CONTAINS)

**Passo 1:** Pesquisa → sem `^` e `$`

**Passo 2:** Mesma estrutura da data

**Passo 3:** Mesmo que o Exemplo A

**Passo 4:**
```
\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])
```

**Passo 5:**
```
"Today is 2024-05-28."     ✅ (encontra a data em qualquer posição)
"Start2023-01-01Middle"    ✅ (a data existe mesmo sem espaços)
"2024-5-8 is invalid"      ❌ (MM e DD sem zero)
```

---

### Exemplo D — URL simples

**Requisito:** `http://`, `https://` ou `ftp://` seguido de domínio

```
Passo 2 — Decompor:
  protocolo + :// + domínio

Passo 3:
  protocolo → http, https, ftp
            → https? → "http" ou "https"  OU  usar (https?|ftp)
  ://       → ://  (literal)
  domínio   → letras, números, pontos, hífens: [a-zA-Z0-9.-]+

Passo 4:
  (https?|ftp)://[a-zA-Z0-9.-]+
  
  Com path opcional:
  (https?|ftp)://[a-zA-Z0-9.-]+(/[^\s]*)?
```

---

### Exemplo E — NIF Português

**Requisito:** 9 dígitos, começa por 1, 2, 3, 5, 6, 7, 8 ou 9

```
Passo 2:
  [primeiro dígito válido] + [8 dígitos]

Passo 3:
  primeiro dígito: [123456789] ou [1-9] (mas excluindo 4 e 0)
                   → [123567890] — não! NIF não começa por 0
                   → [1-9] se todos forem válidos
  restantes: \d{8}

Passo 4:
  ^[1-9]\d{8}$
  
  Se só alguns dígitos iniciais são válidos:
  ^[123456789]\d{8}$   (equivalente a ^[1-9]\d{8}$ se todos 1-9 são válidos)
```

---

## 19. Exemplos de Exame Resolvidos

### E1 — Pergunta tipo "contains" com restrições nos dígitos

**Enunciado:** Regex que encontra uma data `YYYY-MM-DD` onde MM começa por 0 ou 1, e DD começa por 0, 1, 2 ou 3.

```
Análise:
  YYYY → qualquer 4 dígitos → \d{4}
  MM   → 0X ou 1X → [01][0-9]  (mais simples que (0[0-9]|1[0-9]))
  DD   → 0X, 1X, 2X ou 3X → [0-3][0-9]

Resposta (contains, sem âncoras):
  \d{4}-[01][0-9]-[0-3][0-9]

Versus a versão com meses/dias válidos:
  \d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])
```

> ⚠️ **LÊ O ENUNCIADO COM ATENÇÃO:** se diz "first digit is 0 or 1" sem mais restrições → `[01][0-9]`; se especifica meses válidos → `(0[1-9]|1[0-2])`.

---

### E2 — Código postal com validação estrita

**Enunciado:** `XXXX` (4 dígitos) ou `XXXX-YYY` (4+3 dígitos), nada mais.

```
Análise:
  Formato 1: \d{4}
  Formato 2: \d{4}-\d{3}

  Observação: Formato 2 = Formato 1 + "-\d{3}" opcional

Resposta:
  ^\d{4}(-\d{3})?$

Testes:
  "4100"     → ^\d{4}$ ✅
  "4100-123" → ^\d{4}-\d{3}$ ✅
  "123-456"  → \d{4} precisa de 4, só tem 3 ❌
  "50000"    → após \d{4}="5000", sobra "0" que não é fim → $ falha ❌
  "4100-12a" → "a" não é \d ❌
```

---

### E3 — Número de telefone com formatos múltiplos

**Enunciado:** 9 dígitos (`XXXXXXXXX`) OU formato com hífens (`XXX-XXX-XXX`)

```
Análise:
  Formato 1: \d{9}
  Formato 2: \d{3}-\d{3}-\d{3}

  São formatos diferentes → alternação

Resposta:
  ^\d{9}$|^\d{3}-\d{3}-\d{3}$

  Melhor (mais limpo):
  ^(\d{9}|\d{3}-\d{3}-\d{3})$
  ou equivalente:
  ^\d{3}(-\d{3}-\d{3}|\d{6})$

Testes:
  "912345678"   ✅
  "912-345-678" ✅
  "912345"      ❌
  "912-3456-78" ❌
```

---

### E4 — Endereço de email básico

**Enunciado:** Validar endereço de email.

```
Estrutura: local@domínio.tld

  local   → letras, números, pontos, underscores, hífens: [a-zA-Z0-9._%+-]+
  @       → @
  domínio → letras, números, hífens, pontos: [a-zA-Z0-9.-]+
  .       → \. (ponto literal)
  tld     → 2 ou mais letras: [a-zA-Z]{2,}

Resposta:
  ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$

Testes:
  "user@example.com"      ✅
  "user.name+tag@mail.pt" ✅
  "user"                  ❌ (sem @)
  "@example.com"          ❌ (sem local)
  "user@"                 ❌ (sem domínio)
  "user@.com"             ❌ ([a-zA-Z0-9.-]+ precisa de pelo menos 1 char)
```

---

### E5 — Regex para tags HTML

**Objetivo:** Encontrar todas as tags de abertura HTML

```
Estrutura: < + nome + atributos opcionais + >

Resposta (simples):
  <[a-zA-Z][^>]*>

Explicação:
  <            → < literal
  [a-zA-Z]     → nome começa por letra
  [^>]*        → seguido de tudo exceto >, zero ou mais vezes
  >            → > literal

Testes:
  "<p>"                  ✅
  "<div class='x'>"      ✅
  "<br>"                 ✅
  "</p>"                 ❌ (começa por / após <, não é letra)
  "<123>"                ❌ (começa por dígito)
```

---

### E6 — Verificar password forte

**Requisito:** Mínimo 8 chars, pelo menos 1 maiúscula, 1 minúscula, 1 dígito

```
Estratégia: usar lookaheads para verificar cada requisito independentemente

Resposta:
  ^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$

Explicação:
  ^              → início
  (?=.*[A-Z])    → lookahead: em algum sítio tem maiúscula
  (?=.*[a-z])    → lookahead: em algum sítio tem minúscula
  (?=.*\d)       → lookahead: em algum sítio tem dígito
  .{8,}          → pelo menos 8 caracteres (qualquer coisa)
  $              → fim

Testes:
  "Password1"  ✅
  "password1"  ❌ (sem maiúscula)
  "PASSWORD1"  ❌ (sem minúscula)
  "Password"   ❌ (sem dígito)
  "Pass1"      ❌ (menos de 8 chars)
```

---

## 20. Cheat Sheet Final

### Síntese de Todos os Componentes

```
╔══════════════════════════════════════════════════════════════════╗
║                    REGEX — CHEAT SHEET                          ║
╠══════════════════════════════════════════════════════════════════╣
║  LITERAIS                                                       ║
║  abc        → sequência literal "abc"                           ║
║  \.         → ponto literal (escape de .)                       ║
║  \+         → + literal    \*  → * literal                      ║
╠══════════════════════════════════════════════════════════════════╣
║  CLASSES                                                        ║
║  [abc]      → a, b ou c                                         ║
║  [a-z]      → a até z                                           ║
║  [^abc]     → não a, b nem c                                    ║
║  .          → qualquer char (exceto \n)                         ║
╠══════════════════════════════════════════════════════════════════╣
║  ATALHOS                                                        ║
║  \d  [0-9]             \D  [^0-9]                               ║
║  \w  [A-Za-z0-9_]      \W  [^\w]                                ║
║  \s  [ \t\r\n\f]       \S  [^\s]                                ║
╠══════════════════════════════════════════════════════════════════╣
║  QUANTIFICADORES (greedy por padrão)                            ║
║  ?    0 ou 1     ??   lazy                                      ║
║  *    0 ou mais  *?   lazy                                      ║
║  +    1 ou mais  +?   lazy                                      ║
║  {n}  exato n                                                   ║
║  {n,m} entre n e m  {n,m}? lazy                                 ║
║  {n,}  min n    {,m}  max m                                     ║
╠══════════════════════════════════════════════════════════════════╣
║  ÂNCORAS (zero-length)                                          ║
║  ^    início da string (ou linha com flag m)                    ║
║  $    fim da string (ou linha com flag m)                       ║
║  \b   limite de palavra                                         ║
║  \B   não limite de palavra                                     ║
╠══════════════════════════════════════════════════════════════════╣
║  ALTERNAÇÃO                                                     ║
║  a|b         → a ou b                                           ║
║  (cat|dog)   → "cat" ou "dog" (agrupar!)                        ║
╠══════════════════════════════════════════════════════════════════╣
║  GRUPOS                                                         ║
║  (abc)       → grupo de captura (numerado)                      ║
║  (?:abc)     → grupo sem captura                                ║
║  (abc)?      → grupo opcional                                   ║
║  \1 \2 ...   → backreference                                    ║
╠══════════════════════════════════════════════════════════════════╣
║  LOOKAROUND (zero-length)                                       ║
║  (?=Y)   lookahead positivo: seguido de Y                       ║
║  (?!Y)   lookahead negativo: NÃO seguido de Y                   ║
║  (?<=Y)  lookbehind positivo: precedido de Y                    ║
║  (?<!Y)  lookbehind negativo: NÃO precedido de Y               ║
╠══════════════════════════════════════════════════════════════════╣
║  CONTÉM vs VALIDA                                               ║
║  CONTÉM:  sem ^ e $   →   \d{4}-\d{2}-\d{2}                    ║
║  VALIDA:  com ^ e $   →   ^\d{4}-\d{2}-\d{2}$                  ║
╠══════════════════════════════════════════════════════════════════╣
║  PHP                          JAVASCRIPT                        ║
║  preg_match('/p/', $s)        /p/.test(s)                       ║
║  preg_match_all('/p/', $s, $m) s.match(/p/g)                    ║
║  preg_replace('/p/', $r, $s)  s.replace(/p/g, r)                ║
║  preg_split('/p/', $s)        s.split(/p/)                      ║
╠══════════════════════════════════════════════════════════════════╣
║  EXEMPLOS PRONTOS                                               ║
║  Só dígitos:         ^\d+$                                      ║
║  N dígitos:          ^\d{N}$                                    ║
║  Código postal PT:   ^\d{4}(-\d{3})?$                           ║
║  Telefone PT:        ^\d{9}$                                    ║
║  Data YYYY-MM-DD:    ^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$║
║  Email simples:      ^[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,}$         ║
║  Tag HTML:           <[a-zA-Z][^>]*>                            ║
║  URL:                (https?|ftp)://[\w.-]+(/[\w./?=%&-]*)?     ║
╚══════════════════════════════════════════════════════════════════╝
```

---

### Armadilhas Mais Comuns no Exame

| ❌ Erro | ✅ Correto | Explicação |
|---------|-----------|------------|
| `\d{4}` para validar | `^\d{4}$` | Sem âncoras encontra os 4 dígitos em "12345" |
| `[0-9]{2}` para meses | `(0[1-9]\|1[0-2])` | `[0-9]{2}` aceita "00" e "99" |
| `.+` para qualquer texto | `[^X]+` | `.+` é greedy e pode capturar demasiado |
| `http\|https` | `https?` | `http\|https` → tenta "http" primeiro, perde o "s" |
| `(a\|b)+` vs `[ab]+` | `[ab]+` mais eficiente | Para alternativas de 1 char, usar classe |
| Esquecer `$` | Sempre verificar | `^\d{4}` aceita "4100-123" porque encontra "4100" no início |

---

### Sequência de Construção Rápida

```
1. É "contains" ou "is"?
   → Is/validação? Adicionar ^ e $ no início e fim

2. Decompor: "YYYY-MM-DD" → YYYY + - + MM + - + DD

3. Traduzir cada parte:
   YYYY → \d{4}
   -    → -
   MM com restrições → [01][0-9] ou (0[1-9]|1[0-2])
   DD com restrições → [0-3][0-9] ou (0[1-9]|[12][0-9]|3[01])

4. Partes opcionais? → (parte)?

5. Alternativas? → (A|B) ou [AB] para chars

6. Testar com os exemplos dados (✅ e ❌)
```

---

*Guia criado para LTW · FEUP · 2025/2026 · Testado em PHP (PCRE) e JavaScript*
