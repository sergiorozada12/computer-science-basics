function B = BubbleSort( A )
n = length(A);
B = zeros(size(A));

for i = 2:n
    index = i;
    
    while (index>1)&&(A(index)<A(index-1))
        current = A(index);
        prev = A(index-1);
        A(index) = prev;
        A(index-1) = current;
        index = index - 1;
    end
end

B = A;
end

