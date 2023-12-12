<!DOCTYPE html>
<html>
<head>
    <title>Update Book</title>
</head>
<body>
    <h1>Update Book</h1>
    <form action="/books/{{book['id']}}/update" method="post">
        <label for="title">Title:</label>
        <input type="text" id="title" name="title" value="{{book['title']}}" required><br>

        <label for="author">Author:</label>
        <input type="text" id="author" name="author" value="{{book['author']}}" required><br>

        <input type="submit" value="Update Book">
    </form>
    <p><a href="/books/{{book['id']}}">Back to Book Details</a></p>
</body>
</html>
