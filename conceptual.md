### Conceptual Exercise

Answer the following questions below:

- **What is PostgreSQL?**
    
PostgresSQL is an open source relational database management system

- **What is the difference between SQL and PostgreSQL?**
    
SQL and PostgreSQL are very simular however PostgreSQL contains more functionalities like supporting additional data types like arrays, user defined types. PostgreSQL also supports JSON.

- **In `psql`, how do you connect to a database?**
    
If you're in the psql shell already you can use the /c [database_name] command

- **What is the difference between `HAVING` and `WHERE`?**

HAVING is used to filter group or groups of rows
WHERE is used to filter select rows which cannot be used with groups 

- **What is the difference between an `INNER` and `OUTER` join?**

INNER join returns the common / matching data
OUTER join returns the data similar to the INNER join but also includes data where no common / matching data ia found. 


- **What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?**

Table 1 LEFT join Table 2 (All Data from Table 1 and Common Data with Table 2), 
Table 1 RIGHT join Table 2 (Common Data From Table 1 and All Data From Table 2), 
Table 1 FULL join Table 2 (All data from Table 1 and Table 2)

- **What is an ORM? What do they do?**

An Object Relation Mapping software allows the creation of a bridge between the relational database and object oriented program where Models are created that represent each Table and those Models are expressed as objects and object instances that can be used for data retrieval and manipulation

- **What are some differences between making HTTP requests using AJAX and from the server side using a library like `requests`?**

They are essentially making the same HTTP request however the developer can do more on the server side where the data coming from the API can be stored in a database, or the data can be manipulated some way to calucate some other important value. Some APIs also require the use of a password which is done in the server side for security reasons


- **What is CSRF? What is the purpose of the CSRF token?**

CSRF Cross Site Request Forgery is an exploit of a website / web application where the user is tricked into submitting a request that the user did not intend using tactics such as hidden forms, specially crafted images and tags, harmful XML or fetch requests

CSRF Tokens are usually hidden inputs embedded into the form that acts as an identifier for a valid form sumbission. If we didn't have an identifier then it would be very easy for anyone to submit a post request to our endpoint using some external software like curl or Postman. CSRF Tokens ensure that the Post requst is coming from the intended form.


- **What is the purpose of `form.hidden_tag()`?**

form.hidden_tag() adds the hidden form fields that includes the CSRF tokes into the form object created using WTForms
