clear all;clc;
global target
global operation_record
global argument_record
target             = 10;
init_state          = [5 50 10 15 3 74 85];
% state_record        = zeros(10,length(init_state));
% operation_record    = zeros(length(init_state)-1,1);
% argument_record     = zeros(length(init_state)-1,1);

% max_fun(init_state);
% min_fun(init_state);
state=init_state;
disp(state)
while(length(state)~=1)
    [action,state]  = minimax_decision(state);
    disp(action)
    disp(state)
end