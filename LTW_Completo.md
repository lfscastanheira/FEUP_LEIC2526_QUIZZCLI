# Lesson 1: Introduction to the Web

## The Internet
A global system of interconnected computer networks using the standard Internet Protocol Suite to link several billion devices worldwide.

## The Web
A system of interlinked hypertext documents accessed via the Internet using a Browser. Also known as the World Wide Web or WWW.

## The Origins of the WWW
Tim Berners-Lee invented the WWW at CERN (1989).

Three constituents: HTML + URL + HTTP:
* **URL** is a notation for locating resources on servers.
* **HTTP** is a high-level protocol for file transfers.
* **HTML** is an SGML language for hypertext.

## World Wide Web Consortium (W3C)
* Develops HTML, CSS, and most Web technologies.
* Founded in 1994.
* Has 380 companies and organizations as members.
* Is directed by Tim Berners-Lee.
* Located at MIT (US), Inria (France), Keio (Japan).
* [http://www.w3.org/](http://www.w3.org/)

## How does the web work?
What happens when you type `http://www.google.com/` in the address bar of your browser?

### Internet Infrastructure
The Internet is a redundant "network of networks" that connects millions of hardware devices from laptops to servers.

* **Routers:** Computers are usually connected using other devices (such as routers).
* **IP Addresses:** Each connected device has at least one IP (Internet Protocol) address. Given an address, routers can calculate where they should send information to reach the desired device.
* **Internet Service Providers (ISPs):** ISPs are the organizations that connect users to the Internet. Most of the time, the external IP address on each router is assigned by the ISP using DHCP.

### Name Resolution
How do we go from `www.google.com` to `173.194.34.224`?

The **Domain Name System (DNS)** is a hierarchical distributed naming system for computers connected to the Internet.

#### DNS Hierarchy
* If client caches (i.e., computer, router) don't know the IP address, a DNS query must be made to the DNS server assigned by the ISP (via DHCP).
* DNS requests escalate the hierarchy until a DNS server contains a record for the desired name.
* If the root zone DNS does not have the record, the request goes down until it reaches the responsible zone DNS.

## Uniform Resource Locators (URL)
A Uniform Resource Locator (URL) is a character string that constitutes a reference to an Internet resource.

* It always starts with a scheme name followed by a colon and two slashes (`://`).
* In the case of the HTTP scheme, it is followed by a server name (or an IP address) and, optionally:
  * A port number
  * The path of the resource to be fetched
  * A query string
  * A fragment identifier
* Before the server name, it is also possible to add a username and a password.
* Other common schemes: `https`, `file`, `ftp`, `smtp`, ...

### URL Examples
* `http://www.google.com/`
* `http://username:password@www.example.com/path/image.jpg`
* `http://www.example.com:80/path?query_string#fragment_id`

**Components breakdown:**
* The port is `80` by default.
* The query string allows one to pass parameters to the resource.
* The fragment id indicates a specific point on the resource.

## Hypertext Transfer Protocol (HTTP)
The Hypertext Transfer Protocol (HTTP) is a protocol that mediates the flow of information between a client computer (generally in the form of a browser) and a web server.

1. When a particular URL is introduced into the browser location bar, the browser creates an HTTP connection to the desired server and requests the resource represented by the URL.
2. It is the server's responsibility to return that resource to the browser via the same connection (or produce an error).
3. The browser then presents the resource to the user.

### Resources
Resources can be of various types. The most common are HTML pages, but they can also be images, style sheets, PDF files, etc. The browser is responsible for presenting them in the most convenient way to the user.

### A Typical Scenario
1. A web server receives requests for HTML pages.
2. HTML pages are partially generated from data in a database.
3. The HTML reaches the browser that requests additional content (CSS, JavaScript, images, ...).
4. The page is rendered in the browser.




---

---

template:inverse
# Web Development
## Beyond the Basics
<a href="http://www.fe.up.pt/~arestivo">André Restivo</a>

---

name:index
# Index

1. [MPA vs. SPA](#models)
1. [Web APIs](#apis)
1. [Web Frameworks](#frameworks)

---

# MPA vs. SPA

---

# Multiple Page Application: <small>Classic Web</small>

<img src="assets/webdev/classic.svg" style="float: right" width="50%">

* Each interaction renders a **different page**; a different HTTP request. 
* The HTML can mention other **resources** prompting more HTTP requests (*e.g.*, images, CSS, scripts).
* Actions change the server state and **tell the browser** where to go next.
* **Not easy** to **reuse the backend** for different purposes (*e.g.*, as an API).
* **Easy** to understand but can be **slow**; pages are heavy and contain **repeated code**.

---

# Enter AJAX: <small>The Hybrid Model</small>

<img src="assets/webdev/ajax.svg" style="float: right" width="50%">

* Pages can request **more information** from the server.
* Some interactions **do not reload** the entire page (*e.g.*, login and logout, load more items).
* API calls can return **different types** of data:
  * JSON / XML with **client-side** rendering.
  * HTML with **server-side** rendering.
* Faster, as we do not need to transfer so much data, but might require **duplicated rendering code** (client/server).

---

# The Single Page Application (SPA)

<img src="assets/webdev/spa.svg" style="float: right" width="50%">

* The **first interaction** returns an HTML page, and the application **never leaves** that page during its **entire lifecycle**.
* All the remaining interactions are the result of AJAX calls to **fetch more data** and **client-side rendering**.
* Users **do not need to wait** for interactions to finish before performing the next.
* Slower first load, **fast** afterward; feels like a **desktop application**.
* But...

---

# Do Not Break the Web

Users have some **expectations** regarding how web pages work:

* The **back button** will take them to the previous page.
* **Copying/Bookmarking/Sending** the current URL allows them to **resume** their session later, **save** a specific page location, or **send** someone a link to a particular web page.

Break these, and **users won't be happy**!

---

# Fragment

Using the **URL fragment** to store the **current state**:

<img src="assets/webdev/hashes.svg" width="80%">

---

# Fragment Example

Using the **URL fragment** and **regular expressions** to call functions that **load the current state**:

```javascript
function parse_fragment() {
  const hash = window.location.hash

  if (hash) {
    const category = /#category\/(\d+)/.exec(hash)
    if (category) return load_category(category[1])

    const article = /#article\/(\d+)/.exec(hash)
    if (article) return load_article(article[1])

  } else load_articles()
}

parse_fragement()

```

---

# SPA vs. MPA

Single Page Applications (SPA) have several advantages:

* **Speed**: Most pages load faster.
* **Network**: Less network intensive.
* **Decoupling**: The backend and Frontend are decoupled.
* **UX**: Better user experience.

But Multiple Page Applications (MPA) also have some strong points:

* **SEO**: Easier search engine optimization.
* **First Load**: The speed of the first load is usually better.
* **JavaScript Dependency**: Works without JS.
* **Navigation**: Simpler and standard navigation (*e.g.*, link, back button).

---

# CSR vs. SSR

A second dichotomy is **where to render** the **HTML** code:

* Client-side Rendering (**CSR**): The browser receives data in a different format (*e.g.*, JSON or XML) and renders that data as HTML.
* Server-side Rendering (**SSR**): The server already sends data as HTML.

<img src="assets/webdev/csrssr.svg" width="35%">

We can use the **HTTP Accept header** to allow using a single server-side script to generate both JSON and HTML.

---

# The Shadow DOM

Templates are inert HTML fragments that are **not rendered** until cloned.

The Shadow DOM allows **encapsulation** of HTML/CSS, avoiding style collisions.

```html
<template id="user-template"> <!--This is not rendered -->
  <style> <!--This is only valid for this template -->
    .username { font-weight: bold; }
  </style>
  <div class="user">
    Hello, <span class="username"></span>!
  </div>
</template>

<div id="container"></div>
```

Let's try to instantiate the template inside the container...

---

# The Shadow DOM

To instantiate a new user card, we just clone it, modify it, and then insert it into the DOM.

```javascript
function createUserCard(name, container) {
  const template = document.querySelector("#user-template")

  if (!template || !container) return

  const userCard = document.createElement("div")
  const shadow = userCard.attachShadow({ mode: "open" })
  const clone = template.content.cloneNode(true)

  clone.querySelector(".username").textContent = name
  shadow.appendChild(clone)
  container.appendChild(userCard)
}

createUserCard('John Doe', document.querySelector("#container"))

```

---

# Progressive Web Apps (PWA)

[PWA](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps): Apps that have the [capabilities](https://whatwebcando.today/) of **native** apps with the **reach** of **web** apps:

* **Installable**: Just like native apps.
* **Cached Content**: Using web workers and local storage.
* **Web APIs**: Uses web APIs to do more.
* **Responsive**: Works on several devices.

Progressive comes from **progressive enhancement**, starting with a basic level of user experience and using more advanced functionality that will automatically be available to browsers that can use it.

As opposed to **graceful degradation**: starting with all bells and whistles, and degrading to a lower level of user experience on older browsers.

---

# Web APIs

---

# Web APIs

Modern browsers can take advantage of several [Web APIs](https://developer.mozilla.org/en-US/docs/Web/API).

These allow the creation of **web apps** with capabilities similar to **native apps** (PWAs).

---

# Web Workers

Web Workers make it possible to run a script in a **background thread**:

* **Dedicated Workers**: When used by a single script.
* [**Shared Workers**](https://developer.mozilla.org/en-US/docs/Web/API/SharedWorker): Can be used by multiple scripts, possibly running on different windows, and communicating using an active port.
* [**Service Workers**](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API): Act as a proxy that sits between web applications and the network.

Web workers **can't** directly **manipulate the DOM**.

---

# Service Workers

* Intercepts resource requests acting as a **network proxy**.
* Typically used to cache resources and provide an **offline experience**.
* An **enhancement** to existing websites. **No** baseline **functionality is broken** if the browser does not support them.
* After a service worker is installed and activated, it controls the page to offer **improved reliability** and **speed**.

```javascript
navigator.serviceWorker.register("/serviceworker.js");
```

On the service worker:

```javascript
self.addEventListener("install", event => {
   console.log("Service worker installed");
})
self.addEventListener("activate", event => {
   console.log("Service worker activated");
})
```

---

# Cache 

To manage the cache, **service workers** interact with the Cache Storage API.

The [Cache API](https://developer.mozilla.org/en-US/docs/Web/API/Cache) is a storage mechanism for Request / Response pairs cached in long-lived memory.

```javascript
const urls = ["/", "style.css", "script.js"]
// self is a service worker
self.addEventListener("install", event => { 
  event.waitUntil(
    // assets is the name of the cache
    caches.open("assets").then(cache =>
        cache.addAll(urlsToCache)
    )
  )
})
```

---

# Web Storage

Allows browsers to store **key/value pairs** much more intuitively than with cookies.

* sessionStorage: separate storage for each origin.
* localStorage: the same but persists browser restarts.

```javascript
localStorage.setItem('color', 'blue')
const color = localStorage.getItem('color') // blue
```

---

# IndexedDB

A low-level API for **client-side** storage of **significant amounts** of structured data:

* **Object store** paradigm: data as objects.
* **Primary Keys** and **Indexes**.
* **CRUD** operations: create, read, update, and delete.
* **Versioning**: dealing with different database versions.

---

# Other APIs

* [Contact Picker](https://developer.mozilla.org/en-US/docs/Web/API/Contact_Picker_API): access to contact lists.
* [Image Capture](https://developer.mozilla.org/en-US/docs/Web/API/MediaStream_Image_Capture_API): taking pictures.
* [Canvas](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API): drawing pictures in canvas elements.
* [Clipboard](https://developer.mozilla.org/en-US/docs/Web/API/Clipboard_API): read and write from the system clipboard.
* [Geolocation](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API): get the current location.
* [Websockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API): open two-way communication channels with a server.
* [History](https://developer.mozilla.org/en-US/docs/Web/API/History_API): change the browser history.
* [Many More](https://developer.mozilla.org/en-US/docs/Web/API).

---

# Frameworks

---

# Frameworks

Until now, we have been dealing with **low-level(-ish)** web development. 

But most **modern web development** is done with the support of several **frameworks**.

---

# Full-stack Frameworks

A framework that supports development of front-end user interfaces, back-end logic, and database communication:

* [Laravel](https://laravel.com/) (PHP).
* [Django](https://www.djangoproject.com/) (Python).
* [CakePHP](https://cakephp.org/) (PHP).
* [Meteor](https://www.meteor.com/) (JavaScript / NodeJS).

Typically, they include several services:

* **Authentication** and permission management. 
* **Routing**: Mapping URLs to resources.
* **Object Relational Mapping** (ORM): Almost no need to write SQL.
* **Templating**: Easy HTML rendering.

They can also be used to create just the backend.

---

# Client-side Frameworks

Several reactive client-side frameworks that can be easily coupled with an API:

* [React](https://reactjs.org/).
* [Vue](https://vuejs.org/).
* [Angular](https://angular.io/).
* [Svelte](https://svelte.dev/).

Svelte example:

```html
<script>
	let count = 0

	function handleClick() {
		count += 1
	}
</script>

<button on:click={handleClick}>
	Clicked {count} {count === 1 ? 'time' : 'times'}
</button>
```

---

# CSS Frameworks

CSS is complicated; CSS frameworks can be a **good start** for a great design:

* [Bootstrap](https://getbootstrap.com/).
* [Foundation](https://get.foundation/).

More **semantically** (*[class-less](https://dohliam.github.io/dropin-minimal-css/)*) friendly ones:

* [Pico CSS](https://picocss.com/).
* [Milligram](https://milligram.io/).





---

---

template:inverse
# HTTP
<a href="http://www.fe.up.pt/~arestivo">André Restivo</a>

---

name:index
# Index

1. [Introduction](#intro)
1. [Resources](#resources)
1. [URIs and URLs](#urls)
1. [HTTP URL](#httpurl)
1. [HTTP Request](#request)
1. [HTTP Response](#response)
1. [Headers](#headers)
1. [SOP and CORS](#cors)
1. [REST](#rest)
1. [PHP and HTTP](#php)

---

name:intro
# Introduction

---

# HTTP

* **H**yper **T**ext **T**ransfer **P**rotocol.
* [**Application-layer**](https://en.wikipedia.org/wiki/Application_layer) protocol for transmitting hypermedia documents.
* **Client-server** model.
* **Stateless** protocol.

---

# How does it work?

1. The browser wants a **resource**.
   <small>Either the user typed an URL, an HTML needs other resources, a link was followed, a form was submitted...</small>
2. The browser establishes a TCP (most of the time) **connection** to the server.
3. The browser sends a **request**:

![](assets/http/request.svg)

<ol start="4">
<li> The server returns a <strong>response</strong>:</li>
</ol>

![](assets/http/response.svg)

---

# History

* **HTTP/0.9** (1991) Only **GET** method. No headers.
* **HTTP/1.0** (1992&ndash;96) Files of different types. **HEAD** and **POST**.
* **HTTP/1.1** (1995&ndash;97) Reuse connections. **Host** header.

Since then, the **HTTP 1.1** protocol evolved by adding new headers.

* [**HTTP/2.0**](https://developer.mozilla.org/en-US/docs/Glossary/HTTP_2) (2014&ndash;15) A major revision of the **HTTP** network protocol.
* [**HTTP/3**](https://developer.mozilla.org/en-US/docs/Glossary/HTTP_3) (2019&ndash;) A HTTP mapping over [QUIC](https://developer.mozilla.org/en-US/docs/Glossary/QUIC) (a general-purpose transport layer network protocol designed by Jim Roskind at Google).

---

# Resources

- References:
  - [RFC9110](https://www.rfc-editor.org/rfc/rfc9110.html): The official specification.
  - [Mozilla Developer Network (MDN) Reference](https://developer.mozilla.org/en-US/docs/Web/HTTP).

- Tools:
  - [Playing with cURL](https://reqbin.com/curl).

---

# URIs and URLs

---

# URI

**U**niform **R**esource **I**dentifier

* An identifier is an object that can act as a **reference** to something that has an **identity**.
* In the case of a URI, the object is a sequence of characters with a restricted **syntax** [RFC3986](http://tools.ietf.org/html/rfc3986).
* A URI can be further classified as a locator (**URL**), a name (**URN**), or both.
* URI components: scheme, authority, path, query, fragment

![](assets/http/uri.png)

---

# URN

**U**niform **R**esource **N**ames are intended to serve as **persistent**, **location-independent**,
resource **identifiers** [RFC2141](http://tools.ietf.org/html/rfc2141).

![](assets/http/urn.png)
Source: [RFC3986](https://tools.ietf.org/html/rfc3986)

---

# URL

**U**niform **R**esource **L**ocator

URL refers to the **subset** of URI that identifies resources via a representation of
their primary access mechanism (e.g., their network *location*), rather than
identifying the resource by name or by some other attribute(s) of that resource.

A Uniform Resource Name (URN) functions like a person’s **name**, while a Uniform Resource Locator (URL) resembles that person’s unique **address**.

---

# HTTP URL

---

# HTTP URL

Every **HTTP URL** consists of the following, in the given order:

* the **scheme** name (or protocol, *i.e.*, HTTP or HTTPS)
* a colon (:), two slashes (//)
* a **host** (domain name or IP address)
* optionally a colon (:) followed by a **port** number
* the full **path** of the resource
* optionally a **query** string
* optionally a **fragment** identifier

.box_info[scheme://domain:port/path?query_string#fragment_id]

---

# Scheme Name

* For HTTP connections the scheme name can be either **HTTP** or **HTTPS**.
* **H**yper**t**ext **T**ransfer **P**rotocol **S**ecure (HTTPS) is just HTTP on top of the **SSL/TLS** protocol.

.box_info[http://]

---

# Hostname

Either a domain name or an IP address.

.box_info[www.google.com]

.box_info[127.0.0.1]

---

# Port

* The **default port** for a HTTP server on a computer is port **80**.
* Others are also normally used: 8080, 8000.
* The port number can be **omitted** from the URL if it is the default one.

.box_info[:80]

---

# Path

* The full path of the resource.
* A sequence of segments that are separated by slashes.
* **May** resemble or map exactly to a file system path **but not necessarily**.

.box_info[/somewhere/on/this/server.php]

---

# Query String

* The query string contains **data** to be passed to software running on the server.
* It may contain **name/value pairs** separated by ampersands.

.box_info[?first_name=John&last_name=Doe]

---

# Fragment Identifier

* The fragment identifier, if present, specifies a **part** or a **position** within the overall resource or document.
* If used with HTML, represents an element in the page identified by its **id**.

.box_info[\#content]

---

# HTTP Request

---

# Request

The first line contains a request **method** followed by its parameters:
  * the **path** of the document (an absolute URL without the protocol and the domain name).
  * the HTTP protocol **version** used.

```http
GET /~arestivo/index.php HTTP/1.1
```

The subsequent lines each represent a specific HTTP **header**.

The final block is the optional **data block**. It's separated from the headers by a **blank line** and contains further data. <small>Mainly used by the PUT, POST and PATCH methods.</small>

---

# Examples

A **GET** request:

```http
GET /search.php?name=john HTTP/1.1
Host: www.example.com
Accept-Language: pt
```

A **POST** request:

```http
POST /path/save.php HTTP/1.1
Host: www.example.com
Content-Type: application/x-www-form-urlencoded

name=John%20Doe&username=johndoe
```

HTTP 1.1 **requires** the Host header.

---

# Methods

* The request method indicates the **action** to be performed by the server.
* They all have a **semantic** meaning but it is up to the developer to enforce that meaning.
* The HTTP/1.1 standard defines **nine** methods:
  * **GET**, **HEAD**.
  * **POST**, **PUT**, **DELETE**, **PATCH**.
  * **OPTIONS**, **TRACE**, **CONNECT**.
* Other standards can add extra methods.
* HTML links always use the **GET** method, while HTML forms can use the **GET** or **POST** methods.

---

# Safe Methods

A **safe** method is a method that **doesn't have** any **side effects** on the server:

* [**GET**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/GET): Requests a **representation** of a resource identified by the request URI. <small>The **request** should **not include** any **data**.</small>
* [**HEAD**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/HEAD): Identical to GET but **only** requests the **headers** of the response. <small>The **server** should **not** send any **data**. Used to get data about a resource without actually getting the resource.</small>

All HTTP servers **must implement** these two methods. <small>All other methods are optional.</small>

---

# Idempotent Methods

An **idempotent** method is a method where the **side effects** on the server of **several identical**
requests are the **same** as the **side effects** of a **single request**.

* [**PUT**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PUT) Requests that the representation of a resource be **stored** at the supplied URI. <small>Can be used to **create** or **replace** a representation.</small>
* [**DELETE**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/DELETE) Request that the resource identified by the URI be **deleted**.

* **HEAD** and **GET** are also idempotent.

---

# POST

* The [**POST**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST) method requests that the representation of a resource be **stored** at the supplied URI. <small>Can be used to **create** or **replace** a representation.</small>

* The difference between **POST** and **PUT** is that **POST** is **not idempotent**. <small>Each identical call can have additional effects, *e.g.,* placing the same order multiple times.</small>

---

# POST/PUT Body

* The **type of body** is controlled by the [Content-Type](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type) header (more on headers later.)

* In **HTML forms**, we can change this header using the [enctype](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form#attr-enctype) attribute on the [form](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form) elements, or the [formenctype](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/button#attr-formenctype) of the [button](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/button) element.

Possible values for the **Content-Type** header in HTML forms:

* `application/x-www-form-urlencoded`: [url-encoded](https://developer.mozilla.org/en-US/docs/Glossary/percent-encoding) **key-value tuples** separated by *&amp; and with a *=* between key and value.
* `multipart/form-data`: Each value is sent in a **separate body** part with a [Content-Disposition](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Disposition) header. The way to send binary data.
* `text/plain`: A **single text** value.

---

# POST/PUT Body Examples

```http
POST /register.php HTTP/1.1
Host: foo.example
Content-Type: application/x-www-form-urlencoded
Content-Length: 41

username=johndoe&field2=strongpassword123
```

```http
POST /upload.php HTTP/1.1
Host: foo.example
Content-Type: multipart/form-data;boundary="boundary"

--boundary
Content-Disposition: form-data; name="description"

An image of a dog.
--boundary
Content-Disposition: form-data; name="image"; filename="dog.png"

(binary bytes of the image)
--boundary--
```

---

# OPTIONS

* The [**OPTIONS**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/OPTIONS) method requests communication options for a given URL or the entire server. 

* Used in **preflight requests** in [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) (more on this later).

Example **OPTIONS** response:

```http
HTTP/1.1 204 No Content
Allow: OPTIONS, GET, HEAD, POST
Cache-Control: max-age=604800
Date: Thu, 13 Oct 2016 11:45:00 GMT
Server: EOS (lax004/2813)
```

---

# Other Methods

Other not so common/important methods:

* [**TRACE**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/TRACE): Performs a loop-back test.
* [**CONNECT**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/CONNECT): Can be used to open a tunnel.
* [**PATCH**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PATCH): Applies partial modifications to a resource.

[All methods](https://www.rfc-editor.org/rfc/rfc9110.html#name-methods) as defined in *RFC 9110*.

---

# HTTP Response

---

# Status Line

The **status line** is the **first line** in the **response** message. It consists of **three** items:

* The HTTP **version number**.
* A **status code** &mdash; a three-digit code indicating if the request has been successful.
* A **reason phrase** (a non-authoritative, human-readable text that summarizes the meaning of the status code).

```http
HTTP/1.0 200 OK
```

Responses can be grouped into five categories: **informational** (1xx), **success** (2xx), **redirection** (3xx), **client error** (4xx) and **server error** (5xx). <br><small>[Status codes in the RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html#name-status-codes).</small>

---

# Response Example

```http
HTTP/1.0 200 OK
Date: Fri, 31 Dec 1999 23:59:59 GMT
Content-Type: text/html
Content-Length: 1354

<html>
<body>
<h1>Hello World!</h1>
(more file contents)
  .
  .
  .
</body>
</html>
```

---

# Some Status Codes

**2xx Success**:

* **200 OK** - The request has succeeded. The information returned with the response is dependent on the method used in the request.
  * **GET** an entity corresponding to the requested resource is sent in the response.
  * **HEAD** the entity-header fields corresponding to the requested resource are sent in the response without any message-body.
  * **POST** an entity describing or containing the result of the action.
* **201 Created** - The request has been fulfilled and resulted in a new resource being created.

---

# Some Status Codes

**2xx Success**:

* **202 Accepted** - The request has been accepted for processing, but the processing has not been completed.
* **204 No Content** - The server has fulfilled the request but does not need to return an entity-body.
* **206 Partial Content** - The server has fulfilled the partial GET request for the resource. The request MUST have included a *Range* **header**.

---

# Some Status Codes

**3xx Redirect**:

* **301 Moved Permanently** - The requested resource has been assigned a new permanent URI and any future references to this resource should use one of the returned URIs. The new permanent URI should be given by the *Location* **header** in the response.
* **304 Not Modified** - If the client has performed a conditional GET request and access is allowed, but the document has not been modified.

---

# Some Status Codes

**4xx Client Error**:

* **400 Bad Request** - The request could not be understood by the server due to malformed syntax.
* **401 Unauthorized** - The request requires user authentication. The response **must** include a *WWW-Authenticate* **header** containing a challenge applicable to the requested resource.
* **403 Forbidden** - The server understood the request, but is refusing to fulfill it. Authentication will not help and the request should not be repeated.

---

# Some Status Codes

**4xx Client Error**:

* **404 Not Found** - The server has not found anything matching the requested URL.
* **405 Method Not Allowed** - The method specified in the request is not allowed for the resource identified by the URI. The response must include an *Allow* **header** containing a list of valid methods.
* **408 Request Timeout** - The client did not produce a request within the time that the server was prepared to wait.

---

# Some Status Codes

**418 I'm a teapot** - "Any attempt to brew coffee with a teapot should result in the error
   code "418 I'm a teapot". The resulting entity body MAY be short and stout." -- [RFC2324](https://tools.ietf.org/html/rfc2324)

<img src="assets/http/teapot.png" style="width:30%; border: none">

> This error is a reference to Hyper Text Coffee Pot Control Protocol which was an April Fools' joke in 1998.

---

# Some Status Codes

**5xx Server Error**:

* **500 Internal Server Error** - The server encountered an unexpected condition that prevented it from fulfilling the request.
* **502 Bad Gateway** - The server, while acting as a gateway or proxy, received an invalid response from the upstream server it accessed in attempting to fulfill the request.
* **503 Service Unavailable** - The server is currently unable to handle the request due to a temporary overloading or maintenance of the server.

[All status codes](https://www.rfc-editor.org/rfc/rfc9110.html#name-status-codes)

---

# Headers

---

# Client Headers

* **Accept**	Content-Types that are acceptable for the response <br> (text/html, image/jpeg, ...).
* **Accept-Charset**	Character sets that are acceptable <br> (utf-8, iso-8859-1, ...).
* **Accept-Encoding**	List of acceptable encodings <br> (gzip, deflate, ...).
* **Accept-Language**	List of acceptable human languages for response.
* **Connection**	What type of connection the user-agent would prefer <br> (keep-alive, ...).
* **Cookie**	A HTTP cookie previously sent by the server with **Set-Cookie**.
* **Content-Length**	The length of the request body in octets (8-bit bytes).

---

# Client Headers

* **Content-Type**	The MIME type of the body of the request (used with POST and PUT requests).
* **Date**	The date and time that the message was sent. <br> <small>Date: &lt;day-name&gt;, &lt;day&gt; &lt;month&gt; &lt;year&gt; &lt;hour&gt;:&lt;minute&gt;:&lt;second&gt; GMT</small>
* **Host**	The **domain name** of the server (for virtual hosting), and the TCP **port number** on which the server is listening. The port number may be omitted if the port is the standard port for the service requested. **Mandatory since HTTP/1.1**.
* **If-Modified-Since**	Allows a **304 Not Modified** to be returned if the content is unchanged.
* **Range**	Request only part of an entity. Bytes are numbered from 0.
* **User-Agent**	The user agent string of the user agent.

---

# Client Header Examples

<small>
```http
Accept: text/plain
Accept-Charset: utf-8
Accept-Encoding: gzip, deflate
Accept-Language: en-US
Connection: keep-alive
Cookie: username=johndoe; session_id=7f3fe5016a9cda0c4adbd44aeea9d511;
Content-Length: 348
Content-Type: application/x-www-form-urlencoded
Date: Tue, 15 Nov 1994 08:12:31 GMT
Host: www.google.com:80
If-Modified-Since: Sat, 29 Oct 2014 19:43:31 GMT
Range: bytes=500-999
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/21.0
```
</small>

---

# Server Headers

* **Accept-Ranges**	What partial content range types this server supports.
* **Allow**	Valid actions for a specified resource. To be used for a **405 Method not allowed**.
* **Cache-Control**	Tells all caching mechanisms from server to client whether they may cache this object. It is measured in seconds. <br> (max-age=&lt;seconds&gt;, no-cache)
* **Content-Encoding**	The type of encoding used on the data.
* **Content-Language**	The language the content is in. <br> (pt-PT, en-US, ...)
* **Content-Length**	The length of the response body in octets (8-bit bytes)

---

# Server Headers

* **Content-Location**	An alternate location for the returned data.
* **Content-Range**	Where in a full body message this partial message belongs.
* **Content-Type**	The MIME type of this content.
* **Expires**	Gives the date/time after which the response is considered stale.
* **Last-Modified**	The last modified date for the requested object.
* **Location**	Used in redirection, or when a new resource has been created.
* **Set-Cookie**	A HTTP cookie.

> The Multipurpose Internet Mail Extensions (MIME) type is a standardized way to indicate the nature and format of a document.

---

# Example Server Headers

<small>
```http
Accept-Ranges: bytes
Allow: GET, HEAD
Cache-Control: max-age=36001
Content-Encoding: gzip
Content-Language: da
Content-Length: 348
Content-Location: /index.htm
Content-Range: bytes 21010-47021/47022
Content-Type: text/html; charset=utf-8
Expires: Thu, 01 Dec 1994 16:00:00 GMT
Last-Modified: Tue, 15 Nov 1994 12:45:26 GMT
Location: http://www.w3.org/pub/WWW/People.html
Set-Cookie: session_id=7f...; Domain=foo.com; Path=/; Expires=Wed, 13 ... GMT;
```
</small>

Header fields are defined in [RFC9110](https://www.rfc-editor.org/rfc/rfc9110.html#name-fields) in several sections.

---

# SOP and CORS

---

# SOP: Same-origin policy

A **security mechanism** that restricts how a **document**/**script** loaded by **one origin** can interact with a resource from **another origin**.

Two URLs have the **same origin** if the **protocol**, **port** (if specified), and **host** are the same for both.

![](assets/http/sop.svg)

---

# CORS: Cross-Origin Resource Sharing

An **HTTP-header-based mechanism** for web **servers** to indicate origins from which a browser **should allow loading** resources.

* By default, **modern browsers** follow **SOP** for **Ajax** requests. The rules about which requests should be allowed are [complicated and fuzzy](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy#cross-origin_network_access).

* **CORS** can be used to allow **more origins**.

* For extra security, CSRF tokens should be used. More on this [later](https://web.fe.up.pt/~arestivo/slides/?s=security#csrf).

Browsers use CORS by doing an initial **preflight request** using the **OPTIONS** method and these headers:

* [Origin](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Origin): the origin that caused the request (scheme, hostname and path).
* [Access-Control-Request-Method](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Request-Method): which method will be used.
* [Access-Control-Request-Headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Request-Headers): which headers will be sent.

---

# Preflight Request Example

Imagine the following code running on *https://foo.org/somepage.php*. 

```javascript
async function postData(data) {
  return fetch('https://bar.com/savedata.php', {
    method: 'post',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    },
    body: encodeForAjax(data)
  })
}
```

This would be a possible **preflight request** sent to the server at *bar.com*:

```http
OPTIONS /savedata.php HTTP/1.1
Origin: https://foo.org
Access-Control-Request-Method: POST
Access-Control-Request-Headers: Content-Type
```

---

# Preflight Response Example

This would be a **possible response**:

```http
HTTP/1.1 204 No Content
Access-Control-Allow-Origin: https://foo.org
Access-Control-Allow-Method: POST
Access-Control-Allow-Headers: Content-Type
Access-Control-Max-Age: 86400
```

Access-Control-Allow-Origin could be * to allow requests from any origin.

As access was **granted**, the **actual request** would follow.

---

# REST

[REST Cook Book](http://restcookbook.com/)

---

# REST

REST (**Re**presentational **S**tate **T**ransfer) is a resource-based architecture style for designing networked applications.

* **Uniform Interface**: the system is comprised of named resources accessed using a generic interface.
* **Client-Server**: separating the user interface concerns from the data storage concerns.
* **Stateless**: each request from the client to the server must contain all the information necessary to understand the request, and cannot take advantage of any stored context on the server.
* **Cacheable**: to improve network efficiency responses must be capable of being labeled as cacheable or non-cacheable.
* **Layered System** - intermediaries, such as proxy servers, cache servers, gateways, etc, can be inserted between clients and resources to support performance, security, etc.

First described by Roy T. Fielding in his [PhD thesis](http://www.ics.uci.edu/~fielding/pubs/dissertation/top.htm).

---

# Uniform Interface

* Things (**resources**) instead of **actions**. <br> <small>*employee.php* instead of *getemployee.php and saveemployee.php*.</small>
* Individual resources are **identified** in requests using **URIs** as resource identifiers. <br><small>*e.g.,* *employee.php?id=1234* or even just *employee/1234*</small>
* When a client holds a representation of a resource, including any metadata attached, it has **enough information** to **modify** or **delete** the resource on the server.

---

# Uniform Interface

Use the HTTP standard to describe communication.

```
http://www.example.com/employee
```

* **GET** to list all employees.
* **POST** creates a new employee.

```
http://www.example.com/employee/1234
```

* **GET** to get information about employee 1234.
* **PUT** means that you want to create/update employee 1234.
* **DELETE** means that you want to delete employee 1234.

---

# Stateless

* Communication must be **stateless** in nature.
* Each request from the client to the server must contain **all of the necessary information** to understand the request, and cannot take advantage of any stored context on the server.
* Session **state** is therefore kept **entirely on the client**.

---

# Cacheable

* Data within a response to a request should be implicitly or explicitly labeled as **cacheable** or **non-cacheable**.
* If a response is cacheable, then a client cache is **given the right to reuse** that response data for later, equivalent requests.

---

# Content Negotiation

Use the **Accept** header to ask for a particular representation of the resource.

```http
GET /employee/1234 HTTP/1.1
Host: www.example.com
Accept: application/json
```

```http
GET /employee/1234 HTTP/1.1
Host: www.example.com
Accept: application/xml
```

```http
GET /employee/1234 HTTP/1.1
Host: www.example.com
Accept: text/html
```

---

# Scenarios

.smaller[
![](assets/http/rest.svg)

---

# PHP and HTTP

---

# Sending headers

To **add a header** to the response just use the **header** function:

```php
header('Location: somewhere_else.php');
```

Just be careful to do it before outputting any data.

To send HTTP response codes:

```php
header('HTTP/1.0 404 Nothing to see here');
```

Or:

```php
http_response_code(418);
```

---

# Finding HTTP method

To find which **HTTP method** was used to access the resource use the **$_SERVER** array:

```php
if ($_SERVER['REQUEST_METHOD'] == 'PUT') {
  // update resource
}
```

---

# Finding the Accept header

To find the **Accept** header sent by the client we can also use the **$_SERVER** array:

```php
if ($_SERVER['HTTP_ACCEPT'] == 'application/json') {
  echo json_encode($employees);
}
```

Other headers can also be found in the [$_SERVER](http://php.net/manual/en/reserved.variables.server.php) array or using the [apache_request_headers](http://php.net/manual/en/function.apache-request-headers.php) function.

```php
$headers = apache_request_headers();

foreach ($headers as $header => $value) {
    echo "$header: $value <br />\n";
}
```

---

# CORS in PHP

Allowing from any origin:

```php
<?php
  if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
      header('Access-Control-Allow-Origin: *');
      header('Access-Control-Allow-Methods: GET');
      header('Access-Control-Allow-Headers: Content-Type');
      header('Access-Control-Max-Age: 86400'); // cache for 1 day
      die();
  }

  // normal request...
?>
```

---

# CORS in PHP

Allowing from a specific origin:

```php
<?php
  if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    if ($_SERVER['HTTP_ORIGIN'] === 'http://bar.com') {
      header('Access-Control-Allow-Origin: http://bar.com');
      header('Access-Control-Allow-Methods: GET');
      header('Access-Control-Allow-Headers: Content-Type');
      header('Access-Control-Max-Age: 86400'); // cache for 1 day
    } else {
      header("HTTP/1.1 401 Unauthorized");
    }
    die();
  }

  // normal request...
?>
```





---

---

# HTML
<a href="http://www.fe.up.pt/~arestivo">André Restivo</a>

---

# Index

1. [Introduction](#intro)
1. [Resources](#resources)
1. [Content](#content)
1. [Sections](#sections)
1. [Lists](#lists)
1. [Tables](#tables)
1. [Forms](#forms)
1. [Character Entities](#entities)
1. [Media](#media)
1. [Metadata](#metadata)
1. [Validation](#validation)

---

# Introduction
and some History

---

# What is it?

* **H**yper **T**ext **M**arkup **L**anguage.
* **Markup** language used to create **web pages**.
* Written using HTML **elements**.
* **Not** for design or presentation.
* All about **structure** and **semantics**.

---

# History
* 1989-92: **HTML 1.0**, Tim Berners-Lee original [proposal](https://www.w3.org/History/1989/proposal.html)
* 1993: **HTML+**, Dave Raggett's [competing standard](https://www.w3.org/MarkUp/HTMLPlus/htmlplus_1.html)
* 1994: **HTML 2.0**, tables, file upload, ... (<abbr title="Internet Engineering Task Force">IETF</abbr>)
* 1995: Non-standard Netscape features
* 1996: Competing Netscape and Internet Explorer features
* 1996: **HTML 3.2**, W3C standard, the Browser Wars end
* 1997: **HTML 4.0**, stylesheets are introduced
* 1999: **HTML 4.01**, we have a winner!
* 2000: **XHTML 1.0**, an XML version of HTML 4.01
* 2001: **XHTML 1.1**, modularization
* 2008: **HTML 5**, reduces the need for proprietary plug-in based apps
* 2019: **W3C** and <abbr title="Web Hypertext Application Technology Working Group">WHATWG</abbr> reach an <a href="https://www.w3.org/2019/04/WHATWG-W3C-MOU.html">agreement</a> about future HTML developments.

Learn more: http://en.wikipedia.org/wiki/HTML#History

---

# Browser Wars

**The First War (1995 &ndash; 2001)**:

- **Netscape** and **Internet Explorer** battle for WWW dominance.
- Web standards were still **not well established**.
- New **proprietary features** are introduced into HTML as browsers compete for market share.
- Developers were **forced** to have two versions of their websites.

**Aftermath**:

- Internet Explorer won the war and decided to **stale** any **new developments**.
- From the ashes of Netscape, [Firefox](assets/html5/nytimes-firefox-final.pdf) starts to gain market share.
- Eventually, browsers decided to work together, and we now have a **much better** web landscape!

---

# Browser Share (2007 &ndash; now)

![](assets/html5/browsershare.png)

Source: http://www.w3counter.com/trends

---

# HTML Structure

- An **HTML file** has a **tree-like** structure where each node is an **HTML Element**.
- Elements can contain other elements and/or **text**.
- They are defined using **tags** and can have **attributes**.
- Browsers display each tag using a **predefined** style that can be changed using **CSS**.

**HTML** tells the browser how the document is **structured**.

**CSS** tells the browser how it should be **displayed**!

---

# Tags

- Tags start with a **&lt;** and end with a **&gt;** and always contain a name.
- They are case insensitive, but **lowercase** is **recommended**.

```html
<html>
```

- Most tags come in pairs: an opening tag and a closing tag.
- Closing tags have a **/** after the **&lt;**.

```html
<html> ... </html>
```

---

# Tag Content

The content of a tag is everything between the opening and closing tags:

```html
<p>Some content</p>
```

It can be text, but is can also be other tags:

```html
<article>
  <p>Some content</p>
</article>
```

Some tags never have content and do not need to be closed:

```html
<br>
```

---

# Attributes

Tags can have attributes. Some are optional, and some are mandatory:

```html
<img src="dog.png">
```

Quotes around attribute values are [not mandatory](https://html.spec.whatwg.org/multipage/syntax.html#unquoted) in HTML 5, but they are **recommended**.

 *** 

To set a [boolean attribute](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#boolean-attribute) to true, we can either **omit** its value or use the **name of the attribute** as its value.

```html
<input type="checkbox" checked disabled="disabled">
```

This checkbox is both *checked* and *disabled*.

---

# Some Global Attributes

Some attributes ([global](https://html.spec.whatwg.org/multipage/dom.html#global-attributes)) can be used on all HTML elements. These are some of them:
<small>
- **accesskey**: A guide for browsers to create a keyboard shortcut to the element.
- **autofocus**: Automatically focus the element, allowing the user to start typing right away.
- **hidden**: Indicates that the element is not relevant to the current state of the page (should be set using CSS most of the time). 
- **style**: CSS rules to apply to the element. Only use in some very particular cases.
- **lang**: The primary language for the element's content; typically used in **html** tags if the document has only one language.
- **id**: An element *identification* so that CSS and JavaScript can identify the element.
- **class**: An element *class* so that CSS and JavaScript can identify the class of elements.
</small>

There are many more!

---

# Id and Class

The **id** and **class** attributes are used to easily identify a tag for manipulation (using javascript) or styling (using CSS).

An HTML document **cannot** have two elements with the same **id**:

```html
<img id="logo" src="logo.png>
```

An HTML element can have more than one **class** (separated by whitespace).

```html
<p class="first important">Some text</p>
```

You can think of the **id** as the name of the element and the **class** as its type.

---

# The Most Basic Document 

All HTML documents **must** have these elements:

- A document type declaration (DOCTYPE).
- A [&lt;html&gt;](https://html.spec.whatwg.org/multipage/semantics.html#the-html-element) root with two children: [&lt;head&gt;](https://html.spec.whatwg.org/multipage/semantics.html#the-head-element) and [&lt;body&gt;](https://html.spec.whatwg.org/multipage/semantics.html#the-body-element).
- A non-empty [&lt;title&gt;](https://html.spec.whatwg.org/multipage/semantics.html#the-title-element) element inside the &lt;head&gt;.

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Example</title>
  </head>
  <body>
  </body>
</html>
```

- The &lt;head&gt; contains **metadata** about the document.
- The &lt;body&gt; contains the actual **structure** and **content**.

---

# Semantics

During this presentation, we will talk about a lot about semantics:

<blockquote>Syntax describes the rules by which words can be combined into sentences, while semantics describes what they mean &mdash; The Cambridge Dictionary</blockquote>

But **why** is semantics **important** when describing a language to markup text?

Most HTML tags could be easily **replaced** by another (together with some CSS) and have the **same final result**.<br><small>At least for the end user</small>.

End users are **not the only** readers of HTML; in fact, they don't read HTML at all:
- But bots do when they index websites.
- And developers when they fix other developers' mistakes.
- And specialized browsers for people with disabilities (*cf.* [accessibility](https://www.w3.org/WAI/fundamentals/accessibility-intro/)).

---

# Whitespace

Except inside a few elements (e.g., **&lt;pre&gt;** and **&lt;textarea&gt;**), whitespace is collapsed into a single space.

So this *haiku*:

```html
"The Old Pond" by Matsuo Bashō

An old silent pond
A frog jumps into the pond—
Splash! Silence again.
```

Renders as:

The Old Pond by Matsuo Bashō An old silent pond A frog jumps into the pond— Splash! Silence again.]

---

# Resources

- References:
  - [WHATWG Living Standard](https://html.spec.whatwg.org/multipage/)
  - [Mozilla Developer Network (MDN) Reference](http://developer.mozilla.org/en-US/docs/Web/HTML/Element)

- Books:
  - [Dive into HTML 5](http://diveinto.html5doctor.com/)

- Tutorials:
  - https://webplatform.github.io/docs/html/tutorials/
  - http://www.htmldog.com/guides/html/

---

# Content

---

# Paragraphs and Line Breaks

- A paragraph is represented by the [&lt;p&gt;](https://html.spec.whatwg.org/multipage/grouping-content.html#the-p-element) tag.
- If we want to change lines (but not paragraphs, e.g., in a poem) we can use the [&lt;br&gt;](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-br-element) tag.

```html
<p>"The Old Pond" by Matsuo Bashō</p>

<p>An old silent pond<br>
A frog jumps into the pond—<br>
Splash! Silence again.</p>
```

<p>"The Old Pond" by Matsuo Bashō</p>

<p style="padding-top: 0.5em">An old silent pond<br>
A frog jumps into the pond—<br>
Splash! Silence again.</p>

---

# Text Semantics

Some elements that can be used for [text-level semantics](https://html.spec.whatwg.org/multipage/text-level-semantics.html):

```html
<em>emphasized</em>      <!-- emphasized         -->
<small>small</small>     <!-- smaller            -->
<strong>strong</strong>  <!-- important          -->
<sub>subscripted</sub>   <!-- subscripted        -->
<sup>superscripted</sup> <!-- superscripted      -->
<ins>inserted</ins>      <!-- inserted           -->
<del>deleted</del>       <!-- deleted            -->
<mark>highlighted</mark> <!-- marked/highlighted -->
```

<em>emphasized</em><small>small</small><strong>strong</strong><sub>subscripted</sub>
<sup>superscripted</sup><ins>inserted</ins><del>deleted</del><mark>highlighted</mark>

**Note**: Although [&lt;strong&gt;](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-strong-element) is represented by browsers as **bold**, that's not the semantic meaning of the element. The same can be said of all the other elements in this list.

---

# Preformatted Text

Preformatted text ([&lt;pre&gt;](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-pre-element)) can be useful to mark *ascii art*, or used together with other elements to mark, for example, computer code:

```html
<pre>...</pre>   <!-- preformatted text    -->
<code>...</code> <!-- computer code        -->
<kbd>...</kbd>   <!-- keyboard input       -->
<samp>...</samp> <!-- sample computer code -->
<var>...</var>   <!-- a variable           -->
```

```html
<pre><code>
for (i = 0; i < 10; i++)
  print(i)  
</code></pre>
```

<pre><code style="margin: 0">for (i = 0; i < 10; i++)
  print(i)</code></pre>]

---

# More Semantics

Some [text-level semantics](https://html.spec.whatwg.org/multipage/text-level-semantics.html) elements are not even rendered differently by browsers, but they still have importance as they convey meaning to the text.<br><small>HTML is not only for humans.</small>

```html
<abbr></abbr>              <!-- an abbreviation or acronym      -->
<address></address>        <!-- contact information for someone -->
<time></time>              <!-- a time of the day               -->
<progress></progress>      <!-- a progress of a task            -->
<bdo></bdo>                <!-- the text direction              -->
<blockquote></blockquote>  <!-- quoted from another source      -->
<q></q>                    <!-- an inline (short) quotation     -->
<cite></cite>              <!-- the title of a work             -->
<dfn></dfn>                <!-- a definition                    -->
```

```html
Wikipedia says <abbr title="File Transfer Protocol">FTP</abbr> is 
<q cite="https://en.wikipedia.org/wiki/File_Transfer_Protocol">a 
standard communication protocol used for the transfer of computer 
files from a server to a client on a computer network</q>.
```

Wikipedia says <abbr title="File Transfer Protocol">FTP</abbr> is <q cite="https://en.wikipedia.org/wiki/File_Transfer_Protocol">a standard communication protocol used for the transfer of computer files from a server to a client on a computer network</q>.
]]

---

# Span

The [&lt;span&gt;](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-span-element) is an incredibly **useful** element for marking text, that means absolutely **nothing at all** (at least semantically).

But, together with the [id and class](https://html.spec.whatwg.org/multipage/dom.html#classes) attributes, we can convey this element *whatever meaning* we desire. And, with **CSS** and **JavaScript**, we can do whatever we want with it.

However, the **&lt;span&gt;** element should only be used if no other, more *semantically correct*, element exists.

```html
One of the boldest colors in the spectrum, 
<span class="color">red</span> stands out 
in any work of art, hence its use to signal 
danger or warning.
```

---

# Anchor

The [&lt;a&gt;](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-a-element) tag creates anchor elements that represent hyperlinks to other documents:

- The **href** attribute, if present, represents the URL of the other document.
- URLs can be **relative** (to the current document) or **absolute**.

```html
<a href="anotherpage.html">Another Page</a>
<a href="somewhere/deeper.html">Deeper</a>
<a href="../start.html">Back</a>
<a href="http://www.google.com">Search</a>
```

We can create an anchor to an element with a specific **id** within a page:

```html
<a href="anotherpage.html#introduction">Another page</a>
```

---

# Images

- To represent an image we use the [&lt;img&gt;](https://html.spec.whatwg.org/multipage/embedded-content.html#the-img-element) tag.
- The **src** attribute contains the address of the image.<br><small>A relative or absolute URL.</small>
- The [alt](https://html.spec.whatwg.org/multipage/images.html#alt) attribute is mandatory and represents an alternative image description for browsers incapable of showing images (*cf.* [accessibility](https://www.w3.org/WAI/fundamentals/accessibility-intro/)).

> Setting this attribute to the empty string indicates that this image is not a key part of the content; non-visual browsers may omit it from rendering.

- The **width** and **height** indicate the width and height of the image in pixels. 
- The main idea is for the browser to **allocate** space for the image before downloading it.
- Refrain from overusing this to resize images.

```html
<img src="dog.png" alt="A dog" width="300" height="200">
```

---

# Figure

A [&lt;figure&gt;](https://html.spec.whatwg.org/multipage/grouping-content.html#the-figure-element) represents **self-contained content**, potentially with an **optional caption**, which is specified using the [&lt;figcaption&gt;](https://html.spec.whatwg.org/multipage/grouping-content.html#the-figcaption-element) element. The figure, its caption, and its contents are referenced as a *single unit*:

```html
<figure>
  <img src="dog.jpg"
       alt="A dog playing in the garden">
  <figcaption>Fig 1: A dog playing in the garden</figcaption>
</figure>
```

Note: It can be used with **other content** besides images.

---

# Sections

---

# Headings

* There are six levels of document headings, from [&lt;h1&gt; to &lt;h6&gt;](https://html.spec.whatwg.org/multipage/sections.html#the-h1,-h2,-h3,-h4,-h5,-and-h6-elements).
* A heading element briefly **describes** the topic of the **section** it introduces.

```html
<h1>Title</h1> <!-- only one per document -->
<h2>Subtitle</h2>
<h3>Section</h3>
<h4>Sub-section</h4>
<h5>Each one less important...</h5>
<h6>...than the other</h6>
```

---

# Sectioning Content

- The [&lt;article&gt;](https://html.spec.whatwg.org/multipage/sections.html#the-article-element), [&lt;section&gt;](https://html.spec.whatwg.org/multipage/sections.html#the-section-element), [&lt;nav&gt;](https://html.spec.whatwg.org/multipage/sections.html#the-nav-element), and [&lt;aside&gt;](https://html.spec.whatwg.org/multipage/sections.html#the-aside-element) elements are sectioning elements. 
- Sectioning elements are those that are supposed to have **headings**.
- Each one of these has a different semantic meaning:
  - **article**: Represents a complete, or self-contained, element; one that can be independently distributable or reusable, for example, a blog post, a news article, or a comment.
  - **section**: A thematic grouping of content, generally with a heading.
  - **nav**: A section with navigation links.
  - **aside**: For content that is considered separate from the page's main content.

Sectioning content defines the scope of **headings**, **headers**, and **footers**.

---

# Header and Footer

- Sections usually have some **introductory** and **closing** content in the form of a [&lt;header&gt;](https://html.spec.whatwg.org/multipage/sections.html#the-header-element) and a [&lt;footer&gt;](https://html.spec.whatwg.org/multipage/sections.html#the-footer-element).
- Headers normally contain headings (**&lt;h1&gt;** &ndash; **&lt;h6&gt;**), but they can contain anything else.
- The **first** heading of a section represents the heading for that section.

```html
<section id="posts">
  <h1>Posts</h1>
  <article>
    <header>
      <h2>Title of the Post</h2>
      <h3>And the subtitle</h3>
    </header>
    <p>The post content</p>
    <p>More content</p>
    <footer><p>Author of the post</p></footer>
  </article>
</section>
```

---

# Main

- The [&lt;main&gt;](https://html.spec.whatwg.org/multipage/grouping-content.html#the-main-element) element represents the dominant content of the document.
- A document must not have more than one main element (unless some are hidden).

```html
<html>
  <head>...</head>
  <body>
    <header>
      <h1>Page Title</h1>
    </header>
    <nav><ul>...navigation links...</ul></nav>
    <main>
      <section id="posts">...</section>
      ...
    </main>
  </body>
</html>
```

---

# Div

The [&lt;div&gt;](https://html.spec.whatwg.org/multipage/grouping-content.html#the-div-element) is an incredibly **useful** element for grouping content, that means absolutely **nothing at all** (at least semantically).

But, together with the [id and class](https://html.spec.whatwg.org/multipage/dom.html#classes) attributes, we can convey this element *whatever meaning* we desire. And, with **CSS** and **JavaScript**, we can do whatever we want with it.

However, the **&lt;div&gt;** element should only be used if no other, more *semantically correct*, element exists.

```html
<article class="post">
  <p>...</p>
  <div class="emphasis">
    <p>...</p>
    <p>...</p>
  </div>
  <p>...</p>
</article>
```

---

# Lists

---

# Ordered Lists

Ordered lists ([&lt;ol&gt;](https://html.spec.whatwg.org/multipage/grouping-content.html#the-ol-element)) are lists of items ([&lt;li&gt;](https://html.spec.whatwg.org/multipage/grouping-content.html#the-li-element)) that have been **intentionally** ordered; so that if their order changes, it would change the meaning of the document.

```html
<ol>
  <li>An item</li>
  <li>Another item</li>
  <li>And another one</li>
</ol>
```

<ol>
  <li>An item</li>
  <li>Another item</li>
  <li>And another one</li>
</ol>

---

# Ordered List Attributes

The attributes **type** (1, a, A, i, I), **reversed**, and **start** allow us to change the default way the list is presented. The **value** attribute on a list item allows changing the value of that item.

```html
<ol type="I" start="4" reversed>
  <li>An item</li>
  <li>Another item</li>
  <li value="10">And another one</li>
  <li>And another just for good measure</li>
</ol>
```

<ol type="I" start="4" reversed>
  <li>An item</li>
  <li>Another item</li>
  <li value="10">And another one</li>
  <li>And another just for good measure</li>
</ol>

These can also be set in CSS. You should **only** use them in HTML if they convey any meaning (*e.g.,* they are referred to in the text by their values).

---

# Unordered Lists

Unordered lists ([&lt;ul&gt;](https://html.spec.whatwg.org/multipage/grouping-content.html#the-ul-element)) are lists of items ([&lt;li&gt;](https://html.spec.whatwg.org/multipage/grouping-content.html#the-li-element)) where the order of the items is **not important**.

```html
<ul>
  <li>An item</li>
  <li>Another item</li>
  <li>And another one</li>
</ul>
```

<ul>
  <li>An item</li>
  <li>Another item</li>
  <li>And another one</li>
</ul>

---

# Nested Lists

Lists can be nested inside other lists:

```html
<ul>
  <li>A list:
    <ol>
      <li>Something</li>
      <li>Something else</li>
    </ol>
  </li>
  <li>Another item</li>
  <li>And another one</li>
</ul>
```

<ul>
  <li>A list:
    <ol>
      <li>Something</li>
      <li>Something else</li>
    </ol>
  </li>
  <li>Another item</li>
  <li>And another one</li>
</ul>

---

# Description Lists

* A *description list* ([&lt;dl&gt;](https://html.spec.whatwg.org/multipage/grouping-content.html#the-dl-element)) contains terms ([&lt;dt&gt;](https://html.spec.whatwg.org/multipage/grouping-content.html#the-dt-element)) and descriptions ([&lt;dd&gt;](https://html.spec.whatwg.org/multipage/grouping-content.html#the-dd-element)).

* A term can have several descriptions, and a description can describe several terms.

```html
<dl>
  <dt>A term</dt>
  <dd>And its definition</dd>
  <dt>This one</dt>
  <dd>Has a different definition</dd>
  <dd>And an alternative definition</dd>
</dl>
```

<dl>
  <dt>A term</dt>
  <dd>And its definition</dd>
  <dt>This one</dt>
  <dd>Has a different definition</dd>
  <dd>And an alternative definition</dd>
</dl>

---

# Tables

---

# Table

* Tables ([&lt;table&gt;](https://html.spec.whatwg.org/multipage/tables.html#the-table-element)) represent **tabular data** (e.g., student grades) and should **not be used** for any kind of design layout.
* In its most simple form, tables are composed of rows ([&lt;tr&gt;](https://html.spec.whatwg.org/multipage/tables.html#the-tr-element)) of data cells ([&lt;td&gt;](https://html.spec.whatwg.org/multipage/tables.html#the-td-element)):

```html
<table>
  <tr><td>A</td><td>B</td><td>C</td></tr>
  <tr><td>D</td><td>E</td><td>F</td></tr>
</table>
```

<table>
  <tr><td>A</td><td>B</td><td>C</td></tr>
  <tr><td>D</td><td>E</td><td>F</td></tr>
</table>

<small>Note: This table is styled using CSS, and it's not the default table design.</small>

---

# Caption

A table can have an optional **caption**.

```html
<table>
  <caption>Table 1: A table with letters</caption>
  <tr><td>A</td><td>B</td><td>C</td></tr>
  <tr><td>D</td><td>E</td><td>F</td></tr>
</table>
```

<table>
  <caption>Table 1: A table with letters</caption>
  <tr><td>A</td><td>B</td><td>C</td></tr>
  <tr><td>D</td><td>E</td><td>F</td></tr>
</table>

---

# Headers

Some data cells can be headers ([&lt;th&gt;](https://html.spec.whatwg.org/multipage/tables.html#the-th-element)):

* **Not** for making text bold (*e.g.*, pointing out an important value).
* Headers can have an optional **scope** attribute that specifies which cells it applies to (*row*, *col*, *rowgroup*, and *colgroup*).

```html
<table>
  <tr>
    <th scope="col">A</th><th scope="col">B</th><th scope="col">C</th>
  </tr>
  <tr>
    <td>D</td><td>E</td><td>F</td>
  </tr>
</table>
```

<table>
  <tr><th>A</th><th>B</th><th>C</th></tr>
  <tr><td>D</td><td>E</td><td>F</td></tr>
</table>

---

# Cell Merging

We can merge cells horizontally or vertically.

```html
<table>
  <tr>
    <td>A</td><td colspan="2">B</td>
  </tr>
  <tr>
    <td rowspan="2">C</td><td>D</td><td>E</td>
  </tr>
  <tr>
    <td colspan="2">F</td>
  </tr>
  <tr>
    <td colspan="3">G</td>
  </tr>
</table>
```

<table>
  <tr>
    <td>A</td><td colspan="2">B</td>
  </tr>
  <tr>
    <td rowspan="2">C</td><td>D</td><td>E</td>
  </tr>
  <tr>
    <td colspan="2">F</td>
  </tr>
  <tr>
    <td colspan="3">G</td>
  </tr>
</table>

---

# Sections

We can divide tables into three logical sections: [thead](https://html.spec.whatwg.org/multipage/tables.html#the-thead-element), [tfoot](https://html.spec.whatwg.org/multipage/tables.html#the-tfoot-element), and [tbody](https://html.spec.whatwg.org/multipage/tables.html#the-tbody-element):
- The order is not important.
- It allows, for example, a scrollable body with fixed header and footer.

```html
<table>
  <thead>
    <tr><th>A</th><th>B</th><th>C</th></tr>
  </thead>
  <tfoot>
    <tr><td>100</td><td>200</td><td>300</td></tr>
  </tfoot>
  <tbody>
    <tr>
      <td>a</td><td>b</td><td>c</td>
    </tr>
    <tr>
      <td>d</td><td>e</td><td>f</td>
    </tr>
  </tbody>
</table>
```

---

# Column and Row Groups

So that we don't have to repeat the same information for each cell in a column, we can define column groups using the [&lt;colgroup&gt;](https://html.spec.whatwg.org/multipage/tables.html#the-colgroup-element) and [&lt;col&gt;](https://html.spec.whatwg.org/multipage/tables.html#the-col-element) elements. 

```html
<table>
  <colgroup>
    <col span="2" class="firsttwo">
    <col class="middle">
    <col span="2" class="lasttwo">
  </colgroup>
  <tr>
    <td>A</td><td>B</td><td>C</td><td>E</td><td>F</td>
  </tr>
</table>
```

They are very useful to set the *class* of each column without having to do it in each single **&lt;td&gt;**.

---

template:inverse
name:forms
# Forms

---

# Form

A form ([&lt;form&gt;](https://html.spec.whatwg.org/multipage/forms.html#the-form-element)) has form controls that allow users to provide data to be sent to a server for further processing (*e.g.* saving the data, return search results, or perform a calculation).

Forms have two main attributes:

* **action**: the URL of the service that will process the data.
* **method**: either **get** (values are sent in the URL) or **post** (values are sent inside the HTTP header)<br><small>More on HTTP methods later.</small>

```html
<form action="save.php" method="get">
  <!-- form controls go here -->
</form>
```

---

# Form Controls

Four main types of form controls:

* **input**: Several types of user-editable fields.
* **textarea**: A big editable text field.
* **select**: A dropdown list.
* **button**: A generic button.

---

# Input

An [&lt;input&gt;](https://html.spec.whatwg.org/multipage/input.html#the-input-element) field can vary in many ways, depending on the [type](https://html.spec.whatwg.org/multipage/input.html#attr-input-type) attribute.

```html
Date: <input type="date" name="date" value="2020-10-15">
Password: <input type="password" name="password" value="mysecretpassword">
Number: <input type="number" name="number" value="123">
```

Date: <input type="date" name="date" value="2020-10-15">
Password: <input type="password" name="password" value="mysecretpassword">
Number: <input type="number" name="number" value="123">

The **name** attribute is used to identify the field when processed in the server. 

The **value** attribute contains the initial data in the field. 

**Tip**: As always, dates are specified using [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) (<small>[obligatory xkcd](https://xkcd.com/1179/)</small>).

---

# Common Control Attributes

* **placeholder**: hint for the user shown only before text is entered.
* **autocomplete**: allow auto-completion by the browser (on/off).
* **readonly**: input value cannot be modified (boolean).
* **required**: input must be filled out (boolean).
* **disabled**: input is disabled (boolean).

```html
Address: <input type="text" name="address" 
                placeholder="your main address" 
                required="required" disabled>
```

Address: <input type="text" name="address" placeholder="your main address" required="required" disabled>

---

# Text Inputs

There are several different types of inputs just for normal text entry.

* <a href="https://html.spec.whatwg.org/multipage/input.html#text-(type=text)-state-and-search-state-(type=search)">text</a>: text input with no constraints
* <a href="https://html.spec.whatwg.org/multipage/input.html#password-state-(type=password)">password</a>: characters are not shown
* <a href="https://html.spec.whatwg.org/multipage/input.html#telephone-state-(type=tel)">tel</a>: input value is a telephone number
* <a href="https://html.spec.whatwg.org/multipage/input.html#text-(type=text)-state-and-search-state-(type=search)">search</a>: input value is used to perform a search
* <a href="https://html.spec.whatwg.org/multipage/input.html#url-state-(type=url)">url</a>: input value is an URL
* <a href="https://html.spec.whatwg.org/multipage/input.html#email-state-(type=email)">email</a>: input value is an e-mail address

Some browsers may use slightly different controls for each type.

```html
Search: <input type="search" name="search" placeholder="type">
```

Search: <input type="search" name="search" placeholder="type">

---

# Number Inputs

```html
<input name="n" type="number" value="5" min="0" max="10" step="5">
```

There are two **types** for number inputs:
* <a href="https://html.spec.whatwg.org/multipage/input.html#number-state-(type=number)">number</a>: a precise control for setting a number
* <a href="https://html.spec.whatwg.org/multipage/input.html#range-state-(type=range)">range</a>: imprecise control for setting a number

Other attributes:
* **value**: the initial value
* **min**: the minimum value
* **max**: the maximum value
* **step**:  limits the increments at which a value can be set

Number: <input name="n" type="number" value="5" min="0" max="10" step="5">

---

# Date/Time Inputs

There are many **types** for date-like inputs. They also have a **min**, **max**, **step** and **value** attributes.

* <a href="https://html.spec.whatwg.org/multipage/input.html#date-state-(type=date)">date</a>: select a date
* <a href="https://html.spec.whatwg.org/multipage/input.html#time-state-(type=time)">time</a>: control to select a time of the day
* <a href="https://html.spec.whatwg.org/multipage/input.html#local-date-and-time-state-(type=datetime-local)">datetime-local</a>: select a time in a certain day
* <a href="https://html.spec.whatwg.org/multipage/input.html#month-state-(type=month)">month</a>: select a month
* <a href="https://html.spec.whatwg.org/multipage/input.html#week-state-(type=week)">week</a>: control to select a week

```html
Date: <input name="date" type="date" value="2020-10-20" min="2020-10-01">
Time: <input name="time" type="time" value="10:00:30">
Date and Time: <input name="datetime" type="datetime-local" value="2020-10-20T10:00">
Month: <input name="month" type="month" value="2020-10">
Week: <input name="week" type="week" value="2020-W09">
```

Date: <input name="date" type="date" value="2020-10-20" min="2020-10-01">
Time: <input name="time" type="time" value="10:00:30">
Date and Time: <input name="datetime" type="datetime-local" value="2020-10-20T10:00">
Month: <input name="month" type="month" value="2020-10">
Week: <input name="week" type="week" value="2020-W09">

---

# Color Input

We can also select a color using the <a href="https://html.spec.whatwg.org/multipage/input.html#color-state-(type=color)">color</a> type:

```html
Color: <input name="color" type="color" value="#336699">

```

The **value** attribute contains the initial color in hexadecimal format.

Color: <input type="color" value="#336699">

---

# Checkbox

* A <a href="https://html.spec.whatwg.org/multipage/input.html#checkbox-state-(type=checkbox)">checkbox</a> allows selecting **several** from a limited number of choices.
* If a checkbox is **selected**, its name/value pair is submitted to the server. If a checkbox is **not selected**, nothing is submitted.
* If two checkboxes have the **same name** and **both are selected**, both names/values are sent. In this case "vehicle=Bike&vehicle=Car".
* The boolean attribute **checked** sets the initial checked state of the checkbox.

```html
<input type="checkbox" name="vehicle" value="Bike">Ride a bike
<input type="checkbox" name="vehicle" value="Car" checked>Drive a car
```

How do you get to school?<br>
<input type="checkbox" name="vehicle" value="Bike">Ride a bike
<input type="checkbox" name="vehicle" value="Car" checked>Drive a car

---

# Radio Button

* A <a href="https://html.spec.whatwg.org/multipage/input.html#radio-button-state-(type=radio)">radio</a> allows selecting **one** from several choices.
* If a radio button is **selected**, then its name/value pair is submitted to the server.
* If a radio button is **not selected**, nothing is submitted.
* If two radio buttons have the **same name**, then only one can be selected; they form a selection group.

```html
How do you get to school?<br>
<input type="radio" name="gender" value="male" checked="checked">Male
<input type="radio" name="gender" value="female">Female
```

<input type="radio" name="gender" value="male" checked="checked">Male
<input type="radio" name="gender" value="female">Female

---

# File Upload

The <a href="https://html.spec.whatwg.org/multipage/input.html#file-upload-state-(type=file)">file</a> type allows file uploading for storing or processing:

```html
Upload: 
<form action="upload_file.php" method="post" enctype="multipart/form-data">
  <input type="file" name="file" accept="image/png,image/jpeg" multiple>
</form>
```

**Important**: To use file uploading in a form, *method* must be **post** and *enctype* must be **multipart/form-data**.

The **accept** attribute can be used to **hint** the browser about what *mime-types* can be selected.
<br><small>This is not enforced.</small>

The **multiple** attribute allows the selection of **more than one** file.

Upload: <form action="upload_file.php" method="post" enctype="multipart/form-data">
  <input type="file" name="file" accept="image/png,image/jpeg" multiple>
</form>

---

# Hidden Input

Inputs with type <a href"https://html.spec.whatwg.org/multipage/input.html#hidden-state-(type=hidden)">hidden</a> are not shown and are not meant to be changed by the user.

```html
<input type="hidden" name="username" value="mightymouse">
```

.box_info[
We will find what's their purpose later...

---

# Submit

The <a href="https://html.spec.whatwg.org/multipage/input.html#submit-button-state-(type=submit)">submit</a> input type, allows the user to submit the form for processing.

The **value** contains the text to be used for the submit button. A multilingual default will be used if left blank.

```html
<form action="save.php" method="get">
  <!-- Other form controls go here-->
  <input type="submit" value="Send">
</form>
```

The form will be submitted using the *method* and *action* defined in the **form** tag.

<form action="save.php" method="get">
  <input type="submit" value="Send">
</form>

The button element (next slide) is a more modern way to achieve this behavior.

---

# Button

A different control is the [button](https://html.spec.whatwg.org/multipage/form-elements.html#the-button-element) that can be used as:
- a generic button that has to be controlled with JavaScript (**type** button).
- an alternative way to submit a form (**type** submit, the default) using a different action (**formaction**) and method (**formmethod**).

```html
<form>
  <button formaction="login.php" formmethod="post" type="submit">
    Login
  </button>
  <button formaction="register.php" formmethod="post" type="submit">
    Register
  </button>
</form>
```

This way, you can have different buttons with **different** actions and methods.

<button formaction="login.php" formmethod="post">Login</button>
<button formaction="register.php" formmethod="post">Register</button>

---

# Select

The form control [select](https://html.spec.whatwg.org/multipage/form-elements.html#the-select-element) allows the selection of one element (or several, with the **multiple** attribute) from a list of options.

```html
<select name="fruit">
  <option value="orange">Orange</option>
  <option value="banana" selected>Banana</option>
  <option value="tomato">Tomato</option>
  <option value="apple">Apple</option>
</select>
```

For the [option](https://html.spec.whatwg.org/multipage/form-elements.html#the-option-element) element, the **value** is what is sent to the server, the **content** is the value presented to the user, and the **select** attribute allows to set the initially selected option.

<select name="fruit">
  <option value="orange">Orange</option>
  <option value="banana" selected>Banana</option>
  <option value="tomato">Tomato</option>
  <option value="apple">Apple</option>
</select>

---

# Option Groups

Options in select controls can be grouped using the [optgroup](https://html.spec.whatwg.org/multipage/form-elements.html#the-optgroup-element) element; this makes selecting them in large lists more manageable.

```html
<select name="food">
  <optgroup label="Fruits">
    <option value="orange">Orange</option>
    <option value="banana" selected>Banana</option>
  </optgroup>
  <optgroup label="Vegetables">
    <option value="lettuce">Lettuce</option>
    <option value="carrot">Carrot</option>
  </optgroup>
</select>
```

<select name="food">
  <optgroup label="Fruits">
    <option value="orange">Orange</option>
    <option value="banana" selected>Banana</option>
  </optgroup>
  <optgroup label="Vegetables">
    <option value="lettuce">Lettuce</option>
    <option value="carrot">Carrot</option>
  </optgroup>
</select>

---

# DataList

The form control [datalist](https://html.spec.whatwg.org/multipage/form-elements.html#the-datalist-element) is very similar to the **select** element. 

The main difference is that it is connected to an **input** element (using the **list** and **id** attributes) and allows the user to write a value that does not exist in the list.

```html
<input name="fruit" list="fruits" value="Banana">
<datalist id="fruits">
  <option>Orange</option>
  <option selected>Banana</option>
  <option>Tomato</option>
  <option>Apple</option>
</datalist>
```

<input name="fruit" list="fruits" value="Banana">
<datalist id="fruits">
  <option>Orange</option>
  <option selected>Banana</option>
  <option>Tomato</option>
  <option>Apple</option>
</datalist>

---

# Text Area

The [&lt;textarea&gt;](https://html.spec.whatwg.org/multipage/form-elements.html#the-textarea-element) element allows users to write larger, multiline texts.

```html
<textarea name="description" rows="5" cols="60">
  This is an input field that allows
  the user to input several lines of text.
  This is the initial value for that input.
  Be careful about extra white space.
</textarea>
```

The initial value is a content of the tag and whitespace is significant. So be careful with it!

<textarea name="description" rows="5" cols="60">
  This is an input field that allows
  the user to input several lines of text.
  This is the initial value for that input.
  Be careful about extra white space.
</textarea>

---

# Label

The [&lt;label&gt;](https://html.spec.whatwg.org/multipage/forms.html#the-label-element) element allows the association between text (the label) and its corresponding input:

* In most browsers, clicking the **label** focuses the **input**.
* This is of great importance in terms of [accessibility](https://www.w3.org/WAI/fundamentals/accessibility-intro/).<br><small>For example, it helps browsers for the visually impaired!</small>

Two ways of creating the association:

```html
<label for="id_name">Name:</label>
<input type="text" name="name" id="id_name">
```

```html
<label>Name:
  <input type="text" name="name">
</label>
```

<label>Name:
  <input type="text" name="name">
</label>

---

# Field Set

The [&lt;fieldset&gt;](https://html.spec.whatwg.org/multipage/form-elements.html#the-fieldset-element) element is useful to group controls in large forms.

The [&lt;legend&gt;](https://html.spec.whatwg.org/multipage/form-elements.html#the-legend-element) element contains the title of the group.

```html
<form>
  <fieldset>
    <legend>Personal data:</legend>
    <label>Name: <input type="text"></label>
    <label>Email: <input type="text"></label>
    <label>Date of birth: <input type="text"></label>
  </fieldset>
</form>
```

<form>
  <fieldset>
    <legend>Personal data:</legend>
    <label>Name: <input type="text"></label>
    <label>Email: <input type="text"></label>
    <label>Date of birth: <input type="text"></label>
  </fieldset>
</form>

---

# Character Entities

---

# Character Entities

A given [character encoding](https://html.spec.whatwg.org/multipage/infrastructure.html#encoding-terminology) may not be able to express all characters of the document character set.

Some characters might have some special meaning (<, >, " and &) and be confused by the browser as markup.

In HTML, character entity references may appear in two forms:

* Numeric character references (either decimal or hexadecimal).
* Named character entity references.

---

# Character Entities

Character entities always start with a **&** and end with a **;**

For example, the ampersand (&amp;):

* Decimal character: &amp;#38;
* Hexadecimal character: &amp;#x26;
* Named character entity: &amp;amp;

Most important character entities:

* Less than sign (&lt;): &amp;lt;
* Greater than sign (&gt;): &amp;gt;
* Ampersand (&amp;): &amp;amp;
* Double quote sign (&quot;): &amp;quot;
* Non-breaking space (&nbsp;): &amp;nbsp;

[Other character entities](https://html.spec.whatwg.org/multipage/named-characters.html#named-character-references) | [Character entity search](http://www.amp-what.com/unicode/search/arrow) 

---

# Media

---

# Canvas

A **canvas** is an empty rectangle that can be used to draw on the fly using *JavaScript*.

```html
<canvas width="400px" height="300px"></canvas>
```

Some cool <a href="https://code.tutsplus.com/articles/21-ridiculously-impressive-html5-canvas-experiments--net-14210">examples</a>.

---

# SVG

**S**calable **V**ector **G**raphics ([&lt;svg&gt;](https://html.spec.whatwg.org/multipage/embedded-content-other.html#svg-0)):

* SVG images can be created and edited with any text editor.
* SVG images can be searched, indexed, scripted, and **compressed**.
* SVG images are **scalable**.
* SVG images can be printed with high quality at **any resolution**.
* SVG images are **zoomable** without degradation.

---

# SVG Example

```html
<svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="200" height="200">
  <polygon
        points="100,10 40,180 190,60 10,60 160,180"
        style="fill:lime;stroke:purple;stroke-width:5;fill-rule:evenodd;"
  >
</svg>
```

<center>
  <svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="200" height="200" style="display:block; margin: 0 auto;">
    <polygon
          points="100,10 40,180 190,60 10,60 160,180"
          style="fill:lime;stroke:purple;stroke-width:5;fill-rule:evenodd;">
  </svg>
</center>

---

# Other Media Tags

HTML 5 also includes specific tags for:

* [&lt;audio&gt;](https://html.spec.whatwg.org/multipage/media.html#the-audio-element): defines sound, such as music or other audio streams
* [&lt;video&gt;](https://html.spec.whatwg.org/multipage/media.html#the-video-element): specifies video, such as a movie clip or other video streams
* [&lt;source&gt;](https://html.spec.whatwg.org/multipage/media.html#the-source-element): specify multiple media resources for media elements (*e.g.*, audio, video, and images).
* [&lt;track&gt;](https://html.spec.whatwg.org/multipage/media.html#the-track-element): text tracks for video and audio elements

Learn more: [Using HTML5 Audio and Video](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/Using_HTML5_audio_and_video)

---

name:metadata
# Metadata

You can define metadata for your document inside the head tag.

---

# Meta Content

The [&lt;meta&gt;](https://html.spec.whatwg.org/multipage/semantics.html#the-meta-element) element is used to express metadata that cannot be expressed using other metadata elements (*e.g.*, title).

```html
<head>
  <meta name="?" content="?">
</head>
```

Possible values for the **name** attribute:

* **application-name**, defining the name of the web application running in the webpage.
* **author**, defining, in a free format, the name of the author of the document.
* **description**, containing a short and accurate summary of the content of the page.
* **generator**, containing, in a free format, the identifier to the software that generated the page.
* **keywords**, containing, as strings separated by commas, relevant words associated with the content of the page.

---

# Character Set

One of the uses of the **&lt;meta&gt;** element is to specify the [character encoding](https://html.spec.whatwg.org/multipage/semantics.html#charset) of an HTML document.

```html
<head>
  <meta charset="utf-8">
</head>
```
Some encodings:

* **utf-8** Character encoding for Unicode (recommended).
* **iso-8859-1** Character encoding for the Latin alphabet.

Knowing about Unicode and charsets is [important](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/) for every software developer.

---

# Validation

---

# Validation

* Browsers try to correct mistakes done by developers (*e.g.*, missing closing tag).
* But we cannot rely on all browsers fixing our mistakes in the same way.
* Sometimes mistakes are not present in the rendered version of the page (*e.g.*, using the wrong semantic element or missing a mandatory semantic attribute).
* These are some reasons why you should always validate your HTML code:<br>http://validator.w3.org/





---

---

template:inverse
# CSS
<a href="http://www.fe.up.pt/~arestivo">André Restivo</a>

---

name:index
# Index

1. [Introduction](#intro)
1. [Linking](#linking)
1. [Resources](#resources)
1. [Selectors](#selectors)
1. [Combining Selectors](#combining-selectors)
1. [Grouping Selectors](#grouping-selectors)
1. [Pseudo Selectors](#pseudo-selectors)
1. [Complex Selectors](#complex-selectors)
1. [Nesting Selectors](#nesting-selectors)
1. [Color](#color)
1. [Fonts](#fonts)
1. [Text](#text)
1. [Length Units](#units)
1. [Box Model](#boxmodel)
1. [Background](#background)
1. [Lists](#lists)
1. [Tables](#tables)
1. [Transform](#transforms)
1. [Transition](#transitions)
1. [The Flow](#flow)
1. [Flexbox](#flexbox)
1. [Grid](#grid)
1. [Cascading](#cascading)
1. [Vars](#vars)
1. [Responsive Design](#responsive)
1. [Vendor Prefixes](#prefix)
1. [Validation](#validation)

---

# Introduction

---

# What are they?

* **C**ascading **S**tyle **S**heets
* A style sheet language used for describing the look and formatting of a document written in a markup language (like HTML).
* Based on two concepts: **selectors** and **properties**.

---

# History

* 1996 **CSS 1** Limited and poorly supported by browsers
* 1998 **CSS 2**
* 1999 **CSS 1** Supported by browsers
* 2003 **CSS 2** Decently supported by browsers
* 2003 **CSS Zen Garden** (http://www.csszengarden.com/)
* 2011 **CSS 2.1**
* 2011-2012 **CSS 3**

---

# Selectors

Allow us to select the HTML elements to which we want to apply some styles.

---

# Properties

Define what aspect of the selected element will be changed or styled.

```css
p {            /* selector */
  color: red;  /* property: value */
}
```

Together, selectors and properties define CSS **rules**.

---

# Linking to HTML

We can apply CSS styles to HTML documents in three different ways.

---

## Inline

Directly in the HTML element:

```html
<p style="color: red">
  This is a red paragraph.
</p>
```

---

# Internal Style Sheet

Using a stylesheet inside the HTML document:

```html
<head>
  <style>
  p {
    color: red;
  }
  </style>
</head>
<body>
  <p>This is a red paragraph.</p>
</body>
```

---
## External Style Sheet

In a separate stylesheet:

```html
<head>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <p>This is a red paragraph.</p>
</body>
```

style.css

```css
p {
  color: red;
}
```

The preferred way. Allows for style **separation** and **reuse**.

---

# Resources

* References:
  * https://developer.mozilla.org/en/docs/Web/CSS/Reference
  * http://www.w3.org/Style/CSS/specs.en.html

* Tutorials:
  * https://css-tricks.com/almanac/
  * http://www.htmldog.com/guides/css/

---

# Selectors

---

# Selectors

* A selector defines a pattern-matching rule that determines which style rules apply to which elements in the document tree.
* There are several types of **simple** selectors:
  - The [Universal](https://drafts.csswg.org/selectors-3/#universal-selector)(*) selector.
  - [Type](https://drafts.csswg.org/selectors-3/#type-selectors) selectors.
  - [Attribute](https://drafts.csswg.org/selectors-3/#attribute-selectors)([ ]) selectors.
  - [Class](https://drafts.csswg.org/selectors-3/#class-html)(.) & [Id](https://drafts.csswg.org/selectors-3/#id-selectors)(#) selectors.
  - [Pseudo-classes](https://drafts.csswg.org/selectors-3/#pseudo-classes)(:) and [Pseudo-elements](https://drafts.csswg.org/selectors-3/#pseudo-elements)(::).
* There are also ways to:
  - [Group](https://drafts.csswg.org/selectors-3/#grouping)(,) selectors to reuse properties.
  - [Combine](https://drafts.csswg.org/selectors-3/#combinators)(space, &gt;, +, ~) selectors into more complicated ones.

---

# Type Selectors

Select elements by their element type:

```css
a
```

<img src="assets/css3/selectors1.svg" width="80%">

---

# Id Selector

Selects element by their id (#):

```css
#posts
```

<img src="assets/css3/selectors2.svg" width="80%">

---
# Class Selector

Selects element by their class (.):

```css
.intro
```

<img src="assets/css3/selectors3.svg" width="80%">

---

# Universal Selector

Selects all elements (*):
```css
 *
```

<img src="assets/css3/selectors4.svg" width="80%">

---

# Attribute Selectors

Select elements based on their attribute existence and values:

* **[attribute]** &ndash; exists.
* **[attribute=value]** &ndash; equals.
* **[attribute~=value]** &ndash; containing value (word).
* **[attribute|=value]** &ndash; starting with value (word).
* **[attribute^=value]** &ndash; starting with value.
* **[attribute$=value]** &ndash; ending with value.
* **[attribute*=value]** &ndash; containing value.

```css
form[method=get] /* selects all forms with attribute method="get" */
```

---

# Compound Selectors

- A sequence of **simple** selectors that are **not separated by spaces** (or any [combinator](#combining-selectors), more on that soon).
- Represents a set of simultaneous conditions that must all be true for an element to be selected.
- If a type selector (e.g., div, p) or a universal selector (*) is present, it must be the first selector in the sequence, and the only such selector.

```css
/* a button with class primary */
button.primary           

/* any element with id main and classes highlight and posts */
*#main.highlight.posts

/* we can omit the universal selector */
#main.highlight.posts

/* an input of type text with class error */
input[type="text"].error 
```

---

# Combining Selectors

---

# Combining Selectors

* Sometimes, we want to select elements based on their relationship with other elements.
* For this, we can use the following [combinators](https://drafts.csswg.org/selectors-3/#combinators):
  - [Descendant](https://drafts.csswg.org/selectors-3/#descendant-combinators) combinator (space).
  - [Child](https://drafts.csswg.org/selectors-3/#child-combinators) combinator (&gt;).
  - [Next-sibling](https://drafts.csswg.org/selectors-3/#adjacent-sibling-combinators) combinator (+).
  - [Subsequent-siblings](https://drafts.csswg.org/selectors-3/#general-sibling-combinators) combinator (~).
* In combinators, the **last selector** is the one that identifies the element we are selecting.

---

# Descendant Combinator

Selects all descendants (space):

```css
aside a
```

<img src="assets/css3/selectors5.svg" width="80%">

---

# Child Selector

Selects all **direct** children (&gt;):
```css
aside > a
```

<img src="assets/css3/selectors6.svg" width="80%">

---

# Next-sibling Selector

Selects the **next** sibling (+):

```css
.intro + p
```

<img src="assets/css3/selectors7.svg" width="80%">

---

# Subsequent-sibling Selector

Selects all **subsequent** siblings (~):

```css
.selected ~ li
```

<img src="assets/css3/selectors8.svg" width="80%">

---

# Grouping Selectors

---

# Grouping Selectors

Selector groups (,) are just a way to simplify CSS rules:

```css
header > *, main article, #articles p
```

<img src="assets/css3/selectors9.svg" width="80%">

---

# Pseudo-selectors

---

## Pseudo-classes and Pseudo-elements

* A [pseudo-class](https://drafts.csswg.org/selectors-3/#pseudo-classes)(:) is a way of selecting **existing elements** based on their **state** as if it were a class (_e.g._, all elements of the class _visited links_).

* A [pseudo-element](https://drafts.csswg.org/selectors-3/#pseudo-elements)(::) allows logical, not actual, elements to be defined (_e.g._, the first letter of a paragraph).

---

## Anchor Pseudo-classes

Pseudo-classes that select anchors (links) based on their state:

```css
a:visited /* selects all links that were visited */
```

* **:link** &ndash; The link was never visited.
* **:visited** &ndash; The link was visited previously.
* **:active** &ndash; The link is active (being clicked).
* **:hover** &ndash; The mouse is over the link (also works on other element types):

```css
img:hover /* selects images when the mouse pointer is over them */
```

---

# Form Pseudo-classes

Selects form controls based on their state:

```css
input:focus     /* the input is focused */

input:valid     /* the data in the input is valid */
input:invalid   /* the data in the input is not valid */

input:required  /* the input is mandatory */
input:optional  /* the input is optional */

input:read-only  /* the input is read-only */
input:read-write /* the input is not read-only */

radio:checked    /* the radio button is checked */
```

The focus pseudo-class can be used in other elements (*cf.* [accessibility](https://www.w3.org/WAI/fundamentals/accessibility-intro/)).

---

# Target Pseudo-class

The **target** pseudo-class selects the **unique** element, if any, with an *id* matching the URL's fragment identifier (the part after #).

If we have this HTML in our *news.html* page:

```html
<section id="sports">...</section>
<section id="politics">...</section>
```

When the URL changes to *news.html#sports*, the page scrolls to the *section* with *id* "sports", and both these selectors then select that section:

```css
:target
```

```css
section:target
```

---

## First and Last Pseudo-classes

Select elements based on their position in the tree:

```css
/* any paragraphs that are the first child of their parents */ 
p:first-child

/* any element that is the last child of their parents */ 
:last-child
```

* **first-child** &ndash; Selects elements that are the first child of their parents.
* **last-child** &ndash; Selects elements that are the last child of their parents.
* **first-of-type** &ndash; Selects elements that are the first child of their parents having their type.
* **last-of-type** &ndash; Selects elements that are the last child of their parents having their type.

---

## Nth Child Pseudo-classes

The **nth-child(an+b)** selector selects elements that are the **bth** child of an element after all its children have been split into groups of **a** elements each.

In other words, this class matches all children whose index fall in the set *{ an + b; n = 0, 1, 2, ... }*.

```css
:nth-child(1)    /* is the same as :first-child */
:nth-child(2)    /* second child */
:nth-child(2n)   /* the even childs */
:nth-child(2n+1) /* the odd childs */
:nth-child(-n+3) /* one of the first three children */
```

The **nth-of-type(an+b)** selector does the same thing but counts only siblings with the same name.

---

## Empty and Only-child Pseudo-classes

Select elements based on the **number of children** of an element:

```css
/* paragraphs that are the only children of their parents */
p:only-child

/* paragraphs that have no children (not even text) */
p:empty
```

---

# Not Pseudo-class

Represents elements that **do not match** a list of selectors:<br><small>Negation pseudo-class selectors cannot be nested.</small>

```css
:not(p) /* all elements that are not a paragraph  */

/* all paragraphs inside sections that are direct      */
/* children of an element that is not an article       */
section :not(article) > p
```

Be careful with some **pitfalls**:

```html
<section><article><p>
  The quick brown fox jumps over the lazy dog
</p></article></section>
```

```css
section :not(article) p /* does not select the paragraph */
:not(article) > p       /* does not select the paragraph */
:not(article) p         /* selects the paragraph, why?   */
```

---

# Has Pseudo-class

Represents elements where any of the relative selectors passed as arguments match:<br><small>Also known as the "parent selector" because it allows you to select elements based on their descendants.</small>

```css
section:has(p)    /* all sections that contain a paragraph */
h1:has(+ h2)      /* a h1 that is followed by a h2 */
:has(p)            /* any element that contains a paragraph */
```

Examples:

```html
<section>    <!-- selected by :has(p) and section:has(p)-->
  <article>  <!-- selected by :has(p) -->
    <p>The quick brown fox jumps over the lazy dog</p>
  </article>
</section>
```

What about "`section :has(p)`"?

---

## Typographic Pseudo-elements

Select **parts** of elements based on their position in the element:

```css
p::first-letter /* the first letter of any paragraph */
```

* **::first-line** &ndash; Selects the first line of the selector.
* **::first-letter** &ndash; Selects the first character of the selector.

A more complicated example:

```css
/* the first letter of any paragraph that     */
/* is the first paragraph child of an article */
article > p:first-of-type::first-letter
```

---

# Before and After Pseudo-elements

Before and after pseudo-elements can be combined with the **content** property to generate content around an element.

The **content** property can have the following values:

 * **none** &ndash; The default value; adds nothing. Cannot be combined with other values: *none*.
 * **a string** &ndash; Using single quotes. Adds the text to the element: *'Chapter'*.
 * **an url** &ndash; An external resource (such as an image): *url('dog.png')*.
 * **counter** &ndash; Variables maintained by CSS whose values may be [manipulated](https://www.w3.org/TR/css-lists-3/#auto-numbering) by CSS rules to track how many times they're used: *counter(section)*.
 * **open-quote** and **close-quote** &ndash; Open and close quotes: *open-quote*.

```css
blockquote::before { content: open-quote;  }
blockquote::after  { content: close-quote; }
```

---

# Complex Selectors

---

# Complex Selectors

All these type of selectors can be combined to form complex selectors:

```css
nav.menu + * > section :first-child p.intro
```

It's easier to read them from the **right to the left**:

> Paragraphs with class "intro" that are descendants of elements that are the first child of their parents and are descendants of "sections" that are direct children of any element that is the next sibling of a "nav" with class "menu."

<img src="assets/css3/selectors10.svg" width="50%">

---

# Common Mistakes

**Spaces are important** when writing and parsing CSS selectors:

```css
/* a paragraph with class "intro" */
p.intro  

/* an element with class "intro" descendant of a paragraph */
p .intro 
```

```css
/* a paragraph that is the first child of its parent */
p:first-child  

/* an element that is the first child of its */
/* parent and a descendant of a paragraph */
p :first-child
```

---

# Common Mistakes

And so is the whole **context**:

```html
<nav>
  <ul>
    <li><a>...</a></li>
    <li><a>...</a></li>
    <li><a>...</a></li>
  </ul>
</nav>
```

```css
/* selects all links of the list */
a:first-child

/* selects all links of the list */
:first-child a

/* selects the first link of the list */
li:first-child a

/* selects the first link of the list */
:first-child > a
```

---

# Nesting Selectors

---

# Nesting Selectors

Nested style rules **inherit** their parent rule's selector context, eliminating the need for repetition and allowing for further building upon the parent's selector context while still associating properties with elements via selectors.

These two are equivalent:

.split[
```css
.foo {
  color: blue;
  .bar {
    color: red;
  }
}
```

```css
.foo { color: blue; }

.foo .bar { color: red; }
```

.box_warning[
This recent development may not be universally supported across all browsers. It's essential to <a href="https://caniuse.com/css-nesting">verify</a> the percentage of users whose browsers can accommodate this feature before implementation.

---

# Relative Selectors

Nested style rules can use relative selectors to specify relationships other than "descendant":

* The parent of the nested selector: &amp;
* The child, next sibling, and next siblings combinators: &gt;, +, ~ 

.split[
```css
form {
  color: blue;
  & input {
    color: red;
  }
}
```

```css
form { color: blue; }

form input { color: red; }
```

.box_warning[
A nested selector cannot start with an element selector (*i.e.*, an identifier), or it would be hard to distinguish between elements and properties. 

---

# Nested Examples

.split[
```css
header {
  color: blue;

  > h1 {
    color: red;
    + h2 {
      color: yellow;
    }
  }

  body > & {
    color: green;
  }
}
```

```css
header { color: blue; }

header > h1 { color: red; }

header > h1 + h2 { color: yellow; }

body > header { color: green; }
```

---

# Color

---
# Text Color

We can set the text color of any element:

```css
p {
  color: green;
}
```

```html
<p>The quick brown fox jumps over the lazy dog</p>
```

Results in:

<p style="color: green">The quick brown fox jumps over the lazy dog</p>

---

# Background Color

We can set the background color of any element:

```css
p {
  background-color: yellow;
}
```

```html
<p>The quick brown fox jumps over the lazy dog</p>
```

Results in:

<p style="background-color: yellow">The quick brown fox jumps over the lazy dog</p>

The default background color of most elements is **transparent**.

---

# Color by Name

Colors can be referenced using one of these pre-defined names:

```css
aqua, black, blue, fuchsia, gray, green,
lime, maroon, navy, olive, orange, purple,
red, silver, teal, white, and yellow.
```

```css
p {
  background-color: fuchsia;
}
```

<span style="line-height: 2em; padding: 0.2em; background-color: black; color: aqua">aqua</span>
<span style="padding: 0.2em; color: black">black</span>
<span style="padding: 0.2em; color: blue">blue</span>
<span style="padding: 0.2em; color: fuchsia">fuchsia</span>
<span style="padding: 0.2em; color: gray">gray</span>
<span style="padding: 0.2em; color: green">green</span>
<span style="padding: 0.2em; color: lime">lime</span>
<span style="padding: 0.2em; color: maroon">maroon</span>
<span style="padding: 0.2em; color: navy">navy</span>
<span style="padding: 0.2em; color: olive">olive</span>
<span style="padding: 0.2em; color: orange">orange</span>
<span style="padding: 0.2em; color: purple">purple</span>
<span style="padding: 0.2em; color: red">red</span>
<span style="padding: 0.2em; background-color: black; color: silver">silver</span>
<span style="padding: 0.2em; color: teal">teal</span>
<span style="padding: 0.2em; background-color: black; color: white">white</span>
<span style="padding: 0.2em; background-color: black; color: yellow">yellow</span>

Modern browsers support an [extended set](https://www.w3.org/wiki/CSS/Properties/color/keywords) of these. 

---

## Color by Hexadecimal Value

A hexadecimal color is specified using #<span style="color:red">RR</span><span style="color:green">GG</span><span style="color:blue">BB</span>, where the <span style="color:red">RR</span> (red), <span style="color:green">GG</span> (green) and <span style="color:blue">BB</span> (blue) hexadecimal integers specify the components of the color. All values must be between 00 and FF.

```css
p {
  background-color: #336699;
}
```

\#<span style="color:red">R</span><span style="color:green">G</span><span style="color:blue">B</span> is a shorthand for #<span style="color:red">RR</span><span style="color:green">GG</span><span style="color:blue">BB</span>

```css
p {
  background-color: #369;
}
```

---

## Color by Decimal Value

An RGB color value can also be specified using: rgb(<span style="color:red">red</span>, <span style="color:green">green</span>, <span style="color:blue">blue</span>). Each parameter (<span style="color:red">red</span>, <span style="color:green">green</span> and <span style="color:blue">blue</span>) defines the intensity of the color and can be an integer between 0 and 255 or a percentage value (from 0% to 100%).

```css
p {
  background-color: rgb(50, 100, 200);
}
```

Or: 

```css
p {
  background-color: rgb(25%, 50%, 75%);
}
```

---

#Opacity

Opacity represents the transparency of an element. Values can go from 0.0 (completely transparent) to 1.0 (fully opaque).

```css
p {
  opacity: 0.5;
}
```

---

name:fonts
# Fonts

---

# Font Family

In CSS, there are two types of font family names:

* **generic family** - a group of font families with a similar look.
* **font family** - a specific font family (*e.g.*, Times New Roman).

---
# Specific Font Family

You can define a specific font family. Be careful as it might not exist in the target computer.

```css
p {
  font-family: "Arial";
}
```

---
# Generic Font Family

Or a generic family like: **sans-serif**, **serif** and **monospace**.

```css
p {
  font-family: serif;
}
```

<figure>

<img src="assets/css3/serif-sansserif.jpg" width="70%">
<figcaption><center>Sans-serif (left) vs. Serif (right)<center></figcaption>

</figure>

---
# Web Safe Fonts

* To ensure that websites look the same across different platforms, we should use *websafe* fonts like *Arial*, *Helvetica*, *Times New Roman*, *Times*, *Courier New* or *Courier*.

* You can specify several fonts. The browser will try to use the **first** and continue **down the list** if it doesn't exist.

* Start with the font you **want** and gradually **fall back** to platform defaults and finally **generic** defaults:

```css
p {
  font-family: 'Open Sans', 'Droid Sans', Arial, sans-serif;
}
```

---
# Remote Fonts

* The *@font-face* rule specifies a custom font to display text.
* The font can be loaded from a remote server, making it possible to use all kinds of fonts.

```css
@font-face {
  font-family: "Open Sans";
  src: url("/fonts/OpenSans-Regular-webfont.woff2") format("woff2"),
       url("/fonts/OpenSans-Regular-webfont.woff") format("woff");
}
```

* An easier way to use remote fonts is to use [Google's Fonts](https://fonts.google.com/).

```css
@import url('https://fonts.googleapis.com/css?family=Lora:400,700');
```

---

# Font Weight

You can specify the weight of the font using the font-weight property. Values can be **normal**, **bold**, **bolder**, **lighter** or values from **100** to **900**.

```css
p.introduction {
  font-weight: bold;
}
```

Not all fonts support all weights.

---
# Font Style

The font-style property allows you to specify if the font style should be *italic* or not. Values can be **normal**, **italic**, or **oblique**.

```css
span.author {
  font-style: italic;
}
```

---
# Font Size

To define the font size, you use the **font-size** property.

```css
p.introduction {
  font-size: 1.2em;
}
```

Using **rem** or **em** units is a good idea for scalable layouts. More on this [soon](#units).

---

template:inverse
name:text
# Text

---

# Decoration

The **text-decoration** property is mostly used to remove underlines from links. But it has other possible values: **none**, <span style="text-decoration: underline">underline</span>, <span style="text-decoration: overline">overline</span> and <span style="text-decoration: line-through">line-through</span>.

```css
#menu a {
  text-decoration: none;
}
```

---
# Alignment

Text can be aligned **left**, **right**, **center** or justified (**justify**) using the **text-align** property. This property should be used for aligning text only.

```css
p {
  text-align: center;
}
```

<section style="display: flex; flex-wrap: wrap; gap: 0.3em;">
<p style="width: 8em; border:1px solid gray; padding: 0.5em; text-align: left;"><strong>left</strong><br>The quick brown fox jumps over the lazy dog</p>
<p style="width: 8em; border:1px solid gray; padding: 0.5em; text-align: right;"><strong>right</strong><br>The quick brown fox jumps over the lazy dog</p>
<p style="width: 8em; border:1px solid gray; padding: 0.5em; text-align: center;"><strong>center</strong><br>The quick brown fox jumps over the lazy dog</p>
<p style="width: 8em; border:1px solid gray; padding: 0.5em; text-align: justify;"><strong>justified</strong><br>The quick brown fox jumps over the lazy dog</p>
<section>

---

# Text Case

The **text-transform** property makes the text **uppercase**, **lowercase** or capitalized (**capitalize** first letter of each word).

```css
h1 {
  text-transform: capitalize;
}
```

<h4 style="padding: 0.2em; border: 1px solid; text-transform: capitalize">The quick brown fox jumps over the lazy dog</h1>

---

# Indentation

The first line of each paragraph can be indented using the **text-indent** property. This property takes a length as its value.

```css
.chapter p {
  text-indent: 10px;
}
```

<p style="width: 12em; padding: 1em; border: 1px solid; text-align: justify; text-indent: 1em">"The quick brown fox jumps over the lazy dog" is an English-language pangram—a sentence that contains all of the letters of the English alphabet.</h1>

---

# Length Units

---

# Units

We can use several [length units](https://developer.mozilla.org/en-US/docs/Web/CSS/length) to change the dimension of elements in CSS.
These units come in different flavors:

- Absolute units
- Font-relative units
- Viewport-percentage units
- [Percentages](https://developer.mozilla.org/en-US/docs/Web/CSS/percentage)

---

# Absolute units

* Absolute length units represent a physical measurement. 
* They are useful when the physical properties of the output medium are known, such as for print layout.

```css
mm, cm, in, pt and pc
```

* **mm** One millimeter.
* **cm** One centimeter (10 millimeters).
* **in** One inch (2.54 centimeters).
* **pt** One point (1/72nd of an inch).
* **pc** One pica (12 points).

---

# Pixel

* Also considered an **absolute length**.
* On low dpi screens, the **pixel (px)** represents one device pixel (**dot**).
* On higher dpi devices, most devices these days, a pixel represents an integer number of device pixels, so that 1in ≈ 96px.

---
# Font-relative units

Font relative length units are relative to the size of a particular character or font attribute in the font **currently in effect** in the element (or parent element in some cases).

They are useful when the physical properties of the output medium are unknown, such as for **screen layout**.

Units *rem* and *em* are used to create **scalable layouts**, which maintain the [vertical rhythm](https://nowodzinski.pl/syncope/) of the page even when the user changes the font size.

* **rem** Represents the size of the root element font. If used to change the *font-size* in the root element, it represents the browser's initial (default or user-defined) value (typically 16px).

* **em** When used to change the *font-size*, it represents the size of the parent element font. When used to set the size of an element, it represents the size of the current element font.

---
# Example (rem and em)

This example shows how changing font size in some elements affects the font size in others:

* Setting the font-size of the root element (**&lt;html&gt;**) to 2rem.<br><small>For other elements, 1rem becomes 32px (if the user didn't change the default).</small>
* Setting the font-size of other element to 2rem.<br><small>The font-size of that element becomes 64px, twice the size of the root's font-size.</small>
* Setting the font-size of the **&lt;body&gt;** element to 2em.<br><small>The font-size of that element becomes 64px, twice its parent's font-size.</small>

```css
html { font-size: 2rem; } /* 32px */
p    { font-size: 2rem; } /* 64px regardless of its location     */
body { font-size: 2em;  } /* 64px the parent is the html element */
```

---

# Viewport-percentage units

Define lengths relative to the viewport size (the visible part of the document):

* **vw** - 1% of the viewport width.
* **vh** - 1% of the viewport heigth.
* **vmin** - the smaller of *vw* and *vh*.
* **vmax** - the larger of *vw* and *vh*.

So, if the viewport is 600x400 pixels, vw = 6px, vh = 4px, vmin = 4px, vmax = 6px.

---

# Percentage unit

* The *percentage* CSS data type represents a percentage value. 
* A percentage consists of a *number* followed by the percentage sign %. 
* There is no space between the symbol and the number.

Many CSS properties (width, margin, padding, font-size, ...) can take *percentage* values to define a size relative to its parent object.

```css
width: 50%;     /* width is 50% of the parent's  width        */
font-size: 80%; /* font-size is 80% of the parent's font-size */
                /* the same as 0.8em                          */
```

---

# Box Model

---

# Box Model

* All page elements are **rectangular**.
* They can have a **border**.
* Some **space** between themselves and that **border** (**padding**) 
* And some **space** between themselves and the **next element** (**margin**).

![](assets/css3/box-model.svg)

---

# Width and Height

We can use the *width* and *height* properties to change the size of the **content area**:

* Values can be a **length**, a **percentage** or **auto** (the browser will automatically calculate a width/height).
* The *default* value is **auto**.

```css
section {
  width: auto;
  height: 50px;
}
```

![](assets/css3/content-box.svg)

---

# Box-sizing

We can change the behavior of the *width* and *height* properties, by changing the** box-sizing** property:

* **border-box** - the width and height properties include the **padding** and **border** (much easier to work with).
* **content-box** - the width and height properties refer to the **content area** only (the default).

```css
section {
  box-sizing: border-box;
  height: 50px;
}
```

![](assets/css3/border-box.svg)

---

# Minimum and Maximum

* When the width/height is calculated depending on something else (e.g., the parent's size or the amount of content), we can set their minimum and maximum values using the **min-width**, **max-width**, **min-height**, and **max-height** properties.

* Values can be a **length**, a **percentage**, or **auto** (the default value).

```css
section {
  /* width is 50% of the parent's width but 40em at maximum */
  width: 50%; max-width: 40em;

  /* height is automatically calculated but 100px at minimum */
  height: auto; min-height: 100px;
}
```

---

# Margin and Padding 

We can use the *padding* and *margin* properties to change those two areas of the *box-model*:

```css
  padding: 20px;
  margin: 1em;
```

But in reality, each one of these properties is a **shorthand** for four other properies:

* padding-**top**, padding-**right**, padding-**bottom** and padding-**left**.
* margin-**top**, margin-**right**, margin-**bottom** and margin-**left**.

```css
  margin-left: 1em;
  margin-right: 2em;
  padding-top: 100px;
```

---

# Margin/Padding Shorthands

The **margin** and **padding** shorthands can take four forms:

- **One** value: changes **all four** sides of the area at once.
- **Two** values: the first is **top/bottom**, and the second is **left/right**.
- **Three** values: the first is **top**, then **left/right**, and then **bottom**.
- **Four** values: corresponding to **top**, **right**, **bottom**, **left**.

Some examples:

```css
body { margin: 0 auto; } /* A common way to center the body */

#menu { padding: 1em; }  /* 1em padding all around */

/* 1.5em top, 1em left/right, 3em bottom/ */
body > nav li { margin: 1.5em 1em 3em; }  
```

---

# Border

The border can be set using the **border** property:

* It takes three values: the *width*, the *style*, and the *color*.
* The width is a [length](#units), but can also be *thin*, *medium* or *thick*.
* Style is one of the following: *none*, *hidden*, *dotted*, *dashed*, *solid*, *double*, *groove*, *ridge*, *inset*, and *outset*.
* And color is a [color](#color).

```css
section#posts {
  border: 1px solid blue;
}
```

And is just a shorthand for three different properties: **border-width**, **border-style**, and **border-color**.

---

# Border Styles

Border **style** examples (**5px, gray**):

<section style="margin: 0.3em; padding: 0.2em; border: 5px dotted gray">dotted</section>
<section style="margin: 0.3em; padding: 0.2em; border: 5px dashed gray">dashed</section>
<section style="margin: 0.3em; padding: 0.2em; border: 5px solid gray">solid</section>
<section style="margin: 0.3em; padding: 0.2em; border: 5px double gray">double</section>
<section style="margin: 0.3em; padding: 0.2em; border: 5px groove gray">groove</section>
<section style="margin: 0.3em; padding: 0.2em; border: 5px ridge gray">ridge</section>
<section style="margin: 0.3em; padding: 0.2em; border: 5px inset gray">inset</section>
<section style="margin: 0.3em; padding: 0.2em; border: 5px outset gray">outset</section>

---

# Border Shorthands

Each of the three border properties (*border-width*, *border-style*, and *border-color*) is also a shorthand to set all **four** borders at once.

This means what we really have are, for example, **border-bottom-width**, **border-top-style**, or **border-left-color**; 12 (3 &times; 4) properties on total.

Just like with *margin* and *padding*, there are also shorthands for setting different values for each property at once:

<section style="margin:0.3em; padding: 0.2em; border: 5px solid gray; border-width: 2px 4px 6px 8px">border-width: 2px 4px 6px 8px;</section>
<section style="margin:0.3em; padding: 0.2em; border: 5px solid gray; border-style: solid dashed">border-style: solid dashed;</section>
<section style="margin:0.3em; padding: 0.2em; border: 5px solid; border-color: red green blue">border-color: red green blue;</section>

---

# Border Radius

* The **border-radius** property is used to define how rounded border corners are.
* The curve of each corner is defined using **one or two** *radii*, defining its shape: **circle** or **ellipse**.
* We can set different border radius for each corner using the properties:
  * **border-top-left-radius**
  * **border-top-right-radius**
  * **border-bottom-right-radius**
  * **border-bottom-left-radius**.
* Values can be a *length* or a *percentage*.
* If two radii are used, they are separated by a **/**.

---

# Shorthands

As with other properties, we can use more than one value in the *border-radius* property to simultaneously change the *radius* of several corners.

The possible combinations are as follows:

* One value: single radius for the whole element.
* Two values: **top-left-and-bottom-right** and **top-right-and-bottom-left**.
* Three values: **top-left**, **top-right-and-bottom-left** and **bottom-right**.
* Four values: **top-left**, **top-right**, **bottom-right**, **bottom-left**.

---

# Examples

```html
<div id="a"></div><div id="b"></div><div id="c"></div>
<div id="d"></div><div id="e"></div><div id="f"></div>
```

```css
div {
  width: 50px; height: 50px;
}
#a { border-radius: 10px; background-color: blue;}
#b { border-radius: 40px 10px; background-color: red;}
#c { border-radius: 40px 10px / 20px 20px; background-color: green;}
#d { border-radius: 10% / 10% 20% 30% 40%; background-color: orange;}
#e { border-radius: 10% 20% / 40px 10px; background-color: gold;}
#f { border-radius: 20px 0; background-color: fuchsia;}
```

<section style="display:flex; justify-content: center">
<div style="width: 50px; height: 50px; margin: 10px; border-radius: 10px; background-color: blue;"></div>
<div style="width: 50px; height: 50px; margin: 10px; border-radius: 40px 10px; background-color: red;"></div>
<div style="width: 50px; height: 50px; margin: 10px; border-radius: 40px 10px / 20px 20px; background-color: green;"></div>
<div style="width: 50px; height: 50px; margin: 10px; border-radius: 10% / 10% 20% 30% 40%; background-color: orange;"></div>
<div style="width: 50px; height: 50px; margin: 10px; border-radius: 10% 20% / 40px 10px; background-color: gold;"></div>
<div style="width: 50px; height: 50px; margin: 10px; border-radius: 20px 0; background-color: fuchsia;"></div>
</section>

---

# Margin Collapse

Adjacent margins collapse in three different cases:

* The margins of **adjacent siblings** are collapsed.
* The margin of **parents** and **descendants** with no separating content.
* The top and bottom margin of **empty** elements.

Margins collapse into a **single margin** with size equal to the **largest** of the individual margins.

---

# Margin Collapse Examples

The three types of margin collapse, visualized:

![](assets/css3/margin-collapse.svg)

---

# Background

---
# Image

* Besides having a background color, elements can also have an image as background using the **background-image** property.
* This property accepts an URL as its value.

```css
nav#menu {
  background-image: url('squares.png');
}
```

---
# Position

The position of the background image can be set using the **background-position** property. This property receives two values:

* The first one can be **left**, **right**,  **center** or a **length**.
* The second one can be **top**, **bottom**, **center** or a **length**.

```css
nav#menu {
  background-image: url('squares.png');
  background-position: left top;
}
```

---
# Attachment

* Using the **background-attachment** property, we can specify if the background should or not scroll with the page or element.
* Possible values are **fixed** (in relation to the viewport), **scroll** (in relation to the element) and **local** (in relation to the content).
* Scroll is the default value.

```css
nav#menu {
  background-image: url('squares.png');
  background-position: left top;
  background-attachment: local;
}
```

https://css-tricks.com/almanac/properties/b/background-attachment/

---

# Repeat

We can also define if the background repeats along one or both axis with the **background-repeat** property. Possible values are **no-repeat**, **repeat-x**, **repeat-y** and **repeat**.

```css
nav#menu {
  background-image: url('squares.png');
  background-position: left top;
  background-attachment: local;
  background-repeat: repeat;
}
```

---

# Clipping

* By default, background properties, like **background-color**, apply to the content, padding, and border.

* This can be changed using the **background-clip** property.

* The possible values are: **border-box** (default), **padding-box** (only content and padding) and **content-box** (only content).

https://css-tricks.com/almanac/properties/b/background-clip/

---

# Shorthands

* The **background** shorthand property sets all the background properties (including color) in one declaration.

* The properties that can be set, are: **background-color**, **background-position**, **background-size**, **background-repeat**, **background-origin**, **background-clip**, **background-attachment**, and **background-image**.

* It does not matter if one or more of the values above are missing.

```css
nav#menu {
  background: url('squares.png') repeat left top;
}
```

---

name:lists
# Lists

---

# Markers

* In lists, each item has left markers that define their position.
* We can change the markers of both types of lists (ordered and unordered) using the **list-style-type** property.
* Some possible values for unordered lists are: **none**, **disc** (default), **circle** and **square**.
* For ordered lists we can use: **none**, **decimal** (default), **lower-alpha**, **lower-greek**, **lower-roman**, **upper-alpha** and **upper-roman**.

```css
  #menu ul { list-style-type:none }
  .article ol { list-style-type:lower-roman }
```

---

# Images as Markers

It is also possible to use an arbitrary image as the list marker:

```css
div#menu ul{
  list-style-image: url('diamong.gif');
}
```

---

name:tables
# Tables

---

# Borders

To draw border around table elements we can use the **border** property that we have seen before:

```css
table, th, td {
	border: 1px solid red;
}
```

<table style="border-collapse: separate">
  <tr><td style="border: 1px solid red; color: #000">A</td><td style="border: 1px solid red; color: #000">B</td></tr>
  <tr><td style="border: 1px solid red; color: #000">C</td><td style="border: 1px solid red; color: #000">D</td></tr>
</table>

---

# Collapse Borders

There is a gap between the borders of adjacent cells:
* To collapse borders into a single border, use the **border-collapse** property.
* The default value is **separate**.

```css
table { border-collapse: collapse; }
td    { border: 1px solid; }
```

separate
<table style="border-collapse: separate"><tr><td style="border: 1px solid; color: #000">A</td><td style="border: 1px solid; color: #000">B</td></tr></table>
<br>
collapse
<table style="border-collapse: collapse"><tr><td style="border: 1px solid; color: #000">A</td><td style="border: 1px solid; color: #000">B</td></tr></table>

---

# Transform

---

# Transform

* The **transform** property modifies the coordinate space of the CSS visual formatting model:
  * A space-separated list of transforms applied one after the other.
* The **transform-origin** property specifies the origin of the transformation:
  * By default, it is at the center of the element. 
  * It takes two values (x-offset and y-offset) that can be a length, a percentage, or one of *left*, *center*, *right*, *top*, and *bottom*.

---

#Examples

```html
<div id="a"></div><div id="b"></div><div id="c"></div>
<div id="d"></div><div id="e"></div><div id="f"></div>
```

```css
div {
  margin: 30px;
  float: left;
  width: 50px; height: 50px;
}
#a {transform: rotate(30deg); background-color: blue;}
#b {transform: skew(30deg); background-color: red;}
#c {transform: translate(10px, 10%); background-color: green;}
#d {transform: scale(0.3); background-color: orange;}
#e {transform: rotate(30deg) scale(0.5); background-color: yellow;}
#f {transform: skew(30deg) rotate(30deg); background-color: fuchsia;}
```

<center>
<section style="display:flex; justify-content: center">
<div id="a" style="transform: rotate(30deg); margin: 30px; width: 50px; height:50px; background-color: blue"></div>
<div id="b" style="transform: skew(30deg); margin: 30px; width: 50px; height:50px; background-color: red"></div>
<div id="c" style="transform: translate(10px, 10%); margin: 30px; width: 50px; height:50px; background-color: green"></div>
<div id="d" style="transform: scale(0.3); margin: 30px; width: 50px; height:50px; background-color: orange"></div>
<div id="e" style="transform: rotate(30deg) scale(0.5); margin: 30px; width: 50px; height:50px; background-color: yellow"></div>
<div id="f" style="transform: skew(30deg) rotate(30deg); margin: 30px; width: 50px; height:50px; background-color: fuchsia"></div>
<section>
</center>

---

# Transition

---

# Transition

* Provide a way to control **animation speed** when changing CSS properties

* Instead of having property changes take effect immediately, you can cause changes in a property over a period of time.

* CSS transitions let you decide:
  * which properties to animate (**list**)
  * when the animation will start (**delay**)
  * how long the transition will last (**duration**)
  * how the transition will run (**timing function**): ease, ease-in, ease-out, ease-in-out, linear, step-start, step-end

```css
transition-property: opacity, left, top, height;
transition-duration: 3s, 5s; /* repeats (3s, 5s, 3s, 5s) */
transition-delay: 1s;        /* same for all properties  */
transition-timing-function: ease-in;
```

---

#Example

There is also a shorthand to set all these properties.

```css
.box {
    margin: 0 auto;
    border: 1px solid;
    width: 100px; height: 100px;
    background-color: #0000FF;
    transition: width 2s, height 2s, background-color 2s, transform 2s, border-radius 4s;
}

.box:hover {
    background-color: #FFCCCC;
    width: 150px; height: 150px;
    transform: rotate(180deg);
    border-radius: 50%;
}
```

<article class="transition">LTW</article>

---

# The Flow

---

# Normal Flow

Normal flow, or flow layout, is how elements are placed on a page before any layout changes.

There are two primary types of elements contributing to this flow: **block** and inline **elements**.

* Block elements start on the **top** and move **down** the page.
* Inline elements start on the **left** (or the right, depending on the *locale*) and move to the **right**.

![](assets/css3/flow.svg)

---

# Display

* The display property controls if an element is **block** or **inline**.

* There are **many** possible values for this property. 

* For example, **tables** (rows and cells) and **lists** (and items) have **specific** display values.

* But we will concentrate on four of them: **block**, **inline**, **inline-block**, and **none**.

```css
img {
  display: block;
}
```

.box_warning[
  We are simplifying some concepts. [Here](https://www.w3.org/TR/css-display-3/) are all the nasty details!

---

# Block

* Always take a **new line**.
* If its width is *auto*, it occupies the **entire horizontal space** of its parent element.
* If its height is *auto*, it will be **as tall as needed** to contain its child elements.
* Respects **margins** and **padding**.
* Can **contain** other *block-level* and *inline-level* elements.

These are some *block* elements: *p*, *h1*&ndash;*h6*, *main*, *section*, *article*, *header*, *footer*, and *div*.

<section style="width: 20em; font-size: 70%; background-color: #eee; margin: 0 auto; text-align: center">
  <article style="margin: 1em; padding: 0.5em; background-color: cyan">margin: 1em</article>
  <article style="margin: 1em; padding: 0.5em; background-color: cyan">margin: 1em</article>
  <article style="margin: 1em; width: 75%; padding: 0.5em; background-color: cyan">margin: 1em<br>width: 75%</article>
  <article style="margin: 0 auto; width: 8em; padding: 0.5em; background-color: cyan">margin: 0 auto<br>width: 8em</article>
</section>

---

# Inline

* Layed out **horizontally** one after the other.
* Ignore any width or height values. They only take as much space as necessary.
* **Top** and **bottom** margin and padding do not affect other elements.
* May be **aligned vertically** on their tops, bottoms, baselines, and others.
* Can break from one line to the next if there is no more space.

These are some *inline* elements: *a*, *strong*, *em*, *span*, and *text*.

<br>

<figure>
<p style="background-color: #eee">
  The quick brown fox <span style="margin: 1em; padding: 1em; background-color: cyan">margin: 1em; padding: 1em</span> jumps over the lazy dog. 
  The quick brown fox jumps over the lazy dog. 
  The quick brown fox jumps over the lazy dog. 
  The quick brown fox jumps over the lazy dog. 
</p>
<center><figcaption>A paragraph with a cyan span inside.</figcaption></center>
<figure>

---

# Inline-Block

* Inline elements that **behave** as block elements.
* Block elements that **stack** horizontally.

<figure>
<p style="background-color: #eee">
  The quick brown fox <span style="display: inline-block; margin: 1em; padding: 1em; background-color: cyan">margin: 1em; padding: 1em</span> jumps over the lazy dog. 
  The quick brown fox jumps over the lazy dog. 
  The quick brown fox jumps over the lazy dog. 
  The quick brown fox jumps over the lazy dog. 
</p>
<center><figcaption>A paragraph with a cyan span inside having **display: inline-block**.</figcaption></center>
<figure>

---

# None

* Setting the **display** property to none, **removes** the element from the page completely.
* This is different from making it invisible (with the *visibility* attribute).
* The element disappears and does not occupy any space on the page.

---

# Changing the Flow

The **position** property allows the developer to alter how an element is positioned. 

There are four possible values:

* static
* relative
* fixed
* absolute

---

# Position Example

The next few pages will use the following example:

```html
<section>
  <article id="a">A</article>
  <article id="b">B</article>
  <article id="c">C</article>
  <article id="d">D</article>
</section>
```

```css
section { background-color: #eee; width: 10em; padding: 0.2em; }
article { width: 5em; margin: 0.2em; padding: 0.2em; }
#a { background-color: #f3722c } #b { background-color: #f9c74f }
#c { background-color: #90be6d } #d { background-color: #4d908e }
```

---

# Static

* The **default** value.
* The element keeps its place **in the document flow**.

<section style="background-color: #eee; width: 10em; padding: 0.2em">
  <article id="a" style="background-color: #f3722c; width: 5em; margin: 0.2em; padding: 0.2em">A</article>
  <article id="b" style="background-color: #f9c74f; width: 5em; margin: 0.2em; padding: 0.2em">B</article>
  <article id="c" style="background-color: #90be6d; width: 5em; margin: 0.2em; padding: 0.2em">C</article>
  <article id="d" style="background-color: #4d908e; width: 5em; margin: 0.2em; padding: 0.2em">D</article>
</section>

```css
article {
  position: static;
}
```

---

# Position Relative

* The element keeps its position **in the flow**.
* But can be moved relative to its static position using **top**, **right**, **bottom**, and **left**.

<section style="background-color: #eee; width: 10em; padding: 0.2em">
  <article id="a" style="background-color: #f3722c; width: 5em; margin: 0.2em; padding: 0.2em">A</article>
  <article id="b" style="position: relative; background-color: #f9c74f; width: 5em; margin: 0.2em; padding: 0.2em">B</article>
  <article id="c" style="position: relative; left: 20px; top: -20px; background-color: #90be6d; width: 5em; margin: 0.2em; padding: 0.2em">C</article>
  <article id="d" style="background-color: #4d908e;  width: 5em; margin: 0.2em; padding: 0.2em">D</article>
</section>

```css
#b {
  position: relative;
}
#c {
  position: relative;
  left: 20px;
  top: -20px;
}
```

---

# Position Fixed

* The element is **no longer a part of the flow**.
* Can be positioned relative to the **browser window**.
* **Scrolling doesn't** change the element's **position**.

<section style="background-color: #eee; width: 10em; padding: 0.2em">
  <article id="a" style="background-color: #f3722c; width: 5em; margin: 0.2em; padding: 0.2em">A</article>
  <article id="b" style="position: fixed; right: 1em; top: 1em; background-color: #f9c74f; width: 5em; margin: 0.2em; padding: 0.2em">B</article>
  <article id="c" style="background-color: #90be6d; width: 5em; margin: 0.2em; padding: 0.2em">C</article>
  <article id="d" style="background-color: #4d908e;  width: 5em; margin: 0.2em; padding: 0.2em">D</article>
</section>

```css
#b {
  position: fixed; 
  right: 1em; 
  top: 1em;
}
```

---

# Position Absolute

* The element is **no longer a part of the flow**.
* But it **still scrolls** with the page.
* Can be positioned relative to its **first positioned parent** (non-static).

<section style="position: relative; background-color: #eee; width: 10em; padding: 0.2em">
  <article id="a" style="background-color: #f3722c; width: 5em; margin: 0.2em; padding: 0.2em">A</article>
  <article id="b" style="position: absolute; right: 0; top: 0; background-color: #f9c74f; width: 5em; margin: 0.2em; padding: 0.2em">B</article>
  <article id="c" style="background-color: #90be6d; width: 5em; margin: 0.2em; padding: 0.2em">C</article>
  <article id="d" style="background-color: #4d908e;  width: 5em; margin: 0.2em; padding: 0.2em">D</article>
</section>

```css
section { position: relative }
#b {
  position: absolute; 
  right: 0; 
  top: 0;
}
```

---

# Float

The [float](https://developer.mozilla.org/en-US/docs/Web/CSS/float) property removes an element from the document flow and shifts it to the **left** or to the **right** until it touches the edge of its containing box or another floated element.

<section style="background-color: #eee; width: 10em; padding: 0.2em">
  <article id="a" style="background-color: #f3722c; width: 5em; margin: 0.2em; padding: 0.2em">A</article>
  <article id="b" style="float: right; background-color: #f9c74f; width: 5em; margin: 0.2em; padding: 0.2em">B</article>
  <article id="c" style="background-color: #90be6d; width: 5em; margin: 0.2em; padding: 0.2em">C</article>
  <article id="d" style="background-color: #4d908e;  width: 5em; margin: 0.2em; padding: 0.2em">D</article>
</section>

```css
#b {
  float: right;
}
```

.box_info[
Articles "b" and "c" are misaligned due to a strange phenomenon. As "b" is no longer part of the flow, its top margin doesn't collapse anymore.

---
# Floats and Text

Text always **flows around** floated elements. This is useful to make text that **flows around** images.

<section style="margin: 0 auto; background-color: #eee; width: 15em; padding: 0.2em">
  <article id="a" style="float:left; background-color: #f3722c; width: 5em; margin: 0.1em; padding: 0.2em">IMG</article>
  <p style="font-size: 50%; margin: 0">The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog.The quick brown fox jumps over the lazy dog.The quick brown fox jumps over the lazy dog</p>
</section>

```html
<section>
  <img id="a">
  <p>...text...</p>
</section>
```

```css
#a {
  float: left;
}
```

---
# Multiple Floats

Floats go right or left until they find **another float** or the **parent container**.

<section style="background-color: #eee; width: 10em; padding: 0.2em">
  <article id="a" style="background-color: #f3722c; width: 5em; margin: 0.2em; padding: 0.2em">A</article>
  <article id="b" style="float: right; background-color: #f9c74f; width: 2em; margin: 0.2em; padding: 0.2em">B</article>
  <article id="c" style="float: right; background-color: #90be6d; width: 2em; margin: 0.2em; padding: 0.2em">C</article>
  <article id="d" style="background-color: #4d908e;  width: 5em; margin: 0.2em; padding: 0.2em">D</article>
</section>

```css
#b, #c {
  width: 2em;
  float: right; 
}
```

---
## Clear

* The [clear](https://developer.mozilla.org/en-US/docs/Web/CSS/clear) property indicates if an element can be next to floating elements that precede it or must be moved down.
* Values can be **left**, **right** or **both**.

<section style="background-color: #eee; width: 10em; padding: 0.2em;">
  <article id="a" style="background-color: #f3722c; width: 5em; margin: 0.2em; padding: 0.2em">A</article>
  <article id="b" style="float: right; background-color: #f9c74f; width: 2em; margin: 0.2em; padding: 0.2em">B</article>
  <article id="c" style="float: right; clear: right; background-color: #90be6d; width: 2em; margin: 0.2em; padding: 0.2em">C</article>
  <article id="d" style="clear: right; background-color: #4d908e;  width: 5em; margin: 0.2em; padding: 0.2em">D</article>
</section>

```css
#b, #c {
  width: 2em;
  float: right; 
}
#c, #d {
  clear: right; 
}
```

---

# Ordering

* When elements are positioned outside the normal flow, they can **overlap** others. 
* The **z-index** property specifies the stack order of an element and its descendants.
* But it can only be applied to **positioned elements** (non-static).
* An element with **greater** stack order is always in **front** of an element with a lower stack order.
* By **default**, the elements are stacked following the order they are declared in the HTML.

```css
#b {
  position: relative;
  z-index: -1;
}
```

---

# Overflow

* The **overflow** property specifies the behavior of an element when its contents don't fit its specified size.

* Possible values are:

 * **visible**:	The overflow is not clipped. It renders outside the element's box. This is the default.
 * **hidden**:	The overflow is clipped, and the rest of the content will be invisible.
 * **scroll**:	The overflow is clipped, but a scroll bar is added to see the rest of the content.
 * **auto**:	If overflow is clipped, a scroll bar should be added to see the rest of the content.

---

# Units Revisited (em)

|Property Type	| Reference Point	| Key Behavior |
|---------------|-----------------|--------------|
| font-size	    | Parent's font-size	| Nested elements get exponentially larger/smaller. |
| width / height	| Element's own font-size	| Box size scales perfectly with the text inside it. |
| padding / margin	| Element's own font-size	| Spacing grows/shrinks as the text size changes. |
| border-width	| Element's own font-size	| Borders that scale with text. Prefer px. |

---

# Units Revisited (%)

|Property Type	| Reference Point	| Key Behavior |
|---------------|-----------------|--------------|
| font-size	 | Parent's font-size	| Identical to em (150%=1.5em). |
| width	| Parent's width	| Relative to the parent's content box. |
| height	| Parent's height	| Only works if the parent has a fixed height defined. |
| padding / margin	| Parent's width	| Vertical margins/padding use parent width, not height! |
| border	| None	| Borders can't be set using percentages. Use px. |
| left / right	| Parent's width	| Only applies if position is absolute, relative, or fixed. |
| top / bottom	| Parent's height	| Only applies if position is absolute, relative, or fixed. |

---

name:flexbox
# Flexbox

---

# Flexbox

* A direction agnostic alternative to the box model layout model.

* Flexbox provides block level arrangement of **parent** and **child** elements that are **flexible** to adapt to display size.

* Flexbox items **cannot** be floated. 
  
* The flex container's margins **do not collapse** with the margins of its contents.

[A Complete Guide to Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)

---

# Flexbox Vocabulary

<img src="assets/css3/flexbox.svg" width="80%">

---

# Running Example

```html
<div class="container">
  <div class="item">1</div>
  <div class="item">2</div>
  <div class="item">3</div>
</div>
```

```css
.container {
  background-color: #94d2bd;
  padding: 0.5em;
}

.item {
  color: white; text-align: center;
  margin: 0.5em; padding: 0.5em;
  background-color: #0a9396;
}
```

<div class="container" style="background-color: #94d2bd; padding: 0.5em;">
  <div class="item" style="text-align: center; margin: 0.5em; padding: 0.5em; background-color: #0a9396; color: white">1</div>
  <div class="item" style="text-align: center; margin: 0.5em; padding: 0.5em; background-color: #0a9396; color: white">2</div>
  <div class="item" style="text-align: center; margin: 0.5em; padding: 0.5em; background-color: #0a9396; color: white">3</div>
</div>

---

# Flex

Changing the [display](https://css-tricks.com/snippets/css/a-guide-to-flexbox/#aa-display) property of the container to *flex* transforms the contained items into flexboxes.

```css
.container {
  display: flex;
}
```
<div class="container" style="display: flex; background-color: #94d2bd; padding: 0.5em;">
  <div class="item" style="text-align: center; margin: 0.5em; padding: 0.5em; background-color: #0a9396; color: white">1</div>
  <div class="item" style="text-align: center; margin: 0.5em; padding: 0.5em; background-color: #0a9396; color: white">2</div>
  <div class="item" style="text-align: center; margin: 0.5em; padding: 0.5em; background-color: #0a9396; color: white">3</div>
</div>

By default, the *main* axis is horizontal from left to right.

---

# Flex Direction

We can change the direction of the *main* axis by changing the [flex-direction](https://css-tricks.com/snippets/css/a-guide-to-flexbox/#aa-flex-direction) property of the container to: **row**, **row-reverse**, **column** or **column-reverse**.

```css
.container {
  flex-direction: column;
}
```

<div class="container" style="flex-direction: column; display: flex; background-color: #94d2bd; padding: 0.5em;">
  <div class="item" style="text-align: center; margin: 0.5em; padding: 0.5em; background-color: #0a9396; color: white">1</div>
  <div class="item" style="text-align: center; margin: 0.5em; padding: 0.5em; background-color: #0a9396; color: white">2</div>
  <div class="item" style="text-align: center; margin: 0.5em; padding: 0.5em; background-color: #0a9396; color: white">3</div>
</div>

---

# Flex Wrap

The [flex-wrap](https://css-tricks.com/snippets/css/a-guide-to-flexbox/#aa-flex-wrap) property allows us to specify how items should
wrap when changing lines: **nowrap**, **wrap**, **wrap-reverse**. The default is **nowrap**.

```css
.container {
  flex-wrap: wrap;
}
.item {
  width: 4em;
}
```

<div class="container" style="flex-wrap: wrap; display: flex; background-color: #94d2bd; padding: 0.5em;">
  <div class="item" style="width: 4em;text-align: center; margin: 0.5em; padding: 0.5em; background-color: #0a9396; color: white">1</div>
  <div class="item" style="width: 4em;text-align: center; margin: 0.5em; padding: 0.5em; background-color: #0a9396; color: white">2</div>
  <div class="item" style="width: 4em;text-align: center; margin: 0.5em; padding: 0.5em; background-color: #0a9396; color: white">3</div>
  <div class="item" style="width: 4em;text-align: center; margin: 0.5em; padding: 0.5em; background-color: #0a9396; color: white">4</div>
  <div class="item" style="width: 4em;text-align: center; margin: 0.5em; padding: 0.5em; background-color: #0a9396; color: white">5</div>
  <div class="item" style="width: 4em;text-align: center; margin: 0.5em; padding: 0.5em; background-color: #0a9396; color: white">6</div>
  <div class="item" style="width: 4em;text-align: center; margin: 0.5em; padding: 0.5em; background-color: #0a9396; color: white">7</div>
  <div class="item" style="width: 4em;text-align: center; margin: 0.5em; padding: 0.5em; background-color: #0a9396; color: white">8</div>
  <div class="item" style="width: 4em;text-align: center; margin: 0.5em; padding: 0.5em; background-color: #0a9396; color: white">9</div>
  <div class="item" style="width: 4em;text-align: center; margin: 0.5em; padding: 0.5em; background-color: #0a9396; color: white">10</div>
  <div class="item" style="width: 4em;text-align: center; margin: 0.5em; padding: 0.5em; background-color: #0a9396; color: white">11</div>
  <div class="item" style="width: 4em;text-align: center; margin: 0.5em; padding: 0.5em; background-color: #0a9396; color: white">12</div>
</div>

---

# Justify Content

The [justify-content](https://css-tricks.com/snippets/css/a-guide-to-flexbox/#aa-justify-content) property defines the alignment along the **main** axis allowing the distribution of extra space: **flex-start**, **flex-end**, **center**, **space-around**, **space-between**, **space-evenly**. The default is **flex-start**.

```css
.container {
  justify-content: flex-start;
}
```

<div style="display: flex; align-items: center; gap: 1em">
<div class="container" style="flex-grow: 1; justify-content: flex-start; display: flex; background-color: #94d2bd; padding: 0.1em; margin-bottom: 0.1em">
  <div class="item" style="text-align: center; margin: 0.1em; padding: 0.1em 1em; background-color: #0a9396; color: white">1</div>
  <div class="item" style="text-align: center; margin: 0.1em; padding: 0.1em 1em; background-color: #0a9396; color: white">2</div>
  <div class="item" style="text-align: center; margin: 0.1em; padding: 0.1em 1em; background-color: #0a9396; color: white">3</div>
</div>
  <span style="flex-basis: 8em; text-align: left; font-size: 75%">flex-start</span>
</div>

<div style="display: flex; align-items: center; gap: 1em">
<div class="container" style="flex-grow: 1; justify-content: flex-end; display: flex; background-color: #94d2bd; padding: 0.1em; margin-bottom: 0.1em">
  <div class="item" style="text-align: center; margin: 0.1em; padding: 0.1em 1em; background-color: #0a9396; color: white">1</div>
  <div class="item" style="text-align: center; margin: 0.1em; padding: 0.1em 1em; background-color: #0a9396; color: white">2</div>
  <div class="item" style="text-align: center; margin: 0.1em; padding: 0.1em 1em; background-color: #0a9396; color: white">3</div>
</div>
  <span style="flex-basis: 8em; text-align: left; font-size: 75%">flex-end</span>
</div>

<div style="display: flex; align-items: center; gap: 1em">
<div class="container" style="flex-grow: 1; justify-content: center; display: flex; background-color: #94d2bd; padding: 0.1em; margin-bottom: 0.1em">
  <div class="item" style="text-align: center; margin: 0.1em; padding: 0.1em 1em; background-color: #0a9396; color: white">1</div>
  <div class="item" style="text-align: center; margin: 0.1em; padding: 0.1em 1em; background-color: #0a9396; color: white">2</div>
  <div class="item" style="text-align: center; margin: 0.1em; padding: 0.1em 1em; background-color: #0a9396; color: white">3</div>
</div>
  <span style="flex-basis: 8em; text-align: left; font-size: 75%">center</span>
</div>

<div style="display: flex; align-items: center; gap: 1em">
<div class="container" style="flex-grow: 1; justify-content: space-around; display: flex; background-color: #94d2bd; padding: 0.1em; margin-bottom: 0.1em">
  <div class="item" style="text-align: center; margin: 0.1em; padding: 0.1em 1em; background-color: #0a9396; color: white">1</div>
  <div class="item" style="text-align: center; margin: 0.1em; padding: 0.1em 1em; background-color: #0a9396; color: white">2</div>
  <div class="item" style="text-align: center; margin: 0.1em; padding: 0.1em 1em; background-color: #0a9396; color: white">3</div>
</div>
  <span style="flex-basis: 8em; text-align: left; font-size: 75%">space-around</span>
</div>

<div style="display: flex; align-items: center; gap: 1em">
<div class="container" style="flex-grow: 1; justify-content: space-between; display: flex; background-color: #94d2bd; padding: 0.1em; margin-bottom: 0.1em">
  <div class="item" style="text-align: center; margin: 0.1em; padding: 0.1em 1em; background-color: #0a9396; color: white">1</div>
  <div class="item" style="text-align: center; margin: 0.1em; padding: 0.1em 1em; background-color: #0a9396; color: white">2</div>
  <div class="item" style="text-align: center; margin: 0.1em; padding: 0.1em 1em; background-color: #0a9396; color: white">3</div>
</div>
  <span style="flex-basis: 8em; text-align: left; font-size: 75%">space-between</span>
</div>

<div style="display: flex; align-items: center; gap: 1em">
<div class="container" style="flex-grow: 1; justify-content: space-evenly; display: flex; background-color: #94d2bd; padding: 0.1em; margin-bottom: 0.1em">
  <div class="item" style="text-align: center; margin: 0.1em; padding: 0.1em 1em; background-color: #0a9396; color: white">1</div>
  <div class="item" style="text-align: center; margin: 0.1em; padding: 0.1em 1em; background-color: #0a9396; color: white">2</div>
  <div class="item" style="text-align: center; margin: 0.1em; padding: 0.1em 1em; background-color: #0a9396; color: white">3</div>
</div>
  <span style="flex-basis: 8em; text-align: left; font-size: 75%">space-evenly</span>
</div>

---

# Align Items

The [align-items](https://css-tricks.com/snippets/css/a-guide-to-flexbox/#aa-align-items) property defines the default behaviour for how flex items are laid out along the **cross** axis on the current line: **flex-start**, **flex-end**, **center**, **baseline**, **stretch**. The default is **stretch**.

```css
.container {
  align-items: flex-start;
}
```
<div style="display: flex; align-items: center; gap: 1em">
  <div class="container" style="flex-grow:1; align-items: flex-start; display: flex; background-color: #94d2bd; padding: 0.1em; margin-bottom: 0.1em">
    <div class="item" style="font-size: 50%; text-align: center; margin: 0.2em; padding: 0.2em 2em; background-color: #0a9396; color: white">1</div>
    <div class="item" style="text-align: center; margin: 0.1em; padding: 0.1em 1em; background-color: #0a9396; color: white">2</div>
    <div class="item" style="font-size: 50%; text-align: center; margin: 0.2em; padding: 0.2em 2em; background-color: #0a9396; color: white">3</div>
  </div>
  <span style="flex-basis: 5em; text-align: left; font-size: 75%">flex-start</span>
</div>

<div style="display: flex; align-items: center; gap: 1em">
  <div class="container" style="flex-grow:1; align-items: flex-end; display: flex; background-color: #94d2bd; padding: 0.1em; margin-bottom: 0.1em">
    <div class="item" style="font-size: 50%; text-align: center; margin: 0.2em; padding: 0.2em 2em; background-color: #0a9396; color: white">1</div>
    <div class="item" style="text-align: center; margin: 0.1em; padding: 0.1em 1em; background-color: #0a9396; color: white">2</div>
    <div class="item" style="font-size: 50%; text-align: center; margin: 0.2em; padding: 0.2em 2em; background-color: #0a9396; color: white">3</div>
  </div>
  <span style="flex-basis: 5em; text-align: left; font-size: 75%">flex-end</span>
</div>

<div style="display: flex; align-items: center; gap: 1em">
<div class="container" style="flex-grow:1; align-items: center; display: flex; background-color: #94d2bd; padding: 0.1em; margin-bottom: 0.1em">
  <div class="item" style="font-size: 50%; text-align: center; margin: 0.2em; padding: 0.2em 2em; background-color: #0a9396; color: white">1</div>
  <div class="item" style="text-align: center; margin: 0.1em; padding: 0.1em 1em; background-color: #0a9396; color: white">2</div>
  <div class="item" style="font-size: 50%; text-align: center; margin: 0.2em; padding: 0.2em 2em; background-color: #0a9396; color: white">3</div>
</div>
  <span style="flex-basis: 5em; text-align: left; font-size: 75%">center</span>
</div>

<div style="display: flex; align-items: center; gap: 1em">
<div class="container" style="flex-grow:1; align-items: baseline; display: flex; background-color: #94d2bd; padding: 0.1em; margin-bottom: 0.1em">
  <div class="item" style="font-size: 50%; text-align: center; margin: 0.2em; padding: 0.2em 2em; background-color: #0a9396; color: white">1</div>
  <div class="item" style="text-align: center; margin: 0.1em; padding: 0.1em 1em; background-color: #0a9396; color: white">2</div>
  <div class="item" style="font-size: 50%; text-align: center; margin: 0.2em; padding: 0.2em 2em; background-color: #0a9396; color: white">3</div>
</div>
  <span style="flex-basis: 5em; text-align: left; font-size: 75%">baseline</span>
</div>

<div style="display: flex; align-items: center; gap: 1em">
<div class="container" style="flex-grow:1; align-items: stretch; display: flex; background-color: #94d2bd; padding: 0.1em; margin-bottom: 0.1em">
  <div class="item" style="font-size: 50%; text-align: center; margin: 0.2em; padding: 0.2em 2em; background-color: #0a9396; color: white">1</div>
  <div class="item" style="text-align: center; margin: 0.1em; padding: 0.1em 1em; background-color: #0a9396; color: white">2</div>
  <div class="item" style="font-size: 50%; text-align: center; margin: 0.2em; padding: 0.2em 2em; background-color: #0a9396; color: white">3</div>
</div>
  <span style="flex-basis: 5em; text-align: left; font-size: 75%">stretch</span>
</div>

---

# Order

The [order](https://css-tricks.com/snippets/css/a-guide-to-flexbox/#aa-order) property alters the order in which a **flex item** is laid out in its container.

```css
.item:first-child {
   order: 3;
}
```

<div class="container" style="display: flex; background-color: #94d2bd; padding: 0.5em;">
  <div class="item" style="order: 3; text-align: center; margin: 0.5em; padding: 0.5em; background-color: #0a9396; color: white">1</div>
  <div class="item" style="text-align: center; margin: 0.5em; padding: 0.5em; background-color: #0a9396; color: white">2</div>
  <div class="item" style="text-align: center; margin: 0.5em; padding: 0.5em; background-color: #0a9396; color: white">3</div>
</div>

.box_info[
  Notice that we are targetting the items now!

---

# Grow and Shrink

The [flex-grow](https://css-tricks.com/snippets/css/a-guide-to-flexbox/#aa-flex-grow) and [flex-shrink](https://css-tricks.com/snippets/css/a-guide-to-flexbox/#aa-flex-shrink) properties define the ability for a flex item to **grow** (if there is extra space) or **shrink** (if there isn't enough):
* They accept a unitless value that serves as a **proportion**. 
* The default is **0** for *flex-grow*, which means items don't grow by default.
* The default is **1** for *flex-shrink*, which means items shrink equally.

```css
.item:nth-child(1) {
  flex-grow: 1;
}

.item:nth-child(2) {
  flex-grow: 2;  
}
```

<div class="container" style="display: flex; background-color: #94d2bd; padding: 0.5em;">
  <div class="item" style="flex-grow: 1; text-align: center; margin: 0.5em; padding: 0.5em; background-color: #0a9396; color: white">1</div>
  <div class="item" style="flex-grow: 2; text-align: center; margin: 0.5em; padding: 0.5em; background-color: #0a9396; color: white">2</div>
  <div class="item" style="text-align: center; margin: 0.5em; padding: 0.5em; background-color: #0a9396; color: white">3</div>
</div>

---

# Align Self

The [align-self](https://css-tricks.com/snippets/css/a-guide-to-flexbox/#aa-align-self) property allows the alignment specified by *align-items* to be overridden for individual flex items. The default value is **auto**, meaning that items follow the alignment set by *align-items*.

```css
.container {
  align-items: flex-start;
}

.item:nth-child(1) { height: 3em; }
.item:nth-child(2) { align-self: center; }
```

All items aligned as **flex-start** except the second one that is **center**-aligned.

<div class="container" style="align-items: flex-start; display: flex; background-color: #94d2bd; padding: 0.5em;">
  <div class="item" style="height: 3em; text-align: center; margin: 0.5em; padding: 0.5em; background-color: #0a9396; color: white">1</div>
  <div class="item" style="align-self: center; text-align: center; margin: 0.5em; padding: 0.5em; background-color: #0a9396; color: white">2</div>
  <div class="item" style="text-align: center; margin: 0.5em; padding: 0.5em; background-color: #0a9396; color: white">3</div>
</div>

---

# Gap

The [gap](https://css-tricks.com/snippets/css/a-guide-to-flexbox/#aa-gap-row-gap-column-gap) property is a shorthand for two other properties:

- **row-gap**: a gap between every row in a flexbox.
- **column-gap**: a gap between every column in a flexbox.

You can either pass only one value (a length) and set both simultaneously or two values and set each one individually (*row-gap* first, then *column-gap*).

```css
.container { gap: 2em 1em; }

.item { width: 6em; margin: 0; flex-grow: 1; }
```

<div class="container" style="flex-wrap: wrap; gap: 2em 1em; align-items: flex-start; display: flex; background-color: #94d2bd; padding: 0.5em;">
  <div class="item" style="flex-grow: 1; width: 6em; text-align: center; padding: 0.5em; background-color: #0a9396; color: white">1</div>
  <div class="item" style="flex-grow: 1; width: 6em; text-align: center; padding: 0.5em; background-color: #0a9396; color: white">2</div>
  <div class="item" style="flex-grow: 1; width: 6em; text-align: center; padding: 0.5em; background-color: #0a9396; color: white">3</div>
  <div class="item" style="flex-grow: 1; width: 6em; text-align: center; padding: 0.5em; background-color: #0a9396; color: white">4</div>
  <div class="item" style="flex-grow: 1; width: 6em; text-align: center; padding: 0.5em; background-color: #0a9396; color: white">5</div>
  <div class="item" style="flex-grow: 1; width: 6em; text-align: center; padding: 0.5em; background-color: #0a9396; color: white">6</div>
  <div class="item" style="flex-grow: 1; width: 6em; text-align: center; padding: 0.5em; background-color: #0a9396; color: white">7</div>
  <div class="item" style="flex-grow: 1; width: 6em; text-align: center; padding: 0.5em; background-color: #0a9396; color: white">8</div>
</div>

---

# Grid

---

# Grid

A grid layout enables us to align elements into **columns** and **rows** of different sizes.

Elements in a grid layout can occupy the same cells as other elements, thus **overlapping** and creating **layers**.

[A Complete Guide to Grid](https://css-tricks.com/snippets/css/complete-guide-grid/)

---

# Running Example

```html
<div class="container">
  <div class="item header">Header</div>
  <div class="item menu1">Menu 1</div>
  <div class="item menu2">Menu 2</div>
  <div class="item content">Lorem ipsum...</div>
  <div class="item footer">Footer</div>
</div>
```

```css
.container {
  background-color: #eee;padding: 5px;  
}
.item {
  color: black; text-align: center; margin: 2px; padding: 0.2em; background-color: ...
}
```

<div class="container" style="background-color: #eee;padding: 5px;">
  <div class="item header" style="color: black; text-align: center; margin: 2px; padding: 0.2em; background-color: #2a9d8f;">Header</div>
  <div class="item menu1" style="color: black; text-align: center; margin: 2px; padding: 0.2em; background-color: #e9d8a6;">Menu 1</div>
  <div class="item menu2" style="color: black; text-align: center; margin: 2px; padding: 0.2em; background-color: #e9c46a;">Menu 2</div>
  <div class="item content" style="color: black; text-align: center; margin: 2px; padding: 0.2em; background-color: #f4a261;">Content</div>
  <div class="item footer" style="color: black; text-align: center; margin: 2px; padding: 0.2em; background-color: #e76f51;">Footer</div>
</div>

---

# Grid

Changing the [display](https://css-tricks.com/snippets/css/complete-guide-grid/#aa-display) property of the container to *grid* transforms it into a grid layout.

```css
.container {
  display: grid;
}
```

By default, there is only one column.

<div class="container" style="background-color: #eee;padding: 5px; display: grid;">
  <div class="item header" style="color: black; text-align: center; margin: 2px; padding: 0.2em; background-color: #2a9d8f;">Header</div>
  <div class="item menu1" style="color: black; text-align: center; margin: 2px; padding: 0.2em; background-color: #e9d8a6;">Menu 1</div>
  <div class="item menu2" style="color: black; text-align: center; margin: 2px; padding: 0.2em; background-color: #e9c46a;">Menu 2</div>
  <div class="item content" style="color: black; text-align: center; margin: 2px; padding: 0.2em; background-color: #f4a261;">Content</div>
  <div class="item footer" style="color: black; text-align: center; margin: 2px; padding: 0.2em; background-color: #e76f51;">Footer</div>
</div>

---

# Grid Templates

The [grid-template-columns and grid-template-rows](https://css-tricks.com/snippets/css/complete-guide-grid/#aa-grid-template-columnsgrid-template-rows) properties allow us to define the number and size of the columns and rows of our table.

Sizes can be defined as **auto**, a **length**, a **percentage** or a **fraction** of the free space (using the *fr* unit).

```css
.container {
  grid-template-columns: 5em 1fr 2fr;
  grid-template-rows: 2em 3em;
}
```

<div class="container" style="background-color: #eee;padding: 5px; display: grid; grid-template-columns: 5em 1fr 2fr; grid-template-rows: 2em 3em;">
  <div class="item header" style="color: black; text-align: center; margin: 2px; padding: 0.2em; background-color: #2a9d8f;">Header</div>
  <div class="item menu1" style="color: black; text-align: center; margin: 2px; padding: 0.2em; background-color: #e9d8a6;">Menu 1</div>
  <div class="item menu2" style="color: black; text-align: center; margin: 2px; padding: 0.2em; background-color: #e9c46a;">Menu 2</div>
  <div class="item content" style="color: black; text-align: center; margin: 2px; padding: 0.2em; background-color: #f4a261;">Content</div>
  <div class="item footer" style="color: black; text-align: center; margin: 2px; padding: 0.2em; background-color: #e76f51;">Footer</div>
</div>

---

# Grid Templates Repeating

The [repeat()](https://css-tricks.com/snippets/css/complete-guide-grid/#aa-the-repeat-function-and-keywords) function can be used to simplify grid templates with many columns and rows of the same size.

The first parameter is the *repeat count*, and the second are the *tracks* (space-separated) that will be created. 

```css
.container {
  grid-template-columns: repeat(2, 5em) 1fr repeat(2, 5em 4em);
}
```

<div class="container" style="background-color: #eee;padding: 5px; display: grid; grid-template-columns: repeat(2, 5em) 1fr repeat(2, 5em 4em); grid-template-rows: 2em; font-size: 0.8em;">
  <div class="item header" style="color: black; text-align: center; margin: 2px; padding: 0.2em; background-color: #2a9d8f;">(5em)</div>
  <div class="item menu1" style="color: black; text-align: center; margin: 2px; padding: 0.2em; background-color: #2a9d8f;">(5em)</div>
  <div class="item menu2" style="color: black; text-align: center; margin: 2px; padding: 0.2em; background-color: #e9c46a;">(1fr)</div>
  <div class="item content" style="color: black; text-align: center; margin: 2px; padding: 0.2em; background-color: #f4a261;">(5em)</div>
  <div class="item content" style="color: black; text-align: center; margin: 2px; padding: 0.2em; background-color: #e76f51;">(4em)</div>
  <div class="item footer" style="color: black; text-align: center; margin: 2px; padding: 0.2em; background-color: #f4a261;">(5em)</div>
  <div class="item footer" style="color: black; text-align: center; margin: 2px; padding: 0.2em; background-color: #e76f51;">(4em)</div>
</div>

---

# Flexible Grid Repeating

When defining multiple columns with the `repeat()` function, we can also set the *count* to `auto-fit` or `auto-fill`:

- `repeat(n, value)`: Repeats a track definition *n* times.
- `repeat(auto-fill, value)`: Creates as many columns as fit within the container.
- `repeat(auto-fit, value)`: Similar to auto-fill but [collapses](https://css-tricks.com/auto-sizing-columns-css-grid-auto-fill-vs-auto-fit/) unused space.

The `minmax()` function sets a track’s minimum and maximum size, ensuring it stays within a defined range. This allows [responsive](https://jsfiddle.net/7yahvgmp/2/) grid designs.

```css
.container {
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
}
```

---

# Numerical Names

By default, gridlines are assigned a numerical value starting on *one*.

<img src="assets/css3/grid.svg" width="30%">

---

# Assigning Location

We can assign a **location** to an item within the grid by referring to specific grid lines using the [grid-column-start, grid-column-end, grid-row-start, and grid-row-end](https://css-tricks.com/snippets/css/complete-guide-grid/#aa-grid-column-startgrid-column-endgrid-row-startgrid-row-end) properties.

```css
.header {
  grid-column-start: 1;
  grid-column-end: 3;
  grid-row-start: 1;
  grid-row-end: 2;
}
```

The *end* values can also be the number of **rows** or **columns** to **span**. By default, these values have a *span* of 1.

```css
.header {
  grid-column-end: span 2;
  grid-row-end: span 1;    /* not needed - default value */
}
```

---

# Location Shorthand

The [grid-column and grid-row](https://css-tricks.com/snippets/css/complete-guide-grid/#aa-grid-columngrid-row) properties can be used as a **shorthand** for assigning the location of an item. Each receives **two values** separated by a **forward slash** (start / end).

The [grid-area](https://css-tricks.com/snippets/css/complete-guide-grid/#prop-grid-area) property can be used as a **shorthand** for the **four values** at once: *row-start* / *column-start* / *row-end* / *column-end*.

```css
.header {
  grid-area: 1 / 1 / span 1 / span 2;
}

.menu1 {
  grid-column: 1; grid-row: 2;
}

.menu2 {
  grid-column: 1; grid-row: 3 / 5;
}

.content {
  grid-column: 2; grid-row: 2 / span 2;
}

.footer {
  grid-column: 2; grid-row: 4;
}
```

---

# Location Result

```css
.container {
  grid-template-columns: auto 1fr; 
  grid-template-rows: auto auto 1fr auto;
}
.menu1   { height: 3em;  } /* to simulate  */
.content { height: 10em; } /* some content */
```

<div class="container" style="background-color: #eee;padding: 5px; display: grid; grid-template-columns: auto 1fr; grid-template-rows: auto auto 1fr auto;">
  <div class="item header" style="color: black; text-align: center; margin: 2px; padding: 0.2em; background-color: #2a9d8f;grid-area: 1 / 1 / span 1 / span 2;">Header</div>
  <div class="item menu1" style="color: black; text-align: center; margin: 2px; padding: 0.2em; background-color: #e9d8a6;grid-column: 1; grid-row: 2; height: 3em">Menu 1</div>
  <div class="item menu2" style="color: black; text-align: center; margin: 2px; padding: 0.2em; background-color: #e9c46a;  grid-column: 1; grid-row: 3 / 5;">Menu 2</div>
  <div class="item content" style="color: black; text-align: center; margin: 2px; padding: 0.2em; background-color: #f4a261;  grid-column: 2; grid-row: 2 / span 2; height: 10em;">Content</div>
  <div class="item footer" style="color: black; text-align: center; margin: 2px; padding: 0.2em; background-color: #e76f51; grid-column: 2; grid-row: 4;">Footer</div>
</div>

---

# Grid Line Names

We can assign **names** (more than one) to the grid lines.

```css
.container {
  grid-template-columns: [left] auto [middle] 1fr [right];
  grid-template-rows: [top] auto [header-end content-start] auto
                      [menu-sep] 1fr [footer-start] auto [bottom];
}
.content {
  grid-area: content-start / middle / footer-start / right;
}
```

<img src="assets/css3/grid-names.svg" width="35%">

---

# Grid Template Areas

We can define a **grid template** more visually by giving names to items using the *grid-area* property.

Any number of **adjacent periods** can be used to declare a single empty cell.

```css
.container {
  grid-template-columns: auto 1fr;
  grid-template-rows: auto auto 1fr auto;

  grid-template-areas: "header header"
                       "menu1  content"
                       "menu2  content"
                       "menu2  footer";
}

.header { grid-area: header; }

.menu1 { grid-area: menu1; }

.menu2 { grid-area: menu2; }

.content { grid-area: content; }

.footer { grid-area: footer; }
```

---

# Aligning Items

Like with *flexbox*, we can adjust the placement of each item inside its cell on the grid.
For that, we use the following properties:

* [column-gap, row-gap](https://css-tricks.com/snippets/css/complete-guide-grid/#aa-column-gaprow-gapgrid-column-gapgrid-row-gap), and [gap](https://css-tricks.com/snippets/css/complete-guide-grid/#aa-gapgrid-gap): they work just like in **flexbox**.
* [justify-items](https://css-tricks.com/snippets/css/complete-guide-grid/#aa-justify-items): Align items along the **row** with: *start*, *end*, *center*, and *stretch*.
* [align-items](https://css-tricks.com/snippets/css/complete-guide-grid/#aa-align-items): Align items along the **column** with: *start*, *end*, *center*, *stretch*, and *baseline*.
* [justify-content](https://css-tricks.com/snippets/css/complete-guide-grid/#aa-justify-content) and [align-content](https://css-tricks.com/snippets/css/complete-guide-grid/#aa-align-content): Align the rows and columns inside the grid **container** (if they have room to spare) with: *start*, *end*, *center*, *stretch*, *space-around*, *space-between*, *space-evenly*.

There are also properties to adjust each **item individually**: [justify-self](https://css-tricks.com/snippets/css/complete-guide-grid/#aa-justify-self) and [align-self](https://css-tricks.com/snippets/css/complete-guide-grid/#aa-align-self).

---

# Alignment Example

An interactive example to showcase different alignments:

<div id="ex-ji" class="container" style="height: 14em; background-color: #eee;padding: 5px; display: grid; grid-template-columns: auto auto auto; grid-template-rows: auto auto auto;">
  <div class="item-a" style="text-align: center; font-size: 0.8em; margin: 2px; padding: 0.3em; background-color: #e9d8a6; ">A</div>
  <div style="text-align: center; font-size: 1em; margin: 2px; padding: 0.3em; background-color: #f4a261; ">B <br> B</div>
  <div style="text-align: center; font-size: 1.2em; margin: 2px; padding: 0.3em; background-color: #e76f51; ">CCC</div>

  <div style="text-align: center; font-size: 1.2em; margin: 2px; padding: 0.3em; background-color: #e9d8a6; ">DDD</div>
  <div style="text-align: center; font-size: 0.8em; margin: 2px; padding: 0.3em; background-color: #f4a261; ">EEEEE</div>
  <div style="text-align: center; font-size: 1em; margin: 2px; padding: 0.3em; background-color: #e76f51; ">F</div>

  <div style="text-align: center; font-size: 0.8em; margin: 2px; padding: 0.3em; background-color: #e9d8a6; ">GG</div>
  <div style="text-align: center; font-size: 1.2em; margin: 2px; padding: 0.3em; background-color: #f4a261; ">H<br>H<br>H</div>
  <div style="text-align: center; font-size: 1em; margin: 2px; padding: 0.3em; background-color: #e76f51; ">II</div>
</div>
<div style="margin-top: 1em; font-size: 0.6em; font-family: monospace; background-color: #EEE; padding: 0.5em; display: grid; grid-template-columns: auto auto">
  <div>
  .container {
    <div style="display: grid; grid-template-columns: auto; justify-content: start; margin-left: 2em; column-gap: 1em;">
    <label>grid-template-columns: <select onchange="document.querySelector('#ex-ji').style.gridTemplateColumns = this.value">
      <option>auto auto auto</option>
      <option>auto auto 1fr</option>
      <option>auto 20em 1fr</option>
      <option>auto 1fr 2fr</option>
    </select>;</label>
    <label>justify-items: <select onchange="document.querySelector('#ex-ji').style.justifyItems = this.value">
      <option>stretch</option>
      <option>start</option>
      <option>end</option>
      <option>center</option>
    </select>;</label>
    <label>align-items: <select onchange="document.querySelector('#ex-ji').style.alignItems = this.value">
      <option>stretch</option>
      <option>start</option>
      <option>end</option>
      <option>center</option>
      <option>baseline</option>
    </select>;</label>
    <label>justify-content: <select onchange="document.querySelector('#ex-ji').style.justifyContent = this.value">
      <option>stretch</option>
      <option>start</option>
      <option>end</option>
      <option>center</option>
      <option>space-around</option>
      <option>space-between</option>
      <option>space-evenly</option>
    </select>;</label>
    <label>align-content: <select onchange="document.querySelector('#ex-ji').style.alignContent = this.value">
      <option>stretch</option>
      <option>start</option>
      <option>end</option>
      <option>center</option>
      <option>space-around</option>
      <option>space-between</option>
      <option>space-evenly</option>
    </select>;</label>
    </div>
  }
  </div>
  <div>
  .item-a {
    <div style="display: grid; grid-template-columns: auto; justify-content: start; margin-left: 2em; column-gap: 1em;">
    <label>justify-self: <select onchange="document.querySelector('#ex-ji .item-a').style.justifySelf = this.value">
      <option>stretch</option>
      <option>start</option>
      <option>end</option>
      <option>center</option>
    </select>;</label>
    <label>align-self: <select onchange="document.querySelector('#ex-ji .item-a').style.alignSelf = this.value">
      <option>stretch</option>
      <option>start</option>
      <option>end</option>
      <option>center</option>
      <option>baseline</option>
    </select>;</label>
    </div>
  }
  </div>
<div>

---

# Implicit Cells

You can assign an item to a location you **did not define** using [grid-template-columns]((https://css-tricks.com/snippets/css/complete-guide-grid/#prop-grid-template-columns-rows) and [grid-template-rows](https://css-tricks.com/snippets/css/complete-guide-grid/#prop-grid-template-columns-rows).

In that case, the needed column and rows are **automatically** added with size auto.

```css
.container { grid-template-rows: 2em; grid-template-columns: 2em; }
.item_a { grid-column-start: 1 }
.item_b { grid-column-start: 4 }
```

<div style="display: grid; grid-template-rows: 2em; grid-template-columns: 2em;">
  <div style="color: white; text-align: center; background-color: #2a9d8f">A</div>
  <div style="color: white; text-align: center; background-color: #e9c46a; grid-column-start: 4">B</div>
</div>

There are three **implicit** grid tracks in this example.

---

# Auto Column and Rows

We can specify the **size** of any **implicit grid tracks** using *grid-auto-rows* and *grid-auto-columns*.

These properties can receive a **length** &mdash; or a series of lengths &mdash; that is **repeated** as needed.

```css
.container { 
  grid-template-rows: 2em; grid-template-columns: 2em; grid-auto-columns: 3em 4em;
}
.item_a { grid-column-start: 1 }
.item_b { grid-column-start: 4 }
```

<div style="display: grid; grid-template-rows: 2em; grid-template-columns: 2em; grid-auto-columns: 3em 4em">
  <div style="color: white; text-align: center; background-color: #2a9d8f">A</div>
  <div style="color: white; text-align: center; background-color: #e9c46a; grid-column-start: 4">B</div>
</div>

The three **implicit** grid tracks in this example have sizes *3em*, *4em*, and *3em*.
Only the last one has content.

---

# Auto Flow

If some items are **not explicitly** assigned a location, then an *auto-placement* algorithm is used to place them.

The behavior of this algorithm can be changed using the [grid-auto-flow](https://css-tricks.com/snippets/css/complete-guide-grid/#aa-grid-auto-flow) property:

* *row* - The **default** value; Fill empty spaces **row by row** (if the item fits) and add **new rows** if necessary.
* *column* - Fill empty spaces **column by column** (if the item fits) and add **new columns** if necessary.
* *dense* - If some spaces were left **empty**, see if items that appear **later** fit there and use those spaces. This **changes the order** of the items.

---

# Simplified Positioning

We can use the **auto-placement** algorithm to **simplify** item positioning:

```css
.container { 
  grid-template-columns: auto 1fr; 
  grid-template-rows: auto auto 1fr auto; 
}
.header { grid-column-end: span 2 }
.content { grid-row: 2 / span 2; grid-column: 2 }
.menu2 { grid-row-end: span 2 }
```

<div class="container" style="background-color: #eee;padding: 5px; display: grid; grid-template-columns: auto 1fr; grid-template-rows: auto auto 1fr auto;">
  <div class="item header" style="color: black; text-align: center; margin: 2px; padding: 0.2em; background-color: #2a9d8f; grid-column-end: span 2">Header</div>
  <div class="item menu1" style="color: black; text-align: center; margin: 2px; padding: 0.2em; background-color: #e9d8a6;height: 3em">Menu 1</div>
  <div class="item menu2" style="color: black; text-align: center; margin: 2px; padding: 0.2em; background-color: #e9c46a;grid-row-end: span 2">Menu 2</div>
  <div class="item content" style="color: black; text-align: center; margin: 2px; padding: 0.2em; background-color: #f4a261; grid-row: 2 / span 2; grid-column: 2;height: 8em">Content</div>
  <div class="item footer" style="color: black; text-align: center; margin: 2px; padding: 0.2em; background-color: #e76f51;">Footer</div>
</div>

---

# Cascading

---

# Example

What **color** will the **text** be? And what about the **link**?

```html
<section>
 <p>The quick brown fox <a href="#">jumps</a> over the lazy dog</p>
</section>
```

```css
section {
  color: red;
}
```

--

<p style="color:red">The quick brown fox <a href="#" style="color:blue">jumps</a> over the lazy dog</p>

The text becomes red, but the link is still blue. Why?

---

# Defaults

Each browser has **its own** set of default values for the properties of each HTML element.

These defaults are very similar between browsers, but slight differences can make cross-browser development harder.

**Tip**: There are several CSS stylesheets that [normalize](https://github.com/necolas/normalize.css/) and [reset](https://github.com/elad2412/the-new-css-reset) each default value to mitigate this problem.

---

# Inherit

A special value that can be used in almost every property:
* When a property is set to **inherit**, the value of that property is **inherited** from the element's **parent**.
* Most browser defaults have the value **inherit**. 

```html
<nav id="menu">
  <h1>Menu</h1> <!-- inherits the blue color from the nav -->
</nav>
```

```css
h1{
  color: inherit;
}

#menu {
  color: blue;
}
```

---

# Example Revisited

* In most browsers, the **link** color is set as **blue**.
* On the other hand, the **paragraph** color is set as **inherit**.

```html
<section>
 <p>The quick brown fox <a href="#">jumps</a> over the lazy dog</p>
</section>
```

```css
a {
  color: blue;    /* Doesn't inherit the color */
}

p {
  color: inherit; /* Inherits the color from the section */
}

section {
  color: red;
}
```

---

# Specificity

What about this example?

```css
<nav id="menu">
  <p>What is my color?</p>
</nav>
```

```css
#menu p {
  color: green;
}

nav p {
  color: red;
}
```
--

<span style="color: green">Green</span>! Because the first **rule** is **more specific** than the second one.

---
## Calculating Specificity

A rule's specificity is defined as three values (a, b, c).
  
Each one of them is incremented when a certain type of selector is used:

 * **a**: Id
 * **b**: Class, Pseudo class, Attribute
 * **c**: Element, Pseudo Element

Ordering:

* Rules with a bigger **a** value are **more specific**.
* If the **a** value is the same for both rules, the **b** value is used for comparison.
* If still needed, the **c** value is used.

---

## Specificity Examples

* *: - (0, 0, 0)
* p: 1 element – (0, 0, 1)
* div: 1 element – (0, 0, 1)
* \#sidebar: 1 id – (1, 0, 0)
* div#sidebar: 1 element, 1 id – (1, 0, 1)
* div#sidebar p: 2 elements, 1 id – (1, 0, 2)
* div#sidebar p.bio: 2 elements, 1 class, 1 id – (1, 1, 2)

Specificity Calculator: [http://specificity.keegan.st](http://specificity.keegan.st)

---
# Cascading

* The rule to be applied is selected using the following rules in order:
 * **Origin** (author, user, default).
 * **Specificity** (bigger is better).
 * **Position** (last is better).

* **Origin** Explanation:
 * **author**: The CSS rules defined by the page developer.
 * **user**: User defined preferences.
 * **default**: Browser defaults.

---

# Layers

- Cascade Layers allow you to group your CSS into "buckets" and decide which bucket is more important, **regardless** of how **specific** the selectors are.

- Sometimes a **generic rule** (like #menu p) is hard to override later in your CSS because it has **high specificity** (1,0,1). You end up writing longer and longer selectors just to change a color.

- By using `@layer`, the order of the layer defines the winner. A "later" layer **always** beats an "earlier" layer.

---

# Layers Example

```css
/* 1. Define the hierarchy at the top */
@layer base, components;

@layer base {
  /* This has high specificity (1, 0, 1) */
  #menu p { color: red; } 
}

@layer components {
  /* This has low specificity (0, 0, 1) but WINS 
     because 'components' comes after 'base' */
  p { color: blue; } 
}
```
Layers are between **origin** and **specificity** in the cascading order.

---

# Vars

---

# Vars

Entities that contain **reusable values**. Set using a **custom property** notation:

```var
body {
  --main-bg-color: blue;
  --default-margin: 1em;
}
```

Accessed using the *var()* function:

```css
body header {
  margin: var(--default-margin);
}
```

---

# CSS Vars Inheritance

CSS vars are also **inherited**. 

If no value is set for a *var* on a given element, the value of its *parent* is used.

```html
<section>
  <header>
    <h1>Title</h1>     <!-- red -->
    <h2>Sub-title</h2> <!-- blue -->
  </header>
</section>
```

```css
section  { --text-color: blue; }
h1       { --text-color: red; }
header * { color: var(--text-color); } 
```

**Extra**: What if the * is removed?

---

template:inverse
name:responsive
# Responsive Design

---

# Responsive Design

Responsive web design makes websites that work effectively on both desktop browsers and the myriad of mobile devices on the market.

![](assets/css3/responsive.jpg)

.footnote[
Image taken from http://designmodo.com/responsive-design-examples/

---

# Responsive vs. Adaptative

**Adaptive Design**: Multiple **fixed** width layouts

**Responsive Design**: Multiple **fluid** grid layouts

**Mixed Approach**: Multiple fixed width layout for larger screens, multiple fluid layout for smaller screens.

---

# Viewport

Pages optimized for various devices must include a meta viewport element in the head of the document. 

A meta viewport tag gives the browser instructions on how to control the page's dimensions and scale.

```html
<meta name="viewport" 
      content="width=device-width, initial-scale=1.0">
```

* *width=device-width* matchs the screen's width in device independent pixels.
* initial-scale=1* establishs a 1:1 relationship between CSS pixels and device independent pixels.

Learn more: [MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/Viewport_concepts) and a tale of two viewports [part 1](http://www.quirksmode.org/mobile/viewports.html) and [part 2](http://www.quirksmode.org/mobile/viewports2.html).

---

# Media Queries

A **media-query** is composed of a **media type** and/or a number of **media features**.

They can be used when linking to a CSS file from HTML or directly in the CSS code (allowing dynamic changes).

```html
<link rel="stylesheet"
      media="(min-width: 600px) and (max-width: 800px)"
      href="medium.css" />
```

```css
@media (max-width: 600px) {
  .sidebar {
    display: none;
  }
}
```

---

# Media Types

The media type indicates in what media type the CSS is to be applied.

* **all** - suitable for all devices.
* **print** - intended for paged material and for documents viewed on screen in print preview mode.
* **screen** - intended primarily for color computer screens.
* **speech** - intended for speech synthesizers (aural in CSS2).

```html
<link rel="stylesheet" media="print" href="print.css" />
```

---

# Media Features

* **min-width**	width over the value defined in the query.
* **max-width**	width under the value defined in the query.
* **min-height** height over the value defined in the query.
* **max-height** height under the value defined in the query.
* **orientation=portrait** height is greater than or equal to the width.
* **orientation=landscape**	width is greater than the height.

```html
<link rel="stylesheet" 
      media="(min-width: 800px)" 
      href="large.css" />
```

Parentheses are required around expressions; failing to use them is an error.

---

# Logical Operators

* **and** used for combining multiple media features.
* **comma-separated** lists behave as the logical operator **or**.
* **not** applies to the whole media query and returns true if the media query would otherwise return false.

```html
<link rel="stylesheet"
      media="(min-width: 800px) and screen, print"
      href="large.css" />
```

Learn more: [MDN](https://developer.mozilla.org/en-US/docs/Web/Guide/CSS/Media_queries).

---

template:inverse
name:prefix
#Vendor Prefixes

---

#Vendor Prefixes

While the specification of selectors, properties, and values are still being finalized, it is normal for browsers to go through an **experimentation** period.

Browsers might also have **proprietary** extensions to the CSS standard.

In order to accommodate the release of vendor-specific extensions, the CSS specifications define a specific format that vendors should follow:

```css
.round {
  -webkit-border-radius: 2px;
  -moz-border-radius: 2px;
  border-radius: 2px;
}
```

Prefixes: **-webkit-** (chrome, safari), **-moz-** (firefox), **-o-** (opera), **-ms-** (internet explorer), ...

Check browser support: http://caniuse.com/

---

template:inverse
name:validation
#Validation
http://jigsaw.w3.org/css-validator/

---

# Extra stuff

* Frameworks: [Ink](http://ink.sapo.pt/), [Bootstrap](http://getbootstrap.com/), [Flat UI](http://designmodo.github.io/Flat-UI/), [Pure](http://purecss.io/), [Pico](https://picocss.com/), [Tailwind](https://tailwindcss.com/)
* Advanced/Experimental: [Shadows](https://developer.mozilla.org/en-US/docs/Web/CSS/box-shadow), [Animations](https://developer.mozilla.org/en-US/docs/Web/CSS/animation)
* Playgrounds: [JSFiddle](https://jsfiddle.net/), [CodePen](https://codepen.io/)
* Pre-processors: [Less](http://lesscss.org/), [Sass](http://sass-lang.com/)
* Information: [Google Web Essentials](https://developers.google.com/web/fundamentals/), [Mozilla Developer Network](https://developer.mozilla.org/en-US/)
* Icons: [Font Awesome](https://fontawesome.com/)





---

---

# JavaScript

<a href="http://www.fe.up.pt/~arestivo">André Restivo</a>

---

# Index

1. [Introduction](#intro)
1. [Variables](#variables)
1. [Control Structures](#control)
1. [Functions](#functions)
1. [Objects](#objects)
1. [This](#this)
1. [Prototypes](#prototypes)
1. [Classes](#classes)
1. [Arrays](#arrays)
1. [Destructuring](#destructuring)
1. [Map and Set](#map-set)
1. [Error Handling](#error-handling)
1. [Scope](#scope)
1. [Asynchronous Code](#asynchronous)
1. [JSON](#json)

---

# Introduction

---

# JavaScript

  * *JavaScript* is a **dynamic**, **imperative** and **functional** ([ish](https://stackoverflow.com/questions/3962604/is-javascript-a-functional-programming-language)) language.
  * In *JavaScript*, functions are considered **first-class** citizens.
  * It is also **object-oriented**, but **prototype-based** (not class-based).
  * Most commonly used as a **client-side** scripting language (in browsers).
  * But can also be used as a **general purpose** language.

---

# History

  * Originally developed by **Brendan Eich** at **Netscape**.
  * Developed under the name **Mocha** but later named **LiveScript**.
  * Changed name from LiveScript to **JavaScript**, in **1995**, when Netscape added support for Java.
  * Microsoft introduced JavaScript support in Internet Explorer in August **1996** (called JScript).
  * Submitted to **Ecma** International for consideration as an industry-standard in 1996 (**ECMAScript**).
  * Ecma International released the first version of the specification in **1997**.
  * Nowadays, JavaScript is a trademark of the **Oracle** Corporation.
  * But JavaScript is officially managed by the **Mozilla** Foundation.

---

# Console

* Modern browsers all have a *JavaScript* console that can log messages from within web pages.
* It can also inspect variables, evaluate expressions, and just plain experimentation.
* The specifics of how it works vary from browser to browser, but there is a *de facto* set of typically provided features.

* The **console.log(msg)** function outputs a message to the console:
```javascript
console.log('Hello World')
```
* Other debug level are possible: 
  * **console.info(msg)**, **console.warn(msg)** and **console.error(msg)**.
  * Browsers allow filtering messages depending on their level.

---

# Strict Mode

*ECMAScript 5* brought some significant changes. 

To opt-in for those changes, scripts (or functions) must start with:

```javascript
'use strict'
```

Some of those changes:

* **No more** global undeclared variables.
* **No more** declaring variables with **var**.
* Some warnings are now errors.

---

# Automatic Semicolons

Statements are separated by semicolons:

```javascript
console.log(123); console.log('abc');
```

But if a line break separates them:

```javascript
console.log(123);
console.log('abc');
```

The semicolon can be omitted:

```javascript
console.log(123)
console.log('abc')
```

.box_warning[
  This is not always true!

---

# Resources

* Reference:
  * [MDN JavaScript Reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference)
  * [ECMAScript Reference](http://ecma-international.org/ecma-262/5.1/)
  * [MDN DOM Reference](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model)

* Resources:
  * [MDN JavaScript Resources](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
  * [JS Fiddle](http://jsfiddle.net/)

* Tutorials:
  * [The Modern JavaScript Tutorial](http://javascript.info)
  * [JavaScript Style Guide](https://github.com/airbnb/javascript)

---

# Variables

---

# Variables

* JavaScript is a *loosely/weakly* and *dynamically* typed language. 
* That means that:
  * values have types; variables do not.
  * types are checked at runtime.
* Variables are declared using the **let** command.
* Variable names must contain only letters, digits, $, and _ (and not start with a digit).

```javascript
let bar = 10       // bar initialized with a number
bar = 'John Doe'   // bar now has a string
bar = true         // and now a boolean
```

```javascript
let foo = 10, bar  // declaring two variables at once
bar = 'John Doe'   // bar was undefined 
```

---

# Constants

* Constants behave precisely the same way as variables.
* Except they can't be changed.
* Constants are declared using the **const** command.

```javascript
const bar = 10
bar = 20        // TypeError: invalid assignment to const `bar'
```

.box_info[
Always prefer **const**; only use **let** if you need to reassign the variable.

---

# Var

In older scripts, you might find variables declared using **var** instead of **let**.

* They have no block scope (only function scope).
* Are processed when a function starts.
* **And should not be used!**

```javascript
if (true) {
  var bar = '1234'
  console.log(bar)      // 1234
}

console.log(bar)        // 1234
```

```javascript
function foo() {
  bar = '1234'
  console.log(bar)     //1234
  var bar
}
```

---

# Not declaring variables

* Declaring variables in *JavaScript* might seem *optional*, but that is **not the case**.
* When you use a variable without declaring it, that variable will bubble up until it finds a variable declared with the same name.
* If it doesn't, it attaches itself to the *window* or *global* object.
* This might have unforeseen and complex to debug consequences:

```javascript
function foo() {
  bar = 1234
}

let bar = 10
foo()
console.log(bar) // 1234
```

---

# Primitive Data Types

The standard defines the following data types:

  * Number (**double**-precision 64-bit, *e.g.*, 10)
  * String (**text**ual data &mdash; single or double quoted, *e.g.*, 'foo')
  * Boolean (**true** or **false**)
  * BigInt (**numbers** of arbitrary length, *e.g.*, 123456789n)
  * Null (only one possible value: case sensitive **null**)
  * Undefined (has **not** been **assigned** a value; case sensitive **undefined**)

---

# Strings

Strings can be defined equally using single or double quotes:

```javascript
const firstname = 'John'
const lastname = "Doe"
```

We can also use *backticks*. With *backticks*, expressions inside 
*${...}* are evaluated, and the result becomes a part of the string.

```javascript
console.log(`Hello, ${firstname} ${lastname}!`)
// Hello, John Doe!

console.log(`The result is ${1 + 2}`)
// The result is 3
```

---

# The + Operator

The plus (+) operator sums numbers, but if one of the operands is a string, 
it converts the other one into a string and concatenates the two:

```javascript
console.log(11 + 31)     // 42
console.log('11' + 31)   // '1131'
console.log(11 + '31')   // '1131'
console.log('11' + '31') // '1131'
```

---

# Type Conversions

Most of the time, operators and functions automatically convert a value to the right type (type conversion). 

You can still use the *String*, *Number* and *Boolean* functions to manually convert a value:

```javascript
const a = 0
const b = Boolean(a) // false
const c = String(a)  // '0'
const d = String(b)  // 'false'
```

To convert from a string to a number, we can use the **parseInt** and **parseFloat** functions. Don't forget to specify the base:

```javascript
  console.log(parseFloat('123.4')) // 123.4
  console.log(parseInt('123', 10)) // 123
  console.log(parseInt('123', 8))  // 83
  console.log(parseInt('0123'))    // 123 or 83 in some browsers
```

---

# Comparison

When comparing values belonging to different types, they are converted to numbers:

**Examples:**

```javascript
1 == '1'    // 1 == 1 -> true
0 == false  // 0 == 0 -> true
'0' == true // 0 == 1 -> false
'' == false // 0 == 0 -> true
Boolean('0') == false // 1 == 0 -> false
Boolean('0') == true  // 1 == 1 -> true
```

.box_warning[
Primitives are compared by their value; objects (*e.g.*, arrays) are compared by their reference. This means [1, 2, 3] != [1, 2, 3]

---

# Boolean Evaluation

The following values all evaluate to **false**:

  * false
  * undefined
  * null
  * 0
  * NaN (not a number)
  * the empty string

All other values, including objects, evaluate to **true**.

Be careful with the Boolean object:

```javascript
const foo = new Boolean(false)
const bar = Boolean(false)
if (foo) // evaluates to true
if (bar) // evaluates to false
```

---

# Strict Equality

* Strict equality compares two values for equality.  
* Neither value is implicitly converted to some other value before being compared.
* If the values have different types, the values are considered unequal.

```javascript
0 === 0     // true
0 === '0'   // false
0 === false // false
```

Comparing anything with **null** and **undefined** returns false. Comparisons between them have the following results:

```javascript
null === undefined // false
null == undefined  // true
```

---

# Type Of

We can use the **typeof** function to check the type of a variable:

```javascript
console.log(typeof undefined)         // "undefined"
console.log(typeof 0)                 // "number"
console.log(typeof 10n)               // "bigint"
console.log(typeof true)              // "boolean"
console.log(typeof 'foo')             // "string"
console.log(typeof new Boolean(true)) // "object"
console.log(typeof Boolean(true))     // "boolean"
console.log(typeof null)              // "object"
console.log(typeof console.log)       // "function"
```

---

# Nullish Coalescing

A common way to assign a **default value** is to use the **or** operator (||):

```javascript
const bar = foo || some_default_value
```

This works, but it assigns the default value for any **falsy** value.

The nullish coalescing operator (??) returns the second argument if the first is *undefined* or *null*.

```javascript
const bar = foo ?? some_default_value
```

---

# Control Structures

---

# If ... else

* Use the **if** statement to execute a statement if a logical condition is **true**.
* Use the optional **else** clause to execute a statement if the condition is **false**.

```javascript
if (condition) {
  //do domething
} else {
  //something else
}
```

---

# Switch

* A switch statement allows a program to evaluate an expression and 
  attempt to match the expression's value to a case label.
* If a match is found, the program executes the associated statement.

```javascript
switch (expression) {
   case label_1:
      statements_1
      break
   case label_2:
      statements_2
      break
   //...
   default:
      statements_def
      break
}
```

---

# Loops

JavaScript supports the **for**, **do while**, and **while** loop statements:

```javascript
for (let i = 0; i <= 10; i++) {
  console.log(i)
} // 0 1 2 3 4 5 6 7 8 9 10
```

```javascript
let i = 0
do {
   console.log(i)
   i++
} while (i <= 10) // 0 1 2 3 4 5 6 7 8 9 10
```

```javascript
let i = 0
while (i <= 10) {
   console.log(i)
   i++
} // 0 1 2 3 4 5 6 7 8 9 10
```

---

# Ternary Operator

Like in other languages, we can use the conditional ternary operator:

```javascript
const best = value > best ? value : best
```

* This operator takes a condition and two values.
* It returns the first value if the condition is true and the second if it is false.

---

# Break and Continue

* The break statement finishes the current loop prematurely.
* The continue statement finishes the current iteration and continues with the next.

```javascript
for (let i = 0; i < 10; i++) {
  if (i == 8) break
  if (i % 2 == 0) continue
  console.log(i)
} // 1 3 5 7
```

---

# Functions

---

# Defining functions

A function is defined using the **function** keyword.

```javascript
function add(num1, num2) {
  console.log(num1 + num2)
}

add(1, 2) // 3
```

* **Primitive** parameters are passed to functions by **value**.
* **Non-primitive** parameters (objects) are passed by **reference**.

---

# Return

Functions can also return values.

```javascript
function add(num1, num2) {
  return num1 + num2
}

console.log(add(1, 2)) // 3
```

A function with an empty *return* or no *return* at all, returns **undefined**.

---

# Default Values

* If a parameter expected by a function is not passed, it becomes **undefined**.
* Unless we declare a default value for that parameter.
* Default values can be complex expressions and are only calculated when needed.

```javascript
let count = 1

function bar() {
  return count++
}

function foo(var1, var2 = 1234, var3 = bar()) {
  console.log(var1, var2, var3)
}

foo(10, 20, 30) // 10 20 30
foo(10, 20)     // 10 20 1
foo(10)         // 10 1234 2
foo()           // undefined 1234 3
```

---

# Function Expressions

Another way to declare a function is the following:

```javascript
const foo = function() {
  console.log('bar')
}
```

This has the same effect as:

```javascript
function foo() {
  console.log('bar')
}
```

Functions are just another datatype stored in variables. We can even copy them or display them in the console:

```javascript
const bar = foo
bar()
console.log(foo)
```

---

# Functions as Parameters

We can pass functions as parameters to other functions.

```javascript
function foo(i) {
  console.log('bar = ' + i)
}

function executeNTimes(f, n) { // Executes function f, n times
  for (let i = 0; i < n; i++)
    f(i)
}

executeNTimes(foo, 3)   // bar = 0 bar = 1 bar = 2
executeNTimes(foo(), 3) // this is a common mistake
```

---

# Arrow Functions

A more compact way of declaring functions:

```javascript
const foo = function(var1, var2) {
  return var1 + var2
}
```

Is the same as:

```javascript
const foo = (var1, var2) => var1 + var2
```

Using the function from the previous slide:

```javascript
executeNTimes((i) => console.log(i * i), 3)  // 0 1 4
executeNTimes(i => console.log(i * i), 3)    // Even simpler
```

Multi-line arrow functions are also possible using a code-block **{...}**.

---

# Arrow Function Limitations

* Should not be used as methods (no *super* and no *this* binding, more on this later).
* Can not be used as constructors.
* Not ideal to use with *call*, *apply* and *bind* (more on this later).
* Cannot use *yield*.
* Multi-line arrow functions must have a return statement:

```javascript
const sum = (a, b) => {
  const result = a + b
  return result
}
```

---

# Objects

---

# Objects

* JavaScript is designed on a simple **object-based** paradigm.
* An object is a collection of **properties**.
* A property is just an association between a **name** and a **value**.
* A property's value can be a function, in which case the property is known as a **method**.
* JavaScript is a **prototype-based** language and **does not** have a class statement (or does it?).

```javascript
const person = { name: 'John Doe', age: 45 }

person.job = 'Driver'

console.log(person) 
// Object { name: 'John Doe', age: 45, job: 'Driver' }
```

---

# Methods

* Methods are properties of an object that happen to be functions.
* Methods are defined the way normal functions are defined, except that they are assigned as the property of an object.
* You can use the **this** keyword to refer to the current object within a method.

```javascript
const person = 
  { 
    age: 45,
    car: {make: 'Honda', model: 'Civic'},
    print: function() {
      console.log(`${this.name} is ${this.age} years old!`)
    }
  }
person.print() // John Doe is 45 years old!
```

---

# Assigning Methods

We can also assign a method to an object:

```javascript
const person = 
  { name: 'John Doe',
    age: 45,
    car: {make: 'Honda', model: 'Civic'},
  }

person.print = function() {
  console.log(`${this.name} is ${this.age} years old!`)
}

person.print() // John Doe is 45 years old!
```
.box_warning[
  Did we just change a constant???

---

# Constant Objects

Like other types, constant objects cannot be reassigned:

```javascript
const person = { name: 'John Doe' }
person = { name: 'Jane Doe' } // Error!
```

But we can change what's inside them:

```javascript
const person = { name: 'John Doe' }
person.name = 'Jane Doe'
```

---

# Setter and Getters

*Setter* and *getters*, accessor properties, are functions that execute on 
getting and setting a value, but behave like regular properties.

```javascript
const person = {
    firstName: 'John',
    lastName: 'Doe',
    get fullName() {
      return `${this.firstName} ${this.lastName}`
    },
    set fullName (name) {
      const words = name.split(' ')
      this.firstName = words[0]
      this.lastName = words[1]
    }
}

person.fullName = 'John Doe'
console.log(person.firstName)  // John
console.log(person.lastName)   // Doe
console.log(person.fullName)   // John Doe

person.firstName = 'Jane'
console.log(person.fullName)   // Jane Doe
```

---

# For ... in

The **for ... in** statement iterates over all properties of an object.

```javascript
const person = { name: 'John Doe', age: 45 }

for (let key in person)
  console.log(`${key} = ${person[key]}`)

// name = John Doe
// age = 45
```

---

# Objects as Arrays

* Properties of objects can be accessed or set using a bracket notation.
* Objects can be seen as **associative arrays** since each property is 
  associated with a string value that can be used to access it.

```javascript
const person = {}

person['name'] = "John Doe"
person['age'] = 45

console.log(person.age)    // 45
console.log(person['age']) // 45
```

---

# Almost Everything is an Object

* In JavaScript, almost everything is an object.
* Even primitive types, except *null* and *undefined*, are temporarily *casted* into objects when treated as such.

```javascript
const num = 10
console.log(num.toExponential()) // 1e+1

const name = "John Doe"
console.log(name.substring(0,4)) // John
```

In this example, the primitive types are *cast* temporarily into Number and String objects and discarded afterward.

---

# Even Functions are Objects

They really are:

```javascript
function foo() { console.log("Hello") }
const bar = function() { console.log("Hello") }
const baz = () => console.log("Hello")

foo(); bar(); baz() // Hello Hello Hello

foo.info = "This function says hello!"
bar.info = "This function says hello!"
baz.info = "This function says hello!"

console.log(foo.info)  // This function says hello!

foo.goodBye = function() { console.log("Goodbye") }
foo.goodBye() //Goodbye
```

---

# This

---

# This

In *JavaScript*, the **this** keyword (current context) behaves unlike in almost any other language.

* In the global execution context, **this** refers to the *global object*:
  * Or *window* if in a browser.
* Inside a function it depends on how the function was called:
  * Simple function call (**undefined** if in strict mode).
  * Arrow functions (**retain** the enclosing context).
  * Using *apply* or *call* (*this* is the **first** argument).
  * Object method (the object the method was **called** from).
  * Browser Events (the object that **fired** the event, more on this later).

---

# This in Functions

Using **this** in simple functions:

```javascript
'use strict'

function bar(var1, var2) {
  console.log(var1)
  console.log(var2)
  console.log(this)
}

bar(10, 20)                 // 10 20 undefined
bar.call('foo', 10, 20)     // 10 20 foo
bar.apply('foo', [10, 20])  // 10 20 foo
```

* **Call** and **apply** are alternative ways to call functions 
  that allow us to change the calling context (*this*).
* Both receive the **context** as the **first** argument.
* The remaining parameters are sent as **regular parameters** in *call* and as an **array** in *apply*.

---

# Bind

The *bind* method allows us to fixate the *this* (or context of a function):

It receives a *context*, and returns a new function where *this* is **that** *context*.

```javascript
'use strict'

function bar(var1, var2) {
  console.log(var1)
  console.log(var2)
  console.log(this)
}
bar(1, 2) // 1 2 undefined

const foo = bar.bind(3)
foo(1, 2) // 1 2 3
```

It can also be used to bind **parameters**. In this case it returns a function with only one parameter:

```javascript
const baz = bar.bind('this', 'first')
baz('second')    // 'first' 'second' 'this'
```

---

# This in Methods

In methods, *this* contains the object the method was called from:

```javascript
const foo = {}

foo.bar = function() { console.log(this) }
foo.baz = () => console.log(this)

foo.bar()     // Object { bar: f, baz: f }
foo.baz()     // Window or Global

const bar = foo.bar
const baz = foo.baz

bar()         // Window or Global
baz()         // Window or Global
```

Arrow functions **do not have** a *this*, instead, they inherit it from the parent scope (lexical scoping).

---

# Prototypes

---

# Constructor Functions

Functions (but not *arrow* functions) can be used to create new objects using the **new** keyword.

```javascript
function Person(name, age) {
  this.name = name
  this.age = age
  this.print = function() {
    console.log(`${this.name} is ${this.age} years old!`)
  }
}

const john = new Person("John Doe", 45)
john.print() // John Doe is 45 years old!
```

.box_info[
Cool! So, how does this work?

---

# Prototype

* *JavaScript* functions have an internal <code>.prototype</code> property.
* The **new** operator, when used on a function creates a **new object**, and:
  - Sets the new object's **internal**, hidden, <code>[[Prototype]]</code> property to the function's <code>.prototype</code>.
  - The function is called with **this** bound to the new object.
  - Returns the object created, unless the function returns something else.

```javascript
function Person(name, age) {
  this.name = name // this receives a nearly empty object
  this.age = age   // based on the function's prototype
  this.print = function() {  
    console.log(`${this.name} is ${this.age} years old!`) 
  }
}

const john = new Person("John Doe", 45)
john.print() // John Doe is 45 years old!
```

---

# Changing the Prototype

We can inspect and change the prototype of a function:

```javascript
function Person(name) {
  this.name = name
}

console.log(Person.prototype)       // {constructor: f}

const john = new Person("John Doe")
Person.age = 45                     // Only changes the Person function/object
                                    // not its prototype.
const jane = new Person("Jane Doe")
console.log(jane.age)               // undefined

Person.prototype.age = 45           // Changes the prototype.

const mary = new Person("Mary Doe") // All objects constructed using the
console.log(mary.age)  //45            person constructor now have an age.
console.log(jane.age)  //45            Even if created before the change.
```

.box_info[
What? How does THIS work?

---

# Prototype of Objects

Every object in JavaScript has an **internal** <code>[[Prototype]]</code> (also informally called the object's prototype), which is typically set to the <code>.prototype</code> property of the constructor function that created it.

This **internal** prototype can be accessed using <code>Object.getPrototypeOf(obj)</code> and modified using <code>Object.setPrototypeOf(obj, proto)</code>.

```javascript
function Person(name) {
  this.name = name
}

const john = new Person('John Doe')

console.log(Object.getPrototypeOf(john) === Person.prototype) 
// returns true

Object.setPrototypeOf(john, {}) 
// changes the prototype of john to {}
```

---

# The Prototype Chain

- When we attempt to access a property from an object and it’s missing, JavaScript will look for the property in the object's <code>.prototype</code>. 
- If it’s **not found** there, JavaScript will then check the prototype of that prototype, continuing up the **prototype chain** until it reaches **null**. 
- If the property is **not found** by the time it reaches **null**, the result is **undefined**.

```javascript
function Person(name) {
  this.name = name
}

const john = new Person("John")

Person.prototype.age = 45
console.log(Object.getPrototypeOf(john))// Object { age: 45, ... }
console.log(john.age)                   // 45

Object.setPrototypeOf(john, {})         // Changes the prototype
console.log(john.age)                   // undefined
```

---

# Prototype Inheritance

Inheritance can be emulated with prototypes by changing the prototype chain.

```javascript
function Person(name) { this.name = name }

Person.prototype.print = function() { console.log(this.name) }

function Worker(name, job) {
  this.job = job
  Person.call(this, name)  // super constructor with this
}

Worker.prototype = new Person
Worker.prototype.print =
  function() { console.log(`${this.name} is a ${this.job}`) }

const mary = new Person("Mary")
mary.print() // Mary

const john = new Worker("John", "Builder")
john.print() // John is a Builder
```

---

# Classes

---

# Classes

* *Prototype-based* objects have many advantages (and disadvantages) over *class-based* objects.

* For example, we can do complicated meta-programming by manipulating the prototype chain.

* The original decision to use prototypes instead of classes in JavaScript as to do mainly with performance.

But why choose **one** when we can have **both**?

```javascript
class Person {
  constructor(name) {
    this.name = name
  }

  print() { 
    console.log(this.name) 
  }
}
```

---

# Syntatic Sugar

The *class* keyword is ([almost](https://javascript.info/class#not-just-a-syntactic-sugar)) just *syntactic sugar* for *prototype-based* objects:

```javascript
class Person {
  constructor(name) { this.name = name }
  print() { console.log(this.name) }
}
```

What's happening:

- A function named Person is being created. 
- The function code is taken from the constructor method.
- Class methods, such as *print*, are stored in **Person.prototype**.

We can then use the **new** operator on that function just as we did before:

```javascript
const john = new Person('John Doe')
```

---

# Classes and the Prototype Chain

Inheritance is also just prototype chain manipulation:

```javascript
class Person {
  constructor(name) { this.name = name }
  print() { console.log(this.name) }
}

class Worker extends Person {
  constructor(name, job) {
    super(name)
    this.job = job
  }
  print() { console.log(`${this.name} is a ${this.job}`) }  
}

const john = new Worker("John", "Builder")
console.log(Object.getPrototypeOf(Worker) === Person) 
console.log(Object.getPrototypeOf(john) === Worker.prototype) 
// both return true
```

---

# Classes Basic Syntax

* Classes can have **fields**, **methods**, and a single **constructor**.
* The *this* keyword refers to the object that has called the method.

```javascript
class Person {
  name     // undefined field
  age = 45 // a field initialized to a value

  constructor(name) { this.name = name } // a single constructor

  print() { console.log(this.name) }     // a method
}
```

The **new** operator creates a new instance of a class.

```javascript
const john = new Person('John Doe')
```

---

# Inheritance

Classes can extend other classes using the **extends** keyword.

```javascript
class Person {
  constructor(name) { this.name = name }
  print() { console.log(`My name is ${this.name}`) }
}

class Worker extends Person {
  constructor(name, job) {
    super(name)
    this.job = job
  }
  print() { 
    super.print()
    console.log(`And I'm a ${this.job}`) 
  }  
}
```
The **super** keyword allows calling the super-class constructor and methods.

---

# Static

The static keyword allows declaring fields and methods as being part of the class (not the object).

* They must be accessed using the class and not an object.
* Inside a **static** method, **this** refers to the class.

```javascript
class Person {
  static maxAge = 100

  constructor(name, age) { 
    this.name = name 
    this.age = age < Person.maxAge ? age : Person.maxAge
  }

  static compare(p1, p2) { return p1.name === p2.name && p1.age === p2.age }
}

const john1 = new Person('John Doe', 120)
const john2 = new Person('John Doe', 100)

console.log(Person.compare(john1, john2)) // true
console.log(john1.maxAge, Person.maxAge) // undefined 100
```

---

# Private Fields and Methods 

* In older versions of JavaScript, there was no *language-level* way to create *private* or *protected* fields.
* However, there was a *well-established* convention that fields and methods starting with an **underscore** *should* not be accessed directly.
* We could even use this convention, along with getters and setters, to create a read-only property:

```javascript
class Person {
  constructor(name, age) { 
    this.name = name 
    this._age = age
  }

  get age() { return this._age }
}

const john = new Person('John Doe', 45)

console.log(john.age) // 45
john.age = 50         // no error, but no effect
console.log(john.age) // 45
```

---

# Private Fields and Methods

* In more recent versions, there is a *language-level* way to create **private** fields and methods.
* Private fields/methods are marked with a **hash** sign.

```javascript
class Person {
  name
  #age

  constructor(name, age) { 
    this.name = name 
    this.#age = age
  }

  #compare(other) { return this.name === other.name && this.age === other.age }
}

const john1 = new Person('John Doe', 45)
const john2 = new Person('John Doe', 55)

console.log(john1.age)             // undefined
console.log(john1.#age)            // error
console.log(john1['#age'])         // undefined
console.log(john1.#compare(john2)) // error
```

---

# Instance Of

You can use the **instanceof** operator to check if an object belongs to a specific class:

```javascript
class Person {
  constructor(name) { this.name = name }
}

class Worker extends Person {
  constructor(name, job) {
    super(name)
    this.job = job
  }
}

const john = new Person('John Doe')
const jane = new Worker('Jane Doe', 'Builder')

console.log(john instanceof Person) // true
console.log(john instanceof Worker) // false
console.log(jane instanceof Person) // true
console.log(jane instanceof Worker) // true
```

---

# Arrays

---

# Arrays

  * Arrays are **list-like objects** whose **prototype** has methods to perform **traversal** (<code>.forEach</code>...) and **mutation**(<code>push</code>...) operations.
  * *JavaScript* arrays are zero-indexed
  * Arrays can be initialized using a bracket ([]) notation:

```javascript
const years = [1990, 1991, 1992, 1993]
console.log(years[0])     // 1990
years.info = "Nice array" // Arrays are objects
console.log(years.info)   // Nice array
```

Array elements are object properties, but they cannot be accessed using the **dot** notation because their names are invalid.

```javascript
const years = [1990, 1991, 1992, 1993]
console.log(years[0]) // 1990
console.log(years.0)  // Syntax error
```

---

# Array Looping

You can use a **for** loop to iterate over array elements:

```javascript
const years = [1990, 1991, 1992, 1993]
for (let i = 0; i < years.length; i++)
  console.log(years[i])
```

Or you can use a **for ... of** loop:

```javascript
const years = [1990, 1991, 1992, 1993]
for (const year of years)
  console.log(year)
```

.box_warning[
Do not use a **for ... in** loop! Those are for object properties.

---

# Array Prototype

These are some of the methods defined by the [Array prototype](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/prototype):

* Properties: prototype, length
* Mutators: fill, pop, push, reverse, shift, sort, splice, unshift
* Accessor: concat, contains, join, slice, indexOf, lastIndexOf
* Iterator: forEach, entries, every, some, filter

Some examples:

```javascript
const years = [1990, 1991, 1992, 1993]
years.push(1994)
console.log(years.length)   // 5

years.reverse()
console.log(years)          // [1994, 1993, 1992, 1991, 1990]

let sum = 0
years.forEach(e => sum += e)
console.log(sum)            // 9960

years.every(e => e >= 1990) // true
years.some(e => e % 2 == 0) // true
```

---

# Playing with the Array Prototype

We can add methods and properties to all arrays by changing the Array prototype:

```javascript
const years = [1990, 1991, 1992, 1993]

Array.prototype.print = function() {
  console.log("This array has length " + this.length)
}

years.print() // This array has length 4
```

---

# forEach()

The [forEach()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach) method **executes** a function once **for each** array element:

```javascript
const numbers = [4, 8, 15, 16, 23, 42]
numbers.forEach(function(value, index){
    console.log('Element #' + index + ' is ' + value)
})
```

The result would be:

```html
Element #0 is 4
Element #1 is 8
Element #2 is 15
Element #3 is 16
Element #4 is 23
Element #5 is 42
```

---

# filter()

The [filter()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter) method returns a **new array** with all elements that **pass a test**.

```javascript
const numbers = [4, 8, 15, 16, 23, 42]
const even = numbers.filter(function(n) { return n % 2 == 0 })
console.log(even) // [ 4, 8, 16, 42 ]
```

Or using arrow functions:

```javascript
const numbers = [4, 8, 15, 16, 23, 42]
const even = numbers.filter(n => n % 2 == 0)
console.log(even) // [ 4, 8, 16, 42 ]
```

An alternative would be:

```javascript
const numbers = [4, 8, 15, 16, 23, 42]
const even = []
for (let i = 0; i < numbers.length; i++)
  if (numbers[i] % 2 == 0) even.push(numbers[i])
console.log(even) // [ 4, 8, 16, 42 ]
```

---

# map()

The [map()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map) method creates a **new array** by **applying a function** to every element in the original array.

```javascript
const numbers = [4, 8, 15, 16, 23, 42]
const doubled = numbers.map(function(n) { return n * 2 })
console.log(doubled) // 8, 16, 30, 32, 46, 84
```

Or using **arrow functions**:

```javascript
const numbers = [4, 8, 15, 16, 23, 42]
const doubled = numbers.map(n => n * 2)
console.log(doubled) // 8, 16, 30, 32, 46, 84
```

---

# Generic use of map()

The [map()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map) method can be used on **other types** of *array-like* objects:

```javascript
const ascii = Array.prototype.map.call('John', l => l.charCodeAt(0))
console.log(ascii) // [74, 111, 104, 110]
```

Simpler:

```javascript
const ascii = [].map.call('John', letter => letter.charCodeAt(0))
console.log(ascii) // [74, 111, 104, 110]
```

A more useful example:

```javascript
const inputs = document.querySelectorAll('input[type=number]')
const values = [].map.call(inputs, input => input.value)
console.log(values) // an array with all the number input values
```

---

# reduce()

The [reduce()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce) method **applies a function** to each element in the array:

The result is passed to the next iteration as an **accumulator** (starting at 0 by default). <small>The objective is to **reduce** the array to a **single value** in the end.</small>

```javascript
const numbers = [4, 8, 15, 16, 23, 42]
const total = numbers.reduce(function(accumulator, number) {
  return accumulator + number
})
console.log(total) // 108
```

Or with **arrow functions**:

```javascript
[4, 8, 15, 16, 23, 42].reduce( (acc, num) => acc + num ) // 108
```

We can **initialize** the accumulator by adding a second parameter:

```javascript
[4, 8, 15, 16, 23, 42].reduce( (acc, num) => acc + num, 10 ) // 118
```

---

# Spread Operator

The [spread operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax) allows an iterable, such as an array or string, to be **expanded** in places where zero or more arguments are expected:

```javascript
function sum(x, y, z) {
  return x + y + z
}

const numbers = [1, 2, 3]

console.log( sum(...numbers) ) // 6
```

Other example:

```javascript
function sum(...args) { // sum any number of args
  let sum = 0
  for (let i = 0; i < args.length; i++)
    sum += args[i]
  return sum
}
console.log( sum(1, 2, 3) ) // 6
```

---

# Destructuring

---

# Array Destructuring

Destructuring assignment allows us to split an array (or any iterable) into separate variables:

```javascript
const names = ['John', 'Doe']
const [first, last] = names
console.log(first) // John
```

It also works with fields (first, we split a string into an array):

```javascript
const person = {}
[person.first, person.last] = 'John Doe'.split(' ') 
console.log(person) // {first: 'John', last: 'Doe'}
```

Swap and [much more](https://javascript.info/destructuring-assignment):

```javascript
let a = 10, b = 5
[b, a] = [a, b]
console.log(a, b) // 5 10
```

---

# The Rest

After all elements are assigned, the remaining (or "the rest") can be assigned too, using the *spread operator* (...):

```javascript
const numbers = [1, 2, 3, 5, 8]
const [a, b, ...r] = numbers
console.log(a)  // 1
console.log(b)  // 2
console.log(r)  // [3, 5, 8]
```

---

# Destructuring Objects

Destructuring also works with objects:

```javascript
const person = { first: 'John', last: 'Doe', age: 45 }
const {first, last} = person
console.log(first) // John
```

The order does not matter, and we can assign to variables with different names:

```javascript
const person = { first: 'John', last: 'Doe', age: 45 }
const {age: a, first: f, last: l} = person
console.log(a) // 45
console.log(f) // John
console.log(l) // Doe
```

---

# Destructuring in Functions

We can use destructuring when defining functions:

```javascript
function sum(...numbers) {
  let sum = 0
  for (const n of numbers)
    sum += n
  return sum
}

console.log(sum(1, 2, 3)) // 6
```

And even with objects:

```javascript
function print({first, last}) {
  console.log(`${first} ${last}`)
}

print({first: 'John', last: 'Doe', age: 45}) // John Doe
```

---

# Map and Set

---

# Map

* A *Map* is a collection of key-value pairs that allows keys of any type (even objects).
* You can **get**, **set**, and **delete** values from a Map.
* You can also check (**has**) if a key exists in the Map.
* And **clear** all values.  

```javascript
const map = new Map()

map.set('name', 'John Doe')
map.set('age', 45)
map.set(10, 'it is a number')

map.delete(10)

console.log(map.has('name'))  // true
console.log(map.has(10))      // false
console.log(map.get('age'))   // 45

map.clear()
```

---

# Map Looping

There are three ways to access all elements of a Map:

- **.keys()** – returns an iterable for keys
- **.values()** – returns an iterable for values
- **.entries()** – returns an iterable for entries

The **.entries()** method is the *default* when using **for ... of** loops:

```javascript
const map = new Map([['name', 'John Doe'], ['age', 45]])
for (const [key, value] of map) 
  console.log(`${key} = ${value}`)
```

We can also initialize a *Map* with an *iterable* of *key-value* pairs (like a nested *Array*).

---

# Set

* A *Set* is a collection of values (of any type) that cannot contain repeated values.
* You can **add**, and **delete** values from a Set.
* You can also check (**has**) if a value exists in the Set.
* And **clear** all values.  

```javascript
const set = new Set()

set.add('John Doe')
set.add('Jane Doe')

console.log(set.size) // 2
set.add('John Doe')
console.log(set.size) // still 2

set.delete('Jane Doe')

console.log(set.has('John Doe'))  // true
console.log(set.has('Jane Doe'))  // false
```

---

# Set Looping

We can loop over the elements in a Set using **for ... of** loops:

```javascript
const set = new Map(['John Doe', 'Jane Doe'])
for (const element of set) 
  console.log(element)
```

We can also initialize a *Set* with an *Array*.

---

# Error Handling

---

# Try ... Catch ... Finally

* The **try** block contains statements to *try*.

* The **catch** block contains code to deal with any exception thrown inside the **try** block.

* The **finally** block executes regardless of whether an exception is thrown. Useful for cleanup operations (e.g., closing a connection).

```javascript
try {
  doesThisFunctionExist() // it doesn't
  console.log('I will not print')
} catch (e) {
  console.log(e)          // prints the not defined error   
  throw new Error('burp') // uncaught exception
} finally {
  console.log('I always print')
}

console.log('I might not print')
```

---

# Throw

You can throw exceptions using the **throw** statement. You can throw any expression.

```javascript
try {
  throw 'Whoops!'
} catch (e) {
  console.error(`e`) // Whoops!
}```

If you are throwing your own exceptions, to take advantage of the name and message properties, you can use the **Error** constructor.

```javascript
try {
  throw new Error('Whoops!')
} catch (e) {
  console.error(`${e.name}: ${e.message}`) // Error: Whoops!
}
```

Or extend the **Error** class.

---

# Dealing with different Exceptions

To distinguish between different types of exceptions, we can use **instanceof**:

```javascript
try {
  // code to try
}
catch (e) {
  if (e instanceof DatabaseError) {
    // statements to handle DatabaseError exceptions
  } 
  if (e instanceof SomethingElseError) {
    // statements to handle SomethingElseError exceptions
  } 
}
```

---

# Scope

---

# Code Blocks

If a variable is defined inside a **code block**, it is only visible inside that code block:

```javascript
{
  const name = 'John Doe'
  console.log(name)       // John Doe
}
console.log(name)         // undefined
```

We can use this to create **nested functions** (functions are like any other type):

```javascript
function equal(a, b) {
  function difference(a, b) { return b - a }
  return difference(a, b) === 0
}
console.log(equal(10, 10)) // true
difference(10, 10)         // error 
```

---

# Lexical Environments

When we have nested blocks, each one has a **Lexical Environment** 
where local variables are stored.

Each one of these environments has a **pointer** to the 
lexical environment where it was created.

```javascript
function equal(a, b) {
  function difference(a, b) { return b - a }
  return difference(a, b) === 0
}
console.log(equal(10, 10)) // true
difference(10, 10)         // error 
```

Like this: **difference** → **equal** → *global*

---

# Scope

* When we reference a variable, it is **first** searched in
  the current lexical environment. 
* If it isn't found, it is searched in the **outer** lexical 
  environment. This goes on until the global environment is reached.
* That's why using variables that have not been declared
  is a **bad idea**. They will bubble up until the global lexical
  environment and become **global variables**.

---

# Closures

When a function is created, it **retains** the lexical environment in which it was **created**.

That's why this code works:

```javascript
function createCounter() {
  let counter = 0
  return function() {
    return ++counter
  }
}

const counter = createCounter()
console.log(counter()) // 1
console.log(counter()) // 2
console.log(counter()) // 3
```

A **closure** is the combination of a function bundled together with its surrounding lexical environment.

---

# Closures

A **new closure** is created everytime a function is created:

```javascript
function createCounter() {
  let counter = 0
  return function() {
    return ++counter
  }
}

const counter1 = createCounter()
const counter2 = createCounter()

console.log(counter1()) // 1
console.log(counter1()) // 2
console.log(counter2()) // 1
console.log(counter1()) // 3
console.log(counter2()) // 2
```

---

# Asynchronous Code
## Callbacks and Promises

---

# JavaScript Engines

* JavaScript code is executed by a **JavaScript Engine**.
* Some notable examples: [V8](https://v8.dev/) (Chrome, Node.js), [SpiderMonkey](https://spidermonkey.dev/) (Firefox), and [JavaScriptCore](https://docs.webkit.org/Deep%20Dive/JSC/JavaScriptCore.html) Safari.
* They provide a [heap](https://en.wikipedia.org/wiki/Memory_management), a single [call stack](https://en.wikipedia.org/wiki/Call_stack), and a way to run JavaScript code. 

However:

* JavaScript is a **single-threaded** language!<br><small>An *engine* does not provide a way to start new threads.</small>
* There is also no way to do input/output.<br><small>e.g., networking, storage, graphics.</small>

.box_warning[
  So how can we get asynchronous code?

---

# JavaScript Environments

* **JavaScript Runtime Environment**s provide the necessary APIs to do I/O.<br>
  <small>For example, both Chrome and Node.js use the same engine (V8) but provide very **different** environments.</small>
* These environments also allow us to schedule **asynchronous** actions (*e.g.*, timers, events, network).<br>
  <small>Actions that are independent of the main program flow.</small>
* These actions run in **separate** and **independent** <a href="https://en.wikipedia.org/wiki/Thread_(computing)">threads</a>. 
* When they finish, they put a [callback](https://en.wikipedia.org/wiki/Callback_(computer_programming%29) function on an *event queue*, waiting to be executed.

.smaller[
![](assets/javascript/event-loop.svg)

---

# The Event Loop

Consider the following code where **readFile** is an **asynchronous** function provided by some *runtime environment*:

```javascript
const path = '/some/large/file/we/want/to/read.txt'

readFile(path, function(error, content) {
  if (error) handleError(error) // if there is an error, we handle it
  else console.log(content)     // when the file is read, this is executed
})
```

* The **readFile** function asks the *environment* to read a file.<br><small>The environment returns imediately and starts reading the file in a separate process.</small>
* When the *environment* finishes reading the file, the *callback* function is placed in an *event queue*.
* Tasks in this *queue* are executed only when the *call stack* becomes empty.<br><small>In a FIFO order.</small>

.box_info[The **event loop** is an endless loop where the JavaScript *engine* **waits** for tasks, **executes** them, and then **waits** for more tasks.

---

# Callback Hell

What happens if we need to read a series of files, one after the other?

We will end up with code like this:

```javascript
readFile('file1.txt', function(error, content1) {
  if (error) handleError(error)
  else readFile('file2.txt', function(error, content2) {
    if (error) handleError(error)
    else readFile('file3.txt', function(error, content3) {
      if (error) handleError(error)
      else readFile('file4.txt', function(error, content4) {
        if (error) handleError(error)
        else console.log(content1, content2, content3, content4)
      })
    })
  })
})
```

This is called *callback hell* or the *pyramid of doom*!

---

# Why don't we use synchronous code?

Imagine we had a different version of the **readFile** function that worked **synchronously**:

```javascript
const content1 = readFileSync('file1.txt')
const content2 = readFileSync('file2.txt')
const content3 = readFileSync('file3.txt')
const content4 = readFileSync('file4.txt')
```

* This would be much nicer, but JavaScript is **single-threaded**. 
* If these operations take a lot of time, the code will **hang** for the whole duration.

---

# Promises

Promises solve this problem in a very elegant way.

* A promise represents the **eventual result** of an **asynchronous** operation.
* A promise may be in one of 3 possible states: **fulfilled**, **rejected**, or **pending**.
* A Promise is an *object* that takes a **function** with two parameters, functions **resolve** and **reject**:

```javascript
const promise = new Promise((resolve, reject) => {
  readFile('file.txt', (err, data) => {
    if (err) reject(err)
    else resolve(data)
  })
})
```

---

# Consuming

When the *promise* *resolves* or is *rejected*, we can use **.then** and **.catch** to consume it:

```javascript
promise.then(function(content) {
  console.log(content)
}).catch(function(error) {
  handleError(error)
})
```

* <code>.then(result => {...})</code> registers a function to be called when the promise is resolved.
* <code>.catch(error => {...})</code> registers a function to be called when the promise is rejected.

This might not seem much better, but *promises* still have some tricks left!

---

# Returning Promises

The idea behind *promises* is that **instead** of using *callbacks* to transform *synchronous* into *asynchronous* code, *asynchronous* functions should return *promises* instead: 

```javascript
function promiseFile(filename) {
  return new Promise((resolve, reject) => {
    readFile(filename, (err, data) => {
      if (err) reject(err)
      else resolve(data)
    })
  })
}
```

This could then be used like this:

```javascript
promiseFile('file.txt')
  .then(content => console.log(content))
  .catch(error => console.error(error))
```

---

# Promise Chaining

If we return a *promise* from a **.then** handler, we can chain *promises*:

```javascript
promiseFile('file1.txt')
  .then(content => {
    console.log(content)
    return promiseFile('file2.txt')
  })
  .then(content => {
    console.log(content)
    return promiseFile('file3.txt')
  })
  .then(console.log)    // this is not magic!
  .catch(console.error) // one catch for all the errors"
```

* In fact, **.then** and **.catch** handlers always return *promises*.
* If the code inside them returns something else, the result is wrapped in an automatically fulfilled *promise*.
* This simplifies *promise chaining* (no more *callback hell*). 

---

# Error Handling

Promises have an implicit **try ... catch** block around their code.

So, if **readFileSync** throws an error, we don't even need to call **reject**:

```javascript
function promiseFile(filename) {
  return new Promise(function(resolve, reject)) {
    const content = readFileSync('file.txt') // throws an error if it fails
    resolve(content)
  }
}
```

It also happens in promise handlers (**.then** and **.catch**). 

If we throw inside a **.then** handler, the control jumps to the nearest **.catch**.

```javascript
promiseFile('file1.txt')
  .then(console.log)
  .catch(console.error)                // error reading file1.text
  .then(_ => promiseFile('file2.txt')) // needs to be a function
  .then(console.log)
  .catch(console.error)                // error reading file2.text
  .then(_ => promiseFile('file3.txt'))
  .then(console.log)
  .catch(console.error)                // error reading file3.text
```

---

# Promise.all

An easy way to run several *promises* in parallel and **wait** for them **all**:

```javascript
Promise.all([promiseFile('file1.txt'), 
             promiseFile('file2.txt'), 
             promiseFile('file3.txt')])
  .then(([c1, c2, c3]) => console.log(c1, c2, c3))
  .catch(console.error)
```

* **Promise.all** receives an array of *promises*, and returns a single *promise* that:
  * **resolves** when all input *promises* have resolved, producing an array of their results, in the same order;
  * **rejects** immediately if any *promise* rejects, with the reason of the **first rejection**.
* The **.then** handler is called when they all resolve.
* If any of them *throw* an *error* (or call *reject*), then **.catch** is called.

We are using [destructuring](#destructuring) to receive all the results in separate variables.

---

# Async

When we add the **async** keyword before a function declaration then that function always returns a promise:

```javascript
async function getName() {
  return 'John Doe'
}
```

So this would be possible:

```javascript
getName().then(console.log) // John Doe
```

And this would be our read function:

```javascript
async function promiseFile(filename) {
  return new Promise((resolve, reject) => {
    readFile(filename, (err, data) => {
      if (err) reject(err) else resolve(data)
    })
  })
}
```

---

# Await

The **await** keyword instructs *JavaScript* to pause the execution of an **async** function 
until the awaited *promise* settles (either fulfilled or rejected), and then resumes execution 
with the result:

* **await** only works inside *async* functions.
* **await** suspends the current function without blocking the main thread. It leverages the event loop: once the Promise settles, the function is resumed by placing its continuation into the event queue. This way, no CPU resources are wasted.

It's just a more elegant way to use **sequential promises**:

```javascript
async function fileLength(filename) {
  const contents = await readFile(filename)
  return contents.length
}
```

If an error is thrown, the *promise* returned by the *async* function is **rejected**.

---

# Async/Await

Putting it all together, we can write:

```javascript
async function foo() {
  const c1 = await promiseFile('file1.txt')
  const c2 = await promiseFile('file2.txt')
  const c3 = await promiseFile('file3.txt')
  console.log(c1, c2, c3)
}

foo().catch(console.error)
```

And we get *synchronous-like* code that behaves in a **non-blocking** manner. 

---
# JSON

---

# JSON

* JSON (**J**ava**S**cript **O**bject **N**otation) is a *lightweight data-interchange format*. <small>Some alternatives are [YAML](https://yaml.org/) and [TOML](https://toml.io/en/).</small>
* It is easy for humans to **read** and **write**.
* It is easy for machines to **parse** and **generate**.

```javascript
const posts = [
  {
   "id":"1",
   "title":"Mauris...",
   "introduction":"Sed eu...",
   "fulltext":"Donec feugiat..."
  }, {
   "id":"2",
   "title":"Etiam efficitur...",
   "introduction":"Cum sociis ...",
   "fulltext":"Donec feugiat..."
  }

```

---

# JSON

The **JSON.stringify** and **JSON.parse** functions can be used to encode from and to JSON easily.

```javascript
  const encoded = JSON.stringify(posts)  // return a JSON string
  const decoded = JSON.parse(encoded)    // same content as posts
```





---

---

template:inverse
# JavaScript / DOM
<a href="http://www.fe.up.pt/~arestivo">André Restivo</a>

---

name:index
# Index

1. [Introduction](#intro)
1. [Elements](#elements)
1. [Traversing](#traversing)
1. [Events](#events)
1. [Ajax](#ajax)
1. [Timers](#timers)
1. [Advanced](#advanced)

---

# Introduction

---

# DOM

* The **Document Object Model** (DOM) is a fully object-oriented representation of a web page as a logical tree of *nodes*.

* It allow programmatic access to the tree, allowing programs to **read** and **change** the document **structure**, **style** and **content**.

* Nodes can also have event handlers attached to them. Once an event is triggered, the event handlers get executed.

* It can be manipulated from the browser using **JavaScript**.

---
# Document

The [Document](https://developer.mozilla.org/en/docs/Web/API/Document) object represents an HTML document.

You can access the current document in *JavaScript* using the **global** variable **document**.

Some Document **properties**:

  * [URL](https://developer.mozilla.org/en-US/docs/Web/API/Document/URL) &ndash; Read-only location of the document.
  * [title](https://developer.mozilla.org/en-US/docs/Web/API/Document/title) &ndash; The document title.
  * [location](https://developer.mozilla.org/en-US/docs/Web/API/Document/location) &ndash; A [Location](https://developer.mozilla.org/en-US/docs/Web/API/Location) object that can be assigned in order to navigate to another document.

```javascript
document.location.assign('https://www.google.com/')
```

Another **global** variable represents the browser called [Window](https://developer.mozilla.org/en-US/docs/Web/API/Window).

---

# Location

A [Location](https://developer.mozilla.org/en-US/docs/Web/API/Location) allows us to separate the URL into its many components.

If the current URL is:

```url
https://www.example.com:8080/path?key=value#somewhere
```

Then:

```javascript
console.log(document.location.protocol)    // https:
console.log(document.location.host)        // www.example.com:8080
console.log(document.location.hostname)    // www.example.com
console.log(document.location.port ?? 80)  // 8080
console.log(document.location.pathname)    // /path
console.log(document.location.search)      // ?key=vale
console.log(document.location.hash)        // #somewhere
```

---

# DOM UML Diagram

A **partial** representation of the DOM:

![](assets/javascript-dom/uml.svg)

---

# Script Element

The HTML [&lt;script&gt;](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script) element is used to associate *JavaScript* code with an *HTML* page (either **embedded** or using a **reference** to a separate document containing the code):

```html
<html>
  <head>
    <script src="...url of javascript script..."></script>
    <script>...javascript code goes here...</script>
  </head>
</html>
```

.box_warning[
Either way, the &lt;script&gt; tag must be closed.

---

# Defer and Async

By default, when the browser encounters a [&lt;script&gt;](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script) element, it **pauses** rendering HTML, **fetches** the JavaScript script (if not embedded), and **runs** the corresponding code.

However, as most JavaScript code interacts with the page's HTML, normally we need to have all HTML code parsed and rendered before running it. A common way to solve this problem was to only use the [&lt;script&gt;](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script) in the end of the HTML document.

A more modern way is to use one of two special attributes of the [&lt;script&gt;](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script) tag: **defer** and **async**. 

```html
<script src="...url of javascript script..." defer></script>
<script src="...url of javascript script..." async></script>
```

Both don't pause the HTML loading and rendering process, but **defer** only executes the code when the page finishes loading.

---

# Resources

* Reference:
  * [WHATWG DOM Specification](https://dom.spec.whatwg.org/)
  * [W3C DOM Specification](https://www.w3.org/TR/DOM-Level-3-Core/)
  * [MDN DOM Reference](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model)

* Tutorials:
  * [The Modern JavaScript Tutorial](http://javascript.info)
  * [JavaScript Style Guide](https://github.com/airbnb/javascript)

---

# Elements

---

# Selecting Elements

The following [Document](https://developer.mozilla.org/en-US/docs/Web/API/Document) and [Element](https://developer.mozilla.org/en-US/docs/Web/API/Element) **methods** can be used to access specific HTML elements:

* [getElementById(id)](https://developer.mozilla.org/en-US/docs/Web/API/Document/getElementById) that returns an [Element](https://developer.mozilla.org/en-US/docs/Web/API/Element).
  <br><small>returns the element with the specified id.</small>
* [getElementsByClassName(class)](https://developer.mozilla.org/en-US/docs/Web/API/Element/getElementsByClassName) that returns a [NodeList](https://developer.mozilla.org/en-US/docs/Web/API/NodeList). 
  <br><small>returns all elements with the specified class.</small>
* [getElementsByTagName(name)](https://developer.mozilla.org/en-US/docs/Web/API/Element/getElementsByTagName) that returns a [NodeList](https://developer.mozilla.org/en-US/docs/Web/API/NodeList).
  <br><small>returns all elements with the specified tag name.</small>
* [querySelector(selector)](https://developer.mozilla.org/en-US/docs/Web/API/Element/querySelector) that returns an [Element](https://developer.mozilla.org/en-US/docs/Web/API/Element).
  <br><small>returns the **first** element selected by the specified CSS selector.</small>
* [querySelectorAll(selector)](https://developer.mozilla.org/en-US/docs/Web/API/Element/querySelectorAll) that returns a [NodeList](https://developer.mozilla.org/en-US/docs/Web/API/NodeList).
  <br><small>returns all elements selected by the specified CSS selector.</small>

```javascript
const menu = document.getElementById('menu')
const paragraphs = document.getElementsByTagName('p')  
const intros = document.querySelectorAll('article p:first-child')  
const links = menu.querySelectorAll('a')  
```

---

# Element

An [Element](https://developer.mozilla.org/en-US/docs/Web/API/Element) object represents an element in a [Document](https://developer.mozilla.org/en-US/docs/Web/API/Document). 

More specific elements, like the [HTMLElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement), will have more specific properties.

Some common Element **properties**:

* [id](https://developer.mozilla.org/en-US/docs/Web/API/Element/id)  &ndash; The element's identifier.
* [tagName](https://developer.mozilla.org/en-US/docs/Web/API/Element/tagName) &ndash; The tag name.
* [innerHTML](https://developer.mozilla.org/en-US/docs/Web/API/Element/innerHTML) &ndash; The markup code of the element's content.
* [outerHTML](https://developer.mozilla.org/en-US/docs/Web/API/Element/outerHTML) &ndash; The markup code describing the element, including its descendants.
* [textContent](https://developer.mozilla.org/en-US/docs/Web/API/Node/textContent) &ndash; The text content of an Element. <small>Inherited from [Node](https://developer.mozilla.org/en-US/docs/Web/API/Node).</small>

```javascript
const article = document.querySelector('#posts article:first-child')
article.innerHTML = '<p>Changed the content of the article</p>'
```

In most cases, using innerHTML to add new elements is [not a good idea](https://stackoverflow.com/questions/2946656/advantages-of-createelement-over-innerhtml).

---

# Element Attributes

[Element](https://developer.mozilla.org/en-US/docs/Web/API/Element) attributes can be accessed and modified using the following methods:

* [getAttribute(name)](https://developer.mozilla.org/en-US/docs/Web/API/Element/getAttribute) &ndash; **returns** the value for the attribute with the given name (or null).
* [setAttribute(name, value)](https://developer.mozilla.org/en-US/docs/Web/API/Element/setAttribute) &ndash; **modifies** the attribute with the given name to value.
* [removeAttribute(name)](https://developer.mozilla.org/en-US/docs/Web/API/Element/removeAttribute) &ndash; **removes** the attribute with the given name from the element.
* [hasAttribute(name)](https://developer.mozilla.org/en-US/docs/Web/API/Element/hasAttribute) &ndash; returns true if the element **has** an attribute with the given name.

```javascript
const link = document.querySelector('#posts a:first-child')
console.log(link.getAttribute('href'))
link.setAttribute('href', 'http://www.example.com/'))
```

---

# Element Class List

To modify the class attribute of an [Element](https://developer.mozilla.org/en-US/docs/Web/API/Element), we should use the [classList](https://developer.mozilla.org/en-US/docs/Web/API/Element/classList)  property that returns a live collection of classes.

This property can then be used to manipulate the class list:

* [add(class, ...)](https://developer.mozilla.org/en-US/docs/Web/API/DOMTokenList/add) &ndash; **adds** one or more classes to the class list.
* [remove(class, ...)](https://developer.mozilla.org/en-US/docs/Web/API/DOMTokenList/remove) &ndash; **removes** one or more classes from the class list.
* [replace(oldClass, newClass)](https://developer.mozilla.org/en-US/docs/Web/API/DOMTokenList/replace) &ndash; **replaces** *oldClass* with *newClass*.<br><small>But only if the *oldClass* is present. Returns true if the class was replaced.</small>
* [toggle(class)](https://developer.mozilla.org/en-US/docs/Web/API/DOMTokenList/toggle) &ndash; **toggles** class from the class list.<br> <small>Returns true if the class was added, false if it was removed.</small>

```javascript
const article = document.querySelector('#posts article:first-child')
article.classList.add('selected')
```

---

# Creating Elements

The [createElement](https://developer.mozilla.org/en-US/docs/Web/API/Document/createElement) method of the [Document](https://developer.mozilla.org/en-US/docs/Web/API/Document) object is the preferred method for creating new elements:

```javascript
const text = 'The quick brown fox jumps over the lazy dog'
const paragraph = document.createElement('p')

paragraph.textContent = text

console.log(paragraph.outerHTML)
```

The **paragraph** variable is a subclass of the [HTMLParagraphElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLParagraphElement) class.

```html
<p>The quick brown fox jumps over the lazy dog</p>
```

The paragraph still **has not been inserted** anywhere in the *document*.

---

# HTMLElement

The [HTMLElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement) inherits from the [Element](https://developer.mozilla.org/en-US/docs/Web/API/Element) object. 

For each HTML tag, a different class implements (directly or indirectly) this interface. These are some of their **properties**:

* [style](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/style) &ndash; The CSS style of the element.
* [hidden](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/hidden) &ndash; Is the element hidden.

And **methods**:

* [focus()](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/focus) &ndash; Sets keyboard focus on the element.
* [blur()](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/blur) &ndash; Removes keyboard focus on the element.
* [click()](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/click) &ndash; Simulates a mouse click on the element.

---

# HTML*Element

For each *HTML tag*, there is a class implementing the [HTMLElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement) interface.

These are some of them and some of their *attributes* and *methods*:

* [HTMLInputElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement) &ndash; name, type, value, checked, autocomplete, autofocus, defaultChecked, defaultValue, disabled, min, max, readOnly, required, [select()](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/select).
* [HTMLSelectElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLSelectElement) &ndash; name, multiple, required, size, length, [add(item, before)](https://developer.mozilla.org/en-US/docs/Web/API/HTMLSelectElement/add), [item(index)](https://developer.mozilla.org/en-US/docs/Web/API/HTMLSelectElement/item), [remove(index)](https://developer.mozilla.org/en-US/docs/Web/API/HTMLSelectElement/remove).
* [HTMLOptionElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLOptionElement) &ndash; disabled, selected, defaultSelected, text, value.
* [HTMLAnchorElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLAnchorElement) &ndash; href, host, hostname, port, hash, pathname, protocol, text, username, password.
* [HTMLImageElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement)  &ndash; alt, src, width, height.

---

# HTMLInputElement

Notice the difference between using the **value** attribute, and the **getAttribute** method to get the value of an [HTMLInputElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement):

```html
<form id="register">
  <input type="text" name="username" value="johndoe">
</form>
```

<form id="register">
  <input type="text" name="username" value="johndoe">
</form>

If the user changes the value to '*johndoe123*':

```javascript
const input = document.querySelector('#register input')
console.log(input.getAttribute('value'))  // still johndoe
console.log(input.value)                  // changes to johndoe123
```

---

# Node

The [Node](https://developer.mozilla.org/en-US/docs/Web/API/Node) object represents a node in the document tree. 

The *Element* and *HTMLElement* objects inherit these methods from the *Node* object:

* [appendChild(child)](https://developer.mozilla.org/en-US/docs/Web/API/Node/appendChild) &ndash; **adds** a node to the end of a parent's node list of children.
* [replaceChild(newChild, oldChild)](https://developer.mozilla.org/en-US/docs/Web/API/Node/replaceChild) &ndash; **replaces** a child of this node with another one.
* [removeChild(child)](https://developer.mozilla.org/en-US/docs/Web/API/Node/removeChild) &ndash; **removes a child** from this node.
* [insertBefore(newNode, referenceNode)](https://developer.mozilla.org/en-US/docs/Web/API/Node/insertBefore) &ndash;  **inserts** a new child **before** the reference child.
* [remove()](https://developer.mozilla.org/en-US/docs/Web/API/Element/remove) &ndash; **removes the element** from its parent.<br><small>From the [Element](https://developer.mozilla.org/en-US/docs/Web/API/Element) interface</small>.

When adding nodes, if the node already has a parent, it is **first removed** from its current location.

---

# HTMLElement Style

To change the inline style of an [HTMLElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement), we can use the [style](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/style) object.

Either changing the **whole inline style** at once:

```javascript
const article = document.querySelector('#posts article:first-child')
article.style = 'color: red'
```

Or just **one property**:

```javascript
article.style.color = 'red'
```

To **reset** all inline styles we can set the style object to *null* or to an *empty string*:

```javascript
article.style = ''
article.style = null
```

---

# Element and Node

A simple example:

```javascript
// gets the first article
const article = document.querySelector('#posts article:first-child')

article.style.color = 'blue'  // changes the text color to blue
article.style.padding = '2em' // and the padding to 2em

// creates a new paragraph
const paragraph = document.createElement("p") 
// inserts text in the paragraph
paragraph.textContent = 'Some text'

article.appendChild(paragraph) // adds the paragraph to the article
```

See this example in [action](https://jsfiddle.net/52nawdou/2/).

---

# NodeList

* A [NodeList](https://developer.mozilla.org/en-US/docs/Web/API/NodeList) is an object that behaves like an array of elements.
* Functions like [querySelectorAll](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelectorAll) and [getElementsByTagName()](https://developer.mozilla.org/en-US/docs/Web/API/Element/getElementsByTagName) return a *NodeList*.
* In some cases, the NodeList is live. <small>DOM changes automatically update it.</small>

Items in a *NodeList* can be accessed **by index** like in an array:

```javascript
const paragraphs = document.querySelectorAll('p')
for (let i = 0; i < paragraphs.length; i++) {
  const paragraph = paragraphs[i]
  // do something with the paragraph
}
```

Or using a **for..of** loop:

```javascript
const paragraphs = document.querySelectorAll('p')
for (const paragraph of paragraphs) {
  // do something with the paragraph
}
```

---

# Traversing

---

# Traversing the DOM tree (Node)

The *Node* object has the following properties that allow traversing the DOM tree:

* [firstChild](https://developer.mozilla.org/en-US/docs/Web/API/Node/firstChild) and [lastChild](https://developer.mozilla.org/en-US/docs/Web/API/Node/lastChild) &ndash; first and last node children of this node.
* [childNodes](https://developer.mozilla.org/en-US/docs/Web/API/Node/childNodes) &ndash; all children nodes as a **live** [NodeList](https://developer.mozilla.org/en-US/docs/Web/API/NodeList).
* [previousSibling](https://developer.mozilla.org/en-US/docs/Web/API/Node/previousSibling) and [nextSibling](https://developer.mozilla.org/en-US/docs/Web/API/Node/nextSibling) &ndash; previous and next siblings to this node.
* [parentNode](https://developer.mozilla.org/en-US/docs/Web/API/Node/parentNode) &ndash; parent of this node.
* [nodeType](https://developer.mozilla.org/en-US/docs/Web/API/Node/nodeType) &ndash; the type of this node.

.box_warning[
Be careful, as all these functions return nodes that might not be HTMLElements (*e.g.*, text and comment nodes).

See the complete [node type list](https://developer.mozilla.org/en-US/docs/Web/API/Node.nodeType).

---

# Traversing Example

Consider the following HTML:

```html
<section id="posts">
  <h1>Title</h1>
  <p>Some text</p>
</section>
```

And the following *JavaScript*:

```javascript
const posts = document.querySelector('#posts')
console.log(posts.firstChild)                         // #text
console.log(posts.firstChild.textContent)             // '\n '
console.log(posts.firstChild.nextSibling)             // <h1>
console.log(posts.firstChild.nextSibling.textContent) // 'Title'
```

---

# Traversing the DOM tree (Element)

To simplify traversing HTML documents, the following properties have been added to the [Element](https://developer.mozilla.org/en-US/docs/Web/API/Element) interface: <small>they always return Elements; not text or comments.</small>

* [firstElementChild](https://developer.mozilla.org/en-US/docs/Web/API/Element/firstElementChild) and [lastElementChild](https://developer.mozilla.org/en-US/docs/Web/API/Element/lastElementChild) &ndash; first and last element children of this node.
* [children](https://developer.mozilla.org/en-US/docs/Web/API/Element/children) &ndash; all children elements as a NodeList.
* [previousElementSibling](https://developer.mozilla.org/en-US/docs/Web/API/Element/previousElementSibling) and [nextElementSibling](https://developer.mozilla.org/en-US/docs/Web/API/Element/nextElementSibling) &ndash; previous and next element siblings of this node.

```html
<section id="posts">
  <h1>Title</h1>
  <p>Some text</p>
</section>
```

```javascript
const posts = document.querySelector('#posts')
console.log(posts.firstElementChild)              // <h1>
console.log(posts.firstElementChild.textContent)  // 'Title'
```

---

# Events

---

# Event-driven Architecture

The DOM follows an [event-driven](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Events) architecture (an architecture built on top of the publish-subscribe or observer pattern):

* Events are occurrences that happen in the system.<br><small>*e.g.*, the user clicks on a button.</small>
* Specific events in specific objects can have event handlers attached to them.
* When the event happens, the attached handler is called.

**Some** possible events:

* Mouse ([MouseEvent](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent)) &ndash; [click](https://developer.mozilla.org/en-US/docs/Web/API/Element/click_event), [dblclick](https://developer.mozilla.org/en-US/docs/Web/API/Element/dblclick_event), [mouseup](https://developer.mozilla.org/en-US/docs/Web/API/Element/mouseup_event), [mousenter](https://developer.mozilla.org/en-US/docs/Web/API/Element/mouseenter_event), [mouseleave](https://developer.mozilla.org/en-US/docs/Web/API/Element/mouseleave_event), [mouseover](https://developer.mozilla.org/en-US/docs/Web/API/Element/mouseover_event).
* Forms ([InputEvent](https://developer.mozilla.org/en-US/docs/Web/API/InputEvent), [FocusEvent](https://developer.mozilla.org/en-US/docs/Web/API/FocusEvent), [FormDataEvent](https://developer.mozilla.org/en-US/docs/Web/API/FormDataEvent) and [SubmitEvent](https://developer.mozilla.org/en-US/docs/Web/API/SubmitEvent)) &ndash; [input](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/input_event), [change](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/change_event), [focus](https://developer.mozilla.org/en-US/docs/Web/API/Element/focus_event), [blur](https://developer.mozilla.org/en-US/docs/Web/API/Element/blur_event), [formdata](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormElement/formdata_event), [submit](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormElement/submit_event).
* Keyboard ([KeyboardEvent](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent)) &ndash; [keydown](https://developer.mozilla.org/en-US/docs/Web/API/Document/keydown_event), [keyup](https://developer.mozilla.org/en-US/docs/Web/API/Document/keyup_event), [keypress](https://developer.mozilla.org/en-US/docs/Web/API/Document/keypress_event).

---

# Events in HTML

A possible way to get notified of events of a particular type (such as click) for a given object is to specify an event handler using an HTML attribute named on{eventtype} on an element.

For example:

```html
<button onclick="console.log('User clicked button')">
  Click me
</button>
```

Or:

```html
<button onclick="return handleClick(event)">
  Click me
</button>
```

.box_warning[
  But, you should [not use this](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Events#inline_event_handlers_%E2%80%94_dont_use_these)!

---

# Events on Element Properties

Another way of attaching an event handler would be by setting the corresponding property.

For example:

```javascript
document.querySelector("button").onclick = function(event) {
  console.log('User clicked button')
}
```

Or:

```javascript
function handleEvent(event) {
  console.log('User clicked button')
}

document.querySelector("button").onclick = handleEvent
```

---

# Add Event Handler

On modern browsers, the [addEventListener](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener) function is the most common way to attach event handlers.

For example:

```javascript
const button = document.querySelector("button")

button.addEventListener('click', function(event){
  console.log('User clicked button')
})
```

Or:

```javascript
function handleEvent() {
  console.log('User clicked button')
}

const button = document.querySelector("button")
button.addEventListener('click', handleEvent)
```

---

# The Event Object

A function that handles an event can receive a parameter representing the event:

* Depending on its type, the event can have different [properties and methods](https://developer.mozilla.org/en/docs/Web/API/Event#DOM_Event_interface).

* We can use the [preventDefault()](https://developer.mozilla.org/en-US/docs/Web/API/Event/preventDefault) method to ensure that the default behavior is suppressed (*e.g.*, a link isn't followed or a form isn't submitted).

```javascript
function handleEvent(event) {
  console.log('You shall not pass!')
  event.preventDefault()
}

const button = document.querySelector("button")
button.addEventListener('click', handleEvent)
```

See this example in [action](https://jsfiddle.net/wxcmd387/11/).

---

# Bubbling

When an event happens on an element, it first runs any handlers attached to it, then on its parent, then up to the root.

In each step, the handler can know the current target ([event.currentTarget](https://developer.mozilla.org/en-US/docs/Web/API/Event/currentTarget) or *this*) and also the initial target ([event.target](https://developer.mozilla.org/en-US/docs/Web/API/Event/target)).

Example where we add some events on all elements and print **this** and **event.target** [tag names](https://developer.mozilla.org/en-US/docs/Web/API/Element/tagName):

```html
<section> <article> <p>Text</p> </article> </section>
```

```javascript
document.querySelector('section').addEventListener('click', function(event){
  console.log('Bubble: ' + this.tagName + " - " + event.target.tagName)})
document.querySelector('article').addEventListener('click', function(event){
  console.log('Bubble: ' + this.tagName + " - " + event.target.tagName)})
document.querySelector('p').addEventListener('click', function(event){
  console.log('Bubble: ' + this.tagName + " - " + event.target.tagName)})
```

Clicking on the paragraph:
```html
Bubble: P - P
Bubble: ARTICLE - P
Bubble: SECTION - P
```

To stop bubbling, we can use the [event.stopPropagation()](https://developer.mozilla.org/en-US/docs/Web/API/Event/stopPropagation) method.

---

# Capturing

Event processing has [two phases](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Events#event_bubbling_and_capture):

  * Capturing: goes down to the element.
  * Bubbling: the event bubbles up from the element.

Although rarely used, the **useCapture** parameter of the [addEventListener](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener) method allows us to set the event handler on the capturing phase.

Adding capture events to the previous example:

```javascript
document.querySelector('section').addEventListener('click', function(event){
  console.log('Capture: ' + this.tagName + " - " + event.target.tagName)}, true)
document.querySelector('article').addEventListener('click', function(event){
  console.log('Capture: ' + this.tagName + " - " + event.target.tagName)}, true)
document.querySelector('p').addEventListener('click', function(event){
  console.log('Capture: ' + this.tagName + " - " + event.target.tagName)}, true)
```

```html
Capture: SECTION - P
Capture: ARTICLE - P
Capture: P - P
Bubble: P - P
Bubble: ARTICLE - P
Bubble: SECTION - P
```

---

# On Load Event

Besides placing the [&lt;script&gt;](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script) at the end of the HTML code, another common way of waiting for the DOM to be completely loaded before adding events to any elements is to add any initialization code to the *load* event of the *window* element:

```javascript
window.addEventListener('load', function() {
  // initialization code goes here.
})
```

This is no longer needed as we can now use the [defer](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script#attr-defer) attribute.

---

name:ajax
# AJAX

---

# AJAX

AJAX stands for **A**synchronous **J**avaScript **a**nd **X**ML.

* Although originally associated with **XML**, in modern usage **JSON** is far more common as the data format.
* AJAX is not a single technology. It is a **technique** or **approach** for building web applications, first popularized by **Jesse James Garrett** in **2005**. 
* It involves using several existing technologies, originally centered around the **XMLHttpRequest** object (in modern *JavaScript*, we use **fetch**).

---

# AJAX

AJAX involves the asynchronous communication between the client (browser) and the server, without requiring a full page reload (steps 7&ndash;11).

![](assets/javascript-dom/ajax.svg)

---

# XMLHttpRequest

[XMLHttpRequest](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest) makes sending HTTP requests from JavaScript very easy.

```javascript
void open(method, url, async)
```

  * method: **GET** or **POST** <small>(or others to be seen later)</small>.
  * url: The URL to fetch.
  * async: if false, execution will stop while waiting for response.<br><small>Default is true.</small>

Example:

```javascript
function requestListener () {
  console.log(this.responseText)
}

const request = new XMLHttpRequest()
request.addEventListener('load', requestListener)
// or request.onload = requestListener
request.open("GET", "getdata.php", true)
request.send()
```

---

# Monitoring Progress

Different events let us monitor progress of the request:

```javascript
const request = new XMLHttpRequest()

request.addEventListener("progress", updateProgress)
request.addEventListener("load", transferComplete)
request.addEventListener("error", transferFailed)
request.addEventListener("abort", transferCanceled)

request.open("get", "getdata.php", true)
request.send()

function updateProgress (event) {
  if (event.lengthComputable)
    const percentComplete = event.loaded / event.total
}

function transferComplete(event) {
  console.log("The transfer is complete.")
}

function transferFailed(event) {
  console.log("An error occurred while transferring the file.")
}

function transferCanceled(event) {
  console.log("The transfer has been canceled by the user.")
}
```

---

# Sending data

To send data to the server, we first must encode it properly:<br><small>We are simplifying, there are [other ways](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/Using_XMLHttpRequest#using_nothing_but_xmlhttprequest) of doing this.</small>

```javascript
function encodeForAjax(data) {
  return Object.keys(data).map(
    k => encodeURIComponent(k) + '=' + encodeURIComponent(data[k])
  ).join('&')
}
```

Sending it using **get**:

```javascript
request.open("get", 
  "getdata.php?" + encodeForAjax({id: 1, name: 'John'}), true)
request.send()
```

Sending it using **post**:

```javascript
request.open("post", "getdata.php", true)
request.setRequestHeader('Content-Type', 
  'application/x-www-form-urlencoded')
request.send(encodeForAjax({id: 1, name: 'John'}))
```

---

# Analyzing the Response

If the server responds in **XML** format, the [responseXML](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/responseXML) property will be a DOM Object containing a parsed XML document, which can be hard to manipulate and analyze.

If the server responds in **JSON**, it is straightforward to parse the [responseText](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/responseText) property:

```javascript
const request = new XMLHttpRequest()
request.addEventListener("load", transferComplete)
request.open("get", "getdata.php", true)
request.send()

function transferComplete() {
  const response = JSON.parse(this.responseText)
}
```

---

# AJAX with Promises

The [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) is a more modern interface for fetching remote resources:

* The global [fetch()](https://developer.mozilla.org/en-US/docs/Web/API/fetch) can be used to fetch a remote resource.
* It returns a *Promise* that will eventually be **fulfilled** as a [Response](https://developer.mozilla.org/en-US/docs/Web/API/Response).
* It will only get **rejected** if there was a network or permission error (*i.e.*, any response from the server is fulfilled).

```javascript
async function getData() {
    return fetch('https://example.com/')
}

getData().then(response => {
  console.log(response)
}).catch(() => {
  console.error('Network Error')
})
```

---

# Response

Because only failed requests get rejected, the response must be checked:

* [ok](https://developer.mozilla.org/en-US/docs/Web/API/Response/ok) &ndash; Boolean indicating if the response was successful (*i.e.*, the status is in the 200&ndash;299 interval).
* [status](https://developer.mozilla.org/en-US/docs/Web/API/Response/status) &ndash; The status code of the response (*e.g.*, 200, 404).
* [redirected](https://developer.mozilla.org/en-US/docs/Web/API/Response/redirected) &ndash; Indicates if the request was redirected to another URL.
* [url](https://developer.mozilla.org/en-US/docs/Web/API/Response/url) &ndash; Final URL after redirects.
* [body](https://developer.mozilla.org/en-US/docs/Web/API/Response/body) &ndash; The body of the response (*i.e.*, the data).

```javascript
getData().then(response => {
  if (response.ok)
    console.log(response.body)
  else
    console.error(`Error: code ${request.status}`)
}).catch(() => {
  console.error('Network Error')
})
```

---

# JSON Response

To parse a JSON [Response](https://developer.mozilla.org/en-US/docs/Web/API/Response) we use the [json()](https://developer.mozilla.org/en-US/docs/Web/API/Response/json) method that also returns a promise:

```javascript
getData()
  .catch(() => console.error('Network Error'))
  .then(response => response.json())
  .catch(() => console.error('Error parsing JSON'))
  .then(json => console.log(json))
```

If the [Response](https://developer.mozilla.org/en-US/docs/Web/API/Response) is text, then we use the [text()](https://developer.mozilla.org/en-US/docs/Web/API/Response/text) method that also returns a promise:

```javascript
getData()
  .catch(() => console.error('Network Error'))
  .then(response => response.text())
  .then(text => console.log(text))
```

---

# Using Await

This can all be simplified by using the async/await mechanism:

```javascript
async function getJsonData() {
  const response = await getData()
  const content = await response.json()
}
```

Or for text:

```javascript
async function getTextData() {
  const response = await getData()
  const content = await response.text()
}
```

---

# Request

For more complicated requests, the [fetch()](https://developer.mozilla.org/en-US/docs/Web/API/fetch) method can receive an object with extra parameters:

```javascript
async function postData(data) {
  const response = await fetch('https://example.com/', {
    method: 'post',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    },
    body: encodeForAjax(data)
  })
  return await response.json()
}

const result = await postData({id: 100, name: 'John'})
```

More on this will be discussed when we study the **HTTP** protocol in depth.

---

name:timers
#Timers

---

# Set Timeout

The [window.setTimeout(funtion, delay)](https://developer.mozilla.org/en-US/docs/Web/API/setTimeout) fuction sets a timer which executes a function once after a certain delay:

```javascript
const id = window.setTimeout(function() {
  console.log('5 seconds later!')
}, 5000)
```

The return value is an *id* that can be used to cancel the timer:

```javascript
window.clearTimeout(id)
```

---

# Set Interval

The [window.setInterval(function, interval)](https://developer.mozilla.org/en-US/docs/Web/API/setInterval) is similar but executes the function until it is stopped with a fixed time delay between calls.

```javascript
let counter = 1
const id = window.setInterval(function() {
  console.log(`${counter++}s later!`)
}, 1000)
```

The return value is an *id* that can be used to cancel the timer:

```javascript
window.clearInterval(id)
```

---

# Advanced DOM

---

# Closures and Events

Let's start by thinking if this code should work...

```JavaScript
const paragraphs = document.querySelectorAll('p')
for (let i = 0; i < paragraphs.length; i++)
  paragraphs[i].addEventListener('click', function() {
      console.log('I am paragraph #' + i)
  })
```

--

When we click a paragraph, what will be the value of the *i* variable? Let's [test it](https://jsfiddle.net/205byurL/1/).

--

The reason this code works as expected is that each time an event handler is added, a new function is created, and each function captures a **unique closure**. This closure **retains** a **reference** to the value of the variable <code>i</code> at the **moment** the event listener is added, ensuring that each handler has access to the correct value of <code>i</code> for the specific iteration.

> "When a function is created, it **retains** the lexical environment in which it was **created**."<br>&mdash; [Closures](?s=javascript#closures), JavaScript Slides.

---

# Bind and Events

Sometimes we **lose** our *this*:

```javascript
class Foo {
  setup() {
    document.querySelector('h1').addEventListener('click', this.bar)
  }

  bar(event) {
    // we want to get the Foo object, but:
    console.log(this)         // the h1 element
    console.log(event.target) // the h1 element
  }
}

new Foo().setup()
```

We can **fix** it using *bind*:

```javascript
setup() {
  document.querySelector('h1')
    .addEventListener('click', this.bar.bind(this))
}
```

---

# Partial Functions

We might want to call a function with parameters that depend on the element:

```javascript
document.querySelector('p.blue').addEventListener('click', changeColor('blue'))
document.querySelector('p.red').addEventListener('click', changeColor('red'))

function changeColor(color) {
  this.style.color = color
}
```

But it obviously doesn't work. 

A solution would be to create **anonymous functions**:

```javascript
document.querySelector('p.blue').addEventListener('click', function(event) {
  changeColor('blue', event)}
)
document.querySelector('p.red').addEventListener('click', function(event) {
  changeColor('red', event)}
)

function changeColor(color, event) {
  event.target.style.color = color
}
```

---

# Partial Functions

Another, more elegant solution, would be to create **partial functions** using *bind*:

```javascript
const blue = document.querySelector('p.blue')
blue.addEventListener('click', changeColor.bind(blue, 'blue'))

const red = document.querySelector('p.red')
red.addEventListener('click', changeColor.bind(red, 'red'))

function changeColor(color) {
  this.style.color = color
}
```

---

# Mapping Selectors

We already saw how we could use the [map()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map) function with *non-array* iterables (like a [NodeList](https://developer.mozilla.org/en-US/docs/Web/API/NodeList)).

One way we can use this feature:

```javascript
const inputs = document.querySelectorAll('input[type=number]')
const values = [].map.call(inputs, input => input.value)
console.log(values) // an array with all the number input values
```

See this example in [action](https://jsfiddle.net/8sLhp915/3/).

---

# Selectors to Arrays

Other times we just want to **convert** a [NodeList](https://developer.mozilla.org/en-US/docs/Web/API/NodeList) to an **array**, so we can use functions like [map()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map), [reduce()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce), and [filter()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter):

```javascript
const paragraphs = document.querySelectorAll('p')
```

There are several ways to achieve this:

```javascript
const array1 = Array.apply(null, paragraphs)
const array2 = Array.prototype.slice.call(paragraphs)
const array3 = [].slice.call(paragraphs)
const array4 = [...paragraphs]
```

---

# HTML5 Data Attributes

HTML5 data-* attributes allow us to store **extra information** on *standard*, *semantic* HTML elements without using hacks.

This can be useful, for example, to store the id of a certain database tuple to be used in an *Ajax* call.

```html
  <ul>
    <li data-id="1">Apple</li>
    <li data-id="2">Banana</li>
    <li data-id="3">Pear</li>
  </ul>
```

Accessing this values using *JavaScript*:

```javascript
const items = document.querySelectorAll('li');
for (const item of items)
  console.log(item.dataset.id)
```





---

---

template:inverse
# PHP
<a href="http://www.fe.up.pt/~arestivo">André Restivo</a>

---

name:index
# Index

1. [Introduction](#intro)
1. [Variables](#variables)
1. [Control Structures](#control)
1. [Strings](#strings)
1. [Arrays](#arrays)
1. [Functions](#functions)
1. [Classes](#classes)
1. [Exceptions](#exceptions)
1. [Databases](#databases)
1. [HTTP Parameters](#parameters)
1. [Sessions](#sessions)
1. [Passwords](#passwords)
1. [Headers](#headers)
1. [Includes](#includes)
1. [JSON](#json)
1. [Best Practices](#best)

---

name:intro
# Introduction

---

# PHP

* Originally called **P**ersonal **H**ome **P**age, it now stands for **P**HP: **H**ypertext **P**reprocessor, which is a recursive acronym
* Created by Rasmus Lerdorf in 1994.
* It is a **dynamically typed** programming language.
* Usually used to create dynamic web pages but can also be used to create standalone programs.

---

# Hello World

The infamous hello world example in PHP:

```php
<?php echo 'Hello World'; ?>
```

or even shorter

```php
<?='Hello World;
```

---

# PHP Delimiters

* The PHP interpreter only executes PHP code within its delimiters.<br><small>Anything outside its delimiters is not processed by PHP.</small>
* PHP code is delimited using "<?php" and "?>".<br><small>In some cases "<?" and "?>" or "&lt;script language="php">" and "&lt;/script>" also work.</small>
* The purpose is to separate PHP code from non-PHP code (*e.g.*, HTML).
* After processing, the PHP code blocks are replaced by their output.

```php
<section>
  <p><?php echo 'Hello World'?></p>
</section>
```

Becomes:

```html
<section>
  <p>Hello World</p>
</section>
```

---

# How It Works

<img src="assets/php/scenario.svg" width="60%">

1. Browser **asks** the server for a **resource** that corresponds to a PHP script.
2. Server **runs** PHP script.
3. Server **returns** result to the browser. Normally an HTML document.

---

# Echo

* The [echo](https://www.php.net/manual/en/function.echo.php) function outputs one or more strings.
* It is not actually a function (it is a language construct), so you are not required to use parentheses with it.
* It also has a shortcut syntax, where you can immediately follow the opening tag with an equals sign.

```php
<?php echo 'Hello World'; ?>
```
The same as:

```php
<?='Hello World'?>
```

---

# Comments

There are two ways of creating single-line comments:

```php
echo 'Hello World'; // This line prints Hello World
echo 'Hello World'; # This line prints Hello World
```

Multi-line comments can also be used:

```php
/**
 * The following line
 * prints Hello World
 */
echo 'Hello World';
```

---

template:inverse
# Resources

* References:
  * http://php.net/manual/en/
* Books:
  * http://www.phptherightway.com/

---

# Variables

---

# Variables

* Variables are represented by a dollar sign followed by the variable's name.
* The variable's name is **case-sensitive**.
* There are no explicit type definition in variable declarations.
* A variable's type is determined by the context in which the variable is used.

```php
$name = 'John';  // string
$age = 25;       // int
```

---

# Data Types

PHP supports the following scalar types:

* [bool](https://www.php.net/manual/en/language.types.boolean.php): **case-insensitive** *true* or *false*.
* [int](https://www.php.net/manual/en/language.types.integer.php): integer between *PHP_INT_MIN* and *PHP_INT_MAX*.<br><small>Range is platform-dependent; converted to float in the case of an overflow.</small>
* [float](https://www.php.net/manual/en/language.types.float.php): IEEE 754 double precision format.
* [string](https://www.php.net/manual/en/language.types.string.php): A series of characters.

We can find the type of a variable using the [gettype](https://www.php.net/manual/en/function.gettype.php) function:

```php
$name = 'John';
echo gettype($name); // string
```

---

# Assignment

* The variable type is defined when a value is [assigned](https://www.php.net/manual/en/language.operators.assignment.php) to it.
* Type can change when values of another type are assigned.
* Assignment is done by value unless the **&** sign is used.

```php
$foo = 5;        // int
$foo = 'John';   // string

$bar = &$foo;    // by reference, bar and foo are the same
$foo = 'Mary';

echo $bar;       // Mary
```

---

# Type Juggling

* PHP does automatic **type conversion** whenever it is needed.
* For example, the **+** (sum) operator expects two numerical values.

```php
echo 5 + '10 potatoes'; // 15
```

* PHP automatically converts the string into an integer.

More on [type juggling](https://www.php.net/manual/en/language.types.type-juggling.php) and [why](https://owasp.org/www-pdf-archive/PHPMagicTricks-TypeJuggling.pdf) you should be careful.

---

# Null Value

The special **null** value represents a variable with no value.

A variable is considered *null* if:

* it has been assigned the constant *null*.
* it has not been set to any value yet.
* it has been unset().

```php
// $a starts as null
$a = 5;    // 5
$a = null; // null
$a = 10;   // 10;
unset($a); // null;
```

The constant **null** is **case-insensitive**.

---

# Null Coalesce

The [isset](https://www.php.net/manual/en/function.isset.php) function determines if a variable is declared and different from *null*:

```php
$bar = isset($bar) ? $bar : $some_default_value;
```

An easier way to acccomplish this would be to use the *null coalesce* operator:

```php
$bar = $bar ?? $some_default_value;
```

Or even simpler:

```php
$bar ??= $some_default_value;
```

---

# Var Dump

The [var_dump](https://www.php.net/manual/en/function.var-dump.php) function displays structured information about one or more expressions, including their type and value.

Arrays and objects are explored recursively and their values are indented to show their structure.

```php
$a = 10.5;
$b = true;
var_dump($a, $b);
```

```html
float(10.5)
bool(true)
```

Very useful for dirty and straightforward debugging.

An alternative is [print_r](https://www.php.net/manual/en/function.print-r.php), a simplified form of *var_dump*.

---

# Control Structures
Not so different from other languages

---

# While

Executes the nested statement(s) repeatedly, as long as the [while](https://www.php.net/manual/en/control-structures.while.php) expression evaluates to *true*.

```php
while($expr)
  do_something();
```

```php
while($expr) {
  do_something();
  do_something_more();
}
```

```php
while($expr):
  do_something();
  do_something_more();
endwhile;
```

---

# Do While

[Do...while](https://www.php.net/manual/en/control-structures.do.while.php) loops are similar to *while loops*, but the expression is checked at the end of each iteration instead of at the beginning.

```php
do {
  do_something();
} while($expr);
```

---

# For

In [for](https://www.php.net/manual/en/control-structures.for.php) loops, the **first** expression is executed once unconditionally at the beginning of the loop.

At the beginning of each iteration, the **second** expression is evaluated. If it evaluates to *false*, the execution of the loop ends.

At the end of each iteration, the **third** expression is executed.

```php
for ($i = 0; $i < 10; $i++)
  do_something($i);
```

```php
for ($i = 0; $i < 10; $i++) {
  do_something($i);
  do_something_more($i);
}
```

---

# If

Only [if](https://www.php.net/manual/en/control-structures.if.php) the expression evaluates to *true* does the following code execute.

```php
if ($expr)
  do_something();
```

```php
if ($expr) {
  do_something();
  do_something_more();
}
```

---

# Else

The [else](https://www.php.net/manual/en/control-structures.else.php) statement extends an *if* statement to execute alternative code if the expression in the *if* statement evaluates to *false*.

```php
if ($expr)
  do_something();
else
  do_something_else();
```

```php
if ($expr)
  do_something();
else {
  do_something_else();
  do_something_more();
}
```

---

# Break and Continue

[Break](https://www.php.net/manual/en/control-structures.break.php) ends execution of the current **for**, **foreach**, **while**, **do-while** or **switch** structure.

[Continue](https://www.php.net/manual/en/control-structures.continue.php) skips the rest of the current loop iteration and continues execution at the condition evaluation.

```php
while ($expr) {
  do_something();
  if ($foo) break;
  if ($bar) continue;
  do_something_more();
}
```

---

# Switch

The [switch](https://www.php.net/manual/en/control-structures.switch.php) statement is similar to a series of *if statements* on the same expression.

After finding a *true* condition, PHP continues to execute the statements until the end of the switch block, or the first time it sees a break statement.

```php
switch($name) {
  case "John":
    do_something();
    do_something_more();
    break;
  case "Mary":
    do_something();
    break;
  default:
    do_something_else();    
}
```

---

# Die and Exit

Both [die](https://www.php.net/manual/en/function.die.php) and [exit](https://www.php.net/manual/en/function.exit.php) stop the execution of the current PHP script.

* **die**: can receive a status string that will be printed before stopping
* **exit**: can receive a result integer that will be the exit status and not printed.

```php
  if ($something == "wrong") die ("Something is Wrong");
```

```php
  if ($everything == "ok") exit(0);
```

---

# Loose and Strict Comparisons

Comparisons can be [tricky](https://www.php.net/manual/en/types.comparisons.php) in PHP. There are two types of equality operators:

**Loose comparison**: Types can be converted before comparison.

```php
if ($a == $b) {   // != gives the opposite result
  do_something();
}
```  

**Strict comparison**: Types must be the same.

```php
if ($a === $b) {   // !== gives the opposite result
  do_something();
}
```  

---

# Loose and Strict Comparisons

Some Examples:

```php
if (1 == true)  // true - true is casted into the integer 1
if (1 === true) // false;
```

```php
if (1 == "1")  // true - "1" is casted into the integer 1
if (1 === "1") // false;
```

```php
if (null == false)  // true
if (null === false) // false;
```

```php
if ("Car" == true)  // true
if ("Car" === true) // false;
```

Learn [more](http://php.net/manual/en/types.comparisons.php).

---

template:inverse
name:strings
# Strings

---

# Strings

A string is a series of characters.

The simplest way to specify a string is to enclose it in *single quotes*.

```php
$name = 'John';
```

A *single quote* inside a string defined using *single quotes* must be escaped using a **backslash**. To specify a literal backslash, double it.

```php
$title = 'Ender\'s Game';
```

Single quoted strings don't recognize any other escape sequences.

---

# Double Quote

If the string is enclosed in *double quotes*, more escape sequences for special characters are allowed (e.g. \r, \n, \t, \\\\, \", \$):

```php
$title = "The quick brown fox\njumps over the lazy dog";
// The quick brown fox
// jumps over the lazy dog
```
Double quoted strings also expand any variables inside them.

```php
$name = 'John';

echo 'This car belong to $name'; // This car belongs to $name
echo "This car belong to $name"; // This car belongs to John
```

Some developers consider it a best practice to use single quotes when assigning string literals as they denote that there are no variables inside them.

---

# Concatenation

The *sum* operator expects two numeric values as we have seen before. If used with strings, it will try to cast the strings into numbers, and sum them.

A different operator is used to concatenate strings together.

```php
$name = 'John';
echo 'Hello World!' . " This is $name.";
```

---

# Some String Functions

Returns the **length** of the given string:

```php
int strlen (string $string)
```

```php
echo strlen('John')   // 4
```

Find the numeric position of the **first occurrence** of *needle* in the *haystack* string starting at *offset*. Returns false if not found.

```php
mixed strpos (string $haystack, mixed $needle [, int $offset = 0 ])
```

```php
echo strpos ('abccba', 'bc');    // 1
echo strpos ('abccba', 'a');     // 0
echo strpos ('abccba', 'a', 2);  // 5
echo strpos ('abccba', 'bc', 2); // false
```

---

# Some String Functions

Returns the **string portion** specified by the *start* and *length* parameters.

```php
string substr (string $string, int $start [, int $length ])
```

```php
echo substr('abcdefgh', 2, 4); // cdef
```

Returns a string with all occurrences of search in subject **replaced** with the given replace value. <small>Also works with arrays.</small>

```php
mixed str_replace (mixed $search, mixed $replace, 
                   mixed $subject [, int &$count ])
```

```php
$text = str_replace("cd", "--", "abcdabcd", $count);
echo $text;  // ab--ab--
echo $count; //2
```

---

# Some String Functions

Returns an array of strings, each of which is a substring of the initial string formed by **splitting** it on the boundaries defined by the string *delimiter*.

```php
array explode (string $delimiter , string $string [, int $limit ])
```

**Joins** *pieces* from an array with a *glue* string.

```php
string implode (string $glue , array $pieces)
```

```php
$pieces = explode(' ', 'a b c'); // $pieces = array('a', 'b', 'c')
$text = implode('-', $pieces);   //$text = 'a-b-c'
```

---

# Arrays

---

# Arrays

At first glance, PHP arrays might seem similar to arrays in other classical languages.

```php
$values[0] = 5;  // although they don't need to be defined
$values[1] = 10; // and they don't have a fixed size
$values[2] = 20;

// count returns the size of the array
for ($i = 0; $i < count($values); $i++)
  $sum = $sum + $values[$i];

echo $sum / count($values); // calculates average: 11.666666666667
```

---

# Arrays

An array is an **ordered map** organized as an ordered collection of **key-value** pairs.

Keys can be either **integers** or **strings**, and values can hold any data type. They can even hold different kinds of data in the same array.

```php
$values['name'] = 'John';
$values['age'] = 45;
$values[3] = 'Car';
```

---

# Creating Arrays

Arrays can be created just by using a variable as an array. Or they can be explicitly created using the **array()** function.

```php
$values = array(); // this creates an empty array
```

They can also be initialized with some values.

```php
$values = array(1, 2, 3, 'John'); 
// 0 => 1, 1 => 2, 2 => 3, 3 => 'John'
```

```php
$values = array('name' => 'John', 'age' => 45, 3 => 'Car');
```

Or using a simplified syntax:

```php
$values = [1, 2, 3, 'John'];
```

---

# Using Arrays

PHP will increment the **largest previously used** integer key when a key is not provided.

```php
$values = array('name'=>'John', 'age'=>45, 2=>'Car', 'Bicycle');
$values[] = 'Boat';
// 'name'=>John, 'age'=>45, 2=>'Car', 3=>'Bicycle', 4=>'Boat'
```

.box_info[Note that the largest previously used integer key does not need to exist in the array. It needs only to have been used as a key since the last time the array was re-indexed.]

We can also have arrays as an array value:

```php
$people = array(
  array('name' => 'John', 'age' => 45),
  array('name' => 'Mary', 'age' => 35);
);
echo $people[0]['name']; // John
```

---

# Cycling Arrays

As arrays might not have sequential keys, like in other languages, in PHP we use the following construct to cycle through their **values**:

```php
$values = array('name'=>'John', 'age'=>45, 2=>'Car', 'Bicycle');
foreach ($values as $value)
  echo "$value\n";
```

A similiar construct can be used to cycle through the **keys and values** simultaneously:
```php
$values = array('name'=>'John', 'age'=>45, 2=>'Car', 'Bicycle');
foreach ($values as $key => $value)
  echo "$key = $value\n";
```

---

# Some Array Functions

**Searching for data:**

**Searches** *haystack* for *needle* using loose comparison unless strict is set. Returns true if found, false otherwise.

```php
bool in_array (mixed $needle, 
               array $haystack [, bool $strict = false ])
```

Returns the **key** for needle if it exists in the array, *false* otherwise.

```php
mixed array_search (mixed $needle, 
                    array $haystack [, bool $strict = false ])
```

Returns *true* if the given key **exists** in the array, *false* otherwise.

```php
bool array_key_exists (mixed $key, array $array)
```

---

# Some Array Functions

**Sorting data:**

Sorts an array such that array indexes **maintain** their **correlation** with the array elements they are associated with.<br><small>**arsort** does the same but in reverse.</small>

```php
bool asort (array &$array [, int $sort_flags = SORT_REGULAR ])
```

Sorts an array by key, **maintaining** key to data **correlations**.<br><small>**krsort** does the same but in reverse.</small>

```php
bool ksort (array &$array [, int $sort_flags = SORT_REGULAR ])
```

Sort Flags: **SORT_REGULAR**, **SORT_NUMERIC**, **SORT_STRING**, **SORT_LOCALE_STRING**, **SORT_NATURAL** and **SORT_FLAG_CASE**.

Learn more: [php.net &ndash; array sorting](http://php.net/manual/en/array.sorting.php)

---

# Some Array Functions

**Random arrays:**

This function **randomizes** the order of the elements in an array. Returns *true* on success or *false* on failure.

```php
bool shuffle (array &$array)
```

Picks **one or more random entries** out of an array and returns the random entries' key (or keys). 
<br><small>When picking only one entry, returns the key, otherwise returns an array of keys.</small>

```php
mixed array_rand (array $array [, int $num = 1 ])
```

---

# Some Array Functions

Used to assign a list of variables in one operation; not really a function but a language construct.

```php
array list ( mixed $var1 [, mixed $... ] )
```

```php
$values = array('John', 45, 'Bicycle');
list($name, $age, $vehicle) = $values;
echo $name;     // John
echo $age;      // 45
echo $vehicle;  // Bicycle
```

```php
$values = array('John', 45, 'Bicycle');
list($name, , $vehicle) = $values; // skipping some values
```

Many more functions: [php.net &ndash; arrays](http://php.net/manual/en/ref.array.php)

---

template:inverse
name:functions
# Functions

---

# Functions

Any valid PHP code may appear inside a function, even other functions and class definitions.

Functions need not be defined before they are referenced, except when a function is conditionally defined.

Function names are **case-insensitive**.

To create a function, we use the *function* keyword:

```php
function doSomething() {
  echo "done";
}

doSomething(); // prints done
```

---

# Parameters

By default, function parameters are passed by value. Parameters passed by reference are preceded by an ampersand (&).

```php
function sum($a, &$b) {
  return $a++ + $b++;
}

$a = 1; $b = 2;

echo sum($a, $b); // prints 3

echo $a;          // prints 1
echo $b;          // prints 3
```

---

# Default Values

Function parameters can have default values.

Any parameters with a default value should appear after all parameters without defaults.

```php
function sum($a, $b = 0, $c = 0) {
  echo $a + $b + $c;
}

sum(1);     // prints 1
sum(1,2);   // prints 3
sum(1,2,3); // prints 6
```

---

# Returning Values

Functions can return values.

The type of the returned value does not need to be specified. A function can even return different types of values depending on some condition.

Functions that do not return a value return *null*. 

```php
function sum($a, $b = 0, $c = 0) {
  return $a + $b + $c;
}

echo sum(1);     // prints 1
echo sum(1,2);   // prints 3
echo sum(1,2,3); // prints 6
```

---

# Returning Multiple Values

There is no way for a function to return multiple values.

But we can achieve a similar result using *arrays* and the *list* construct.

```php
function sort2($a, $b) {
  if ($a > $b) return array($b, $a);
  else return array($a, $b);
}

list($smaller, $larger) = sort2(10, 5);

echo $smaller; // 5
echo $larger;  // 10
```

---

# Global

As PHP variables do not need to be defined before usage, we need to declare global variables as global to use them inside functions.

```php
function foo() {
  echo $baz;
}

function bar() {
  global $baz;
  echo $baz;
}

$baz = 10;

foo(); // prints nothing, may result in a warning
bar(); // prints 10
```

---

# Coercive Typing

PHP is a dynamically typed language, but since PHP 7, it is possible to add [type hints](https://www.php.net/manual/en/language.types.declarations.php) to function **parameters**:

```php
function add($a, $b) {
  return $a + $b;
}

echo add(1, 4);          // 5 
echo add(1.2, 3.6);      // 4.8
echo add("1.2", "3.6");  // 4.8
```

With *type hints*, types are **coerced** into the correct type (if possible):<br><small>Otherwise an error is thrown.</small>

```php
function add(int $a, int $b) {
  return $a + $b;
}

echo add(1, 4);          // 5 
echo add(1.2, 3.6);      // 4
echo add("1.2", "3.6");  // 4
```

---

# Coercive Typing

**Type hints** can also be added to **return values**:

```php
function add($a, $b) : int {
  return $a + $b;
}

echo add(1, 4);          // 5 
echo add(1.2, 3.6);      // 4
echo add("1.2", "3.6");  // 4
```

Returned values are **coerced** into the correct type (if possible).<br><small>Otherwise an error is thrown.</small>

Besides the four scalar types, the following are also possible type hints: *array*, *object*, a *class/interface name*, *callable*, *iterable*, *self*, and *parent*.

---

# Strict Typing

It is possible to enable **strict mode** on a per-file basis by using this directive at the beginning of a PHP file:

```php
declare(strict_types=1);
```

In strict mode, only values corresponding to the type declaration will be accepted.
<br><small>The only exception to this rule is that an **int** value will pass a **float** type declaration.</br>

```php
declare(strict_types=1);

function add(int $a, int $b) : int {
  return $a + $b;
}

echo add(1, 4);          // 5 
echo add(1.2, 3.6);      // Error
echo add("1.2", "3.6");  // Error
```

---

# Nullable Types

Sometimes we want to declare a type but also **allow the null value**.

This can be achieved by **prefixing** the type name with a '?':

```php
declare(strict_types=1);

function add(?int $a, ?int $b) : ?int {
  if ($a === null || $b === null) return null;

  return $a + $b;
}

echo add(1, 4);          // 5 
echo add(1, null);       // null 
```

Nullable types also work with return values.

---

template:inverse
name:classes
# Classes

---

# Classes

PHP 5 marked the introduction of a brand new **object model** for PHP.

Every class starts with the word *class* followed by its *name* and the *class definition* (inside curly brackets):

```php
class Car {

  // class definition goes here

}
```

---

# Properties

Properties are defined by using the visibility keywords **public**, **protected**, or **private**, followed by a variable declaration.

This declaration may include an initialization, but this initialization must be a constant value.

```php
class Car {
  private $plate = '12-34-AB';
  private $driver = 'John Doe';
}
```

Properties can also be *coercively* and *strictly* typed:

```php
class Car {
  private string $plate = '12-34-AB';
  private string $driver = 'John Doe';
}
```

---

# Methods

Methods are like functions that have access to the private properties of the class. They also have the same visibility keywords as properties.

However, due to the dynamic typed nature of PHP, to access these properties the pseudo-variable **$this** must be used:

```php
class Car {
  private $plate;
  private $driver = 'John Doe';

  public function getDriver() : string {
    return $this->driver; // return $driver would have returned null
  }
}
```

Methods can also be *coercively* and *strictly* typed.

---

# Creating

To create an instance of a class, we use the **new** keyword.

An object will always be created unless the object has a constructor defined that throws an exception on error.

```php
$car = new Car();
```

---

# Constructors

PHP allows developers to declare constructor methods for classes.

Classes that have a constructor method, call this method on each newly-created object.

The constructor method is always called **__construct** and can receive any number of parameters. The destructor method is, as expected, called **__destruct**.

```php
class Car {
  private $plate;
  private $driver;

  public function __construct($driver, $plate) {
    $this->driver = $driver;
    $this->plate = $plate;
  }

}

$car = new Car('John Doe', '12-34-AB');
```

---

# Extends

A class can inherit the methods and properties of another class by using the keyword extends in the class declaration. 

Extending from multiple classes is impossible; a class can only inherit from one base class.

```php
class RaceCar extends Car {

  // Specific race car definitions

}
```

---

# Static

The static keyword allows us to define static properties and methods shared between all class instances.

```php
class Car {
  static public $mile = 1.609344; //km
  // ...
}

echo Car::mile;
```

Static members can be accessed using the name of the class and the **::** operator.

Obviously, **$this** cannot be used inside a static method.

---
# Scope

These are used to access **static properties or methods** from inside the class definition:

* **self::** - the current class
* **parent::** - the parent class
* **static::** - the class of the current object

```php
class Car {
  static private $mile = 1.609344; //km

  public function __construct($driver, $plate) {
    parent::__construct($driver, $plate);
  }

  public static function milesToKm($miles) {
    return $miles * static::mile;
  }
}

echo Car::milesToKm(10);
```

---

# Self vs. Static

```php
class Foo
{
  protected static $bar = 'fizz';

  public function print() {
    echo static::$bar;
    echo self::$bar;
  }
}

class Bar extends Foo
{
  protected static $bar = 'buzz';
}

$foo = new Foo();
$bar = new Bar();

$foo->print();  // fizz fizz
$bar->print();  // buzz fizz
```

Read [more](https://www.php.net/manual/en/language.oop5.late-static-bindings.php).

---

# Abstract

* Classes defined as abstract may not be instantiated.
* Classes that contain abstract methods must be abstract.
* Methods defined as abstract do not have an implementation.

```php
abstract class Car {
  private $plate;
  private $driver = 'John Doe';

  public function getDriver() {
    return $this->driver;
  }

  abstract public function getPlate();
}
```

---

# Interfaces

* We use the **interface** keyword to define an interface, just as we use the *class* keyword to define a class.
* Interfaces are just like classes, but their methods do not have an implementation.
* The **implements** keyword specifies that a specific class implements the interface.

```php
interface Car {
  public function getDriver() : string;
  public function getPlate() : string;
}

class RaceCar implements Car {
  private $plate;
  private $driver;

  public function getDriver() : string {
    return $this->driver;
  }

  public function getPlate() : string {
    return $this->plate;
  }
}
```  

---

# Final

The *final* keyword prevents child classes from overriding a method.

If the class itself is *final*, it cannot be extended.

```php
final class RaceCar implements Car {
  private $plate;
  private $driver;

  public function getDriver() : string {
    return $this->driver;
  }

  final public function getPlate() : string {
    return $this->plate;
  }
}
```

---

template:inverse
name:exceptions
# Exceptions

---

# Exceptions

Exceptions are events that disrupt the normal flow of instructions.

As in other programming languages, exceptions can be **thrown** and **caught**.

To throw an exception we use the throw keyword:

```php
if ($db == null)
  throw new Exception('Database not initialized');
```

---

# Exceptions

**Exception** is a class with the following public methods:

```php
final public string getMessage ();
final public Exception getPrevious ();
final public mixed getCode ();
final public string getFile ();
final public int getLine ();
final public array getTrace ();
final public string getTraceAsString ();
```

User-defined exceptions can be defined by extending the built-in *Exception* class.

---

# Try and Catch

The **try-catch** statement consists of a try block followed by one or more catch clauses, which specify handlers for different exceptions.

```php
try {
  $car = getCar($id);
} catch (DatabaseException $e) {
  echo 'Database error: ' . $e->getMessage();
} catch (Exception $e) {
  echo 'Unknown error: ' . $e->getMessage();
}
```

---

template:inverse
name:databases
# Databases

---

# PDO

The PHP Data Objects ([PDO](https://www.php.net/manual/en/book.pdo.php)) extension defines a lightweight, consistent interface for accessing databases in PHP.

---

# Connecting

To connect to a database, we use a [PDO](https://www.php.net/manual/en/class.pdo.php) object.

The connection string is database-dependent.

```php
$dbh = new PDO('mysql:host=localhost;dbname=test', $user, $pass);
```

```php
$dbh = new PDO('pgsql:host=localhost;port=5432;dbname=anydb', 
               $user, $pass);
```

```php
$dbh = new PDO('sqlite:database.db');
```

---

# Prepared Statements

Prepared statements (first [prepare](https://www.php.net/manual/en/pdo.prepare.php), then [execute](https://www.php.net/manual/en/pdostatement.execute.php)) are the recommended way of executing queries as they prevent **SQL injection** attacks (more on this later):

```php
$stmt = $dbh->prepare('INSERT INTO person (name, address)
                       VALUES (:name, :address)');

$stmt->bindParam(':name', $name);
$stmt->bindParam(':address', $address);

$stmt->execute();
```

---

# Prepared Statements

Another form of prepared statements:

```php
$stmt = $dbh->prepare('INSERT INTO person (name, address) 
                       VALUES (?, ?)');
                       
$stmt->execute(array($name, $address));
```

Values are bound to each question mark by their order.

---

# Getting Results

To get the query results, we use the [fetch](https://www.php.net/manual/en/pdostatement.fetch.php) function.

This function fetches one row at a time and returns *false* if there are no more rows.

```php
$stmt = $dbh->prepare('SELECT * FROM person WHERE name = ?');
$stmt->execute(array($name));

while ($row = $stmt->fetch()) {
  echo $row['address'];
}
```

---

# Getting Results

The [fetchAll](https://www.php.net/manual/en/pdostatement.fetchall.php) function returns the complete result as an array of rows.

```php
$stmt = $dbh->prepare('SELECT * FROM person WHERE name = ?');
$stmt->execute(array($name));

$result = $stmt->fetchAll()

foreach ($result as $row) {
  echo $row['address'];
}
```

Using *fetchAll* might take too much memory if the result size is substantial.

---

# Fetch Mode

Query results can return results in several different modes. Some of them:

* PDO::FETCH_ASSOC: returns an array indexed by column name.
* PDO::FETCH_NUM: returns an array indexed by column number.
* PDO::FETCH_BOTH (default): returns an array indexed by both column name and 0-indexed column number.

Changing the default fetch mode (has to be done every time a connection is created):

```php
$dbh->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);
```

---

# Transactions

Unfortunately, not every database supports transactions, so PDO needs to run in what is known as "auto-commit" mode when you first open the connection.

If you need a transaction, you must use the [beginTransaction](https://www.php.net/manual/en/pdo.begintransaction.php) method to initiate one.

```php
$dbh->beginTransaction();

// queries go here

$dbh->commit; // or $dbh->rollBack();
```

To close a transaction we can either use [commit](https://www.php.net/manual/en/pdo.commit.php) or [rollBack](https://www.php.net/manual/en/pdo.commit.php).

---

# Error Handling

PDO offers you a choice of 3 different error handling strategies:

* **PDO::ERRMODE_SILENT** The default mode. No error is shown. You can use the errorCode()
  and errorInfo() on both database and statement objects to inspect the error.

* **PDO::ERRMODE_WARNING** Similar to previous one but a warning is shown.

* **PDO::ERRMODE_EXCEPTION** In addition to setting the error code, PDO will throw a PDOException and set its properties to reflect the error code and error information.

---

# Error Handling

Setting the default error handling strategy:

```php
$dbh->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
```

Using PDO exceptions:

```php
try {
  $stmt = $dbh->prepare("SELECT * FROM person WHERE name = ?");
  $stmt->execute(array($name));

  $result = $stmt->fetchAll()
} catch (PDOException $e) {
  // Do something about it...
  echo $e->getMessage();
}
```

---

template:inverse
name:parameters
# HTTP Parameters

---

# Query String

The **query string** allows extra information to be sent to a webserver when requesting a resource.

<img src="assets/php/url.svg">

```html
<a href="newsitem.php?id=10">
```

```html
<form action="search.php" method="get"> <!-- search.php?q=... -->
  <input type="search" name="q">
  <button type="submit">
</form>
```

For a form with *method="post"*, it works the same way but the information is sent separately from the URL (more on this later).

---

# HTTP Parameters

Extra information sent to a resource, can be accessed in a PHP script using two different arrays, **$_GET** and **$_POST**, depending on the way the information was sent.

```html
<a href="newsitem.php?id=10">
```

```php
$id = $_GET['id'];  // On newsitem.php
```
***
```html
<form action="search.php" method="post">
  <input type="search" name="q">
  <button type="submit">
</form>
```

```php
$q = $_POST['q'];  // On search.php
```

These arrays are **superglobal**, or **automatically global**, variables. There is no need to do *"global $variable;"* to access them within functions or methods.

---

template:inverse
name:sessions
# Sessions

---

# Cookies

* The HTTP protocol is a **stateless** protocol.

* No state information is stored on the server.
<br><small>Every request must be understood in isolation.</small>

* Cookies are a mechanism for storing data in the browser.
<br><small>That is sent to the server in every request.</small>

![](assets/php/cookies.svg)

---

# Cookies

Cookies can be set using the **setcookie** function:

```php
bool setcookie (string $name, string $value, int $expire = 0, 
                string $path, string $domain, bool $secure = false,
                bool $httponly = false)
```

* All parameters are optional except the *cookie name*.
* Cookies must be sent before any output from your script.<br><small>This is an HTTP protocol restriction.</small>
* This requires that you place calls to this function prior to any output, including any **whitespace**.

You can access the cookies sent by the browser using the special **$_COOKIE** array.

---

# Sessions

As cookies are stored in the browser, they **cannot be used** as a secure mechanism for storing sensitive information (*e.g.*, the current user).

Sessions are a mechanism that can be used to persist state information between page requests in the server:

* A **unique session identifier** is stored on the **client** (*e.g.*, using a cookie).
* The **server** keeps any **session information** associated with that **session id**.

![](assets/php/sessions.svg)

---

# Sessions in PHP

PHP automatically manages sessions. When a session is started:

1. Retrieve session information:
 * if a *session id* is received (usually from a cookie), **retrieve** any state information for that id.
 * if no *session id* is received, **generate** a new *session id* and **send** it to the client (usually to a cookie).
2. Populate the **$_SESSION** superglobal array with session information associated with the *session id*.
3. When the script ends, serialize the **$_SESSION** contents and store them.

---

# Session Start

Sessions can be started using the **session_start** function:

```php
bool session_start (void)
```

* Like other header functions, sessions must be started before any output from your script.<br><small>Because we are using cookies.</small>

* Normally called in every page to ensure session variables are always accessible.

```php
session_start();

var_dump($_SESSION);               // inspect session variables

$_SESSION['username'] = $username; // modify session variables
```

---

# Session Destroy

The function **session_destroy** destroys all of the data associated with the current session.

```php
bool session_destroy (void)
```

It must be called after calling **session_start()**.

---

# Session Parameters

The parameters of the cookie used for the session cookie can be changed using the **session_set_cookie_params** function.

```php
void session_set_cookie_params 
  (int $lifetime, string $path, string $domain,
   bool $secure = false, bool $httponly = false)
```

All parameters are optional except *lifetime*.

* **lifetime** of the session cookie, defined in seconds. The value 0 means "until the browser is closed.
* **path** on the domain where the cookie will work. Use a single slash ('/') for all paths on the domain.
* Cookie **domain**, for example 'www.fe.up.pt'. To make cookies visible on all subdomains, then the domain must be prefixed with a dot, *e.g.*, '.fe.up.pt'.

We will talk about the *secure* and *httponly* parameters when we talk about security.

---
# Storing Passwords

---

# Hash Functions

Password should never be stored in plain text. Instead you should use a one-way hashing function.

```php
echo md5('apple');  
// 1f3870be274f6c49b3e31a0c6728957f
echo sha1('apple');
// d0be2dc421be4fcd0172e5afceea3970e2f3d940
echo hash('sha256', 'apple');
// 3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b
```

We will talk about better ways of storing passwords when we talk about security.

---
template:inverse
name:headers
# HTTP Headers

---

# Header

The header function sends a raw HTTP header to the browser.

* This can be used, for example, to redirect the browser to another page:

```php
header('Location: another_page.php');
```

* Headers must be sent before any output from your script.<br><small>This is a protocol restriction.</small>
* Do not forget that this does not stop the execution of the script. 
* If you want to stop execution you must follow this instruction with **die()** or **exit()**.

We will talk more about headers when we study the HTTP protocol.

---

template:inverse
name:includes
# Includes

---

# Includes

* The **include** statement includes and evaluates the specified file.

* The **require** statement is identical to include, except, upon failure, it will also produce a fatal **E_COMPILE_ERROR** level error.

* The **include_once** statement is identical to include, except PHP will check if the file has already been included.

* The **require_once** statement is identical to require, except PHP will check if the file has already been included.

```php
include_once('other_file.php');
```

---

# Relative Includes

In PHP, includes are relative to the **file requested** by the browser, not the file that contains the 'include'. This means that:

```php
  b/Y.php // file requested by the browser
  b/Z.php // file included by Y.php

  //Y.php only needs to do: include('Z.php')
```

But:

```php
  a/X.php // file requested by the browser
  b/Y.php // file included by X.php
  b/Z.php // file included by Y.php

  //X.php needs to do: include('../b/Y.php')
  //Y.php needs to do: include('../b/Z.php')
```

---

# Magic Constants

To make including files in PHP more manageable, we can use the following [magic constants](https://www.php.net/manual/en/language.constants.magic.php):

```php
__FILE__ // The full path and filename of the current file.
__DIR__  // The folder of the current file.
```

And the following function that returns the folder of a file:

```php
string dirname ( string $path [, int $levels = 1 ] )
```

For example:

```php
dirname(__FILE__) // same as __DIR__
dirname(__DIR__)  // returns the parent folder of the current file
```

.box_info[
  Magic constants change value depending on where they are used!

---
template:inverse
name:json
# JSON

---

# JSON

* JSON (**J**ava**S**cript **O**bject **N**otation) is a *lightweight data-interchange format*. <small>Some alternatives are [YAML](https://yaml.org/) and [TOML](https://toml.io/en/).</small>
* It is easy for **humans** to read and write.
* It is easy for **machines** to parse and generate.

```json
[
  {
   "id":"1",
   "title":"Mauris...",
   "introduction":"Sed eu...",
   "fulltext":"Donec feugiat..."
  }, {
   "id":"2",
   "title":"Etiam efficitur...",
   "introduction":"Cum sociis ...",
   "fulltext":"Donec feugiat..."
  }

```

---

#JSON

The **json_encode** and **json_decode** functions can be used to encode from and to JSON easily.

```php
$encoded = json_encode($posts);
$decoded = json_decode($encoded); //$decoded === $posts
```

Don't forget to tell the client your are sending JSON data:

```php
$data = getSomeData();
header('Content-Type: application/json; charset=utf-8');
echo json_encode($data);
```

---

# Best Practices

---

# Validate your input

Never trust the user:

```php
  if (empty($_GET['username']) || length($_GET['username'] > 20))
    // Do something about it
```

Always verify if the data you are receiving is in the expected format.

---

# Separate your PHP and HTML code

Always start by calculating/querying all your data, and only after that output HTML.

```php
<?php
  $stmt = $dbh->prepare('SELECT * FROM car WHERE make = ?');
  $stmt->execute(array($make));

  $cars = $stmt->fetchAll();
?>
<body>
<?php foreach ($cars as $car) { ?>
  <ul>
    <li><strong>Model:</strong> <?=$car['model']?></li>
    <li><strong>Price:</strong> <?=$car['price']?></li>
  </ul>
<?php } ?>
</body>
```

You can use the short *echo* version to make your code look nicer.

**Tip**: PHP delimiters can break in the middle of a block and pick up later.

---

# Don't Repeat Yourself (DRY)

Use include and/or functions to avoid code repetitions:

```php
// inside database/cars.php
function getAllCars(PDO $dbh) : array { 
  $stmt = $dbh->prepare('SELECT * FROM car WHERE make = ?');
  $stmt->execute(array($make));

  $cars = $stmt->fetchAll();
}
```

```php
include ('database/connection.php');
include ('database/cars.php');
$cars = getAllCars($dbh);
```

---

# Don't Repeat Yourself (DRY)

Use include and/or functions to avoid code repetitions:

```html
<html> <!-- inside templates/header.html -->
  <head>
    <title>My Site</title>
    <meta charset="utf-8">
  </head>
  <body>
```

```html
  </body> <!-- inside templates/footer.html -->
</html>
```

---

# Don't Repeat Yourself (DRY)

Use include and/or functions to avoid code repetitions:

```php
<?php
  include ('database/connection.php');
  include ('database/cars.php');
  $cars = getAllCars($dbh);

  include ('templates/header.html');

  foreach ($cars as $car) { ?>

    <ul>
      <li><strong>Model:</strong> <?=$car['model']?></li>
      <li><strong>Price:</strong> <?=$car['price']?></li>
    </ul>

<? }
  include ('templates/footer.html');
?>
```

---

# Templates

You can also create and reuse **parameterized** functions that output HTML code:

```php
<?php function drawCarList(array $cars) { ?>
  <?php foreach ($cars as $car) { ?>
  <ul>
    <li><strong>Model:</strong> <?=$car['model']?></li>
    <li><strong>Price:</strong> <?=$car['price']?></li>
  </ul>
  <?php } ?>
<?php } ?>
```

---

# Templates

And in the end, you will get clean PHP code:

```php
<?php
  include ('database/connection.php');
  include ('database/cars.php');

  include ('templates/common.php');
  include ('templates/cars.php');

  $cars = getAllCars($dbh);

  drawHeader();       // from templates/common.php
  drawCarList($cars); // from templates/cars.php
  drawFooter();       // from templates/common.php
?>
```

---

# Separate Actions from Views

**Never mix** scripts that **return** data with scripts that **change** data:

  * **list_articles.php**
    * Shows all news.
    * Has links to each one of the news articles **view_article.php**.
  * **view_article.php**
    * Shows one news article and its comments.
    * Receives the id of the article.
    * Link to **edit_article.php**.
  * **edit_article.php**
    * Shows a form that allows the user to edit a news article.
    * Submits to **save_article.php**.
  * **save_article.php**
    * Receives the new data for the news article.
    * Saves it in the database and redirects to **view_item.php** (on success).

---

# Separate Actions from Views

![](assets/php/best-practices.svg)

---

# Extra Stuff

* Functions: [Dates](http://php.net/manual/en/ref.datetime.php), [Image Processing](http://php.net/manual/en/book.image.php)
* Charts: [jpGraph](http://jpgraph.net/), [pChart](http://pchart.sourceforge.net/index.php), [phpChart](https://phpchart.com/), [Charts 4 PHP](https://www.chartphp.com/)
* Standard Library: [SPL](http://php.net/manual/en/book.spl.php)
* Dependency Manager: [Composer](https://getcomposer.org/)
* Template Engines: [Twig](https://twig.symfony.com/), [Blade](https://laravel.com/docs/blade), [Smarty](http://www.smarty.net/)
* Frameworks: [CodeIgniter](https://codeigniter.com/), [CakePHP](http://cakephp.org/), [Symfony](http://symfony.com/), [Zend](http://framework.zend.com/), [Laravel](http://laravel.com/), ...





---

---

template:inverse
# Regular Expressions
<a href="http://www.fe.up.pt/~arestivo">André Restivo</a>

---

name:index
# Index

1. [Introduction](#intro)
1. [Literal Characters](#literal)
1. [Character Classes](#classes)
1. [Zero-Length Matches](#zero-length)
1. [Alternation](#alternation)
1. [Quantifiers](#quantifiers)
1. [Grouping and Capturing](#grouping)
1. [Backreferences](#backreferences)
1. [Backtracking](#backtracking)
1. [Lookaround](#lookaround)
1. [NFA](#nfa)
1. [In HTML](#html)
1. [In PHP](#php)
1. [In Javascript](#javascript)

---

name:intro
# Introduction

---

# Regular Expressions

A sequence of characters that forms a **search pattern**.

Used in:

* Data validation.
* Search and Replace.
* Parsing.

---

# Variants

* There are **several** different regular expression **processors**.
* All of them translate regular expressions into a Nondeterministic Finite Automaton (**NFA**).
* But can have slightly **different syntaxes**.

---

# Matching

* Matching is the process of **applying** a regular expression **pattern** to a text string and finding
  strings that are represented by that pattern.
* When **validating**, we normally expect the **whole** string to match the pattern.
* When **searching**, we expect a **substring** of that string to match the pattern.

---

# References

* [Online Regular Expression Tester](http://regex101.com/)
* [Regular Expressions Tutorial](http://www.regular-expressions.info/tutorial.html)
* [Regex Golf](https://alf.nu/RegexGolf)
* [Regex Crossword](https://regexcrossword.com/)
* [Mail RFC822 Regexp](http://ex-parrot.com/~pdw/Mail-RFC822-Address.html)

---

# Literal Characters

---

# Literal Characters

A literal character matches the first occurrence of that character in the string.

```text
a
```

.box_regexp[
I **a**te an apple.

You can tell the processor to **match all occurrences** if needed.

.box_regexp[
I **a**te **a**n **a**pple.

---

# Literal Characters

A series of literal characters, matches those same characters in the same order.

```text
at
```

.box_regexp[
I **at**e an apple.

---

# Special Characters

There are twelve characters that have special meanings in regular expressions:

```text
\ ^ $ . | ? * + ( ) [ {
```

To match any of these symbols, you need to escape them with a **backslash**.

```text
\+
```

.box_regexp[
1**+**1=2

All other characters should **not** be escaped as the backslash also has special meaning.

---

#Non-Printable Characters

* **\t** - tab
* **\r** - carriage return
* **\n** - line feed

---

# Character Classes

---

# Character Classes

A character class, or set, matches **only one** out of several characters.

```text
gr[ae]y
```

Matching all occurrences:

.box_regexp[
**gray** or **grey**

---

# Ranges

You can use an hyphen to specify ranges in a character class.

```text
[0-9a-fA-F]
```

This matches all digits from '0' to '9' and all letters from 'a' to 'f' (both in lowercase and uppercase).

.box_regexp[
Th**e** cat is inside the box.

---

# Negated

A **caret**(^) after the opening square bracket negates the character class.

```text
[^A-Za-f]
```

This matches all letters except those in uppercase and from 'a' to 'f'.

.box_regexp[
T**h**e cat is inside the box.

---

# Special Characters

Inside a character class, the only special characters are:

```text
] \ ^ -
```

All others do not need to be escaped.

---

#Shorthand Character Classes

* **\d** digit - the same as **[0-9]**
* **\w** word character - the same as **[A-Za-z0-9_]**
* **\s** whitespace character - the same as **[ \t\r\n\f]**

* **\D** not a digit - the same as **[^0-9]** or **[^\d]**
* **\W** not a word character - the same as **[^A-Za-z0-9_]** or **[^\w]**
* **\S** not a whitespace character - the same as **[^ \t\r\n\f]** or **[^\s]**

---

# Dot

The **dot**(.) matches any character except line breaks.

```perl
c.t
```

.box_regexp[
The **cat** is inside the box.

---

# Zero Length Matches

---

# Anchors

Anchors can be used to specify the position of the matched string.

* The **caret**(^) matches the position before the first character in the string.
* The **dollar sign**($) matches right after the last character in the string.
* We can use both anchors to validate a complete string.

```perl
boys$
```

Matching all occurrences:

.box_regexp[
Everyone knows boys will be **boys**

---

# Word Boundaries

* The metacharacter **\b** is an anchor.
* It matches at a position that is called a *word boundary*.
* It always produces a zero-length match.
* This allows you to do whole word searches.

```perl
\bis\b
```

.box_regexp[
This island **is** beautiful.

---

# Alternation

---

# Alternation

The **vertical bar**(|) allows you to match a single regular expression out of several possible regular expressions.

```perl
cat|dog
```

Matching all occurrences:

.box_regexp[
I like both **cat**s and **dog**s.

---

# Quantifiers

---

# Optional Items

The **question mark**(?) makes the preceding token in the regular expression optional.

```perl
colou?r
```

Matching all occurrences:

.box_regexp[
Do you write **color** our **colour**s?

---

# Repetition quantifiers

Repetition **quantifiers** allow the preceding token to repeat:

* The **star**(*) allows the token to repeat 0 or more times.
* The **plus**(+) allows the token to repeat 1 or more times.

```perl
[0-9]+
```

.box_regexp[
My phone number is **12345**.

The **question mark**(?) is also a repetition **quantifier** that allows the token to repeat 0 or 1 times.

---

# Custom Repetitions

Using **curly brackets**({}) we can specify the maximum and minimum number of repetitions:

Repeat exactly 9 times:

```php
[0-9]{9}
```

Repeat between 1 and 3 times:

```perl
[0-9]{1,3}
```

Repeat at least twice:

```perl
[0-9]{2,}
```

Repeat at most three times:

```perl
[0-9]{,3}
```

---

# Repetitions are Greedy

By default, regular expression processors try to match as many characters as possible when handling repetitions.

```php
<.+>
```

.box_regexp[
This tea is **```<```strong```>```good```<```/strong```>```**.

This might cause unexpected effects.

---

# Lazy Repetitions

To make repetitions lazy, we add a **question mark**(?) after the repetition operator.

```perl
<.+?>
```

Matching all occurrences:

.box_regexp[
This tea is **```<```strong```>```**good**```<```/strong```>```**.

---

# Being lazy is hard work!

The reason why repetitions are greedy by default, is because being lazy forces the processor to **backtrack** more often.

An **alternative** would be using **negated classes**:

```php
<[^>]+>
```

Matching all occurrences:

.box_regexp[
This tea is **```<```strong```>```**good**```<```/strong```>```**.

---

# Grouping and Capturing

---

#Grouping

Putting part of a pattern inside **parentheses** creates a group.

Groups can be used to apply **quantifiers** and **alternation** to specific parts of the pattern.

```html
((https?|ftp)://)?www\.example\.com
```

Matching all occurrences:

.box_regexp[
**ftp://www.example.com** or just **www.example.com**

---

# Capturing

Groups are automatically **captured** and **numbered**.

This allow you to **extract** different parts of the matched expression.

```html
(cats|dogs) are (lazy|smart)
```

.box_regexp[
i think **cats are lazy**

* Group #0: cats are lazy
* Group #1: cats
* Group #2: lazy

The **complete** match is always group **#0**.

---

# Capturing

## Other Example

```html
((https?|ftp)://)?www\.example\.com
```

.box_regexp[
**http://www.example.com**

* Group #0: http://www.example.com
* Group #1: http://
* Group #2: http

---

# Non Capturing

Sometimes we want to create a group without capturing it. To do that we start the group with a **question mark**(?) and a **colon**(:):

```html
(?:(?:https?|ftp)://)?www\.example\.com
```

.box_regexp[
**http://www.example.com**

* Group #0: http://www.example.com

---

# Backreferences

---

# Backreferences

Backreferences can be used to match the same text twice.

Some regular expression processor use **\n** to reference captured groups while other use **$n**.

Number with at least 3 digits and where the first number is the same as the last:

```html
([0-9])[0-9]+\1
```

.box_regexp[
**1231**

---

# Backtracking

---

# Backtracking

Although regular expression processors are greedy, they can backtrack if they fail to find a match.

```html
([0-9])[0-9]+\1
```

.box_regexp[
41231

Here, the processor starts by matching the 4 but when it fails to find another 4 in the text it backtracks and tries to start with the 1.

.box_regexp[
4**1231**

---

# Lookaround

---

# Lookahead and lookbehind

**Lookahead** and **lookbehind** are **zero-length** **assertions** (just like the start and end of line, and word boundaries)

* These are also called **lookaround** assertions.
* They match characters but then **give up the match** without consuming the characters.
* They only **assert** whether a match is possible or not.

---

#Positive lookahead

Using **?=** we can match something followed by something else: 

```html
(cat|dog)(?=s)
```

Matches *cat* or *dog* if followed by an *s*:

.box_regexp[
My dog is not like other **dog**s.

---

#Negative lookahead

Using **?!** we can match something **not** followed by something else: 

```html
(cat|dog)(?!s)
```

Matches *cat* or *dog* if **not** followed by an *s*:

.box_regexp[
All the cats are smarter than my **cat**.

---

#Positive lookbehind

**?<=** tells the processor to temporarily **step backwards** in the string and check if the text inside the lookbehind can be **matched** there.

```perl
(?<=is)land
```

Matches *land* if preceded by *is*:

.box_regexp[
England is part of an is**land**.

---

#Negative lookbehind

**?<!** Tells the processor to temporarily **step backwards** in the string and check if the text inside the lookbehind **cannot** be matched there.

```perl
(?<!some)thing
```

Matches *thing* if it is **not** preceded by *some*:

.box_regexp[
There is something about this **thing**.

---

template:inverse
# Nondeterministic Finite Automaton

---

# Regular Expressions are NFAs

**D**eterministic **F**inite **A**utomaton (DFA) are finite state machines where:

* each of its transitions is **uniquely** determined by its **source** state and **input** symbol, and
* reading an input symbol is **required** for each state transition.

Non-deterministic Finite Automaton don't need to obey these restrictions.

Regular expressions can [easily](https://www.youtube.com/watch?v=RYNN-tb9WxI) be transformed into NFAs. And NFA can [easily](https://www.youtube.com/watch?v=taClnxU-nao) be transformed into DFAs.

https://cyberzhg.github.io/toolbox/nfa2dfa

---

# Example

```perl
(a(b|c)+a)|([a-z])*T
```

![](assets/regexp/dfa.svg)

---

template:inverse
# In HTML

---

# Form Validation

In HTML, input elements have a pattern attribute that can contain a regular expression pattern specifying the allowed values of the field.

```html
<input type="text" pattern="\d{9}|\d{3}-\d{3}-\d{3}">
```

---

template:inverse
# In PHP

---

# Patterns

* PHP uses Perl-Compatible Regular Expressions (PCRE)
* In PHP, patterns must be delimited by either **forward-slashes** (/), **hash** signs (#) or **tildes** (~).

```php
/ab|c/
```

* This means that the chosen delimiter must be **escaped** inside the pattern.
* You may add [pattern modifiers](http://php.net/manual/en/reference.pcre.pattern.modifiers.php) after the ending delimiter.

```php
/ab|c/i
```

For example, the **i** pattern modifier makes the pattern case **insensitive**.

---

# preg_match

```php
int preg_match (string $pattern ,string $subject [,array &$matches])
```

The [preg_match](http://php.net/manual/en/function.preg-match.php), searches *subject* for a match to the regular expression given in *pattern*.

* If matches is provided, then it is filled with the results of the search.
* Returns 1 if the pattern matches given subject, 0 if it does not and false if an error occurred.

```php
preg_match('/(\d{4})(?:-(\d{3}))?/', '4100-122', $matches);
print_r($matches);
```

```text
Array ( [0] => 4100-122
        [1] => 4100
        [2] => 122 )
```

---

# preg_match_all

```php
int preg_match_all (string $pat, string $subj [,array &$matches])
```

The [preg_match_all](http://php.net/manual/en/function.preg-match-all.php), searches *subject* for **all** matches to the regular expression given in *pattern*.

* If matches is provided, then it is filled with all the results of the search in a multi-dimensional array.
* Returns the number of full pattern matches and false if an error occurred.

```php
preg_match_all('/(\d{4})(?:-(\d{3}))?/', '4100-122 4200', $matches);
print_r($matches);
```

```text
Array ( [0] => Array ([0] => 4100-122 [1] => 4200)
        [1] => Array ([0] => 4100 [1] => 4200)
        [2] => Array ([0] => 122 [1] => ) )
```

---

# preg_replace

```php
mixed preg_replace (mixed $pat, mixed $repl, mixed $subj)
```

The [preg_replace](http://php.net/manual/en/function.preg-replace.php) function, searches *subject* for matches to *pattern* and replaces them with *replacement*.

The replacement can contain backreferences in the form $n or ${n}.

```php
echo preg_replace('/(cat|dog)/', 'my $1s', 'dog are dog');
```

Result:

```bash
my dogs are my dogs
```

---

# Validation

Using the **preg_match** function, we can easily validate data using regular expressions:

```php
function is_phone_number($element) {
	return preg_match ("/^\d{9}|\d{3}-\d{3}-\d{3}$/", $element);
}
```

Don't forget the beginning and end of string anchors.

---

# Cleaning

You can also use the **preg_replace** function to clean up input data before storing it in the database.

```php
$text = preg_replace('/[^\w\d\s\.!,\?]/', '', $_GET['text']);
```

---

template:inverse
# In Javascript

---

# Patterns

* In javascript, patterns must be delimited by **forward-slashes** (/).
* This means that the forward-slashes must be **escaped** inside the pattern.
* You may add modifiers after the ending delimiter:

The **g** modifier is used to perform a global match (find all matches).

The **i** modifier is used to perform a case insensitive match.

---

# test

```javascript
regexObj.test(str)
```

The [test](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/test) function, tests for a match in a string. It returns true or false.

```javascript
console.log(/(\d{4})(?:-(\d{3}))?/.test('4100-122'));
```

Result:

```bash
true
```

---

# match

```javascript
str.match(regexp)
```

The [match](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/match) function, executes a search for a regular expression in a string.

```javascript
console.log('4100-122 4200'.match(/(\d{4})(?:-(\d{3}))?/))
console.log('4100-122 4200'.match(/(\d{4})(?:-(\d{3}))?/g))
```

Result:

```bash
["4100-122", "4100", "122", index: 0, input: "4100-122 4200"]
["4100-122", "4200"]
```

---

# search

```javascript
str.search([regexp])
```

If successful, [search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/search) returns the index of the first match of the regular expression inside the string.

```javascript
console.log('Zip code is 4100-122'.search(/(\d{4})(?:-(\d{3}))?/))
```

Result:

```bash
12
```

---

# replace

```javascript
str.replace(regexp, replacement)
```

The replacement can contain backreferences in the form $n.

```javascript
console.log('dog are dog'.replace(/(cat|dog)/, 'my $1s'))
console.log('dog are dog'.replace(/(cat|dog)/g, 'my $1s'))
```

Result:

```bash
my dogs are dog
my dogs are my dogs
```

---

# Validation

Using the **test** function, we can easily validate data using regular expressions:

```javascript
function is_phone_number(element) {
  return /^\d{9}|\d{3}-\d{3}-\d{3}$/.test(element)
}
```

Don't forget the beginning and end of string anchors.





---

---

template:inverse
# Web Security
<a href="http://www.fe.up.pt/~arestivo">André Restivo</a>

---

name:index
# Index

1. [Introduction](#intro)
1. [Path Traversal](#path)
1. [SQL Injection](#sql)
1. [Cross-site Scripting](#xss)
1. [Cross-site Request Forgery](#csrf)
1. [Man-in-the-Middle](#maninthemiddle)
1. [Credential Storage](#credential)
1. [Passwords](#passwordright)

---

name:intro
template:inverse

# Introduction

---

# Attacks and Vulnerabilities

* A **vulnerability** is a **flaw** or **weakness** in an application &mdash; whether in its design or implementation &mdash; that **can be exploited** by an attacker to compromise the security or functionality of the system, potentially causing harm to its stakeholders.

* An **attack** is a **technique** or **method** used by an attacker to **exploit** a vulnerability in order to gain unauthorized access, disrupt operations, or otherwise compromise the system.

Reference: [Open Web Application Security Project](https://www.owasp.org/)

---

# OWASP Top 10 (2013)

* Injection
* Broken Authentication and Session Management
* Cross-Site Scripting (XSS)
* Insecure Direct Object References
* Security Misconfiguration
* Sensitive Data Exposure
* Missing Function Level Access Control
* Cross-Site Request Forgery (CSRF)
* Using Components with Known Vulnerabilities
* Unvalidated Redirects and Forwards

[OWASP Top 10 - 2013](https://owasp.org/www-pdf-archive/OWASP_Top_10_-_2013.pdf)

---

# OWASP Top 10 (2017)

* Injection
* Broken Authentication
* Sensitive Data Exposure
* XML External Entities
* Broken Access Control
* Security Misconfiguration
* Cross-Site Scripting (XSS)
* Insecure Deserialization
* Using Components with Known Vulnerabilities
* Insufficient Logging & Monitoring

[OWASP Top 10 - 2017](https://owasp.org/www-project-top-ten/2017/)

---

# OWASP Top 10 (2021)

* Broken Access Control <br><small>including **CSRF**</small>
* Cryptographic Failures <br><small>including **no HTTPS**</small>
* Injection <br><small>including **SQL Injection** and **XSS**</small>
* Insecure Design
* Security Misconfiguration
* Vulnerable and Outdated Components
* Identification and Authentication Failures <br><small>including bad **password management**</small>
* Software and Data Integrity Failures
* Security Logging and Monitoring Failures
* Server-Side Request Forgery (SSRF)

[OWASP Top 10 - 2021](https://owasp.org/Top10/)

---

# Security Impact

* Financial losses
* Theft of intellectual property
* Damage to brand reputation
* Fraudulent activities
* Legal liability and regulatory exposure
* Extortion and ransom demands

---

# Path Traversal Attack

---

# Path Traversal Attack

An attacker exploits **file path manipulation** &mdash; typically using the <code>..</code> (parent directory) and <code>/</code> (directory separator) symbols &mdash; to **gain access** to files and directories outside the intended scope.

```http
http://www.foo.com/../../database.db
```

Normally, web servers are well protected against serving files **outside** the designated **root** directory, but the application itself can also be targeted:

```http
http://www.foo.com/page.php?page=../../database.db
```

```http
http://www.foo.com/viewimage.php?path=viewimage.php
```

Such attacks can expose sensitive files such as **configuration files**, **source code**, or **credentials** if proper input validation is not enforced.

---

# Preventing

A common example is attempting to access version control metadata such as the .git directory:

```http
http://www.foo.com/.git/config
```

To prevent this, ensure that the web server is configured to serve **only the necessary files and directories**. Sensitive files and folders &mdash; such as <code>.git</code>, configuration files, environment variables (<code>.env</code>), sqlite database, and other sensitive files &mdash; should never be exposed over HTTP.

If you are using PHP, **serve only a specific public folder** (*e.g.*, <code>/public</code>) that contains the pages, action handlers, and API entry points. All other application files &mdash; including logic, configuration, and version control &mdash; should reside outside the web root and be inaccessible via HTTP.

---

# Preventing

A common vulnerable pattern is including **user-controlled** input directly in file paths:

```http
http://www.foo.com/index.php?page=news
```

Vulnerable code:

```php
  include('header.php');
  include($_GET['page']);
  include('footer.php');
```

Secure alternative using a fixed allowlist:

```php
  include('header.php');
  if ($page == 'news') include('news.php');
  if ($page == 'login') include('login.php');
  include('footer.php');
```

---

# SQL Injection

---

# SQL Injection

SQL Injection is the **manipulation** of SQL queries through **input data** sent from the client to the application.

SQL injection **attacks** can allow an attacker to:

* Spoof **identities** (e.g., impersonate other users).
* Tamper with existing **data** (insert, update, or delete records).
* Extract sensitive **information** (full disclosure of database contents).
* Gain **administrative** access to the database server.
* Execute arbitrary **commands**, in some cases, depending on database configuration.

---

# Disclosure of data

```php
// $username has the name of the logged in user
$dbh->query("SELECT * FROM items 
             WHERE owner = '" . $username . "'");
```

Create an account with username: <span class="inline-code">johndoe' OR 1 = 1--</span>

```sql
SELECT * FROM items WHERE owner = 'johndoe' OR 1 = 1--'
```

---

# Spoof identity

```php
// verifies if username and password are correct
$dbh->query("SELECT * FROM users WHERE " .
      "username = '" . $username . "' " . 
      "AND password ='" . $password . "'");
```

Use these credentials to login: 

<span class="inline-code">username: "johndoe" and password: "' OR 1 = 1; --"</span>

```sql
SELECT * users 
WHERE username = 'johndoe' 
AND password = '' OR 1 = 1; --'
```

---

# Gain privileges

```php
// searches for specific item
$dbh->query("SELECT * FROM items WHERE title = '" . $title . "'");
```

Navigate to URL:

```http
http://foo.com/search.php?title='; INSERT INTO users VALUES
('johndoe', 'password', true); --
```

Third parameter has admin status of user:

```sql
SELECT * FROM items WHERE title = ''; INSERT INTO users VALUES
('johndoe', 'password', true); --'
```

---

# Preventing

To prevent SQL injection, consider the following best practices:

* Use **Prepared Statements** (Parameterized Queries): This ensures that user input is treated as data, not executable code.
* Escape all user-supplied input: While parameterized queries are **preferred**, escaping input can be an **additional layer** of defense.

```php
$stmt = $dbh->prepare('SELECT * FROM items WHERE title = ?');
$stmt->execute(array($title));
$items = $stmt->fetchAll();
```

[SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)

---

# Cross-site Scripting (XSS)

---

# Cross-site Scripting (XSS)

Cross-Site Scripting (XSS) attacks are a type of **injection**, in which **malicious scripts** are injected into otherwise benign and trusted websites.

---

# Types

There are several types of XSS attacks:

* **Stored** XSS: The malicious script is stored on the server (e.g., in a database) and is served to users when they access the compromised page.
* **Reflected** XSS: The malicious script is reflected off a web server, typically via user input in URLs, form submissions, or query strings.
* **DOM-based** XSS: The vulnerability is in the client-side code, where the DOM (Document Object Model) is manipulated by malicious input.

---

# XSS : Stored

```php
<?php
 $stmt = $dbh->prepare("INSERT INTO comment 
                        VALUES (DEFAULT, ?, ?, ?)");
 $stmt->execute(array($_POST['postid'], $_POST['text'], 
                      $_SESSION['username']));
?>
```

```php
<?php
 $stmt = $dbh->prepare("SELECT * FROM comment WHERE postid = ?");
 $stmt->execute(array($_POST['postid']));
 $comments = $stmt->fetchAll();
?>

<?php foreach($comments as $comment) {?>
  <div class="comment"><?=$comment['text']?></div>
<?php } ?>
```

Comments can contain malicious code that is stored and shown to all users:

```http
comment.php?postid=10&text=<script>alert("hacked")</script>
```

---

# XSS : Reflected

Reflected XSS occurs when malicious scripts are **reflected off the web server**, typically via user input in URLs, form submissions, or query strings. The script is executed **immediately** after being included in the server's response, affecting **users who click the link**.

```php
<?php
echo "You searched for: " . $_GET["query"];
// List search results
?> 
```

In this code, the user’s search query is directly echoed into the response without any sanitization or escaping.

```http
http://foo.com/search.php?query=<script>alert("hacked")</script>
```

---

# XSS : DOM-based

DOM-based XSS occurs when a vulnerability in the client-side code allows malicious input to be executed in the browser. The attack is typically triggered by manipulating the Document Object Model (DOM), where user input is inserted directly into the page without proper sanitization or escaping.

```javascript
  const query = new URLSearchParams(window.location.search).get('q')
  document.getElementById('searchResult').innerHTML = query
```

In this code, the user’s search query is directly echoed into the response without any sanitization or escaping.

```http
http://foo.com/search.php?query=<script>alert("hacked")</script>
```

---

# Preventing

Never put untrusted data:

* directly in a **script**
* inside an **HTML comment**
* in an **attribute name**
* in a **tag name**
* directly in **CSS**
* inside **non-safe attribute** values

---

# Preventing

**Validation** ensures that user input matches an expected pattern, rejecting any unexpected characters or formats.

```php
if ( !preg_match ("/^[a-zA-Z\s]+$/", $_GET['name'])) {
  // ERROR: Name can only contain letters and spaces
}
```

**Filtering** removes unwanted characters, sanitizing the input before processing it.

```php
$name = preg_replace ("/[^a-zA-Z\s]/", '', $_GET['name']);
```

---

# Preventing

When **displaying** untrusted data on the web page, always **encode** it to prevent malicious scripts from being executed using functions like [htmlspecialchars()](http://php.net/manual/en/function.htmlspecialchars.php) or [htmlentities()](http://php.net/manual/en/function.htmlentities.php):

```php
<?=htmlentities($post['text'])?>     // encodes all characters
<?=htmlspecialchars($post['text'])?> // encodes only special chars
```

So that this:

```html
<script>alert("hacked")</script>
```

Becomes this:

```html
&#x3C;script&#x3E;alert(&#x22;hacked&#x22;)&#x3C;/script&#x3E;
```

---

# Preventing

When using untrusted data to **create URLs**, always **encode** the data to prevent malicious content from being executed using [urlencode()](http://php.net/manual/en/function.urlencode.php):

```php
<a href="search.php?q=<?=urlencode($_GET['q'])?>">
```

So that this:

```http
search.php?q=<script>alert("hacked")</script>
```

Becomes this:

```http
search.php?q%3D%3Cscript%3Ealert(%22hacked%22)%3C%2Fscript%3E
```

---

# Preventing : Advanced Techniques

Context-aware Encoding:

 * When writing untrusted data in various **locations** (attributes, tag names, comments, etc.), use context-aware encoders like [PHP-ESAPI](https://github.com/OWASP/PHP-ESAPI).

Allowing HTML?:

 * [strip_tags()](https://www.php.net/manual/en/function.strip-tags.php) **isn't enough**. 
 * Use libraries like [HTML Purifier](http://htmlpurifier.org/) to properly **filter** and **sanitize** user-generated HTML.
 * HTML Purifier ensures only safe HTML is allowed, removing malicious tags or attributes while keeping valid content.

---

# Preventing in Javascript

HTML Escape Before Inserting Untrusted Data into HTML Element Content

```javascript
const entityMap = {
  "&": "&amp;",
  "<": "&lt;",
  ">": "&gt;",
  '"': '&quot;',
  "'": '&#39;',
  "/": '&#x2F;'
};

function escapeHtml(string) {
  return String(string).replace(/[&<>"'\/]/g, function (s) {
    return entityMap[s];
  });
}
```

Not enough in all locations; use **context-aware encoders**. For example [OWASP ESAPI for Javascript](https://github.com/ESAPI/owasp-esapi-js).

---

# Cookies

* Preventing all XSS flaws is **difficult**, but you can **mitigate the impact** by securing your session cookies.
* Set the [HTTPOnly](https://owasp.org/www-community/HttpOnly) flag on your **session cookie** to **prevent** client-side scripts from **accessing** the cookie. 
* This is a key defense against XSS attacks **targeting session cookies**.

Use [session-set-cookie-params](http://php.net/manual/en/function.session-set-cookie-params.php) before starting your session:

```php
session_set_cookie_params(0, '/', 'www.fe.up.pt', true, true);
```

If the HttpOnly flag is included in the HTTP response header, the cookie **cannot be accessed** through a client-side script.

---

# XSS Mantra

.center[
## "filter input, encode output"

Read more:

* [OWASP XSS Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
* [OWASP DOM Based XSS Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html)
* [OWASP XSS Filter Evasion Cheat Sheet](https://www.owasp.org/index.php/XSS_Filter_Evasion_Cheat_Sheet)
* [A comprehensive tutorial on cross-site scripting](https://excess-xss.com/)

---

template:inverse
# Cross-site Request Forgery (CSRF)

---

# Cross-site Request Forgery (CSRF)

CSRF occurs when an attacker tricks a user into submitting a state-changing request without their knowledge or consent.

**Example**: The application allows state-changing requests that don’t require any secret (e.g., an authentication token).

```http
http://foo.com/transfer.php?amount=1500&destination=4673243
```

**Example**: The attacker constructs a malicious request that performs a state-changing action (e.g., transferring money) and embeds it in a hidden image request:

```html
<img
  src="http://foo.com/transfer.php?amount=1500&destination=4673243"
  width="0" height="0" />
```

If the victim is already authenticated to <code>foo.com</code>, this request will automatically be sent with the victim’s session information, performing the action without the victim’s knowledge.

---

# Things that do NOT WORK

Common techniques like secret cookies, POST-only restrictions, and multi-step transactions **are not sufficient** to prevent CSRF.

* Using a Secret Cookie
* Only Accepting POST Requests
* Multi-Step transactions

These methods **DO NOT WORK**

---

# Preventing

Effective prevention requires using **anti-CSRF tokens** and ensuring proper request validation.

* **Generate** a random token per session
* **Store** this token as a session variable
* **Send** this token as part of every (sensitive) request
* **Verify** the token is correct on every page

[OWASP CSRF](https://owasp.org/www-community/attacks/csrf)

---

# Preventing

```php
function generate_random_token() {
  return bin2hex(openssl_random_pseudo_bytes(32));
}
```

```php
session_start();
if (!isset($_SESSION['csrf'])) {
  $_SESSION['csrf'] = generate_random_token();
}
```

```php
<form action="transfer.php">
  <input type="hidden" name="csrf" value="<?=$_SESSION['csrf'])?>">
</form>
```

```php
session_start();
\\...
if ($_SESSION['csrf'] !== $_POST['csrf']) {
  // ERROR: Request does not appear to be legitimate
}
```

---

name:maninthemiddle
# Man-in-the-middle Attack

---

# Man-in-the-middle Attack

* **Intercept** a communication between two systems.
* Using different techniques, the attacker **splits** the original TCP connection into 2 new connections, one between the client and the attacker and the other between the attacker and the server
* Once the TCP connection is intercepted, the attacker acts as a **proxy**, being able to read, insert and modify the data in the intercepted communication.

.smaller[
  ![](assets/security/maninthemiddle.png)

---

# Public-key Cryptography

Also known as **asymmetric** cryptography, is a class of cryptographic algorithms that requires two separate keys, one of which is private and one of which is public.

* If the sender **signs** a message with his private key, any receiver can **verify** that the message was sent by him.
* If a sender **encrypts** a message with a public key, **only** the receiver having the private key can read that message.
* Let's see how this works without going too deep into the [math](https://www.onebigfluke.com/2013/11/public-key-crypto-math-explained.html) behind it.

---

# Public-key Cryptography

.smaller[
  ![](assets/security/publickey.png)

---

# Man-in-the-middle (again)

* Using encryption is **not enough** because every encryption method requires an additional exchange or transmission of information over a secure channel (e.g. the public key).

.smaller[
  ![](assets/security/maninthemiddle2.png)

* The solution is to use public keys that have been signed by a **certificate authority** (CA).

---

# Digital Signature

* Digital signatures are a scheme that allows the demonstration of a message's **authenticity**.
* For efficiency reasons, **normally only a hash** of the original message is signed.

.smaller[
  ![](assets/security/signature.png)

---

# Certificates

* Certificates are small data files that digitally **bind** a **cryptographic key** to an **organization**.
* By signing a certificate, a **Certificate Authority (CA)** states that it **verified** the organization's information.

.smaller[
  ![](assets/security/certificate.png)

---

# Certificate Authority

* Web browsers **trust** websites based on CAs that come **pre-installed** (Verisign/Comodo/Microsoft/...).
* The user trusts the CA to **vouch** only for **legitimate websites**.
* The website **provides** a **valid** certificate, which means it was signed by a trusted authority.
* The certificate **correctly identifies** the website.
* The user trusts that the protocol's encryption layer (TLS/SSL) is sufficiently **secure** against eavesdroppers.

---

# Chain of Thrust

* A **certificate chain** is an **ordered list** of certificates, where each one certifies the next until a root certificate is reached.
* This allows browsers to only **pre-install a few** root certificates.

.smaller[
  ![](assets/security/authorities.png)

---

# HTTPS

* **H**yper**t**ext **T**ransfer **P**rotocol **S**ecure (HTTPS) is just HTTP on top of the **SSL/TLS** protocol.
* The browser uses the **pre-installed CAs certificates** to verify the authenticity of the **server's public key**.

.smaller[
  ![](assets/security/https.png)

.center[
For **efficiency** reasons, public-key cryptography is used to exchange a **symmetric key** that is used for the rest of the session (SSL handshake).

---

# Credential Storage

---

# Password Transmission

Passwords have to be sent from the browser to the server. But they should **never**:

* Be sent over **HTTP** (only HTTPS) to prevent man-in-the-middle attacks or eavesdropping.
* Be sent using **GET** parameters as they will be displayed in the URL.
* Be encrypted in the browser. <small>Being able to capture the encrypted password would be the same as capturing the plain text password.</small>

---

# Hashing

In the case of a database breach, having passwords stored in **clear text**, allows the attacker to have **instant** access to **all** user passwords.

So passwords should be stored as hashes:

* Hash algorithms are **one-way** functions. They turn any amount of data into a **fixed-length** *fingerprint* that **cannot** be reversed.
* Small changes in the original text produce **completely different hashes**.

---

# Hashing Workflow

* The user **creates** an account by entering a username and password.
* Their password is **hashed** and **stored** in the database.
* When the user attempts to login, the **hash** of the password they entered is **checked** against the **hash** of their real password.
* If the hashes **match**, the user is granted **access**. If not, the user is told they entered invalid login credentials.

```php
$stmt = $db->prepare(INSERT INTO users VALUES (?, ?))';
$stmt->execute(array($username, md5($password)));
```

```php
$stmt = $db->prepare('SELECT * FROM users 
                      WHERE username = ? AND password = ?');

$stmt->execute(array($username, md5($password)));

if ($stmt->fetch() !== false) {
  $_SESSION['username'] = $username;
}  
```

---

# Cracking Hashes

* **Brute Force Attacks** - Try every possible combination of characters up to a given length.
* **Dictionary Attack** - Try every password and variants from a file. These files come from dictionaries and real password databases.
* **Lookup Tables** - Pre-computed tables containing passwords hashes in a password dictionary.
* **Rainbow Tables** - Rainbow tables are a time-memory trade-off technique. Slower but can store more hashes. [Examples](https://freerainbowtables.com/).

---

# Using Salt

* Lookup tables and rainbow tables only work because each password is hashed the **exact same way**.
* We can prevent this by **appending** a string to each password making pre-existing rainbow tables useless.
* This is called adding **salt** to a password. <small>"Everything is better with salt."</small>

---

# Salt Reuse

Using the same salt for every user is **ineffective**:

* Two users with the **same password** will still have the same hash.
* The attacker can generate a **rainbow table** for that specific salt.
* Finding the salt is relatively easy (especially if the salt is short).

---

# Double Hashing

Double hashing passwords, sometimes with different hashing algorithms, can make hashes **less secure**.

---

# Hashing Algorithm

* There are several hashing algorithms available. Some of them are currently considered **weaker** ([MD5](https://www.mscs.dal.ca/~selinger/md5collision/), [SHA1](https://shattered.io/)).
* More secure hashing functions should be used like SHA256, SHA512 or bcrypt (blowfish).

---

# Slow Hash Functions

* High-end graphics cards (GPUs) and custom hardware can compute **billions of hashes per second** making brute force attacks still very effective.
* The goal is to make the hash function **slow enough** to impede attacks, but still **fast enough** to not cause a noticeable delay for the user.
* Key stretching is implemented using a special type of **CPU-intensive** hash function (e.g. **bcrypt**).
* These algorithms take a **security factor** or iteration count as an argument. This value determines how slow the hash function will be.

---

# Secret Key

* By adding a **secret fixed key** to all passwords, we prevent an attacker that only gained access to the database, to even try to crack the passwords.
* This key has to be **kept secret** from an attacker even in the event of a breach.
* The key must be stored in an **external system**, such as a physically separate server dedicated to password validation.
* One can even use special **dedicated hardware** to store this secret key.

---

template:inverse
# Passwords Done Right

---

# Salt

* Salt should be generated using a Cryptographically Secure Pseudo-Random Number Generator (**CSPRNG**).
* The salt needs to be **unique** per user.
* The salt needs to be **long**.

---

# Generating

* Prepend the **salt** to the **password** and **hash** it with a standard cryptographic hash function such as **bcrypt**.
* Save both the salt and the hash in the **user's database record**.

---

# Validating

* Retrieve the user's **salt** and **hash** from the database.
* Prepend the **salt** to the given **password** and **hash** it using the same hash function.
* Compare the **hash** of the given password with the **hash** from the database.

Read more: [Hashing Security](https://crackstation.net/hashing-security.htm)

---

# Passwords in PHP

The recommended method to hash and validate passwords in PHP is by using the [password-hash](http://php.net/manual/en/function.password-hash.php) and [password-verify](http://php.net/manual/en/function.password-verify.php) functions.

```php
string password_hash (string $pwd , integer $algo [, array $opts])
```

```php
boolean password_verify ( string $pwd , string $hash )
```

* These functions generate their own salt.
* The **hash** function returns the used algorithm, cost and salt as part of the hash. Therefore, all information that's needed to verify the hash is included in it.
* This allows the **verify** function to verify the hash without needing separate storage for the salt or algorithm.

.smaller[
![](assets/security/password_hash.svg)

---

# PHP Example

```php
<?php
  $options = ['cost' => 12];
  $stmt = $db->prepare(INSERT INTO users VALUES (?, ?))';
  $stmt->execute(array(
    $username,
    password_hash($password, PASSWORD_DEFAULT, $options))
  );
```

```php
<?php
  $stmt = $db->prepare('SELECT * FROM users WHERE username = ?');
  $stmt->execute(array($username));
  $user = $stmt->fetch();

  if ($user && password_verify($password, $user['password'])) {
    $_SESSION['username'] = $username;
  }  
```

The current default algorithm is **bcrypt**.

---

# More on Passwords

* Make sure your usernames/userids are case **insensitive** (even emails).
* Implement proper **password strength** controls.
* Do **not** apply short or no length, character set, or encoding restrictions on the entry or storage of credentials.
* Design password storage **assuming** eventual compromise.

[OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)

[OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)



