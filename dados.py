
import sqlite3
#
 # conecta/cria banco
conn = sqlite3.connect("expedicao.db")
#
# # cursor
cursor = conn.cursor()
#
# # cria tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS expedicao (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    lote INTEGER,
    nf_saida INTEGER,
    loja TEXT,
    ce TEXT,
    cor TEXT,

    peso_programado REAL,
    data_programada TEXT,

    data_enviada TEXT,
    peso_enviado REAL,

    peso_bruto REAL,

    carga_rack TEXT,

    data_recebida TEXT,
    peso_recebido REAL,

    apontamento TEXT
)
""")
#
# # inserir dados exemplo
dados = [
    (
        523090, 241362, 'ND', 'CLIENTE', 'PRETO',
        10.10, '2024-05-08',
        '2024-05-09', 9.88,
        None,
        None,
        '2024-05-16', 9.88,
        None
    ),

    (
        513749, 236288, 'ND', 'TMB/EST', 'PRETO',
        1742.00, '2024-04-02',
        '2024-04-02', 1742.00,
        None,
        None,
        '2024-04-15', 1742.00,
        None
    ),

    (
        511639, 236134, 'DIVERSOS', 'DIVERSOS', 'PRETO',
        1860.00, None,
        '2024-04-01', 1880.80,
        None,
        None,
        '2024-04-15', 1880.80,
        None
    )
]

cursor.executemany("""
INSERT INTO expedicao (
    lote,
    nf_saida,
    loja,
    ce,
    cor,
    peso_programado,
    data_programada,
    data_enviada,
    peso_enviado,
    peso_bruto,
    carga_rack,
    data_recebida,
    peso_recebido,
    apontamento
)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", dados)

# salvar alterações
conn.commit()

# consultar dados
cursor.execute("SELECT * FROM expedicao")

for linha in cursor.fetchall():
    print(linha)

# fechar conexão
conn.close()
