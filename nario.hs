data ArbolN a = Nodo a [ArbolN a] deriving Show

a1::ArbolN Int
a1 = Nodo 2 [ Nodo 4 [Nodo 12 [], Nodo 24 [], Nodo 40 []], Nodo 8 [Nodo 16 [], Nodo 32 []], Nodo 5 [Nodo 25 [], Nodo 50 []]]

buscarEnArbol::Int->ArbolN Int->Bool
buscarEnArbol n (Nodo x []) = if x == n then True else False
buscarEnArbol n (Nodo x (y:ys)) = if n == x then True
                                  else buscarEnArbol n y || buscarEnArbol2 n ys
buscarEnArbol2 n [] = False
buscarEnArbol2 n (y:ys) = buscarEnArbol n y || buscarEnArbol2 n ys


he:: [a]-> [a]
he (x:xs) = xs 

suma::[Int]-> Int
suma[]=0
suma(x:xs) = x + suma(xs)

mayo:: [Int] -> Int
mayo (x:xs)
  |x > mayo(xs) = x 
  | otherwise = mayo(xs)
	
		