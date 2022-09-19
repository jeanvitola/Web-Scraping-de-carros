# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# FIRTS DAG IN AIRFLOW-ALKEMY

# Esté modulo permite manipular fechas y tiempo
from datetime import datetime, timedelta

#Se crea el objeto DAG que es necesario para crear la instancia DAG
from airflow import DAG

args= {
  'email': ['jeanvitola@gmail.com'],
  'retries': 5,
  'retry_delay': timedelta(minutes=5)
}

with DAG
(
    default_args=args,
    description = 'simple Dag Alkemy",
    schedule_interval='0 1 2 * *',
    start_date=datetime(2022,12,12),
    catchup=False,
    tags=['example'] 
    

) as dag:
    pass

 """ t1,t2 y t3 serian las principales tareas creadas por operadores de instacia
    
    #Extracción
    PostgresOperator para hacer la conexión a la BBDD y hacer las Querys
    t1 =PostgresOperator
    
    #Transformación
    PythonOperator Para hacer la limpieza y transformación de datos
    t2=PythonOperator
    
    #Carga
    S3CreateBucketOperator Para crear un bucket en S3 
    t3=CreateBucketOperator
    
    
    t1 >> >> t2 >> t3]
    """
    









