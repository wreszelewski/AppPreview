appName = "Test";
rpcEndPoint = 'http://localhost:8080/api/'; 
functions = {
    'get_list' :
        {
            "tabName": 'List',
            "headers": ['id', 'name'],
        },
    'get_another' :
        {
            "tabName": 'Another',
            "headers": ['numer', 'nazwa'],
        },
};
startMethod='get_list';
