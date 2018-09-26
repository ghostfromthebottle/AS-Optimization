close all;
clear all;
clc;

%% Variable setup
time = [120;190;45;300;165;84;77;20;40;80;20;180;72;200;190;80;150;100;25;800];
time_min = [70;40;20;100;65;50;40;10;20;20;10;40;30;30;20;20;30;30;10;300];
time_bound = time-time_min; %Upper bound for optimization variable
cost = [400;40;50;300;70;60;77;180;150;360;20;18;27;34;31;28;32;41;550;650];

%% Optimization setup
prob = optimproblem('ObjectiveSense','min');
x = optimvar('x',20,2,'Type','integer','LowerBound',0);
prob.Objective = cost'*x(:,1);
% Set upper bounds
prob.Constraints.cons1 = x(:,1) <= time_bound;
prob.Constraints.cons2 = x(20,2) + time(20) - x(20,1) <= 1095;
%% Set node bounds
prob.Constraints.cons3 = x(2,2) >= time(1)-x(1,1); %B-A
prob.Constraints.cons4 = x(3,2) >= time(1)-x(1,1); %C-A
prob.Constraints.cons5 = x(4,2) >= time(1)-x(1,1); %D-A
prob.Constraints.cons6 = x(5,2) >= time(1)-x(1,1); %E-A
prob.Constraints.cons7 = x(6,2) >= x(2,2) + time(2)-x(2,1); %F-B
prob.Constraints.cons8 = x(7,2) >= x(3,2) + time(3)-x(3,1); %G-C
prob.Constraints.cons9 = x(8,2) >= x(4,2) + time(4)-x(4,1); %H-D
prob.Constraints.cons10 = x(9,2) >= x(8,2) + time(8)-x(8,1); %I-H
prob.Constraints.cons11 = x(9,2) >= x(5,2) + time(5)-x(5,1); %I-E
prob.Constraints.cons12 = x(10,2) >= x(9,2) + time(9)-x(9,1); %J-I
prob.Constraints.cons13 = x(11,2) >= x(6,2) + time(6)-x(6,1); %K-F
prob.Constraints.cons14 = x(11,2) >= x(7,2) + time(7)-x(7,1); %K-G
prob.Constraints.cons15 = x(12,2) >= x(11,2) + time(11)-x(11,1); %L-K
prob.Constraints.cons16 = x(13,2) >= x(2,2) + time(2)-x(2,1); %M-B
prob.Constraints.cons17 = x(13,2) >= x(3,2) + time(3)-x(3,1); %M-C
prob.Constraints.cons18 = x(14,2) >= x(13,2) + time(13)-x(13,1); %N-M
prob.Constraints.cons19 = x(15,2) >= x(13,2) + time(13)-x(13,1); %O-M
prob.Constraints.cons20 = x(16,2) >= x(13,2) + time(13)-x(13,1); %P-M
prob.Constraints.cons21 = x(17,2) >= x(12,2) + time(12)-x(12,1); %Q-L
prob.Constraints.cons22 = x(17,2) >= x(13,2) + time(13)-x(13,1); %Q-M
prob.Constraints.cons23 = x(17,2) >= x(14,2) + time(14)-x(14,1); %Q-N
prob.Constraints.cons24 = x(17,2) >= x(15,2) + time(15)-x(15,1); %Q-P
prob.Constraints.cons25 = x(18,2) >= x(17,2) + time(17)-x(17,1); %R-Q
prob.Constraints.cons26 = x(19,2) >= x(10,2) + time(10)-x(10,1); %S-J
prob.Constraints.cons27 = x(19,2) >= x(18,2) + time(18)-x(18,1); %S-R
prob.Constraints.cons28 = x(20,2) >= x(19,2) + time(19)-x(19,1); %T-S

%% Solver
showproblem(prob)

[sol,fval] = solve(prob);
sol.x %ans = [50;150;25;145;0;27;0;10;20;58;10;140;42;123;113;0;120;70;7;0];
fval
