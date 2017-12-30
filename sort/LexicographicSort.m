function B=LexicographicSort(A)
n=size(A);
B=zeros(size(A));

if n(1,2)==1
    for i=1:n
        [minValue,minIndex]=min(A);
        B(i)=minValue;
        A(minIndex)=[];
    end
    return;
end

for i=1:n
    [minValue,minPosition]=min(A(:,1));
    idx=find(A(:,1)==minValue);
    
    if length(idx)==1
        B(i,:)=A(minPosition,:);
        A(minPosition,:)=[];
    else
        C=LexicographicSort(A(idx,2:n(1,2)))
        C=[A(idx,1) C];
        B(i:i+size(C,1)-1,:)=C;
        A(idx,:)=[];
    end
end
end