-- La Columna de localidad se hará mas adelante según lo acordado

SELECT 
       universidad                     AS university,
       carrerra                        AS career,
       fechaiscripccion                AS inscription_date,
       ( Split_part(nombrre, ' ', 1) ) AS firts_name,
       ( Split_part(nombrre, ' ', 2) ) AS last_name,
       --(Split_part(String,delimiter,position))
       sexo                            AS gender,
       nacimiento                      AS age,
       codgoposstal                    AS postal_code,
       direccion                       AS Address,
       eemail                          AS email
FROM   moron_nacional_pampa
WHERE  TO_DATE(fechaiscripccion,'DD MM YYYY') BETWEEN '2020-09-01' AND '2021-02-01'



