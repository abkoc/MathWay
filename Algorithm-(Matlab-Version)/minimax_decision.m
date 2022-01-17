function [action,state_next] = minimax_decision(state)
    Utility     = inf;
    for operation = 1:4
        for k = 1:(length(state)-1)
            state_new   = new_state_fun(state,operation,k);
            Utility_old = Utility;
            Utility     = min(min_fun(state_new,-inf,inf), Utility);
            if Utility_old ~= Utility
                action  = [operation k];
                state_next = state_new;
            end
        end
    end
end