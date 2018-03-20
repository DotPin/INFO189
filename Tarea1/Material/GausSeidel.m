
%  A = Matriz cuadrada
%  B = vector sistema AX=B
%  nn = factor de error
%  p= norma subordinada 1,2,inf
%  programa ejecutarlo directo en programa corriendo octave:n>GausSeidel([Matriz],[Vector],error,NormaSubordinada):

%Matriz A de valores
clear


A = dlmread("matriz_a",",");
B = dlmread("vector_b");
B = B'
%nn = 0.0000003
%p = 2

disp("*************Calculo iterativo de la solucion u(x) con GausSeidel************")
disp("\n\n\n\n")


disp("Ingrese la cota de error asociado para el criterio de parada del método")
disp("El intervalo debe ser entre ]0,1[")

nn = input("Ingrese la cota de error: ")
while (nn>1 && nn<0)
  if (nn>1 && nn<0)
    disp("ERROR, ingrese un valor dentro del intervalo ]0,1[")
  endif
  nn = input("Ingrese la cota de error: ")
endwhile


disp("Ingrese la norma a utilizar para el calculo del criterio de parada")
disp("Norma 1= 1 ; Norma 2= 2; Norma Infinito= inf")
do
  p = input("Ingrese norma subordinada: ")
  if (p!=1 || p!=2 ||p!=inf)
    disp("ERROR! Ingrese la norma correcta")
  end
until (p!=1 || p!=2 || p!=inf) 


n = length(B);


% Matriz D
D=zeros(n,n);
for i=1:1:n
    D(i,i)=A(i,i);
           
end

% Matriz U
F=zeros(n,n);
for c=1:1:n
    for f=c+1:1:n
        F(c,f) = A(c,f);
    end
end

% Matriz L
E = zeros(n,n);
for c=1:1:n
    for f=c+1:1:n
        E(f,c) = A(f,c);
    end
end

%Matrices D,L,U
D
F
E
% Matriz Mgs y Vgs
Mgs = -inv(D+E)*F
Vgs = inv(D+E)*B


x=zeros(n,1);

disp("Norma aplicada a la matriz de iteración")
norm(Mgs,p)

disp("Numero de iteraciones aproximada segun la norma y el error aplicado")
% nº de Iteraciones para solucion aproximada del sistema
k = log((nn*(1-norm(Mgs,p)))/norm((Mgs*x+Vgs - x),p))/log(norm(Mgs,p))

for i=0:1:k
    x=Mgs*x+Vgs;
end

%Solución del sistema lineal aproximado
x

plot(x)

pause(10)