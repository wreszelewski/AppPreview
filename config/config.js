appName = "Test";
rpcEndPoint = 'http://localhost:8080/api/'; 
functions = {
    'get_list' :
        {
            "tabName": 'List',
            "headers": ['id', 'name'],
            "col_names": ["Numer", "Nazwa"],
        },
    'get_another' :
        {
            "tabName": 'Another',
            "headers": ['numer', 'nazwa'],
            "col_names": ['Id', 'Value'],
        },
};
startMethod='get_list';
