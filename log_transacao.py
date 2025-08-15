from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT_PATH = Path(__file__).parent


def log_transacao(func):
    def envelope(*args, **kwargs):
        fuso = ZoneInfo("America/Sao_Paulo")
        agora = datetime.now(fuso)
        resultado = func(*args, **kwargs)
        with open(ROOT_PATH / "log.txt", "a") as arquivo:
            arquivo.write(
                f"[{agora}] Função '{func.__name__}'executada com argumentos {args} e {kwargs}."
                f" Retornou {resultado}\n"
            )
        return resultado

    return envelope
