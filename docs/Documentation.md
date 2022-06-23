---
title: Cornershop API v1
language_tabs:
  - shell: Shell
  - http: HTTP
  - javascript: JavaScript
  - ruby: Ruby
  - python: Python
  - php: PHP
  - java: Java
  - go: Go
toc_footers: []
includes: []
search: true
highlight_theme: darkula
headingLevel: 2

---

<!-- Generator: Widdershins v4.0.1 -->

<h1 id="cornershop-api">Cornershop API v1</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

Cornershop API documentation

Base URLs:

* <a href="http://127.0.0.1:8000/">http://127.0.0.1:8000/</a>

<a href="https://www.google.com/policies/terms/">Terms of service</a>
Email: <a href="mailto:cestrada1716@gmail.com">Support</a> 
 License: BSD License

# Authentication

- HTTP Authentication, scheme: basic 

<h1 id="cornershop-api-cornershop_food">cornershop_food</h1>

## cornershop_food_api_v1_login_view_list

<a id="opIdcornershop_food_api_v1_login_view_list"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://127.0.0.1:8000/cornershop_food/api/v1/login_view

```

```http
GET http://127.0.0.1:8000/cornershop_food/api/v1/login_view HTTP/1.1
Host: 127.0.0.1:8000

```

```javascript

fetch('http://127.0.0.1:8000/cornershop_food/api/v1/login_view',
{
  method: 'GET'

})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

result = RestClient.get 'http://127.0.0.1:8000/cornershop_food/api/v1/login_view',
  params: {
  }

p JSON.parse(result)

```

```python
import requests

r = requests.get('http://127.0.0.1:8000/cornershop_food/api/v1/login_view')

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','http://127.0.0.1:8000/cornershop_food/api/v1/login_view', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://127.0.0.1:8000/cornershop_food/api/v1/login_view");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://127.0.0.1:8000/cornershop_food/api/v1/login_view", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /cornershop_food/api/v1/login_view`

This class handles the render of a login page.

<h3 id="cornershop_food_api_v1_login_view_list-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## cornershop_food_api_v1_login_view_create

<a id="opIdcornershop_food_api_v1_login_view_create"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://127.0.0.1:8000/cornershop_food/api/v1/login_view

```

```http
POST http://127.0.0.1:8000/cornershop_food/api/v1/login_view HTTP/1.1
Host: 127.0.0.1:8000

```

```javascript

fetch('http://127.0.0.1:8000/cornershop_food/api/v1/login_view',
{
  method: 'POST'

})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

result = RestClient.post 'http://127.0.0.1:8000/cornershop_food/api/v1/login_view',
  params: {
  }

p JSON.parse(result)

```

```python
import requests

r = requests.post('http://127.0.0.1:8000/cornershop_food/api/v1/login_view')

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','http://127.0.0.1:8000/cornershop_food/api/v1/login_view', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://127.0.0.1:8000/cornershop_food/api/v1/login_view");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://127.0.0.1:8000/cornershop_food/api/v1/login_view", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /cornershop_food/api/v1/login_view`

This class handles the render of a login page.

<h3 id="cornershop_food_api_v1_login_view_create-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|none|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## cornershop_food_api_v1_menu_list

<a id="opIdcornershop_food_api_v1_menu_list"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://127.0.0.1:8000/cornershop_food/api/v1/menu \
  -H 'Accept: application/json'

```

```http
GET http://127.0.0.1:8000/cornershop_food/api/v1/menu HTTP/1.1
Host: 127.0.0.1:8000
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('http://127.0.0.1:8000/cornershop_food/api/v1/menu',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get 'http://127.0.0.1:8000/cornershop_food/api/v1/menu',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('http://127.0.0.1:8000/cornershop_food/api/v1/menu', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','http://127.0.0.1:8000/cornershop_food/api/v1/menu', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://127.0.0.1:8000/cornershop_food/api/v1/menu");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://127.0.0.1:8000/cornershop_food/api/v1/menu", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /cornershop_food/api/v1/menu`

This class handles the creation of a new menu and
retrive all menus in the system.

> Example responses

> 200 Response

```json
{
  "id": "string",
  "name": "string",
  "menu_date": "string",
  "options": [
    "string"
  ]
}
```

<h3 id="cornershop_food_api_v1_menu_list-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Created|[MenuObject](#schemamenuobject)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|BadRequest|[forbiden](#schemaforbiden)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## cornershop_food_api_v1_menu_create

<a id="opIdcornershop_food_api_v1_menu_create"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://127.0.0.1:8000/cornershop_food/api/v1/menu \
  -H 'Accept: application/json'

```

```http
POST http://127.0.0.1:8000/cornershop_food/api/v1/menu HTTP/1.1
Host: 127.0.0.1:8000
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('http://127.0.0.1:8000/cornershop_food/api/v1/menu',
{
  method: 'POST',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.post 'http://127.0.0.1:8000/cornershop_food/api/v1/menu',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.post('http://127.0.0.1:8000/cornershop_food/api/v1/menu', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','http://127.0.0.1:8000/cornershop_food/api/v1/menu', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://127.0.0.1:8000/cornershop_food/api/v1/menu");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://127.0.0.1:8000/cornershop_food/api/v1/menu", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /cornershop_food/api/v1/menu`

This class handles the creation of a new menu and
retrive all menus in the system.

> Example responses

> 201 Response

```json
{
  "id": "string",
  "name": "string",
  "menu_date": "string",
  "options": [
    "string"
  ]
}
```

<h3 id="cornershop_food_api_v1_menu_create-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created|[MenuObject](#schemamenuobject)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|[ApiBadResponse](#schemaapibadresponse)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|[forbiden](#schemaforbiden)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## cornershop_food_api_v1_menu_view_read

<a id="opIdcornershop_food_api_v1_menu_view_read"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://127.0.0.1:8000/cornershop_food/api/v1/menu/view/{id} \
  -H 'Accept: application/json'

```

```http
GET http://127.0.0.1:8000/cornershop_food/api/v1/menu/view/{id} HTTP/1.1
Host: 127.0.0.1:8000
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('http://127.0.0.1:8000/cornershop_food/api/v1/menu/view/{id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get 'http://127.0.0.1:8000/cornershop_food/api/v1/menu/view/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('http://127.0.0.1:8000/cornershop_food/api/v1/menu/view/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','http://127.0.0.1:8000/cornershop_food/api/v1/menu/view/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://127.0.0.1:8000/cornershop_food/api/v1/menu/view/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://127.0.0.1:8000/cornershop_food/api/v1/menu/view/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /cornershop_food/api/v1/menu/view/{id}`

This class handles the render of a menu page.

<h3 id="cornershop_food_api_v1_menu_view_read-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "id": "string",
  "name": "string",
  "menu_date": "string",
  "options": [
    "string"
  ]
}
```

<h3 id="cornershop_food_api_v1_menu_view_read-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Ok|[MenuObject](#schemamenuobject)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|BadRequest|[forbiden](#schemaforbiden)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## cornershop_food_api_v1_menu_update

<a id="opIdcornershop_food_api_v1_menu_update"></a>

> Code samples

```shell
# You can also use wget
curl -X PUT http://127.0.0.1:8000/cornershop_food/api/v1/menu/{id} \
  -H 'Accept: application/json'

```

```http
PUT http://127.0.0.1:8000/cornershop_food/api/v1/menu/{id} HTTP/1.1
Host: 127.0.0.1:8000
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('http://127.0.0.1:8000/cornershop_food/api/v1/menu/{id}',
{
  method: 'PUT',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.put 'http://127.0.0.1:8000/cornershop_food/api/v1/menu/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.put('http://127.0.0.1:8000/cornershop_food/api/v1/menu/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PUT','http://127.0.0.1:8000/cornershop_food/api/v1/menu/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://127.0.0.1:8000/cornershop_food/api/v1/menu/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "http://127.0.0.1:8000/cornershop_food/api/v1/menu/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PUT /cornershop_food/api/v1/menu/{id}`

This class handles the update of a menu.

<h3 id="cornershop_food_api_v1_menu_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "id": "string",
  "name": "string",
  "menu_date": "string",
  "options": [
    "string"
  ]
}
```

<h3 id="cornershop_food_api_v1_menu_update-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Ok|[MenuObject](#schemamenuobject)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|[ApiBadResponse](#schemaapibadresponse)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|BadRequest|[forbiden](#schemaforbiden)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## cornershop_food_api_v1_menu_dashboard_list

<a id="opIdcornershop_food_api_v1_menu_dashboard_list"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://127.0.0.1:8000/cornershop_food/api/v1/menu_dashboard

```

```http
GET http://127.0.0.1:8000/cornershop_food/api/v1/menu_dashboard HTTP/1.1
Host: 127.0.0.1:8000

```

```javascript

fetch('http://127.0.0.1:8000/cornershop_food/api/v1/menu_dashboard',
{
  method: 'GET'

})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

result = RestClient.get 'http://127.0.0.1:8000/cornershop_food/api/v1/menu_dashboard',
  params: {
  }

p JSON.parse(result)

```

```python
import requests

r = requests.get('http://127.0.0.1:8000/cornershop_food/api/v1/menu_dashboard')

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','http://127.0.0.1:8000/cornershop_food/api/v1/menu_dashboard', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://127.0.0.1:8000/cornershop_food/api/v1/menu_dashboard");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://127.0.0.1:8000/cornershop_food/api/v1/menu_dashboard", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /cornershop_food/api/v1/menu_dashboard`

This class handles the render of get menu page.

<h3 id="cornershop_food_api_v1_menu_dashboard_list-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## cornershop_food_api_v1_option_list

<a id="opIdcornershop_food_api_v1_option_list"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://127.0.0.1:8000/cornershop_food/api/v1/option \
  -H 'Accept: application/json'

```

```http
GET http://127.0.0.1:8000/cornershop_food/api/v1/option HTTP/1.1
Host: 127.0.0.1:8000
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('http://127.0.0.1:8000/cornershop_food/api/v1/option',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get 'http://127.0.0.1:8000/cornershop_food/api/v1/option',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('http://127.0.0.1:8000/cornershop_food/api/v1/option', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','http://127.0.0.1:8000/cornershop_food/api/v1/option', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://127.0.0.1:8000/cornershop_food/api/v1/option");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://127.0.0.1:8000/cornershop_food/api/v1/option", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /cornershop_food/api/v1/option`

This class handles the creation of a new option and
retrive all options in the system.

> Example responses

> 200 Response

```json
{
  "id": "string",
  "name": "string",
  "price": "string",
  "description": "string"
}
```

<h3 id="cornershop_food_api_v1_option_list-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Created|[OptionObject](#schemaoptionobject)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|[forbiden](#schemaforbiden)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## cornershop_food_api_v1_option_create

<a id="opIdcornershop_food_api_v1_option_create"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://127.0.0.1:8000/cornershop_food/api/v1/option \
  -H 'Accept: application/json'

```

```http
POST http://127.0.0.1:8000/cornershop_food/api/v1/option HTTP/1.1
Host: 127.0.0.1:8000
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('http://127.0.0.1:8000/cornershop_food/api/v1/option',
{
  method: 'POST',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.post 'http://127.0.0.1:8000/cornershop_food/api/v1/option',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.post('http://127.0.0.1:8000/cornershop_food/api/v1/option', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','http://127.0.0.1:8000/cornershop_food/api/v1/option', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://127.0.0.1:8000/cornershop_food/api/v1/option");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://127.0.0.1:8000/cornershop_food/api/v1/option", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /cornershop_food/api/v1/option`

This class handles the creation of a new option and
retrive all options in the system.

> Example responses

> 201 Response

```json
{
  "id": "string",
  "name": "string",
  "price": "string",
  "description": "string"
}
```

<h3 id="cornershop_food_api_v1_option_create-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created|[OptionObject](#schemaoptionobject)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|[ApiBadResponse](#schemaapibadresponse)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|[forbiden](#schemaforbiden)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## cornershop_food_api_v1_option_update

<a id="opIdcornershop_food_api_v1_option_update"></a>

> Code samples

```shell
# You can also use wget
curl -X PUT http://127.0.0.1:8000/cornershop_food/api/v1/option/{id} \
  -H 'Accept: application/json'

```

```http
PUT http://127.0.0.1:8000/cornershop_food/api/v1/option/{id} HTTP/1.1
Host: 127.0.0.1:8000
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('http://127.0.0.1:8000/cornershop_food/api/v1/option/{id}',
{
  method: 'PUT',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.put 'http://127.0.0.1:8000/cornershop_food/api/v1/option/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.put('http://127.0.0.1:8000/cornershop_food/api/v1/option/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PUT','http://127.0.0.1:8000/cornershop_food/api/v1/option/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://127.0.0.1:8000/cornershop_food/api/v1/option/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "http://127.0.0.1:8000/cornershop_food/api/v1/option/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PUT /cornershop_food/api/v1/option/{id}`

This class handles the update of an option.

<h3 id="cornershop_food_api_v1_option_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "id": "string",
  "name": "string",
  "price": "string",
  "description": "string"
}
```

<h3 id="cornershop_food_api_v1_option_update-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Ok|[OptionObject](#schemaoptionobject)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|[ApiBadResponse](#schemaapibadresponse)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|BadRequest|[forbiden](#schemaforbiden)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## cornershop_food_api_v1_options_list

<a id="opIdcornershop_food_api_v1_options_list"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://127.0.0.1:8000/cornershop_food/api/v1/options

```

```http
GET http://127.0.0.1:8000/cornershop_food/api/v1/options HTTP/1.1
Host: 127.0.0.1:8000

```

```javascript

fetch('http://127.0.0.1:8000/cornershop_food/api/v1/options',
{
  method: 'GET'

})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

result = RestClient.get 'http://127.0.0.1:8000/cornershop_food/api/v1/options',
  params: {
  }

p JSON.parse(result)

```

```python
import requests

r = requests.get('http://127.0.0.1:8000/cornershop_food/api/v1/options')

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','http://127.0.0.1:8000/cornershop_food/api/v1/options', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://127.0.0.1:8000/cornershop_food/api/v1/options");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://127.0.0.1:8000/cornershop_food/api/v1/options", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /cornershop_food/api/v1/options`

This class handles the render of get options page.

<h3 id="cornershop_food_api_v1_options_list-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## cornershop_food_api_v1_order_list

<a id="opIdcornershop_food_api_v1_order_list"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://127.0.0.1:8000/cornershop_food/api/v1/order \
  -H 'Accept: application/json'

```

```http
GET http://127.0.0.1:8000/cornershop_food/api/v1/order HTTP/1.1
Host: 127.0.0.1:8000
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('http://127.0.0.1:8000/cornershop_food/api/v1/order',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get 'http://127.0.0.1:8000/cornershop_food/api/v1/order',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('http://127.0.0.1:8000/cornershop_food/api/v1/order', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','http://127.0.0.1:8000/cornershop_food/api/v1/order', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://127.0.0.1:8000/cornershop_food/api/v1/order");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://127.0.0.1:8000/cornershop_food/api/v1/order", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /cornershop_food/api/v1/order`

This class handles the creation of a new order and
retrive all orders in the system.

> Example responses

> 200 Response

```json
{
  "id": "string",
  "menu": "string",
  "create_at": "string",
  "option": "string",
  "commentary": "string",
  "quantity": 0
}
```

<h3 id="cornershop_food_api_v1_order_list-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Created|[OrderObject](#schemaorderobject)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|BadRequest|[forbiden](#schemaforbiden)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## cornershop_food_api_v1_order_create

<a id="opIdcornershop_food_api_v1_order_create"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://127.0.0.1:8000/cornershop_food/api/v1/order \
  -H 'Accept: application/json'

```

```http
POST http://127.0.0.1:8000/cornershop_food/api/v1/order HTTP/1.1
Host: 127.0.0.1:8000
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('http://127.0.0.1:8000/cornershop_food/api/v1/order',
{
  method: 'POST',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.post 'http://127.0.0.1:8000/cornershop_food/api/v1/order',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.post('http://127.0.0.1:8000/cornershop_food/api/v1/order', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','http://127.0.0.1:8000/cornershop_food/api/v1/order', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://127.0.0.1:8000/cornershop_food/api/v1/order");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://127.0.0.1:8000/cornershop_food/api/v1/order", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /cornershop_food/api/v1/order`

This class handles the creation of a new order and
retrive all orders in the system.

> Example responses

> 201 Response

```json
{
  "id": "string",
  "menu": "string",
  "create_at": "string",
  "option": "string",
  "commentary": "string",
  "quantity": 0
}
```

<h3 id="cornershop_food_api_v1_order_create-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created|[OrderObject](#schemaorderobject)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|[ApiBadResponse](#schemaapibadresponse)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|[forbiden](#schemaforbiden)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## cornershop_food_api_v1_order_view_list

<a id="opIdcornershop_food_api_v1_order_view_list"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://127.0.0.1:8000/cornershop_food/api/v1/order_view

```

```http
GET http://127.0.0.1:8000/cornershop_food/api/v1/order_view HTTP/1.1
Host: 127.0.0.1:8000

```

```javascript

fetch('http://127.0.0.1:8000/cornershop_food/api/v1/order_view',
{
  method: 'GET'

})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

result = RestClient.get 'http://127.0.0.1:8000/cornershop_food/api/v1/order_view',
  params: {
  }

p JSON.parse(result)

```

```python
import requests

r = requests.get('http://127.0.0.1:8000/cornershop_food/api/v1/order_view')

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','http://127.0.0.1:8000/cornershop_food/api/v1/order_view', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://127.0.0.1:8000/cornershop_food/api/v1/order_view");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://127.0.0.1:8000/cornershop_food/api/v1/order_view", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /cornershop_food/api/v1/order_view`

This class handles the render of get orders page.

<h3 id="cornershop_food_api_v1_order_view_list-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## cornershop_food_api_v1_order_view_create

<a id="opIdcornershop_food_api_v1_order_view_create"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://127.0.0.1:8000/cornershop_food/api/v1/order_view

```

```http
POST http://127.0.0.1:8000/cornershop_food/api/v1/order_view HTTP/1.1
Host: 127.0.0.1:8000

```

```javascript

fetch('http://127.0.0.1:8000/cornershop_food/api/v1/order_view',
{
  method: 'POST'

})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

result = RestClient.post 'http://127.0.0.1:8000/cornershop_food/api/v1/order_view',
  params: {
  }

p JSON.parse(result)

```

```python
import requests

r = requests.post('http://127.0.0.1:8000/cornershop_food/api/v1/order_view')

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','http://127.0.0.1:8000/cornershop_food/api/v1/order_view', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://127.0.0.1:8000/cornershop_food/api/v1/order_view");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://127.0.0.1:8000/cornershop_food/api/v1/order_view", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /cornershop_food/api/v1/order_view`

This class handles the render of get orders page.

<h3 id="cornershop_food_api_v1_order_view_create-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|none|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## cornershop_food_api_v1_orders_dashboard_list

<a id="opIdcornershop_food_api_v1_orders_dashboard_list"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://127.0.0.1:8000/cornershop_food/api/v1/orders_dashboard

```

```http
GET http://127.0.0.1:8000/cornershop_food/api/v1/orders_dashboard HTTP/1.1
Host: 127.0.0.1:8000

```

```javascript

fetch('http://127.0.0.1:8000/cornershop_food/api/v1/orders_dashboard',
{
  method: 'GET'

})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

result = RestClient.get 'http://127.0.0.1:8000/cornershop_food/api/v1/orders_dashboard',
  params: {
  }

p JSON.parse(result)

```

```python
import requests

r = requests.get('http://127.0.0.1:8000/cornershop_food/api/v1/orders_dashboard')

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','http://127.0.0.1:8000/cornershop_food/api/v1/orders_dashboard', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://127.0.0.1:8000/cornershop_food/api/v1/orders_dashboard");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://127.0.0.1:8000/cornershop_food/api/v1/orders_dashboard", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /cornershop_food/api/v1/orders_dashboard`

This class handles the render of get orders page.

<h3 id="cornershop_food_api_v1_orders_dashboard_list-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## cornershop_food_api_v1_users_create

<a id="opIdcornershop_food_api_v1_users_create"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://127.0.0.1:8000/cornershop_food/api/v1/users

```

```http
POST http://127.0.0.1:8000/cornershop_food/api/v1/users HTTP/1.1
Host: 127.0.0.1:8000

```

```javascript

fetch('http://127.0.0.1:8000/cornershop_food/api/v1/users',
{
  method: 'POST'

})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

result = RestClient.post 'http://127.0.0.1:8000/cornershop_food/api/v1/users',
  params: {
  }

p JSON.parse(result)

```

```python
import requests

r = requests.post('http://127.0.0.1:8000/cornershop_food/api/v1/users')

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','http://127.0.0.1:8000/cornershop_food/api/v1/users', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://127.0.0.1:8000/cornershop_food/api/v1/users");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://127.0.0.1:8000/cornershop_food/api/v1/users", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /cornershop_food/api/v1/users`

This class handles the creation of a new user and

<h3 id="cornershop_food_api_v1_users_create-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|none|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

<h1 id="cornershop-api-healthz">healthz</h1>

## healthz_list

<a id="opIdhealthz_list"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://127.0.0.1:8000/healthz

```

```http
GET http://127.0.0.1:8000/healthz HTTP/1.1
Host: 127.0.0.1:8000

```

```javascript

fetch('http://127.0.0.1:8000/healthz',
{
  method: 'GET'

})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

result = RestClient.get 'http://127.0.0.1:8000/healthz',
  params: {
  }

p JSON.parse(result)

```

```python
import requests

r = requests.get('http://127.0.0.1:8000/healthz')

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','http://127.0.0.1:8000/healthz', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://127.0.0.1:8000/healthz");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://127.0.0.1:8000/healthz", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /healthz`

<h3 id="healthz_list-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

# Schemas

<h2 id="tocS_MenuObject">MenuObject</h2>
<!-- backwards compatibility -->
<a id="schemamenuobject"></a>
<a id="schema_MenuObject"></a>
<a id="tocSmenuobject"></a>
<a id="tocsmenuobject"></a>

```json
{
  "id": "string",
  "name": "string",
  "menu_date": "string",
  "options": [
    "string"
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|false|read-only|none|
|name|string|false|read-only|none|
|menu_date|string|false|read-only|none|
|options|[string]|false|none|none|

<h2 id="tocS_OptionObject">OptionObject</h2>
<!-- backwards compatibility -->
<a id="schemaoptionobject"></a>
<a id="schema_OptionObject"></a>
<a id="tocSoptionobject"></a>
<a id="tocsoptionobject"></a>

```json
{
  "id": "string",
  "name": "string",
  "price": "string",
  "description": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|false|read-only|none|
|name|string|false|read-only|none|
|price|string|false|read-only|none|
|description|string|false|none|none|

<h2 id="tocS_OrderObject">OrderObject</h2>
<!-- backwards compatibility -->
<a id="schemaorderobject"></a>
<a id="schema_OrderObject"></a>
<a id="tocSorderobject"></a>
<a id="tocsorderobject"></a>

```json
{
  "id": "string",
  "menu": "string",
  "create_at": "string",
  "option": "string",
  "commentary": "string",
  "quantity": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|false|read-only|none|
|menu|string|false|read-only|none|
|create_at|string|false|read-only|none|
|option|string|false|none|none|
|commentary|string|false|none|none|
|quantity|integer|false|none|none|

<h2 id="tocS_forbiden">forbiden</h2>
<!-- backwards compatibility -->
<a id="schemaforbiden"></a>
<a id="schema_forbiden"></a>
<a id="tocSforbiden"></a>
<a id="tocsforbiden"></a>

```json
{
  "detail": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|detail|string|false|none|none|

<h2 id="tocS_ApiBadResponse">ApiBadResponse</h2>
<!-- backwards compatibility -->
<a id="schemaapibadresponse"></a>
<a id="schema_ApiBadResponse"></a>
<a id="tocSapibadresponse"></a>
<a id="tocsapibadresponse"></a>

```json
{
  "errors": [
    "string"
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|errors|[string]|false|read-only|none|

