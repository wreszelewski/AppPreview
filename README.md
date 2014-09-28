AppPreview
==========

It's a tool for creating tables basing on return value of some api call.
It's based on Twitter Bootstrap, jQuery, jsonTable and jsonrpc jQuery plugin.

# How to use it?

You only have to prepare an api method that returns a list of hashes, configure website properly and serve this project as static content from your app (to avoid CORS).
Let's assume you've prepared a method *test_method* that returns:

```javascript
[{'id' : 1, 'name' : 'one'}, {'id' : 2, 'name' : 'two'}]
```

and method *another_test_method* that returns:
```javascript
[{'number' : 3, 'name' : 'three'}, {'numer' : 4, 'name' : 'four'}]
```


Those methods are available on localhost:8080/.
Your configuration (stored in config/config.js file) should look like this:

```javascript
appName = "SomeName";                       //application name, will be desplayed on navbar
rpcEndPoint = 'http://localhost:8080/';     //rpc endpoint
functions = {                               //rpc functions that can be called
    'test_method' :                         //api method name
        {
            "tabName": 'Test',              //name of tab where result should be displayed
            "jsonKeys": ['id', 'name'],     //keys of each dict that should be displayed
            "colNames": ['Number', 'Name'], //optional: column name corresponding to each displayed key, default is a key name
        },
      'another_test_method':
        {
            "tabName": 'AnotherTest',
            "jsonKeys": ['number', 'name'],
        }
};
startMethod='test_method';                  //method that should be displayed first
```



