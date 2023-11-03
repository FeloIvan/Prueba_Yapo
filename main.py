# importo modulos del package
from Carga_CSV import lectura_csv 
from Procesamiento import procesamiento_data
 
 
def main():
    csv_list = lectura_csv.lee_csv()
    lectura_csv.carga_csv(csv_list)
    procesamiento_data.procesamiento()


main()