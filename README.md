# HY Cyber security course project

This is a simple notebook web application. Shows 5 different flaws in software and how to avoid some web application security risks

[OWASP Top 10 Web Application Security Risks 2021](https://owasp.org/www-project-top-ten/)

## Installation

create database using
```
python3 manage.py migrate
```

then start a server by
```
python3 manage.py runserver
```

## Recommended versions for required libraries
 - python v3.10.6
 - django v4.1.3
 - sqlite3 v3.37.2

## Enabled flaws in application from OWASP 2021 list

### FLAW 1: https://owasp.org/www-community/attacks/csrf 

https://cybersecuritybase.mooc.fi/module-2.3/1-security#heading-cross-site-request-forgery 

Cross-site Request Forgery (CSRF) is a security flaw that allows the attacker to trick a user, so he executes unwanted requests to target web application, when he is logged in, by giving them malicious links to click. By making unwanted requests the user makes unwanted actions, for example sends money to someone, or does changes in data, deletes something. The site should have CSRF protection, and it should check CSRF-token on form submitting, so requests can't be done just by sending parameters via link without CSRF-token. If no CSRF-token were sent with request, it should be forbidden with http status 403.  

In project, index page has CSRF-token commented 

https://github.com/olegTervo/CyberSecurityProject/tree/master/notebook/notebookapp/templates/pages/index.html#L37 

 and 

https://github.com/olegTervo/CyberSecurityProject/tree/master/notebook/notebookapp/views.py#L18 

Has @csrf_protect commented away and @csrf_exempt added. Remove comments from html form, @csrf_exempt and uncomment @csrf_protect to enable CSRF protection on adding new note. 


### FLAW 2: https://owasp.org/Top10/A01_2021-Broken_Access_Control/ 

Access to resources should be controlled to avoid leaks and unauthorized access to data. Also access to user resources should be limited. Other users shouldn’t be able to access one’s data. But in situations where no check is done, it is possible to read other’s data, for example by manipulating parameters. That means access control is vulnerable and the flaw exists. 

In the project, it’s possible to see other user’s notes by simply changing URL. It uses user id to list notes and by using other’s user id you will get other’s notes because no check is done on back-end side.  

To fix it, username should be taken from request.user.username, not from URL. Uncomment lines 33-36 and comment lines 38-40 away in 

https://github.com/olegTervo/CyberSecurityProject/tree/master/notebook/notebookapp/views.py#L33 

Also, you can remove user_id parameter in views, line 30, 27, 13, and urls: 

https://github.com/olegTervo/CyberSecurityProject/tree/master/notebook/notebookapp/urls.py#L7 

 
### FLAW 3: https://owasp.org/Top10/A03_2021-Injection/ 

When user input is not validated or sanitized and we use it for queries, it's possible to have leaks by injections. For example, SQL-injections, when using a combination of raw string and user input as SQL-query.  
Some of the most common injections, according to OWASP are SQL, NoSQL, OS command, Object Relational Mapping (ORM), LDAP, and Expression Language (EL) or Object Graph Navigation Library (OGNL) injection.  

For example, in application there is a raw SQL in 

https://github.com/olegTervo/CyberSecurityProject/tree/master/notebook/notebookapp/views.py#L39 

and user_id is coming from URL as raw string. Using name_id in URL like 

http://localhost:8000/notebookapp/list/name_id 

will result in listing all notes from database. Also, some more complex UNION injections are possible to leak any data from database. 

To fix it, use Note.object.filter(…) in 

https://github.com/olegTervo/CyberSecurityProject/tree/master/notebook/notebookapp/views.py#L36 

Django default user models related with migrated models and queries are done through Note.objects interface, which sanitizes user inputs before inserting it into the database. 

 
### FLAW 4: https://owasp.org/Top10/A05_2021-Security_Misconfiguration/ 

Security Misconfiguration is a flaw in software configuration and set up. For example, default users with unchanged passwords or missing/default settings. There could be sample projects or test features left. This can result in some unwanted and undocumented features or unauthorized access to information.  

For example, project is using DEBUG = True in  

https://github.com/olegTervo/CyberSecurityProject/tree/master/notebook/notebook/settings.py#L28 

which results in detailed error logs with code parts. It makes reverse engineering easier and shows the implementation and possibly sensitive information. 

It needs to be changed to use lines 26-27. Disabling debug mode and listing available hosts restricts unwanted access and hides error details. 

 
### FLAW 5: https://owasp.org/Top10/A07_2021-Identification_and_Authentication_Failures/ 

Identification and Authentication Failures are weaknesses in user identification system, that allows to steal other’s identity. One example is poorly handled session, without automatic logouts. Another example is an easy password that can be brute-forced or is in the top used passwords list. There should be minimum security requirements for passwords, such as password length, use of different symbols to make brute-force harder, check for common passwords and check for using personal info in password. Passwords like NameSurnameYY are probably not in the top passwords list, but also a very common pattern that is easy to break. 

In the project, when a new user is signing up, there is no password check, so it can be any unsafe string, such as 123. To add password verification, go and uncomment AUTH_PASSWORD_VALIDATORS, Lines 88-99. 

https://github.com/olegTervo/CyberSecurityProject/tree/master/notebook/notebook/settings.py#L87 

It’s possible to add more validation, as django uses external modules to check password validity, so you can add you own implementation following their instructions 

https://docs.djangoproject.com/en/4.2/topics/auth/passwords/#writing-your-own-validator 
