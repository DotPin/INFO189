echo "Comenzando algoritmo de diferencias divididas"
for i in 1 2 3
do
 echo "."
 sleep 1
done

python dif_div.py
echo "A continuación el programa solicitará los parámetros de la EDO"
for i in 1 2 3
do
 echo "."
 sleep 1
done

echo "Exporados los polinomios, procede a resolver el sistema"
python descomposicion.py
for i in 1 2 3
do
 echo "."
 sleep 1
done
