import httpx
import os
from dotenv import load_dotenv

load_dotenv()
API_URL = os.getenv("API_URL")

async def register_user(name, email) -> bool:
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(f'{API_URL}/reg', json={"name": name, "email": email})
            return response.status_code == 200
        except Exception as e:
            print(e)
            return False

async def get_all_users():
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f'{API_URL}/users')
            if response.status_code == 200:
                return response.json()
            return []
        except Exception as e:
            print(e)
            return []

