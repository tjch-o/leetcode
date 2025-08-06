SELECT
    lb.book_id,
    lb.title,
    lb.author,
    lb.genre,
    lb.publication_year,
    count(br.book_id) AS current_borrowers
FROM
    library_books lb
    JOIN borrowing_records br ON lb.book_id = br.book_id
WHERE
    br.return_date IS NULL
GROUP BY
    lb.book_id,
    lb.title,
    lb.author,
    lb.genre,
    lb.publication_year,
    lb.total_copies,
    br.book_id
HAVING
    count(br.book_id) = lb.total_copies
ORDER BY
    current_borrowers DESC,
    lb.title ASC;