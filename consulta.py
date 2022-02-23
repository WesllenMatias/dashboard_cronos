import pymssql
import config



def PesoVendido():
    conn = pymssql.connect(server=config.servidor, port=config.porta, 
                           database=config.db, user=config.user, password=config.passwd)
    sql = conn.cursor()
    sql.execute("SELECT SUM(PesoLiquido) as PesoVendido FROM dbo.Movimento WHERE DtMov = CONVERT(date,GETDATE()) AND NotaFiscalImpressa='S' AND StatusOS != 'C'")
    row = sql.fetchone()
    peso = row[0]
    sql.close()
    return peso

def ValorVendido():
    conn = pymssql.connect(server=config.servidor, port=config.porta, 
                           database=config.db, user=config.user, password=config.passwd)
    sql = conn.cursor()
    sql.execute("SELECT SUM(TotMov) FROM dbo.Movimento WHERE DtMov = CONVERT(DATE,GETDATE()) AND NotaFiscalImpressa = 'S' AND StatusOS != 'C';")
    row = sql.fetchone()
    vendas = row[0]
    sql.close()
    return vendas

def QtdVendas():
    conn = pymssql.connect(server=config.servidor, port=config.porta, 
                           database=config.db, user=config.user, password=config.passwd)
    sql = conn.cursor()
    sql.execute("SELECT COUNT(StatusOS) FROM dbo.Movimento WHERE DtMov = CONVERT(DATE,GETDATE()) AND NotaFiscalImpressa = 'S' AND StatusOS != 'C';")
    row = sql.fetchone()
    qtd_vendas = row[0]
    sql.close()

    return qtd_vendas


#SELECT COUNT(StatusOS) FROM dbo.Movimento WHERE DtMov = CONVERT(DATE, GETDATE()) AND NotaFiscalImpressa = 'S' AND StatusOS = 'C';
def QtdCanceladas():
    conn = pymssql.connect(server=config.servidor, port=config.porta, 
                    database=config.db, user=config.user, password=config.passwd)
    sql = conn.cursor()
    sql.execute("SELECT COUNT(StatusOS) FROM dbo.Movimento WHERE DtMov = CONVERT(DATE,GETDATE()) AND NotaFiscalImpressa = 'S' AND StatusOS = 'C';")
    row = sql.fetchone()
    qtd_canceladas = row[0]
    sql.close()
    
    return qtd_canceladas