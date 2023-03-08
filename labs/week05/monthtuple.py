# tuple stores months of the year
# second tuple stores only the summer months

months = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
)

summer = months[4:7]
for month in summer:
    print(month)

spring = months[0:4]
for month in spring:
    print(month)

autumn = month[7:9]
for month in autumn:
    print(month)

winter = month[-1:9]
for month in winter:
    print(month)