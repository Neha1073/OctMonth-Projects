from fastapi import FastAPI, HTTPException
import csv

app = FastAPI()

def read_csv_file():
    books = []
    with open("venv/books.csv", mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            books.append(row)
    return books


@app.put("/update/{book_id}/{new_copies}")
async def update_available_copies(book_id: int, new_copies: int):
    books = read_csv_file()
    for book in books:
        if int(book["id"]) == book_id:
            book["available_copies"] = new_copies
            with open("books.csv", mode="w", newline="") as file:
                fieldnames = ["id", "title", "author", "available_copies", "publication_year"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(books)
            return {"message": f"Updated available copies for book {book_id}"}
    raise HTTPException(status_code=404, detail=f"Book {book_id} not found")
