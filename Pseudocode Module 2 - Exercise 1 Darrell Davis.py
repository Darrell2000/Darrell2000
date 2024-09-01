main
start
   input =model_name
      input =float=height
        input =width=float
        input=depth=float
        input= cubic_inches_per_cubic_foot = 1728
          cubic_inches =height * width * depth
    capacity_cubic_feet = cubic_inches / cubic_inches_per_cubic_foot
output
print model_name
print capacity_cubic_feet: 2f
main
