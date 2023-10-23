import cx_Oracle
import unittest


username = "AERO"
password = "aero123"
database = "xe"
host="10.1.2.10"
port="1521"

IN_INBOX_ID = 0
IN_DEVICE_ID = '0306'
IN_SOURCE_CHANNEL = 'G'
V_VEHICLE_ID = 571435
OUT_STATUS = 0


class TestStringMethods(unittest.TestCase):
    def __init__(self, methodName='runTest'):
        super(TestStringMethods, self).__init__(methodName)
        cx_Oracle.init_oracle_client(lib_dir=r"C:\oracle\instantclient_21_11")
        self.connection = cx_Oracle.connect(f"{username}/{password}@{host}:{port}/{database}")
        self.cursor = self.connection.cursor()
        self.IN_INBOX_ID = 0
        self.IN_DEVICE_ID = '0306'
        self.IN_SOURCE_CHANNEL = 'G'
        self.V_VEHICLE_ID = 571435
        self.OUT_STATUS = 0


    def test_verifica_se_retorna_37_no_tempo_de_carregamento(self):

        self.IN_MESSAGE='>RUV02123,0.6,171023164319-2967875-05112780000344300D8,000A,0,10000000,FFFFFFFF,FFFFFFFF,04311219,RF,000,0,0,0000000,00037,0,00020,00100;ID=0306;#2956;*6C<'
        e_tempo_carregamento = 37
        s_tempo_carregamento = None
        self.cursor.callproc('PKG_HW_VIRLOC8.PARSE_V0', [self.IN_INBOX_ID, self.IN_DEVICE_ID, self.IN_MESSAGE, self.IN_SOURCE_CHANNEL, self.OUT_STATUS])
        self.connection.commit()
        self.cursor.execute("SELECT CONTAGEM_EVENTO FROM aero.eventos WHERE VEHICLE_ID = 571435 AND rownum = 1 ORDER BY id DESC")
        
        s_tempo_carregamento = self.cursor.fetchone()[0]
        self.assertEqual(s_tempo_carregamento, e_tempo_carregamento)

        self.connection.rollback()
        self.cursor.close()
        self.connection.close()

if __name__ == '__main__':

    unittest.main()