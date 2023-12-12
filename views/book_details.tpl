<!DOCTYPE html>
<html>
<head>
    <title>{{book['title']}}</title>
</head>
<body>
    <h1>{{book['title']}}</h1>
    <p>Author: {{book['author']}}</p>
    
    <h2>Ratings</h2>
    <ul>
        % for rating in ratings:
            <li>{{rating}}</li>
        % end
    </ul>

    <p><a href="/books/{{book['id']}}/add_rating">Add Rating</a></p>
    <p><a href="/books/{{book['id']}}/update">Update Book</a></p>
    <p><a href="/books/{{book['id']}}/delete">Delete Book</a></p>
    <p><a href="/books">Back to Books</a></p>
</body>
</html>
