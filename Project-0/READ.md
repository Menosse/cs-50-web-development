# Design a front-end for Google Search, Google Image Search, and Google Advanced Search.

## This is the initial project for cs50-web-development-python-django-js
## First analysis to a query string from a GET api call
### field1=value1&field2=value2&field3=value3... > where an = separates the name of the parameter from its value, and the & symbol separates parameters from one another.

Google search results for "Harvard", for instance > https://www.google.com/search?sxsrf=ALeKk03voU3XScUZlUnCjN0pQRCURJUWhQ%3A1595862205745&source=hp&ei=veweX5K1K9qV5OUP8aS0wAs&q=Harvard&oq=Harvard&gs_lcp=CgZwc3ktYWIQDDIECCMQJzIECC4QJzIFCAAQsQMyBQgAELEDMgQIABBDMgcIABCxAxBDMgUILhCxAzIFCAAQsQMyAggAMggIABCxAxCDAVDLAljLAmCECmgAcAB4AIABf4gBf5IBAzAuMZgBAKABAqABAaoBB2d3cy13aXo&sclient=psy-ab&ved=0ahUKEwjSh4f_2e3qAhXaCrkGHXESDbgQ4dUDCAs

- parameters:
* sxsrf=ALeKk03voU3XScUZlUnCjN0pQRCURJUWhQ%3A1595862205745
* source=hp
* ei=veweX5K1K9qV5OUP8aS0wAs
* q=Harvard
* oq=Harvard
* gs_lcp=CgZwc3ktYWIQDDIECCMQJzIECC4QJzIFCAAQsQMyBQgAELEDMgQIABBDMgcIABCxAxBDMgUILhCxAzIFCAAQsQMyAggAMggIABCxAxCDAVDLAljLAmCECmgAcAB4AIABf4gBf5IBAzAuMZgBAKABAqABAaoBB2d3cy13aXo
* sclient=psy-ab
* ved=0ahUKEwjSh4f_2e3qAhXaCrkGHXESDbgQ4dUDCAs