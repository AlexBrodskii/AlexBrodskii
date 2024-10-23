SELECT TIME_FORMAT(calls.date, '%H:%i') AS time,
       CONCAT(managers.first_name, ' ',managers.last_name) AS manager,
       CONCAT(clients.first_name, ' ',clients.last_name) AS client,
       companies.name AS company,
       SEC_TO_TIME(calls.duration_sec) AS duration 
FROM calls 
LEFT JOIN 
    managers ON calls.manager_id=managers.id
LEFT JOIN 
    clients ON calls.client_id=clients.id
LEFT JOIN 
    companies ON clients.company_id=companies.id
WHERE calls.date BETWEEN '2018-04-05 00:00:00' AND '2018-04-05 23:59:59'
ORDER BY time;
SELECT  companies.name AS company,
        SEC_TO_TIME(IFNULL(SUM(calls.duration_sec),0)) AS  duration 
FROM companies
LEFT JOIN 
    clients ON companies.id=clients.company_id
LEFT JOIN 
    calls ON clients.id=calls.client_id
GROUP BY company
ORDER BY duration;
SELECT 
    managers.first_name AS first_name, 
    managers.last_name AS last_name, 
    DATE_FORMAT(SEC_TO_TIME(AVG(calls.duration_sec)), '%H:%i:%s') AS avg_duration
FROM 
    calls 
LEFT JOIN 
    managers ON calls.manager_id = managers.id
LEFT JOIN 
    clients ON calls.client_id = clients.id
LEFT JOIN 
    companies ON clients.company_id = companies.id
WHERE 
    companies.name = 'Cloud Computing'
GROUP BY 
    managers.id, managers.first_name, managers.last_name
ORDER BY 
    avg_duration DESC;




