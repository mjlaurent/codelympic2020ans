# codelympic2020ans
Codelympic 2020 Linear Interpolation Answer

This question is about quantity-price relation in company warehouse, the key is to find the estimated price for certain quantity based on past sales.
If the amount of the quantity is on the array of the price, then it will return its key-value pair.
If the amount not in the array, then linear interpolation will be needed in order to predict the price of certain amount of quantity.

Data cleaning will be needed as there will be outliers in price(it should be larger than 0).

The uploaded solution is using list indexing for the data cleaning.
Another solution is using dictionary from collections library, however, the rules only allow us to use provided library.
