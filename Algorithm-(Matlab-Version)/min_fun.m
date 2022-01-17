function Utility = min_fun(state,alpha,beta)
    global target
    global operation_record
    global argument_record
    if length(state)==1
        Utility     = (abs(state - target));
    else
        Utility=inf;
        for operation = 1 : 4
            for k = 1: (length(state)-1)
                state_new   = new_state_fun(state,operation,k);
%                 display(state)
%                 disp(operation)
%                 display(k)
%                 display(state_new)
                
                Utility_old     = Utility;
                Utility_test    = max_fun(state_new,alpha,beta);
                Utility         = min(Utility_test, Utility_old);
                if Utility_old ~= Utility
                    operation_record(length(state)-1)   = operation;
                    argument_record(length(state)-1)    = k;
                end
                if Utility <= alpha
                    return;
                end
                beta    = min(beta,Utility);
%                 display(Utility)
                
            end
        end
%         Utility = max(v, max_fun(state_new))
    end
end