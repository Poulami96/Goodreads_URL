This project contains an API which takes a Goodreads URL string as input and gives out information of book as output in python.

1.The structure of function is as follows:
def get_book_details(url:str)->dict

2.The technology used is via ElementTree for parsing data of books.

3.If any error occurs during inappropriate url being sent,an exception InvalidGoodreadsURL has been raised.

4.If Goodreads returns invalid XML response,an empty dictionary has been returned.

5.Fields not having value  during goodreads response, the field has NULL values.

6.The function in the script has URL taken from command line input(BONUS).