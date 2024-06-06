from db_func.base_db import BaseDb


class FormDb(BaseDb):
    async def add_row(self, user_id, name, phone, instagram):
        query = """
        INSERT INTO forms (user_id, name, phone, instagram)
        VALUES ($1, $2, $3, $4)
        """

        try:
            await self.execute(query, user_id, name, phone, instagram)
        except Exception as e:
            print(f"Ошибка: {e}")