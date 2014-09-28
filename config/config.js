appName = "Test";
rpcEndPoint = 'http://localhost:8080/api/'; 
functions = {
    'get_list' :
        {
            "tabName": 'List',
            "jsonKeys": ['id', 'name'],
            "colNames": ["Numer", "Nazwa"],
        },
    'get_another' :
        {
            "tabName": 'Another',
            "jsonKeys": ['numer', 'nazwa'],
        },
};
startMethod='get_list';
