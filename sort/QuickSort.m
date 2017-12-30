function B = QuickSort( A , low , high)
mid = int32(low+high)/2;

low_part = [];
high_part = [];
mid_part = [];

for i=low:high
    if A(i)<A(mid)
        low_part = [A(i) low_part];
    elseif A(i)>A(mid)
        high_part = [A(i) high_part];
    else
        mid_part = [A(i) mid_part];
    end
end

A = [low_part mid_part high_part];

if length(A) > 3
    low_part = QuickSort(low_part,1,length(low_part));
    high_part = QuickSort(high_part,1,length(high_part));
    A = [low_part mid_part high_part];
end

B=A;
end

