function state_new = new_state_fun(state,operation,k)
    len = length(state);
    
    if operation == 1 % Summation
        arg_new = state(k)+state(k+1);
    elseif operation == 2 % Subtraction
        arg_new = abs(state(k)-state(k+1));
    elseif operation == 3 % Multiplication
        arg_new = state(k)*state(k+1);
    elseif operation == 4 % Division
        arg_new = state(k)/state(k+1);
    else
        print('no such operation')
    end
    for i=1:k
        state_new=state(1:k);
        state_new(k)= arg_new;
        if k~=(len-1)
            state_new = [state_new, state(k+2:len)];
        end
    end
end