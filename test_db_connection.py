from database import get_db

def test_connection():
    db = get_db()
    try:
        # Próbuj pobrać listę kolekcji w bazie danych
        collections = db.list_collection_names()
        print("Połączenie zakończone sukcesem! Kolekcje w bazie danych:")
        print(collections)
    except Exception as e:
        print("Błąd podczas łączenia z bazą danych:", e)

if __name__ == "__main__":
    test_connection()
