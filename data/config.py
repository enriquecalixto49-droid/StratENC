from pydantic_settings import BaseSettings, SettingsConfigDict


class DataBaseSettings(BaseSettings):
    POSTGRES_SERVER: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_FRED_DB: str
    FRED_API_KEY: str

    model_config = SettingsConfigDict(
        env_file= "./.env",
        env_ignore_empty=True,
        extra="ignore",
        
    )

    @property
    def POSTGRES_URL(self):
        '''
        The property decorator allows to access this method as a class variable. 
        '''
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_FRED_DB}"

settings = DataBaseSettings()
 
