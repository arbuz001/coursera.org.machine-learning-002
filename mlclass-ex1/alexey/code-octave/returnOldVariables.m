function X_old = returnOldVariables(X, mu, sigma)
%RETURNOLDVARIABLES Normalizes the features in X 
%   RETURNOLDVARIABLES(X, mu, sigma) returns to old variables by applying inverse of normalization of X

X_old = X .* (ones(size(X,1),1)*sigma) + ones(size(X,1),1)*mu;

end