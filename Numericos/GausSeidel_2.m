%  A = Matriz cuadrada
%  u(x) = vector sistema AX=u(x)
%  nn = factor de error
%  p= norma subordinada 1,2,inf
%  programa ejecutarlo directo en programa corriendo octave:n>GausSeidel([Matriz],[Vector],error,NormaSubordinada):

%Matriz A de valores

clear

A = dlmread("matriz_a",",");
vv = dlmread("len")

%Recupera valor resultado u(x)
load resultado
B = x

%Recupera valores validados para criterios de parada
load norma
load error


%nn = 0.0000003
%p = 2

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
Mgs=-inv(D+E)*F
Vgs= inv(D+E)*B


x=zeros(n,1);

norm(Mgs,p);
% nº de Iteraciones para solucion aproximada del sistema
k = log((nn*(1-norm(Mgs,p)))/norm((Mgs*x+Vgs - x),p))/log(norm(Mgs,p))

for i=0:1:k
    x=Mgs*x+Vgs;
end

%Solución del sistema lineal aproximado
x


index = 1
srf = zeros(vv(1),vv(2))
for i=2:vv(1)-1
  for j=2:vv(2)-1
    srf(i,j) = x(index)
    index = index+1
  end
end

save "Resultado_final_GausSeidel" x

surf(srf)
xlabel("Eje x");
ylabel("Eje y");
zlabel("Eje z");
title ("Gr�fico Gaus-Seidel");
pause(10)

