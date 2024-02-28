


def notes_serializer(notes):
    result = []
    for note in notes:
        result.append({
            "text": note.text,
            "id": note.id,
        })
    return result