import json

from sqlalchemy import text

from app.db.database import engine


def insert_prediction(input_data: dict, prediction: int, probability: float) -> None:
    query = text("""
        INSERT INTO predictions (input_data, prediction, probability)
        VALUES (:input_data, :prediction, :probability)
    """)

    with engine.connect() as conn:
        conn.execute(
            query,
            {
                "input_data": json.dumps(input_data, ensure_ascii=False),
                "prediction": prediction,
                "probability": probability,
            },
        )
        conn.commit()