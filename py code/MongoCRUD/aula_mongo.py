from pymongo import MongoClient
from pprint import pprint

MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "aula_mongo"
COLLECTION_NAME = "crud_básico"

try: 
    CLIENT = MongoClient(MONGO_URI)
    DB = CLIENT[DB_NAME]
    COLECAO = DB[COLLECTION_NAME]
    print(" Conexão com MongoDB estabelecida com sucesso.")

except Exception as e:
    print(f" Erro de conexão: Certifique-se de que o mongod está ativo. Erro: {e}")
    exit()

def imprimir_resultados(query_desc, query):
    """Executa a busca e imprime os resultados de forma legível."""
    
    cursor = COLECAO.find(query)
    count = COLECAO.count_documents(query)
    
    print(f"\n--- 🔎 {query_desc} ({count} resultados) ---")
    if count > 0:
        for doc in cursor:
            pprint(doc)
    else:
        print("Nenhum documento encontrado.")
    print("-" * 60)

COLECAO.delete_many({})
print(f"\n--- Limpando a coleção '{COLLECTION_NAME}' para iniciar o CREATE. ---")

alunos = [
  {"nome": "Alice Silva", "idade": 21, "telefone": "9999-0001"},
  {"nome": "Bruno Costa", "idade": 25, "telefone": "9999-0002"},
  {"nome": "Carla Souza", "idade": 19, "telefone": "9999-0003"},
  {"nome": "Daniel Lima", "idade": 30, "telefone": "9999-0004"},
  {"nome": "Eduarda Melo", "idade": 22, "cidade_origem": "São Paulo"},
  {"nome": "Felipe Nogueira", "idade": 28, "cidade_origem": "Rio de Janeiro"},
  {"nome": "Giovanna Alves", "idade": 20, "cidade_origem": "Belo Horizonte"},
  {"nome": "Henrique Pires", "idade": 26, "cidade_origem": "Salvador"},
  {"nome": "Isabela Rocha", "idade": 24, "telefone": "9999-0009", "cidade_origem": "Curitiba"},
  {"nome": "João Vítor", "idade": 27, "telefone": "9999-0010", "cidade_origem": "Porto Alegre"},
  {"nome": "Karen Dias", "idade": 31, "telefone": "9999-0011", "cidade_origem": "Fortaleza"},
  {"nome": "Lucas Gomes", "idade": 23}, # Alvo do UPDATE/DELETE
  {"nome": "Mariana Santos", "idade": 29},
  {"nome": "Nícolas Ferreira", "idade": 18},
  {"nome": "Olívia Mendes", "idade": 35}
]
COLECAO.insert_many(alunos)
print(f"✅ CREATE: Inseridos {COLECAO.count_documents({})} documentos.")

print("\n" + "="*20 + " READ (Buscas Complexas) " + "="*20)

query_gt = {"idade": {"$gt": 25}}
imprimir_resultados("1. Alunos com idade (Maior Que) 25", query_gt)

query_lt = {"idade": {"$lt": 22}}
imprimir_resultados("2. Alunos com idade (Menor Que) 22", query_lt)

query_ne = {"cidade_origem": {"$ne": "São Paulo"}}
imprimir_resultados("3. Alunos com cidade_origem de 'São Paulo'", query_ne)

query_in = {"idade": {"$in": [20, 24, 28]}}
imprimir_resultados("4. Alunos com idade [20, 24, 28]", query_in)

query_exists = {"telefone": {"$exists": True}}
imprimir_resultados("5. Alunos que possuem o campo 'telefone' ", query_exists)

CLIENT.close()
print("\nConexão com MongoDB encerrada.")