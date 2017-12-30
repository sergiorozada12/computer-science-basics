function res = LinearSearch( A , v )
n = length(A);

for i=1:n
    if (A(i) == v)
        res = i;
    end
end

