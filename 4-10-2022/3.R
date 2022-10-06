# i20   => hyundai, 15, petrol 
# nano  => tata, 2.5, petrol
# punch => tata, 15, EV
# nexon => tata, 12, EV

dimnames = list(c('m1', 'm2', 'm3', 'm4'),
                c("name",'company', 'price', "fuel.type"))

data = c('i20', 'hyundai', 15, 'petrol', 
          'nano', 'tata', 2.5, 'petrol', 
          "punch",'tata', 15, 'EV', 
          'nexon', 'tata', 12, 'EV')

cars = matrix(data, nrow = 4, ncol = 4, byrow = T, dimnames)
print(cars)

(cars[, 'price'])
