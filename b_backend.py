# 1. Cargar la bbdd con langchain

from langchain.sql_database import SQLDatabase
from langchain.llms import OpenAI
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain_experimental.sql import SQLDatabaseChain

db = SQLDatabase.from_uri("sqlite:///gadget.db")

# 2. Importar las APIs
import a_env_vars
import os
os.environ["OPENAI_API_KEY"] = a_env_vars.OPENAI_API_KEY

# 3. Crear el LLM
from langchain.chat_models import ChatOpenAI
llm = ChatOpenAI(temperature=0.3,model_name='gpt-4')

# 4. Crear la cadena
from langchain_experimental.sql import SQLDatabaseChain
cadena = SQLDatabaseChain(llm=llm, database= db, verbose=False)

# 5. Formato personalizado de respuesta
formato = """
Dada una pregunta del usuario: (Responde y actua como un asistente amigable virtual)
1. crea una consulta de sqlite3 o para sql server
2. revisa los resultados
3. devuelve el dato exacto
4. si tienes que hacer alguna aclaración o devolver cualquier texto que sea siempre en español y
limitate a responder puntualmente 
#{question}
"""

# 6. Función para hacer la consulta

def consulta(input_usuario):
    consulta = formato.format(question = input_usuario)
    resultado = cadena.run(consulta)
    return(resultado)