function Utility = max_fun(state,alpha,beta)
    global target
    global operation_record
    global argument_record
    if length(state)==1
        Utility = (abs(state - target));
    else
        Utility=-inf;
        for operation = 1 : 4
            for k = 1: (length(state)-1)
                state_new = new_state_fun(state,operation,k);
%                 display(state)
%                 display(operation)
%                 display(k)
%                 display(state_new)
                
                Utility_old = Utility;
                Utility_test = min_fun(state_new,alpha,beta);
                Utility = max(Utility_test, Utility_old);
                
                if Utility_old ~= Utility
                    operation_record(length(state)-1)=operation;
                    argument_record(length(state)-1)=k;
                end
                if Utility >= beta
                    return;
                end
                alpha   = max(alpha,Utility);

%                 display(Utility)
                
            end
        end
    end
end
