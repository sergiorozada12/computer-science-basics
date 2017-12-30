function B = MergeSort( A )
n = length(A);
mid = fix(n/2);
left = [];
right = [];
B = [];

if n>2
    left = MergeSort (A(1:mid));
    right = MergeSort (A((mid+1):n));
elseif n==2
    left = [left A(1)];
    right = [right A(2)];
else
    B = [left A(1)];
    return;
end

index_left = 1;
index_right = 1;
n_left = length(left);
n_right = length(right);

while true
    if left(index_left)<right(index_right)
        B=[B left(index_left)];
        index_left=index_left+1;
    else 
        B=[B right(index_right)];
        index_right=index_right+1;
    end
    
    if index_left == n_left+1
        B=[B right(index_right:n_right)];
        return;
    elseif index_right == n_right+1
        B=[B left(index_left:n_left)];
        return;
    end
    
end

end

