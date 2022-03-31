import pymssql
import config



def PesoVendido():
    conn = pymssql.connect(server=config.servidor, port=config.porta, 
                           database=config.db, user=config.user, password=config.passwd)
    sql = conn.cursor()
    sql.execute("SELECT SUM(PesoLiquido) as PesoVendido FROM dbo.Movimento WHERE DtMov = CONVERT(date,GETDATE()) AND NotaFiscalImpressa='S' AND Status != 'C'")
    row = sql.fetchone()
    peso = row[0]
    sql.close()
    return peso

def ValorVendido():
    conn = pymssql.connect(server=config.servidor, port=config.porta, 
                           database=config.db, user=config.user, password=config.passwd)
    sql = conn.cursor()
    sql.execute("SELECT SUM(TotMov) FROM dbo.Movimento WHERE DtMov = CONVERT(DATE,GETDATE()) AND NotaFiscalImpressa = 'S' AND Status != 'C';")
    row = sql.fetchone()
    vendas = row[0]
    sql.close()
    return vendas

def QtdVendas():
    conn = pymssql.connect(server=config.servidor, port=config.porta, 
                           database=config.db, user=config.user, password=config.passwd)
    sql = conn.cursor()
    sql.execute("SELECT COUNT(Status) FROM dbo.Movimento WHERE DtMov = CONVERT(DATE,GETDATE()) AND NotaFiscalImpressa = 'S' AND Status != 'C';")
    row = sql.fetchone()
    qtd_vendas = row[0]
    sql.close()

    return qtd_vendas


#SELECT COUNT(StatusOS) FROM dbo.Movimento WHERE DtMov = CONVERT(DATE, GETDATE()) AND NotaFiscalImpressa = 'S' AND StatusOS = 'C';
def QtdCanceladas():
    conn = pymssql.connect(server=config.servidor, port=config.porta, 
                    database=config.db, user=config.user, password=config.passwd)
    sql = conn.cursor()
    sql.execute("SELECT COUNT(Status) FROM dbo.Movimento WHERE DtMov = CONVERT(DATE,GETDATE()) AND NotaFiscalImpressa = 'S' AND Status = 'C';")
    row = sql.fetchone()
    qtd_canceladas = row[0]
    sql.close()
    
    return qtd_canceladas

def QtdNaoVendido():
    conn = pymssql.connect(server=config.servidor, port=config.porta, 
                    database=config.db, user=config.user, password=config.passwd)
    sql = conn.cursor()
    sql.execute("SELECT COUNT(Status) FROM dbo.Movimento WHERE DtMov = CONVERT(DATE, GETDATE());")
    row = sql.fetchone()
    qtd_nvendido = row[0]
    sql.close()
    
    return qtd_nvendido

def RkVendedores():
    conn = pymssql.connect(server=config.servidor, port=config.porta, 
                    database=config.db, user=config.user, password=config.passwd)
    sql = conn.cursor()
    sql.execute("""SELECT TOP 5 v.NomeVendedor , SUM(m.TotMov) FROM Movimento m 
    JOIN Vendedores v on m.CodVendedor = v.CodVendedor 
    WHERE DtMov = CONVERT(DATE,GETDATE()) AND NotaFiscalImpressa = 'S' AND
    Status != 'C' GROUP BY v.NomeVendedor 
    ORDER BY SUM (m.TotMov) DESC;""")
    row = sql.fetchall()
    rkvendas = row
    sql.close()
    
    return rkvendas


#RkVendedores()