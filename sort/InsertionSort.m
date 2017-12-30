function B=InsertionSort(A)
n=length(A);
index = 1;

while index<n
    if A(index+1)<A(index)
        temp=A(index);
        A(index)=A(index+1);
        A(index+1)=temp;
        if index>1
            index=index-1;
        else
            index=index+1;
        end
    else
        index=index+1
    end        
end

B=A;
end