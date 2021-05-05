function [x,w]=GaussIntergration(N)
%N only has 5 values: 1 2 3 4 5; intergration interval [-1,1];
if N==1
    x=[0];
    w=[2];
elseif N==2
    x=[-1/sqrt(3);1/sqrt(3)];
    w=[1;1];
elseif N==3
    x=[-sqrt(3/5);0;sqrt(3/5)];
    w=[5/9;8/9;5/9];
elseif N==4
    x=[-sqrt((3+2*sqrt(6/5))/7);-sqrt((3-2*sqrt(6/5))/7);sqrt((3-2*sqrt(6/5))/7);sqrt((3+2*sqrt(6/5))/7)];
    w=[1/2-sqrt(5/6)/6;1/2+sqrt(5/6)/6;1/2+sqrt(5/6)/6;1/2-sqrt(5/6)/6];
elseif N==5
    x=[-sqrt(5+2*sqrt(10/7))/3;-sqrt(5-2*sqrt(10/7))/3;0;sqrt(5-2*sqrt(10/7))/3;sqrt(5+2*sqrt(10/7))/3];
    w=[(322-13*sqrt(70))/900;(322+13*sqrt(70))/900;512/900;(322+13*sqrt(70))/900;(322-13*sqrt(70))/900];
else
    error('input value exceeds the valid range');
end