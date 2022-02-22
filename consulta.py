import pymssql
import config



def PesoVendido():
    conn = pymssql.connect(server=config.servidor, port=config.porta, 
                           database=config.db, user=config.user, password=config.passwd)
    sql = conn.cursor()
    sql.execute("SELECT SUM(PesoLiquido) as PesoVendido FROM dbo.Movimento WHERE DtMov = CONVERT(date,GETDATE()) AND NotaFiscalImpressa='S'")
    row = sql.fetchone()
    peso = row[0]
    sql.close()
    return peso

def ValorVendido():
    conn = pymssql.connect(server=config.servidor, port=config.porta, 
                           database=config.db, user=config.user, password=config.passwd)
    sql = conn.cursor()
    sql.execute("SELECT SUM(TotMov) as TotalVendido FROM dbo.Movimento WHERE DtMov = CONVERT(DATE,GETDATE()) AND NotaFiscalImpressa = 'S';")
    row = sql.fetchone()
    vendas = row[0]
    sql.close()
    return vendas
