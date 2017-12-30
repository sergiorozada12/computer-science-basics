function res = BinarySearch( A , v, low, high )
    if low > high
        res = -1;
    end
    
    mid = int32((low + high)/2);
    
    if (A(mid) == v)
        res = mid;
    elseif (A(mid) > v)
        res = BinarySearch ( A, v, low, mid-1);
    else
        res = BinarySearch ( A, v, mid+1, high);
    end

end

