from ecommerce.shipping import calculate_shipping, calculate_shipping_tax

cost = [20, 300, 470, 34, 89]
shipping_cost = calculate_shipping(cost)
shipping_tax = calculate_shipping_tax(cost)
print('shipping cost: ',shipping_cost)
print('shipping tax: ',shipping_tax.__ceil__())