import mysql.connector
from mysql.connector import Error

def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name,
            port = 3307
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection
    
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")
def create_server_connection(host_name, user_name, user_password,port=3307):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            port=3307
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

timezones = {
    "ACDT" :  10.5,
    "ACST" :  9.5,
    "ACT" :  -5,
    "ACT" :  9.5 / 10.5,
    "ACWST" :  8.75,
    "ADT" :  4,
    "ADT" :  -3,
    "AEDT" :  11,
    "AEST" :  10,
    "AET" :  10 / 11,
    "AFT" :  4.5,
    "AKDT" :  -8,
    "AKST" :  -9,
    "ALMT" :  6,
    "AMST" :  -3,
    "AMST" :  5,
    "AMT" :  -4,
    "AMT" :  4,
    "ANAST" :  12,
    "ANAT" :  12,
    "AQTT" :  5,
    "ART" :  -3,
    "AST" :  3,
    "AST" :  -4,
    "AT" :  -4 / -3,
    "AWDT" :  9,
    "AWST" :  8,
    "AZOST" :  0,
    "AZOT" :  -1,
    "AZST" :  5,
    "AZT" :  4,
    "AoE" :  -12,
    "BNT" :  8,
    "BOT" :  -4,
    "BRST" :  -2,
    "BRT" :  -3,
    "BST" :  6,
    "BST" :  11,
    "BST" :  1,
    "BTT" :  6,
    "CAST" :  8,
    "CAT" :  2,
    "CCT" :  6.5,
    "CDT" :  -5,
    "CDT" :  -4,
    "CEST" :  2,
    "CET" :  1,
    "CHADT" :  13.75,
    "CHAST" :  12.75,
    "CHOST" :  9,
    "CHOT" :  8,
    "CHUT" :  10,
    "CIDST" :  -4,
    "CIST" :  -5,
    "CKT" :  -10,
    "CLST" :  -3,
    "CLT" :  -4,
    "COT" :  -5,
    "CST" :  -6,
    "CST" :  8,
    "CST" :  -5,
    "CT" :  -6 / -5,
    "CVT" :  -1,
    "CXT" :  7,
    "ChST" :  10,
    "DAVT" :  7,
    "DDUT" :  10,
    "EASST" :  -5,
    "EAST" :  -6,
    "EAT" :  3,
    "ECT" :  -5,
    "EDT" :  -4,
    "EEST" :  3,
    "EET" :  2,
    "EGST" :  0,
    "EGT" :  -1,
    "EST" :  -5,
    "ET" :  -5 / -4,
    "FET" :  3,
    "FJST" :  13,
    "FJT" :  12,
    "FKST" :  -3,
    "FKT" :  -4,
    "FNT" :  -2,
    "GALT" :  -6,
    "GAMT" :  -9,
    "GET" :  4,
    "GFT" :  -3,
    "GILT" :  12,
    "GMT" :  0,
    "GST" :  4,
    "GST" :  -2,
    "GYT" :  -4,
    "HDT" :  -9,
    "HKT" :  8,
    "HOVST" :  8,
    "HOVT" :  7,
    "HST" :  -10,
    "ICT" :  7,
    "IDT" :  3,
    "IOT" :  6,
    "IRDT" :  4.5,
    "IRKST" :  9,
    "IRKT" :  8,
    "IRST" :  3.5,
    "IST" :  5.5,
    "IST" :  1,
    "IST" :  2,
    "JST" :  9,
    "KGT" :  6,
    "KOST" :  11,
    "KRAST" :  8,
    "KRAT" :  7,
    "KST" :  9,
    "KUYT" :  4,
    "LHDT" :  11,
    "LHST" :  10.5,
    "LINT" :  14,
    "MAGST" :  12,
    "MAGT" :  11,
    "MART" :  -9.5,
    "MAWT" :  5,
    "MDT" :  -6,
    "MHT" :  12,
    "MMT" :  6.5,
    "MSD" :  4,
    "MSK" :  3,
    "MST" :  -7,
    "MT" :  -7 / -6,
    "MUT" :  4,
    "MVT" :  5,
    "MYT" :  8,
    "NCT" :  11,
    "NDT" :  -2.5,
    "NFT" :  11,
    "NOVST" :  7,
    "NOVT" :  6,
    "NPT" :  5.75,
    "NRT" :  12,
    "NST" :  -3.5,
    "NUT" :  -11,
    "NZDT" :  13,
    "NZST" :  12,
    "OMSST" :  7,
    "OMST" :  6,
    "ORAT" :  5,
    "PDT" :  -7,
    "PET" :  -5,
    "PETST" :  12,
    "PETT" :  12,
    "PGT" :  10,
    "PHOT" :  13,
    "PHT" :  8,
    "PKT" :  5,
    "PMDT" :  -2,
    "PMST" :  -3,
    "PONT" :  11,
    "PST" :  -8,
    "PST" :  -8,
    "PT" :  -8 / -7,
    "PWT" :  9,
    "PYST" :  -3,
    "PYT" :  -4,
    "PYT" :  8.5,
    "QYZT" :  6,
    "RET" :  4,
    "ROTT" :  -3,
    "SAKT" :  11,
    "SAMT" :  4,
    "SAST" :  2,
    "SBT" :  11,
    "SCT" :  4,
    "SGT" :  8,
    "SRET" :  11,
    "SRT" :  -3,
    "SST" :  -11,
    "SYOT" :  3,
    "TAHT" :  -10,
    "TFT" :  5,
    "TJT" :  5,
    "TKT" :  13,
    "TLT" :  9,
    "TMT" :  5,
    "TOST" :  14,
    "TOT" :  13,
    "TRT" :  3,
    "TVT" :  12,
    "ULAST" :  9,
    "ULAT" :  8,
    "UYST" :  -2,
    "UYT" :  -3,
    "UZT" :  5,
    "VET" :  -4,
    "VLAST" :  11,
    "VLAT" :  10,
    "VOST" :  6,
    "VUT" :  11,
    "WAKT" :  12,
    "WARST" :  -3,
    "WAST" :  2,
    "WAT" :  1,
    "WEST" :  1,
    "WET" :  0,
    "WFT" :  12,
    "WGST" :  -2,
    "WGT" :  -3,
    "WIB" :  7,
    "WIT" :  9,
    "WITA" :  8,
    "WST" :  13,
    "WST" :  1,
    "WT" :  0,
    "YAKST" :  10,
    "YAKT" :  9,
    "YAPT" :  10,
    "YEKST" :  6,
    "YEKT" :  5
}
# connection = create_server_connection("localhost","root", "root54668")