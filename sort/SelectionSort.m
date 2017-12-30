function B=SelectionSort(A)
n=length(A);
B=zeros(size(A));

for i=1:n
    [minValue,minIndex]=min(A);
    B(i)=minValue;
    A(minIndex)=[];
end

end